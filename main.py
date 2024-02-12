from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Replace this URL with the actual URL of your backend API
backend_api_url = "https://grade-ease-api.onrender.com"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    text1 = request.form.get('text1')
    text2 = request.form.get('text2')

    # Sending data to backend API
    data = {"student_ans": text1, "reference_ans": text2}
    response = requests.post(f"{backend_api_url}/p", json=data)

    if response.status_code == 200:
        result = response.json().get('result')
        return render_template('result.html', result=result)
    else:
        return "Error communicating with the backend API"

if __name__ == '__main__':
    app.run(debug=True)
