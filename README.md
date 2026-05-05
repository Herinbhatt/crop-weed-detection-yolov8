<div class="md">
 
      <!-- Hero -->
      <div class="hero-banner">
        <div class="hero-title">🌿 Crop and Weed Detection System</div>
        <div class="hero-sub">
          Two-stage YOLOv8 pipeline for precision agriculture in Indian soybean fields<br>
          <em>Final Year B.E. Project · Neotech Campus, Vadodara · GTU · 2025</em>
        </div>
        <div class="badge-row">
          <div class="gh-badge"><span class="bl">accuracy</span><span class="br green">90%+</span></div>
          <div class="gh-badge"><span class="bl">framework</span><span class="br blue">YOLOv8</span></div>
          <div class="gh-badge"><span class="bl">dataset</span><span class="br teal">MH-16</span></div>
          <div class="gh-badge"><span class="bl">species</span><span class="br orange">16 weeds</span></div>
          <div class="gh-badge"><span class="bl">python</span><span class="br purple">3.10</span></div>
          <div class="gh-badge"><span class="bl">license</span><span class="br red">MIT</span></div>
        </div>
      </div>
 
      <!-- Result cards -->
      <div class="result-grid">
        <div class="result-card">
          <span class="num">90%+</span>
          <span class="lbl">Top-1 Classification<br>Accuracy</span>
        </div>
        <div class="result-card">
          <span class="num">16</span>
          <span class="lbl">Indian Weed Species<br>Detected</span>
        </div>
        <div class="result-card">
          <span class="num">24k+</span>
          <span class="lbl">Training Images<br>Processed</span>
        </div>
        <div class="result-card">
          <span class="num">100</span>
          <span class="lbl">Training Epochs<br>(After Fine-Tuning)</span>
        </div>
      </div>
 
      <h2>📋 Table of Contents</h2>
      <ul>
        <li><a href="#">Problem Statement</a></li>
        <li><a href="#">What This Project Does</a></li>
        <li><a href="#">Pipeline Architecture</a></li>
        <li><a href="#">Dataset</a></li>
        <li><a href="#">Results</a></li>
        <li><a href="#">How to Run</a></li>
        <li><a href="#">Project Structure</a></li>
        <li><a href="#">Limitations</a></li>
        <li><a href="#">Future Work</a></li>
        <li><a href="#">Acknowledgements</a></li>
      </ul>
 
      <hr>
 
      <h2>🌾 Problem Statement</h2>
      <p>
        Soybean is one of India's most important crops, grown primarily in Madhya Pradesh, Maharashtra, and Rajasthan. During the <strong>first 15–45 days after sowing</strong>, soybean plants grow slowly with wide row spacing — creating ideal conditions for fast-growing weeds to establish themselves.
      </p>
      <p>
        If uncontrolled during this window, <strong>yield losses range from 30% to 80%</strong>. The conventional response — blanket herbicide spraying across entire fields — causes:
      </p>
      <ul>
        <li>Direct chemical damage to healthy soybean plants</li>
        <li>Long-term soil health degradation and loss of microbial diversity</li>
        <li>Groundwater contamination in surrounding ecosystems</li>
        <li>Chemical residues in the food chain</li>
      </ul>
      <blockquote>
        An intelligent system that locates weeds at individual plant level enables targeted treatment — applying chemicals <em>only where weeds actually are</em> — rather than saturating entire fields.
      </blockquote>
 
      <h2>🎯 What This Project Does</h2>
      <p>
        This project implements a <strong>two-stage deep learning pipeline</strong> that:
      </p>
      <ol>
        <li><strong>Classifies</strong> each plant image as one of 16 weed species or soybean crop (17 classes total)</li>
        <li><strong>Detects and localises</strong> each weed in a full field image — drawing labelled bounding boxes around every individual weed plant</li>
        <li><strong>Outputs coordinates</strong> in <code>(x, y, w, h)</code> format suitable for driving a precision sprayer actuator on a drone or ground robot</li>
      </ol>
 
      <h2>🏗️ Pipeline Architecture</h2>
 
      <h3>Training Pipeline</h3>
      <div class="pipeline">
        <div class="pipe-step"><div class="pt">MH-16 Dataset</div><div class="ps">Raw field images</div></div>
        <div class="pipe-arrow">→</div>
        <div class="pipe-step"><div class="pt">Data Cleaning</div><div class="ps">Remove corrupt/blur</div></div>
        <div class="pipe-arrow">→</div>
        <div class="pipe-step"><div class="pt">Augmentation</div><div class="ps">Balance to 1,500/class</div></div>
        <div class="pipe-arrow">→</div>
        <div class="pipe-step"><div class="pt">YOLOv8 Train</div><div class="ps">Stage 1 + Stage 2</div></div>
        <div class="pipe-arrow">→</div>
        <div class="pipe-step"><div class="pt">Fine-Tuning</div><div class="ps">LR + epochs + dropout</div></div>
        <div class="pipe-arrow">→</div>
        <div class="pipe-step"><div class="pt">Model Weights</div><div class="ps">.pt files saved</div></div>
      </div>
 
      <h3>Inference Pipeline</h3>
      <div class="pipeline">
        <div class="pipe-step"><div class="pt">Field Image</div><div class="ps">Camera / drone / file</div></div>
        <div class="pipe-arrow">→</div>
        <div class="pipe-step"><div class="pt">Preprocess</div><div class="ps">Resize + normalise</div></div>
        <div class="pipe-arrow">→</div>
        <div class="pipe-step"><div class="pt">Stage 1</div><div class="ps">Species classification</div></div>
        <div class="pipe-arrow">→</div>
        <div class="pipe-step"><div class="pt">Stage 2</div><div class="ps">Bounding box detection</div></div>
        <div class="pipe-arrow">→</div>
        <div class="pipe-step"><div class="pt">Output</div><div class="ps">(x,y,w,h) + label</div></div>
      </div>
 
      <h2>📊 Dataset — MH-16 Weed Dataset</h2>
      <p>
        The <strong>MH-16 (Maharashtra-16) Weed Dataset</strong> is an Indian agricultural dataset containing images of 16 distinct weed species commonly found in soybean fields across Maharashtra and surrounding states. It was curated to address the lack of region-specific datasets for precision agriculture in India.
      </p>
 
      <table>
        <thead><tr><th>#</th><th>Species</th><th>Common Name</th><th>Type</th><th>Prevalence</th></tr></thead>
        <tbody>
          <tr><td>0</td><td><em>Commelina benghalensis</em></td><td>Kena</td><td>Broadleaf</td><td>🔴 Very High</td></tr>
          <tr><td>1</td><td><em>Parthenium hysterophorus</em></td><td>Gajar Gavat</td><td>Broadleaf</td><td>🟠 High</td></tr>
          <tr><td>2</td><td><em>Cynodon dactylon</em></td><td>Harali</td><td>Grass</td><td>🟠 High</td></tr>
          <tr><td>3</td><td><em>Malva parviflora</em></td><td>Little Mallow</td><td>Broadleaf</td><td>🟡 Moderate</td></tr>
          <tr><td>4</td><td><em>Cyperus rotundus</em></td><td>Lavhala</td><td>Sedge</td><td>🟠 High</td></tr>
          <tr><td>5</td><td><em>Euphorbia geniculata</em></td><td>Moti Dudhi</td><td>Broadleaf</td><td>🟠 High</td></tr>
          <tr><td>6</td><td><em>Ipomoea obscura</em></td><td>Morning Glory</td><td>Creeper</td><td>🟡 Moderate</td></tr>
          <tr><td>7</td><td><em>Digitaria sanguinalis</em></td><td>Digitaria</td><td>Grass</td><td>🟡 Moderate</td></tr>
          <tr><td>8</td><td><em>Clitoria ternatea</em></td><td>Pigeon Wings</td><td>Creeper</td><td>🟡 Moderate</td></tr>
          <tr><td>9</td><td><em>Euphorbia hypericifolia</em></td><td>Sandmat</td><td>Broadleaf</td><td>🟡 Moderate</td></tr>
          <tr><td>10</td><td><em>Argemone mexicana</em></td><td>Bilayat</td><td>Broadleaf</td><td>🟡 Moderate</td></tr>
          <tr><td>11</td><td><em>Chamaecrista pumila</em></td><td>Dwarf Cassia</td><td>Broadleaf</td><td>🟡 Moderate</td></tr>
          <tr><td>12</td><td><em>Senna obtusifolia</em></td><td>Sicklepod</td><td>Broadleaf</td><td>🟡 Moderate</td></tr>
          <tr><td>13</td><td><em>Chenopodium album</em></td><td>Lambs Quarter</td><td>Broadleaf</td><td>🟡 Moderate</td></tr>
          <tr><td>14</td><td><em>Euphorbia hirta</em></td><td>Choti Dudhi</td><td>Broadleaf</td><td>🟢 Low–Mod</td></tr>
          <tr><td>15</td><td><em>Boerhaavia diffusa</em></td><td>Punarnava</td><td>Broadleaf</td><td>🟠 High</td></tr>
        </tbody>
      </table>
 
      <h3>Data Preprocessing Steps</h3>
      <ul>
        <li>Removed corrupt, blurry, and unreadable image files</li>
        <li>Standardised all images to <code>640×640</code> pixels</li>
        <li>Balanced each class to <strong>1,500 samples</strong> using augmentation where needed</li>
        <li>Augmentation applied: horizontal/vertical flips, rotation <code>±15°</code>, brightness and contrast variation</li>
        <li>Train/test split: <strong>80% training, 20% testing</strong></li>
        <li>Created YOLO-format annotation <code>.txt</code> files for object detection training</li>
      </ul>
 
      <h2>📈 Results</h2>
 
      <h3>Stage 1 — Classification Model</h3>
      <div class="callout success">
        ✅ &nbsp;<strong>Final Result: 90%+ top-1 classification accuracy</strong> on held-out test set after fine-tuning.
      </div>
 
      <table>
        <thead><tr><th>Metric</th><th>Initial (50 epochs)</th><th>After Fine-Tuning (100 epochs)</th></tr></thead>
        <tbody>
          <tr><td>Top-1 Accuracy</td><td>&lt; 90%</td><td><strong>&gt; 90%</strong></td></tr>
          <tr><td>Top-5 Accuracy</td><td>~99.98%</td><td><strong>~100%</strong></td></tr>
          <tr><td>Train Loss</td><td>~0.16 → 0.10</td><td><strong>~0.16 → 0.07</strong></td></tr>
          <tr><td>Val Loss</td><td>~0.09 → 0.05</td><td><strong>~0.09 → 0.03</strong></td></tr>
          <tr><td>Learning Rate</td><td>0.01</td><td><strong>0.001</strong></td></tr>
        </tbody>
      </table>
 
      <p><strong>Fine-tuning steps taken:</strong></p>
      <ul>
        <li>Reduced learning rate: <code>0.01</code> → <code>0.001</code></li>
        <li>Extended training from 50 → <code>100 epochs</code></li>
        <li>Added <strong>dropout regularisation</strong> to reduce overfitting</li>
      </ul>
 
      <h3>Stage 2 — Object Detection Model</h3>
      <div class="callout info">
        ℹ️ &nbsp;Detection model trained on YOLO-format bounding box annotations generated using Stage 1 classification outputs as reference.
      </div>
 
      <table>
        <thead><tr><th>Metric</th><th>Value</th></tr></thead>
        <tbody>
          <tr><td>mAP@0.5</td><td>~0.82</td></tr>
          <tr><td>Precision</td><td>~0.85</td></tr>
          <tr><td>Recall</td><td>~0.80</td></tr>
          <tr><td>Training Epochs</td><td>50</td></tr>
          <tr><td>Hardware</td><td>Google Colab T4 GPU (15 GB VRAM)</td></tr>
        </tbody>
      </table>
 
      <div class="screenshot">
        <span class="icon">🖼️</span>
        <strong>Detection output samples</strong><br>
        <em>See <code>results/detection_samples.png</code> — bounding boxes around each detected weed with species label and confidence score</em>
      </div>
 
      <h2>🚀 How to Run</h2>
 
      <h3>1. Clone the Repository</h3>
      <div class="lang-bar">bash</div>
      <pre><code>git clone https://github.com/herinbhatt/crop-weed-detection-yolov8.git
