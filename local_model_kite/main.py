import pytemperature

def predict(rider_level, temperature, windspeed):
    """
        Predicts whether it's good weather for kitesurfing
        rider_level str : the level of the kitesurfer
        temperature float: the temperature in Fahrenheit
        windspeed float: the wind speed in knots
    """
    if rider_level == 'beginner':
        return pytemperature.f2c(temperature) > 5 and windspeed >= 20 and windspeed < 30
    elif rider_level == 'intermediate':
        return pytemperature.f2c(temperature) > 5 and windspeed >= 20 and windspeed < 40
    elif rider_level == 'advanced':
        return pytemperature.f2c(temperature) > 5 and windspeed >= 20 and windspeed < 50


print(f"Is it kiteweather? {predict('beginner', 45,20)}")
