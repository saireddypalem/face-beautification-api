from flask import Flask, request, send_file
from ultralytics import YOLO
import os

app = Flask(__name__)

# Load your model
model = YOLO("models/best.pt")

# Create folders automatically
os.makedirs("uploads", exist_ok=True)
os.makedirs("outputs", exist_ok=True)

@app.route("/predict", methods=["POST"])
def predict():
    file = request.files["image"]

    input_path = os.path.join("uploads", file.filename)
    output_path = os.path.join("outputs", file.filename)

    file.save(input_path)

    # Run model
    results = model(input_path)

    # Save output image
    results[0].save(filename=output_path)

    return send_file(output_path, mimetype="image/jpeg")

if __name__ == "__main__":
    app.run(debug=True)