from flask import Flask, request, jsonify, render_template,url_for
import numpy as np
from keras.models import load_model
import pickle


app = Flask(__name__, static_url_path='/static')

# Charger le modèle
model = load_model('temperature_prediction_model.h5')

# Charger le scaler sauvegardé avec pickle
with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form['values']
    input_data = np.array(list(map(float, data.split(','))))

    # Normaliser les données d'entrée avec fit_transform()
    input_data_scaled = scaler.fit_transform(input_data.reshape(-1, 1))

    # Créer la séquence pour la prédiction
    sequence_length = 12
    X_input = input_data_scaled.reshape(1, sequence_length, 1)  # Reshape pour le modèle

    # Faire la prédiction
    predicted_temperature_scaled = model.predict(X_input)

    # Dénormaliser la prédiction
    predicted_temperature = scaler.inverse_transform(predicted_temperature_scaled)

    return jsonify({'predicted_temperature': float(predicted_temperature[0][0])})

if __name__ == '__main__':
    app.run()
