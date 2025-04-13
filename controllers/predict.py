from flask import Blueprint, request, jsonify
import joblib
import numpy as np
# Membuat blueprint untuk controller predict
predict_bp = Blueprint('predict_bp', __name__)

# Muat model dari folder models
model = joblib.load('models/gb_model.pkl')

@predict_bp.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    input_data = np.array(data['input']).reshape(1, -1)
    result = model.predict(input_data).tolist()
    return jsonify({'prediction': result})