cd crop-weed-detection-yolov8</code></pre>
 
      <h3>2. Install Dependencies</h3>
      <div class="lang-bar">bash</div>
      <pre><code>pip install -r requirements.txt</code></pre>
 
      <div class="lang-bar">txt — requirements.txt</div>
      <pre><code>ultralytics>=8.0.0
torch>=2.0.0
torchvision>=0.15.0
opencv-python>=4.8.0
numpy>=1.24.0
matplotlib>=3.7.0
Pillow>=10.0.0
pandas>=2.0.0</code></pre>
 
      <h3>3. Download the Dataset</h3>
      <div class="lang-bar">bash</div>
      <pre><code># Download MH-16 dataset from Kaggle
# https://www.kaggle.com/datasets/mh16-indian-soybean-weed-dataset
 
# After download, place in:
# data/train/images/   data/train/labels/
# data/test/images/    data/test/labels/</code></pre>
 
      <h3>4. Train Classification Model (Stage 1)</h3>
      <div class="lang-bar">python</div>
      <pre><code>from ultralytics import YOLO
 
# Load pretrained YOLOv8 classification model
model = YOLO('yolov8n-cls.pt')
 
# Train on MH-16 dataset
results = model.train(
    data='data/',          # path to dataset root
    epochs=100,
    imgsz=640,
    batch=16,
    lr0=0.001,             # fine-tuned learning rate
    dropout=0.2,           # regularisation
    project='runs/classify',
    name='mh16_weed_cls'
)</code></pre>
 
      <h3>5. Train Object Detection Model (Stage 2)</h3>
      <div class="lang-bar">python</div>
      <pre><code>from ultralytics import YOLO
 
