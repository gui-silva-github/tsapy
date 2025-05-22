from flask import Flask, request, jsonify
import numpy as np
from keras import models
import joblib

app = Flask(__name__)

model = models.load_model('h5/modelo_fraude.h5')
scaler = joblib.load('scaler/scaler.pkl')

@app.route('/prever', methods=['POST'])
def prever():
    try:
        dados = request.get_json()
        entrada = np.array(dados['valores']).reshape(1, -1)
        entrada = scaler.transform(entrada)
        resultado = model.predict(entrada)
        return jsonify({'fraude': bool(resultado[0][0] > 0.5)})
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)