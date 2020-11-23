from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
import webbrowser
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
model = pickle.load(open('decision_tree_model_2.pkl', 'rb'))
@app.route('/', methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        age = int(request.form['age'])
        gender = int(request.form['gender'])
        if(gender == '1'):
            gender = 1
        else:
            gender = 0
        prediction = model.predict([[age, gender]])
        output = prediction[0]
        if output == 'Classic':
            webbrowser.open(
                "https://open.spotify.com/playlist/37i9dQZF1DWY1kDGbdPb81")
        elif output == 'Chill':
            webbrowser.open(
                "https://open.spotify.com/playlist/37i9dQZF1DX9L0PulSSl2E")
        elif output == 'Indie':
            webbrowser.open(
                "https://open.spotify.com/playlist/37i9dQZF1DX5q67ZpWyRrZ")
        elif output == 'Jazz':
            webbrowser.open(
                "https://open.spotify.com/playlist/37i9dQZF1DWSwxyU5zGZYe")
        elif output == 'Travel':
            webbrowser.open(
                "https://open.spotify.com/playlist/37i9dQZF1DXd05hd2jmMZL")
        elif output == 'Dance':
            webbrowser.open(
                "https://open.spotify.com/playlist/37i9dQZF1DX8xfQRRX1PDm")

        return render_template('index.html', prediction_text="{} ".format(output))
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