# Load pretrained YOLOv8 detection model
model = YOLO('yolov8s.pt')
 
# Train detection model
results = model.train(
    data='data/data.yaml',
    epochs=50,
    imgsz=640,
    batch=8,
    project='runs/detect',
    name='mh16_weed_det'
)</code></pre>
 
      <h3>6. Run Inference on a New Image</h3>
      <div class="lang-bar">python</div>
      <pre><code>from ultralytics import YOLO
import cv2
 
# Load trained detection model
model = YOLO('models/best_detection.pt')
 
# Run on a field image
results = model.predict(
    source='path/to/field_image.jpg',
    conf=0.4,
    save=True,
    project='runs/inference'
)
 
# Each result contains bounding boxes in (x, y, w, h) format
# — suitable for driving a precision sprayer actuator
for r in results:
    boxes = r.boxes.xywh   # (x_centre, y_centre, width, height)
    labels = r.boxes.cls   # class index
    confs  = r.boxes.conf  # confidence scores
    print(f"Detected {len(boxes)} weeds")</code></pre>
 
      <h2>⚠️ Known Limitations</h2>
      <div class="callout warn">
        ⚠️ &nbsp;These limitations are documented honestly — understanding failure modes is part of responsible AI engineering.
      </div>
      <ul>
        <li><strong>Species scope:</strong> Trained only on MH-16 — weed species not in this dataset will be misclassified or missed</li>
        <li><strong>Crop scope:</strong> Only soybean crop images used — cannot reliably identify other crop types</li>
        <li><strong>Lighting:</strong> Performance degrades under heavy shadow, overcast sky, or dense canopy cover</li>
        <li><strong>Overlap:</strong> Bounding boxes partially merge for heavily overlapping plants (instance segmentation would solve this)</li>
        <li><strong>Deployment:</strong> Not yet deployed on edge hardware — runs on Colab T4 GPU only</li>
      </ul>
 
      <h2>🔭 Future Work</h2>
      <ul>
        <li>Upgrade to <strong>YOLOv8-seg</strong> for pixel-level instance segmentation — enabling more precise spray targeting</li>
        <li>Optimise with <strong>TensorRT</strong> for real-time inference on NVIDIA Jetson Nano (target: 30+ FPS)</li>
        <li>Expand dataset to wheat, rice, and cotton fields across Indian states</li>
        <li>Integrate with <strong>ROS</strong> for sensor fusion (camera + GPS + IMU) for precise field localisation</li>
        <li>Develop mobile interface for farmers to upload field images and receive weed density maps</li>
        <li>Collaborate with agricultural research institutions for real field validation</li>
      </ul>
 
      <h2>🙏 Acknowledgements</h2>
      <div class="ack">
        <ul>
          <li><strong>MH-16 Weed Dataset</strong> — Indian agricultural dataset curated for precision agriculture research</li>
          <li><strong>Ultralytics YOLOv8</strong> — Framework that made high-performance object detection accessible</li>
          <li><strong>Google Colab</strong> — Free GPU access (T4, 15 GB VRAM) that made training feasible without expensive hardware</li>
          <li><strong>Mr. Sanjay Macwan</strong> — Internal guide and Head of Department, Computer Engineering, Neotech Campus</li>
          <li><strong>Neotech Campus, Vadodara</strong> — Department resources and academic support</li>
        </ul>
      </div>
 
      <hr>
 
      <p style="text-align:center; color: #8b949e; font-size: 13px; margin-top: 20px;">
        <strong style="color:#e6edf3;">Herin Bhatt</strong> · herinbhattflux@gmail.com · Vadodara, India<br>
        B.E. Computer Engineering · Neotech Campus · Gujarat Technological University · 2025<br>
        <a href="#">github.com/herinbhatt</a> · <a href="#">linkedin.com/in/herinbhatt</a>
      </p>
 
    </div><!-- .md --><div class="md">
 
      <!-- Hero -->
      <div class="hero-banner">
        <div class="hero-title">🌿 Crop and Weed Detection System</div>
        <div class="hero-sub">
          Two-stage YOLOv8 pipeline for precision agriculture in Indian soybean fields<br>
          <em>Final Year B.E. Project · Neotech Campus, Vadodara · GTU · 2025</em>
        </div>
        <div class="badge-row">
          <div class="gh-badge"><span class="bl">accuracy</span><span class="br green">90%+</span></div>
          <div class="gh-badge"><span class="bl">framework</span><span class="br blue">YOLOv8</span></div>
          <div class="gh-badge"><span class="bl">dataset</span><span class="br teal">MH-16</span></div>
          <div class="gh-badge"><span class="bl">species</span><span class="br orange">16 weeds</span></div>
          <div class="gh-badge"><span class="bl">python</span><span class="br purple">3.10</span></div>
          <div class="gh-badge"><span class="bl">license</span><span class="br red">MIT</span></div>
        </div>
      </div>
 
      <!-- Result cards -->
      <div class="result-grid">
        <div class="result-card">
          <span class="num">90%+</span>
          <span class="lbl">Top-1 Classification<br>Accuracy</span>
        </div>
        <div class="result-card">
          <span class="num">16</span>
          <span class="lbl">Indian Weed Species<br>Detected</span>
        </div>
        <div class="result-card">
          <span class="num">24k+</span>
          <span class="lbl">Training Images<br>Processed</span>
        </div>
        <div class="result-card">
          <span class="num">100</span>
          <span class="lbl">Training Epochs<br>(After Fine-Tuning)</span>
        </div>
      </div>
 
      <h2>📋 Table of Contents</h2>
      <ul>
        <li><a href="#">Problem Statement</a></li>
        <li><a href="#">What This Project Does</a></li>
        <li><a href="#">Pipeline Architecture</a></li>
        <li><a href="#">Dataset</a></li>
        <li><a href="#">Results</a></li>
        <li><a href="#">How to Run</a></li>
        <li><a href="#">Project Structure</a></li>
        <li><a href="#">Limitations</a></li>
        <li><a href="#">Future Work</a></li>
        <li><a href="#">Acknowledgements</a></li>
      </ul>
 
      <hr>
 
      <h2>🌾 Problem Statement</h2>
      <p>
        Soybean is one of India's most important crops, grown primarily in Madhya Pradesh, Maharashtra, and Rajasthan. During the <strong>first 15–45 days after sowing</strong>, soybean plants grow slowly with wide row spacing — creating ideal conditions for fast-growing weeds to establish themselves.
      </p>
      <p>
        If uncontrolled during this window, <strong>yield losses range from 30% to 80%</strong>. The conventional response — blanket herbicide spraying across entire fields — causes:
      </p>
      <ul>
        <li>Direct chemical damage to healthy soybean plants</li>
        <li>Long-term soil health degradation and loss of microbial diversity</li>
        <li>Groundwater contamination in surrounding ecosystems</li>
        <li>Chemical residues in the food chain</li>
      </ul>
      <blockquote>
        An intelligent system that locates weeds at individual plant level enables targeted treatment — applying chemicals <em>only where weeds actually are</em> — rather than saturating entire fields.
      </blockquote>
 
      <h2>🎯 What This Project Does</h2>
      <p>
        This project implements a <strong>two-stage deep learning pipeline</strong> that:
      </p>
      <ol>
        <li><strong>Classifies</strong> each plant image as one of 16 weed species or soybean crop (17 classes total)</li>
        <li><strong>Detects and localises</strong> each weed in a full field image — drawing labelled bounding boxes around every individual weed plant</li>
        <li><strong>Outputs coordinates</strong> in <code>(x, y, w, h)</code> format suitable for driving a precision sprayer actuator on a drone or ground robot</li>
      </ol>
 
      <h2>🏗️ Pipeline Architecture</h2>
 
      <h3>Training Pipeline</h3>
      <div class="pipeline">
        <div class="pipe-step"><div class="pt">MH-16 Dataset</div><div class="ps">Raw field images</div></div>
        <div class="pipe-arrow">→</div>
        <div class="pipe-step"><div class="pt">Data Cleaning</div><div class="ps">Remove corrupt/blur</div></div>
        <div class="pipe-arrow">→</div>
        <div class="pipe-step"><div class="pt">Augmentation</div><div class="ps">Balance to 1,500/class</div></div>
        <div class="pipe-arrow">→</div>
        <div class="pipe-step"><div class="pt">YOLOv8 Train</div><div class="ps">Stage 1 + Stage 2</div></div>
        <div class="pipe-arrow">→</div>
        <div class="pipe-step"><div class="pt">Fine-Tuning</div><div class="ps">LR + epochs + dropout</div></div>
        <div class="pipe-arrow">→</div>
        <div class="pipe-step"><div class="pt">Model Weights</div><div class="ps">.pt files saved</div></div>
      </div>
 
      <h3>Inference Pipeline</h3>
      <div class="pipeline">
        <div class="pipe-step"><div class="pt">Field Image</div><div class="ps">Camera / drone / file</div></div>
        <div class="pipe-arrow">→</div>
        <div class="pipe-step"><div class="pt">Preprocess</div><div class="ps">Resize + normalise</div></div>
        <div class="pipe-arrow">→</div>
        <div class="pipe-step"><div class="pt">Stage 1</div><div class="ps">Species classification</div></div>
        <div class="pipe-arrow">→</div>
        <div class="pipe-step"><div class="pt">Stage 2</div><div class="ps">Bounding box detection</div></div>
        <div class="pipe-arrow">→</div>
        <div class="pipe-step"><div class="pt">Output</div><div class="ps">(x,y,w,h) + label</div></div>
      </div>
 
      <h2>📊 Dataset — MH-16 Weed Dataset</h2>
      <p>
        The <strong>MH-16 (Maharashtra-16) Weed Dataset</strong> is an Indian agricultural dataset containing images of 16 distinct weed species commonly found in soybean fields across Maharashtra and surrounding states. It was curated to address the lack of region-specific datasets for precision agriculture in India.
      </p>
 
      <table>
        <thead><tr><th>#</th><th>Species</th><th>Common Name</th><th>Type</th><th>Prevalence</th></tr></thead>
        <tbody>
          <tr><td>0</td><td><em>Commelina benghalensis</em></td><td>Kena</td><td>Broadleaf</td><td>🔴 Very High</td></tr>
          <tr><td>1</td><td><em>Parthenium hysterophorus</em></td><td>Gajar Gavat</td><td>Broadleaf</td><td>🟠 High</td></tr>
          <tr><td>2</td><td><em>Cynodon dactylon</em></td><td>Harali</td><td>Grass</td><td>🟠 High</td></tr>
          <tr><td>3</td><td><em>Malva parviflora</em></td><td>Little Mallow</td><td>Broadleaf</td><td>🟡 Moderate</td></tr>
          <tr><td>4</td><td><em>Cyperus rotundus</em></td><td>Lavhala</td><td>Sedge</td><td>🟠 High</td></tr>
          <tr><td>5</td><td><em>Euphorbia geniculata</em></td><td>Moti Dudhi</td><td>Broadleaf</td><td>🟠 High</td></tr>
          <tr><td>6</td><td><em>Ipomoea obscura</em></td><td>Morning Glory</td><td>Creeper</td><td>🟡 Moderate</td></tr>
          <tr><td>7</td><td><em>Digitaria sanguinalis</em></td><td>Digitaria</td><td>Grass</td><td>🟡 Moderate</td></tr>
          <tr><td>8</td><td><em>Clitoria ternatea</em></td><td>Pigeon Wings</td><td>Creeper</td><td>🟡 Moderate</td></tr>
          <tr><td>9</td><td><em>Euphorbia hypericifolia</em></td><td>Sandmat</td><td>Broadleaf</td><td>🟡 Moderate</td></tr>
          <tr><td>10</td><td><em>Argemone mexicana</em></td><td>Bilayat</td><td>Broadleaf</td><td>🟡 Moderate</td></tr>
          <tr><td>11</td><td><em>Chamaecrista pumila</em></td><td>Dwarf Cassia</td><td>Broadleaf</td><td>🟡 Moderate</td></tr>
          <tr><td>12</td><td><em>Senna obtusifolia</em></td><td>Sicklepod</td><td>Broadleaf</td><td>🟡 Moderate</td></tr>
          <tr><td>13</td><td><em>Chenopodium album</em></td><td>Lambs Quarter</td><td>Broadleaf</td><td>🟡 Moderate</td></tr>
          <tr><td>14</td><td><em>Euphorbia hirta</em></td><td>Choti Dudhi</td><td>Broadleaf</td><td>🟢 Low–Mod</td></tr>
          <tr><td>15</td><td><em>Boerhaavia diffusa</em></td><td>Punarnava</td><td>Broadleaf</td><td>🟠 High</td></tr>
        </tbody>
      </table>
 
      <h3>Data Preprocessing Steps</h3>
      <ul>
        <li>Removed corrupt, blurry, and unreadable image files</li>
        <li>Standardised all images to <code>640×640</code> pixels</li>
        <li>Balanced each class to <strong>1,500 samples</strong> using augmentation where needed</li>
        <li>Augmentation applied: horizontal/vertical flips, rotation <code>±15°</code>, brightness and contrast variation</li>
        <li>Train/test split: <strong>80% training, 20% testing</strong></li>
        <li>Created YOLO-format annotation <code>.txt</code> files for object detection training</li>
      </ul>
 
      <h2>📈 Results</h2>
 
      <h3>Stage 1 — Classification Model</h3>
      <div class="callout success">
        ✅ &nbsp;<strong>Final Result: 90%+ top-1 classification accuracy</strong> on held-out test set after fine-tuning.
      </div>
 
      <table>
        <thead><tr><th>Metric</th><th>Initial (50 epochs)</th><th>After Fine-Tuning (100 epochs)</th></tr></thead>
        <tbody>
          <tr><td>Top-1 Accuracy</td><td>&lt; 90%</td><td><strong>&gt; 90%</strong></td></tr>
          <tr><td>Top-5 Accuracy</td><td>~99.98%</td><td><strong>~100%</strong></td></tr>
          <tr><td>Train Loss</td><td>~0.16 → 0.10</td><td><strong>~0.16 → 0.07</strong></td></tr>
          <tr><td>Val Loss</td><td>~0.09 → 0.05</td><td><strong>~0.09 → 0.03</strong></td></tr>
          <tr><td>Learning Rate</td><td>0.01</td><td><strong>0.001</strong></td></tr>
        </tbody>
      </table>
 
      <p><strong>Fine-tuning steps taken:</strong></p>
      <ul>
        <li>Reduced learning rate: <code>0.01</code> → <code>0.001</code></li>
        <li>Extended training from 50 → <code>100 epochs</code></li>
        <li>Added <strong>dropout regularisation</strong> to reduce overfitting</li>
      </ul>
 
      <h3>Stage 2 — Object Detection Model</h3>
      <div class="callout info">
        ℹ️ &nbsp;Detection model trained on YOLO-format bounding box annotations generated using Stage 1 classification outputs as reference.
      </div>
 
      <table>
        <thead><tr><th>Metric</th><th>Value</th></tr></thead>
        <tbody>
          <tr><td>mAP@0.5</td><td>~0.82</td></tr>
          <tr><td>Precision</td><td>~0.85</td></tr>
          <tr><td>Recall</td><td>~0.80</td></tr>
          <tr><td>Training Epochs</td><td>50</td></tr>
          <tr><td>Hardware</td><td>Google Colab T4 GPU (15 GB VRAM)</td></tr>
        </tbody>
      </table>
 
      <div class="screenshot">
        <span class="icon">🖼️</span>
        <strong>Detection output samples</strong><br>
        <em>See <code>results/detection_samples.png</code> — bounding boxes around each detected weed with species label and confidence score</em>
      </div>
 
      <h2>🚀 How to Run</h2>
 
      <h3>1. Clone the Repository</h3>
      <div class="lang-bar">bash</div>
      <pre><code>git clone https://github.com/herinbhatt/crop-weed-detection-yolov8.git
