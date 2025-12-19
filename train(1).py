from ultralytics import YOLO

model = YOLO('yolo11n.pt')
model.train(
    data="/home/mlaa_user01/Downloads/pi-data/yolo_config.yaml",
    epochs=100,
    imgsz=640,
    batch=16
) 




