import os
os.environ["CUDA_VISIBLE_DEVICES"] = ""

from flask import Flask, request, send_file, jsonify
from ultralytics import YOLO
import torch

torch.set_num_threads(1)

app = Flask(**name**)

MODEL = None

os.makedirs("uploads", exist_ok=True)
os.makedirs("outputs", exist_ok=True)

def get_model():
global MODEL
if MODEL is None:
MODEL = YOLO("models/best.pt")
return MODEL

@app.route("/health")
def health():
return jsonify({"status": "ok"})

@app.route("/predict", methods=["POST"])
def predict():
file = request.files["image"]

```
input_path = os.path.join("uploads", file.filename)
output_path = os.path.join("outputs", file.filename)

file.save(input_path)

model = get_model()

results = model(input_path)
results[0].save(filename=output_path)

return send_file(output_path, mimetype="image/jpeg")
```

if **name** == "**main**":
app.run(host="0.0.0.0", port=5000)

