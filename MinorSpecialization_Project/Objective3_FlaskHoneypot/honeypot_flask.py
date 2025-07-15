from flask import Flask, request, jsonify
import json
from datetime import datetime

app = Flask(__name__)

# Initialize a risk level counter
risk_level = 0

@app.route('/')
def home():
    return "Welcome to the Cyber Defense Flask Server!"

@app.route('/trap')
def honeypot():
    global risk_level

    visitor_ip = request.remote_addr

    # Increment risk each time an attack hits the honeypot
    risk_level += 1

    # Classify risk levels
    if risk_level < 3:
        risk_label = "LOW"
    elif risk_level < 6:
        risk_label = "MEDIUM"
    else:
        risk_label = "HIGH"

    alert_data = {
        "ip": visitor_ip,
        "event": "Intrusion attempt detected on /trap endpoint",
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "status": "logged",
        "risk_level": risk_label
    }

    # Save log
    with open("alert.json", "w") as f:
        json.dump(alert_data, f, indent=4)

    print(f"🚨 Honeypot triggered! IP: {visitor_ip} | Risk: {risk_label}")

    return jsonify({
        "message": "You have triggered the honeypot. Your activity is logged!",
        "logged_data": alert_data
    })

if __name__ == '__main__':
    app.run(debug=True)
