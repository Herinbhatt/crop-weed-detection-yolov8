# inference.py
# Crop and Weed Detection System — Herin Bhatt
# Run this file to detect weeds in any new field image

from ultralytics import YOLO
import cv2
import sys
import os

# ── CONFIG ────────────────────────────────────────────────────────────────────
MODEL_PATH       = "models/best_detection.pt"   # path to your trained model
CONFIDENCE       = 0.4                           # only show detections above 40% confidence
IOU_THRESHOLD    = 0.3                           # overlap threshold for removing duplicate boxes
OUTPUT_FOLDER    = "runs/inference"              # where to save result images

# ── CLASS NAMES ───────────────────────────────────────────────────────────────
CLASS_NAMES = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

# ── MAIN FUNCTION ─────────────────────────────────────────────────────────────
def run_inference(image_path):

    # Check image exists
    if not os.path.exists(image_path):
        print(f"Error: Image not found at '{image_path}'")
        sys.exit(1)

    print(f"\nLoading model from: {MODEL_PATH}")
    model = YOLO(MODEL_PATH)

    print(f"Running detection on: {image_path}")
    results = model.predict(
        source      = image_path,
        conf        = CONFIDENCE,
        iou         = IOU_THRESHOLD,
        save        = True,
        project     = OUTPUT_FOLDER,
        line_width  = 2
    )

    # ── PRINT RESULTS ─────────────────────────────────────────────────────────
    print("\n" + "="*50)
    print("DETECTION RESULTS")
    print("="*50)

    for result in results:
        boxes  = result.boxes.xywh     # x_centre, y_centre, width, height
        labels = result.boxes.cls      # class index
        confs  = result.boxes.conf     # confidence scores

        weed_count = sum(1 for l in labels if int(l) != 16)
        crop_count = sum(1 for l in labels if int(l) == 16)

        print(f"Total detections : {len(boxes)}")
        print(f"Weeds detected   : {weed_count}")
        print(f"Crop plants      : {crop_count}")
        print("-"*50)

        for i, (box, label, conf) in enumerate(zip(boxes, labels, confs)):
            x, y, w, h     = box.tolist()
            class_name     = CLASS_NAMES[int(label)]
            is_weed        = int(label) != 16

            tag = "WEED" if is_weed else "CROP"
            print(f"  [{tag}] {class_name}")
            print(f"         Confidence : {conf:.1%}")
            print(f"         Position   : x={x:.0f}, y={y:.0f}")
            print(f"         Size       : w={w:.0f}px, h={h:.0f}px")
            print()

    print(f"Result image saved to: {OUTPUT_FOLDER}/")
    print("="*50)


# ── RUN ───────────────────────────────────────────────────────────────────────
if __name__ == "__main__":

    # Usage: python inference.py path/to/your/image.jpg
    if len(sys.argv) < 2:
        print("Usage: python inference.py <path_to_image>")
        print("Example: python inference.py field_photo.jpg")
        sys.exit(1)

    image_path = sys.argv[1]
    run_inference(image_path)