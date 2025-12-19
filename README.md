
# LEGO-Based Unpaved Road Hazard Detection on IMX500 (YOLOv11)

This project was developed for the **Machine Learning Applications in Automotive Systems (Winter Term 2025/26)** lecture.  
Goal: build an **object detection** system that identifies common unpaved-road hazards in a miniature/LEGO test setup and deploy it on the **Sony IMX500** edge-AI camera.

The model detects:
- **Potholes**
- **Stones**
- **Vegetation / Green area**

This matches the course project scope: training a lightweight YOLO detector, collecting/labeling a custom dataset, evaluating it in a desktop setup, and exporting/deploying the trained network to the IMX500.

---

## Motivation 
Unpaved-road hazards can reduce traction, damage tires, or impact ride comfort specially in south american roads. Detecting hazards like potholes, stones, and vegetation supports:
- safer speed adaptation,
- better path planning,
- early hazard warning for small robotic/vehicle platforms.

---

## System Overview
**Pipeline**
1. Collect images in a LEGO road environment (camera facing forward like a vehicle).
2. Annotate hazards with bounding boxes (YOLO format) using https://www.makesense.ai/ 
3. Fine-tune a **YOLOv11** detector (Ultralytics).
4. Evaluate performance (precision/recall, confusion matrix).
5. Export to **IMX500 format** and package for Raspberry Pi deployment. 

---


## Tech Stack
- **Ultralytics YOLOv11** 
- Python + `uv` environment 
- Export script for IMX500 

---

## Dataset
Images were collected using a forward-facing perspective to simulate a vehicle camera view.  
Labels follow YOLO bounding-box format.

**Classes**
- `pothole`
- `stone`
- `green_area`

---

├── yolo_export.py             # IMX export
└── README.md
# LEGO-Based-Unpaved-Road-Hazard-Detection-on-IMX500-YOLOv11-