cd crop-weed-detection-yolov8</code></pre>
 
      <h3>2. Install Dependencies</h3>
      <div class="lang-bar">bash</div>
      <pre><code>pip install -r requirements.txt</code></pre>
 
      <div class="lang-bar">txt — requirements.txt</div>
      <pre><code>ultralytics>=8.0.0
torch>=2.0.0
torchvision>=0.15.0
opencv-python>=4.8.0
numpy>=1.24.0
matplotlib>=3.7.0
Pillow>=10.0.0
pandas>=2.0.0</code></pre>
 
      <h3>3. Download the Dataset</h3>
      <div class="lang-bar">bash</div>
      <pre><code># Download MH-16 dataset from Kaggle
# https://www.kaggle.com/datasets/mh16-indian-soybean-weed-dataset
 
# After download, place in:
# data/train/images/   data/train/labels/
# data/test/images/    data/test/labels/</code></pre>
 
      <h3>4. Train Classification Model (Stage 1)</h3>
      <div class="lang-bar">python</div>
      <pre><code>from ultralytics import YOLO
 
# Load pretrained YOLOv8 classification model
model = YOLO('yolov8n-cls.pt')
 
# Train on MH-16 dataset
results = model.train(
    data='data/',          # path to dataset root
    epochs=100,
    imgsz=640,
    batch=16,
    lr0=0.001,             # fine-tuned learning rate
    dropout=0.2,           # regularisation
    project='runs/classify',
    name='mh16_weed_cls'
)</code></pre>
 
      <h3>5. Train Object Detection Model (Stage 2)</h3>
      <div class="lang-bar">python</div>
      <pre><code>from ultralytics import YOLO
 
