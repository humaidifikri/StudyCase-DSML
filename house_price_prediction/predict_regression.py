import joblib

def reg_predict(data):
    reg = joblib.load(".\house_price_prediction\models\gradboost_model.pkl")
    predictions = reg.predict(data)
    pred_to_int = predictions.astype(int)
    # Format sebagai nominal uang
    formatted_prediction = f"$ {pred_to_int[0]:,}".replace(",", ".")
    return formatted_prediction