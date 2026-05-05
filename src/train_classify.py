# train_classify.py
from ultralytics import YOLO

def train():
    model = YOLO('yolov8n-cls.pt')
    model.train(
        data='data/',
        epochs=100,
        imgsz=640,
        lr0=0.001,
        dropout=0.2
    )

if __name__ == "__main__":
    train()