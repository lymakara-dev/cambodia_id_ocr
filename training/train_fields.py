from ultralytics import YOLO

model = YOLO("yolov8n.pt")

model.train(
    data="datasets/fields/dataset.yaml",
    epochs=100,
    imgsz=640,
    batch=8,
    device=0,
    name="cambodia_id_fields"
)