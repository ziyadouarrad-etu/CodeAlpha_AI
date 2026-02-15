# CodeAlpha_ObjectDetection&Tracking

### 🤖 Real-Time Multi-Object Tracking & Analytics Pipeline

## 📌 Project Overview

Developed for the **CodeAlpha AI Internship**, this project implements a high-performance computer vision pipeline for real-time object detection and tracking. Using **YOLOv8** and **BoT-SORT**, the system identifies objects, assigns persistent unique IDs, calculates real-time performance metrics (FPS), and logs all activity to a structured data file for post-event analysis.

---

## 🏗️ System Architecture

The project follows a **Modular Design Pattern**, ensuring that each stage of the pipeline is isolated and independently maintainable:

1.  **Input Stage (`VideoManager`):** Handles stream synchronization from either a live webcam or local video files using OpenCV.
2.  **Inference Stage (`ObjectDetector`):** Leverages a YOLOv8 neural network to perform detection and motion-based tracking. It maps raw tensor outputs to semantic class names.
3.  **Analytics Stage (`DataLogger`):** Records object persistence, class types, and confidence scores into a CSV format.
4.  **Visualization Stage (`Visualizer`):** Renders high-fidelity bounding boxes, unique Tracking IDs, and a dynamic FPS counter on the output stream.

---

## 🛠️ Key Technical Features

-   **Persistent Tracking:** Uses BoT-SORT to ensure object IDs remain consistent even during partial occlusions or fast movement.
-   **Hardware Agnostic:** Automated hardware detection that utilizes **NVIDIA CUDA** when available, with an optimized fallback for **Intel Integrated GPUs** (CPU mode).
-   **Data Persistence:** Generates a `session_log.csv` containing timestamps and unique IDs, enabling future data analysis or database integration.
-   **CLI Versatility:** Fully configurable through Command Line Arguments for easy testing across different environments.

---

### 📂 Project Structure

This section demonstrates your ability to organize a modular AI pipeline. It makes the code easy to navigate for other developers.

Plaintext

```
CodeAlpha_ObjectDetection/├── models/                 # Pre-trained YOLOv8 weights (.pt files)├── src/                    # Core logic package│ ├── __init__.py           # Marks directory as a Python package│ ├── detector.py           # Stage 2: YOLOv8 Inference & BoT-SORT Tracking│ ├── logger.py             # Stage 4: CSV Data logging logic│ ├── video_manager.py      # Stage 1: Robust Input (File/Webcam) handling│ └── visualizer.py         # Stage 3: OpenCV Drawing & UI overlays├── logs/                   # Storage for generated session CSV files├── main.py                 # Orchestrator & CLI Entry Point├── requirements.txt        # Project dependencies└── README.md               # Technical documentation
```

---

## 🚀 Getting Started

### 1. Installation

PowerShell

```
# Clone the repositorygit clone https://github.com/ziyadouarrad-etu/CodeAlpha_ObjectDetection-Tracking.git# Install dependenciespipinstall -r requirements.txt
```

### 2. Usage

**To run with your default webcam:**

PowerShell

```
python main.py
```

**CLI Commands & Usage**

The application is controlled via a Command Line Interface (CLI). This allows you to switch between cameras, models, and logging modes without modifying the source code.

**Command Arguments**

**Option**

**Type**

**Default**

**Description**

`--video`

`String/Int`

`0`

Path to a `.mp4` file or a Camera Index (e.g., `1` for iPhone/Camo).

`--model`

`String`

`yolov8n.pt`

YOLOv8 model version (`yolov8n.pt`, `yolov8s.pt`, `yolov8m.pt`).

`--log`

`Integer`

`0`

Enable (`1`) or Disable (`0`) CSV data logging.

  

#### **Example Usage Scenarios:**

**1. Development (Internal Webcam, No Logging):**

PowerShell

```
python main.py
```

**2. Professional Demo (iPhone via Camo + Logging):**

PowerShell

```
python main.py --video 1 --log 1
```

**3. High-Accuracy Analysis (Video File + Medium Model):**

PowerShell

```
python main.py --video "detection_test.mp4" --model yolov8m.pt --log 1
```

---

### 👤 Made By

**Ziyad Ouarrad** *AI & CS Engineering Student at ENSAM Casablanca* *AI/ML Trainer at GDG on Campus ENSAM Casablanca*

---

### 🙏 Acknowledgments

I would like to extend my gratitude to **CodeAlpha** for providing this internship opportunity and for the challenging tasks that have allowed me to sharpen my skills in Artificial Intelligence and Computer Vision.