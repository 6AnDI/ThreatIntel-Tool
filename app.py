from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    intel_data = None
    
    if request.method == 'POST':
        ip_address = request.form.get('ip_address')
        url = f"http://ip-api.com/json/{ip_address}"
        
        try:
            response = requests.get(url)
            intel_data = response.json()
        except Exception as e:
            intel_data = {"status": "fail", "message": "Failed to connect to the API."}
            
    return render_template('index.html', data=intel_data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)