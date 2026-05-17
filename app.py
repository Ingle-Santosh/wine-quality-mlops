from flask import Flask, render_template, request, jsonify
import os 
import numpy as np
import pandas as pd
from wine_quality_mlops.pipeline.prediction_pipeline import PredictionPipeline
from wine_quality_mlops.utils.logger import logger
from wine_quality_mlops.utils.exceptions import CustomException


app = Flask(__name__)

# Load model once during startup
prediction_pipeline = PredictionPipeline()

FEATURE_COLUMNS = [
    "fixed_acidity",
    "volatile_acidity",
    "citric_acid",
    "residual_sugar",
    "chlorides",
    "free_sulfur_dioxide",
    "total_sulfur_dioxide",
    "density",
    "pH",
    "sulphates",
    "alcohol"
]


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        logger.info("Prediction request received")

        # Extract input features
        features = [
            float(request.form[col])
            for col in FEATURE_COLUMNS
        ]

        logger.info(f"Input features: {features}")

        # Convert to numpy array
        data = np.array(features).reshape(1, -1)

        # Prediction
        prediction = prediction_pipeline.predict(data)

        logger.info(f"Prediction completed: {prediction}")

        return render_template(
            "results.html",
            prediction=str(prediction)
        )

    except Exception as e:

        custom_error = CustomException(e, sys)

        logger.error(custom_error)

        return jsonify({
            "error": "Something went wrong during prediction"
        }), 500


if __name__ == "__main__":

    logger.info("Starting Flask application")

    app.run(
        host="0.0.0.0",
        port=8080,
        debug=True
    )