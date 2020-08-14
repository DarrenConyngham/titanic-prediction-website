def fake_predict(user_age):
    if user_age < 10:
        prediction = 'survives'
    else:
        prediction = 'dies'
    return prediction