# Load pretrained YOLOv8 detection model
model = YOLO('yolov8s.pt')
 
# Train detection model
results = model.train(
    data='data/data.yaml',
    epochs=50,
    imgsz=640,
    batch=8,
    project='runs/detect',
    name='mh16_weed_det'
)</code></pre>
 
      <h3>6. Run Inference on a New Image</h3>
      <div class="lang-bar">python</div>
      <pre><code>from ultralytics import YOLO
import cv2
 
# Load trained detection model
model = YOLO('models/best_detection.pt')
 
# Run on a field image
results = model.predict(
    source='path/to/field_image.jpg',
    conf=0.4,
    save=True,
    project='runs/inference'
)
 
# Each result contains bounding boxes in (x, y, w, h) format
# — suitable for driving a precision sprayer actuator
for r in results:
    boxes = r.boxes.xywh   # (x_centre, y_centre, width, height)
    labels = r.boxes.cls   # class index
    confs  = r.boxes.conf  # confidence scores
    print(f"Detected {len(boxes)} weeds")</code></pre>
 
      <h2>⚠️ Known Limitations</h2>
      <div class="callout warn">
        ⚠️ &nbsp;These limitations are documented honestly — understanding failure modes is part of responsible AI engineering.
      </div>
      <ul>
        <li><strong>Species scope:</strong> Trained only on MH-16 — weed species not in this dataset will be misclassified or missed</li>
        <li><strong>Crop scope:</strong> Only soybean crop images used — cannot reliably identify other crop types</li>
        <li><strong>Lighting:</strong> Performance degrades under heavy shadow, overcast sky, or dense canopy cover</li>
        <li><strong>Overlap:</strong> Bounding boxes partially merge for heavily overlapping plants (instance segmentation would solve this)</li>
        <li><strong>Deployment:</strong> Not yet deployed on edge hardware — runs on Colab T4 GPU only</li>
      </ul>
 
      <h2>🔭 Future Work</h2>
      <ul>
        <li>Upgrade to <strong>YOLOv8-seg</strong> for pixel-level instance segmentation — enabling more precise spray targeting</li>
        <li>Optimise with <strong>TensorRT</strong> for real-time inference on NVIDIA Jetson Nano (target: 30+ FPS)</li>
        <li>Expand dataset to wheat, rice, and cotton fields across Indian states</li>
        <li>Integrate with <strong>ROS</strong> for sensor fusion (camera + GPS + IMU) for precise field localisation</li>
        <li>Develop mobile interface for farmers to upload field images and receive weed density maps</li>
        <li>Collaborate with agricultural research institutions for real field validation</li>
      </ul>
 
      <h2>🙏 Acknowledgements</h2>
      <div class="ack">
        <ul>
          <li><strong>MH-16 Weed Dataset</strong> — Indian agricultural dataset curated for precision agriculture research</li>
          <li><strong>Ultralytics YOLOv8</strong> — Framework that made high-performance object detection accessible</li>
          <li><strong>Google Colab</strong> — Free GPU access (T4, 15 GB VRAM) that made training feasible without expensive hardware</li>
          <li><strong>Mr. Sanjay Macwan</strong> — Internal guide and Head of Department, Computer Engineering, Neotech Campus</li>
          <li><strong>Neotech Campus, Vadodara</strong> — Department resources and academic support</li>
        </ul>
      </div>
 
      <hr>
 
      <p style="text-align:center; color: #8b949e; font-size: 13px; margin-top: 20px;">
        <strong style="color:#e6edf3;">Herin Bhatt</strong> · herinbhattflux@gmail.com · Vadodara, India<br>
        B.E. Computer Engineering · Neotech Campus · Gujarat Technological University · 2025<br>
        <a href="#">github.com/herinbhatt</a> · <a href="#">linkedin.com/in/herinbhatt</a>
      </p>
 
    </div><!-- .md -->
