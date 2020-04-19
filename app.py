"""imports"""
import logging
import os
from flask import Flask, request, jsonify

import pandas as pd
from os.path import basename
from sklearn.externals import joblib
from sklearn.preprocessing import StandardScaler

ME = basename(__file__)
LOGGER = logging.getLogger()
LOGGER.setLevel(logging.DEBUG)
# Add the console handler
handler_console = logging.StreamHandler()
format_console = logging.Formatter(
    ME + ": %(asctime)s: %(levelname)8s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
    )
handler_console.setFormatter(format_console)
LOGGER.addHandler(handler_console)

APP = Flask(__name__)

def scale(payload):
    """Scales Payload"""

    LOGGER.info("Scaling Payload: \n{}".format(payload))
    scaler = StandardScaler().fit(payload.astype(float))
    scaled_adhoc_predict = scaler.transform(payload.astype(float))
    return scaled_adhoc_predict

@APP.route("/")
def home():
    """predictions"""
    LOGGER.info("Invoking Prediction Home page")
    html = "<h3>Sklearn Prediction Home</h3>"
    return html.format(format)

@APP.route("/predict", methods=['POST'])
def predict():
    """Performs an sklearn prediction

        input looks like:
        {
        "CHAS":{
        "0":0
        },
        "RM":{
        "0":6.575
        },
        "TAX":{
        "0":296.0
        },
        "PTRATIO":{
        "0":15.3
        },
        "B":{
        "0":396.9
        },
        "LSTAT":{
        "0":4.98
        }

        result looks like:
        { "prediction": [ <val> ] }

        """

    LOGGER.info("Invoking prediction API ..")
    # Logging the input payload
    json_payload = request.json
    LOGGER.info("JSON payload: \n{}".format(json_payload))
    inference_payload = pd.DataFrame(json_payload)
    LOGGER.info("Inference payload DataFrame: \n{}".format(inference_payload))
    # scale the input
    scaled_payload = scale(inference_payload)
    # get an output prediction from the pretrained model, CLF
    prediction = list(CLF.predict(scaled_payload))
    # TO DO:  Log the output prediction value
    LOGGER.info("Predection values for the input: {}".format(prediction))
    return jsonify({'prediction': prediction})

if __name__ == "__main__":
    # load pretrained model as CLF
    CLF = joblib.load("./model_data/boston_housing_prediction.joblib")
    APP.run(host='0.0.0.0', port=80, debug=True) # specify port=80
