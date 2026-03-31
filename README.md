# 🎯 g1eduyolo

Real-time object detection and distance estimation system using YOLO and Intel RealSense depth camera.

## 📖 Description

The **g1eduyolo** project implements a real-time computer vision system that combines deep learning-based object detection with depth sensing.

The system uses the YOLO (You Only Look Once) architecture for object detection and an Intel RealSense camera to estimate object distances in meters.

A key contribution of this project is the comparison between two distance estimation methods:

- 📍 Single pixel distance (traditional approach)
- 📊 Median distance over a region (proposed robust method)

This makes the system suitable for research, experimentation, and academic publications.

## 🚀 Features

- 🎯 Real-time object detection using YOLO
- 📏 Distance estimation using depth data
- 📊 Robust median-based distance calculation
- 📁 Automatic logging to CSV for experiments
- ⚡ Performance metrics (FPS and inference time)
- 🖼️ Annotated image output
- 🔬 Designed for scientific evaluation

## 🛠️ Technologies Used

- Python
- OpenCV
- NumPy
- Intel RealSense SDK (`pyrealsense2`)
- Ultralytics YOLO

## ⚙️ System Architecture

1. Capture synchronized **RGB and Depth frames**
2. Align depth data to the color frame
3. Perform object detection using YOLO
4. Compute object distance:
   - Single pixel (center)
   - Median of surrounding region
5. Save results to CSV
6. Display annotated output

## 📂 Project Structure

```

g1eduyolo/
│── main.py                # Main application
│── results.csv            # Output data (generated)
│── deteccao.jpg           # Annotated frame (generated)
│── requirements.txt       # Dependencies
│── README.md              # Documentation

````

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/vitor-souza-ime/g1eduyolo.git
cd g1eduyolo
````

Install dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ Usage

Run the system:

```bash
python main.py
```

The system will:

* Start the RealSense camera
* Perform object detection
* Estimate distances
* Save results automatically

Press **Ctrl + C** to stop execution.

## 📊 Output Data (CSV)

Each detected object generates a record with:

| Field               | Description                       |
| ------------------- | --------------------------------- |
| frame               | Frame number                      |
| modelo              | YOLO model used                   |
| classe              | Detected class                    |
| confianca           | Detection confidence              |
| dist_pixel_unico    | Distance from single pixel        |
| dist_mediana        | Median distance (proposed method) |
| dist_real_m         | Ground truth distance (manual)    |
| tempo_inferencia_ms | Inference time                    |
| fps                 | Frames per second                 |
| x1,y1,x2,y2         | Bounding box                      |

## 📏 Distance Estimation Methods

### 1. Single Pixel (Baseline)

Distance is computed using the center pixel of the bounding box:

* Fast
* Sensitive to noise
* Unstable in real-world scenarios

### 2. Median Region (Proposed Method)

Distance is computed using the median value of a region around the center:

* More robust
* Reduces noise impact
* Better suited for scientific analysis

## 🧪 Experimental Use

This project is suitable for:

* 📚 Academic research
* 🤖 Robotics applications
* 🚁 UAV navigation
* 🧠 Computer vision studies
* 📊 Performance benchmarking

## 📈 Performance Metrics

The system computes:

* Inference time (ms)
* Frames per second (FPS)
* Average processing time

## ⚠️ Requirements

* Intel RealSense camera (e.g., D435, D415)
* Python 3.8+
* GPU recommended (for YOLO acceleration)

## 📚 References

* Redmon, J. et al. "You Only Look Once: Unified, Real-Time Object Detection"
* Intel RealSense Documentation
* Ultralytics YOLO Documentation

## 🤝 Contribution

Contributions are welcome!

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Submit a Pull Request

## 📄 License

This project is licensed under the MIT License.

## 👨‍🏫 Author

**Vitor Amadeu Souza**
Professor and Researcher in Computer Engineering
Focus: Computer Vision, Embedded Systems, Artificial Intelligence

---

⭐ If this project helps your research, consider giving it a star!

