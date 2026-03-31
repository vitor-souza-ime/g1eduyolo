# 🎯 Evaluation of YOLO Models for Obstacle Detection and Distance Estimation Using a Depth Camera on the Unitree G1 EDU Humanoid Robot

## 📖 Overview

This repository presents the implementation and experimental evaluation of multiple YOLO (You Only Look Once) models for **real-time obstacle detection** and **distance estimation** using a depth camera.

The system is designed for integration with the **Unitree G1 EDU humanoid robot**, leveraging RGB-D data acquired from an Intel RealSense camera.

The primary goal is to analyze detection performance and compare distance estimation strategies in real-world robotic scenarios.

---

## 🎯 Objectives

- Evaluate different YOLO models for obstacle detection
- Estimate object distance using depth data
- Compare distance estimation techniques
- Analyze real-time performance (FPS and inference time)
- Generate experimental data for scientific research

---

## 🚀 Features

- Real-time object detection using YOLO
- Integration with Intel RealSense (RGB-D)
- Depth alignment (depth → color)
- Dual distance estimation methods:
  - Single pixel (baseline)
  - Median region (robust approach)
- Automatic CSV logging for experiments
- Performance metrics (FPS and inference time)
- Annotated image output

---

## 🛠️ Technologies Used

- Python
- OpenCV
- NumPy
- Intel RealSense SDK (`pyrealsense2`)
- Ultralytics YOLO

---

## ⚙️ Methodology

The system follows the pipeline below:

1. Capture synchronized RGB and depth frames
2. Align depth data to the color frame
3. Perform object detection using YOLO
4. Extract bounding boxes and class predictions
5. Estimate distance using two approaches:
   - **Single pixel distance** (center of bounding box)
   - **Median distance** (region around the center)
6. Log all results into a CSV file
7. Display annotated output in real time

---

## 📏 Distance Estimation Approaches

### 1. Single Pixel (Baseline)

- Distance measured at the center pixel of the bounding box
- Fast but sensitive to noise and invalid depth values

### 2. Median Region (Proposed Method)

- Uses a window around the center of the object
- Ignores invalid depth values
- Computes the median for robustness

✔ More stable  
✔ Better suited for real-world environments  
✔ Recommended for scientific analysis  

---

## 📂 Project Structure

```

g1eduyolo/
│── main.py                # Main application
│── results.csv            # Experimental results (generated)
│── deteccao.jpg           # Output frame (generated)
│── requirements.txt       # Dependencies
│── README.md              # Documentation

````id="3z3a3b"

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/vitor-souza-ime/g1eduyolo.git
cd g1eduyolo
````

Install dependencies:

```bash id="t6y8pd"
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the system:

```bash id="k6kqfz"
python main.py
```

The application will:

* Start the RealSense pipeline
* Perform object detection
* Estimate distances
* Save results automatically

Press **Ctrl + C** to stop execution.

---

## 📊 Output Data

Each detection is stored in a CSV file with the following fields:

| Field               | Description                       |
| ------------------- | --------------------------------- |
| frame               | Frame number                      |
| modelo              | YOLO model used                   |
| classe              | Detected class                    |
| confianca           | Detection confidence              |
| dist_pixel_unico    | Distance (single pixel)           |
| dist_mediana        | Distance (median method)          |
| dist_real_m         | Ground truth (manual measurement) |
| tempo_inferencia_ms | Inference time                    |
| fps                 | Frames per second                 |
| x1,y1,x2,y2         | Bounding box                      |

---

## 📈 Performance Metrics

The system records:

* Inference time (milliseconds)
* Frames per second (FPS)
* Average processing time

These metrics are used for comparing YOLO model efficiency.

---

## 🤖 Hardware Platform

* **Robot:** Unitree G1 EDU humanoid robot
* **Depth Camera:** Intel RealSense (D400 series, e.g., D435i)
* **Processing Unit:** Embedded computing platform (GPU recommended)

---

## 🧪 Experimental Applications

* Obstacle detection for humanoid robots
* Autonomous navigation
* Human-robot interaction
* Real-time perception systems
* Performance benchmarking of deep learning models

---

## 📚 References

* Redmon, J. et al. *You Only Look Once: Unified, Real-Time Object Detection*
* Ultralytics YOLO Documentation
* Intel RealSense SDK Documentation

---

## 🤝 Contribution

Contributions are welcome!

1. Fork the repository
2. Create a new branch (`feature/new-feature`)
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍🏫 Author

**Vitor Amadeu Souza**
Professor and Researcher in Computer Engineering
Research Areas: Computer Vision, Robotics, Embedded Systems, Artificial Intelligence

---

⭐ If this repository supports your research, please consider giving it a star!


