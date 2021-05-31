import pytemperature
import json
from flask import Flask, request

app = Flask(__name__)

@app.route("/predict", methods=['POST'])
def predict():
    """
        Predicts whether it's good weather for kitesurfing
        rider_level str : the level of the kitesurfer
        windspeed float: the wind speed in knots
    """

    request_dict = request.get_json()

    if request_dict['rider_level'] == 'beginner':
        return_value = pytemperature.f2c(request_dict['temperature']) > 5 \
            and request_dict['windspeed'] >= 20 \
            and request_dict['windspeed'] < 30
    elif request_dict['rider_level'] == 'intermediate':
        return_value = pytemperature.f2c(request_dict['temperature']) > 5 \
            and request_dict['windspeed'] >= 20 \
            and request_dict['windspeed'] < 40
    elif request_dict['rider_level'] == 'advanced':
        return_value = pytemperature.f2c(request_dict['temperature']) > 5 \
            and request_dict['windspeed'] >= 20 \
            and request_dict['windspeed'] < 50
    return app.response_class(
        response=json.dumps({'kiteweather': return_value}),
        status=200,
        mimetype='application/json'
    )


if __name__ == '__main__':
    app.run()
