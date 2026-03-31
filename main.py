import pyrealsense2 as rs
import numpy as np
import cv2
import time
import csv
import os
from ultralytics import YOLO


# ─── Configuração ───────────────────────────────────────────
MODELO = "yolo26n.pt"          # troque para testar outros modelos
CONFIANCA_MIN = 0.5
OUTPUT_CSV = "/home/unitree/Documents/resultados.csv"
OUTPUT_IMG = "/home/unitree/Documents/deteccao.jpg"
JANELA_DEPTH = 10              # pixels ao redor do centro para mediana


model = YOLO(MODELO)


# ─── Pipeline RealSense com alinhamento ─────────────────────
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
pipeline.start(config)


# IMPORTANTE para artigo: alinhar depth ao color
align = rs.align(rs.stream.color)


# ─── CSV ─────────────────────────────────────────────────────
csv_existe = os.path.exists(OUTPUT_CSV)
csv_file = open(OUTPUT_CSV, "a", newline="")
csv_writer = csv.writer(csv_file)
if not csv_existe:
   csv_writer.writerow([
       "frame", "modelo", "classe", "confianca",
       "dist_pixel_unico",   # método antigo (1 ponto)
       "dist_mediana",       # método novo (região)
       "dist_real_m",        # você preenche manualmente depois
       "tempo_inferencia_ms", "fps",
       "x1", "y1", "x2", "y2"
   ])


print(f"Modelo: {MODELO} | Ctrl+C para parar")


frame_count = 0
tempo_total = 0


def distancia_mediana(depth_frame, cx, cy, janela=10):
   """Mediana de uma região ao redor do centro — mais robusta que 1 ponto."""
   h, w = 480, 640
   x1 = max(0, cx - janela)
   x2 = min(w, cx + janela)
   y1 = max(0, cy - janela)
   y2 = min(h, cy + janela)


   depth_array = np.asanyarray(depth_frame.get_data())
   regiao = depth_array[y1:y2, x1:x2].astype(float)
   regiao[regiao == 0] = np.nan  # ignorar pixels sem leitura


   if np.all(np.isnan(regiao)):
       return 0.0


   return float(np.nanmedian(regiao)) * depth_frame.get_units()


try:
   while True:
       frames = pipeline.wait_for_frames()


       # Alinhar depth ao color
       aligned = align.process(frames)
       color_frame = aligned.get_color_frame()
       depth_frame = aligned.get_depth_frame()


       if not color_frame or not depth_frame:
           continue


       color_image = np.asanyarray(color_frame.get_data())


       t_inicio = time.time()
       results = model(color_image, verbose=False)
       t_fim = time.time()


       tempo_inferencia = (t_fim - t_inicio) * 1000
       fps = 1000 / tempo_inferencia
       frame_count += 1
       tempo_total += tempo_inferencia
       tempo_medio = tempo_total / frame_count


       print(f"\n--- Frame {frame_count} | {tempo_inferencia:.1f}ms | FPS: {fps:.1f} ---")


       objetos_frame = []


       for result in results:
           for box in result.boxes:
               confianca = float(box.conf[0])
               if confianca < CONFIANCA_MIN:
                   continue


               classe = model.names[int(box.cls[0])]
               x1, y1, x2, y2 = map(int, box.xyxy[0])
               cx, cy = (x1 + x2) // 2, (y1 + y2) // 2


               # Dois métodos de distância — comparar no artigo
               dist_pixel = depth_frame.get_distance(cx, cy)
               dist_mediana = distancia_mediana(depth_frame, cx, cy, JANELA_DEPTH)


               objetos_frame.append(classe)
               print(f"   → {classe} | {confianca:.0%} | ponto={dist_pixel:.2f}m | mediana={dist_mediana:.2f}m")


               # Salvar no CSV (dist_real_m = 0.0, você preenche depois com fita)
               csv_writer.writerow([
                   frame_count, MODELO, classe, f"{confianca:.4f}",
                   f"{dist_pixel:.4f}", f"{dist_mediana:.4f}", "0.0",
                   f"{tempo_inferencia:.2f}", f"{fps:.2f}",
                   x1, y1, x2, y2
               ])
               csv_file.flush()


               # Visualização
               if confianca >= 0.8:
                   cor = (0, 255, 0)
               elif confianca >= 0.6:
                   cor = (0, 165, 255)
               else:
                   cor = (0, 0, 255)


               cv2.rectangle(color_image, (x1, y1), (x2, y2), cor, 2)


               # Mostra os dois métodos no label
               label = f"{classe} {confianca:.0%} | med={dist_mediana:.1f}m"
               (w_txt, h_txt), _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 2)
               cv2.rectangle(color_image, (x1, y1 - h_txt - 8), (x1 + w_txt, y1), cor, -1)
               cv2.putText(color_image, label, (x1, y1 - 4),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)


       if objetos_frame:
           print(f"   📦 {len(objetos_frame)} objeto(s): {', '.join(objetos_frame)}")


       cv2.putText(color_image, f"FPS: {fps:.1f}", (10, 25),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)
       cv2.putText(color_image, f"Inf: {tempo_inferencia:.0f}ms", (10, 50),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)
       cv2.putText(color_image, f"Modelo: {MODELO}", (10, 75),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)


       cv2.imwrite(OUTPUT_IMG, color_image)


finally:
   pipeline.stop()
   csv_file.close()
   print(f"\n✅ Frames: {frame_count} | Tempo médio: {tempo_medio:.1f}ms")
   print(f"📄 Dados salvos em: {OUTPUT_CSV}")
