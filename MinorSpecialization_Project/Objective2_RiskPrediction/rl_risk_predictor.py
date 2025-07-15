import numpy as np
import matplotlib.pyplot as plt

# Simulated cyber events: 1 = attack, 0 = no attack
alerts = [1, 0, 1, 1, 0, 1, 0, 0, 1, 1]

risk_level = 0
risk_history = []

for i, alert in enumerate(alerts):
    if alert:
        risk_level += 1
        print(f"[ALERT] Attack detected at step {i} → risk increased to {risk_level}")
    else:
        risk_level = max(0, risk_level - 0.5)
        print(f"[INFO] No attack at step {i} → risk decreased to {risk_level}")
    
    risk_history.append(risk_level)

# Plot the risk level over time
plt.figure(figsize=(8,4))
plt.plot(risk_history, marker='o')
plt.title("Cyber Risk Level Over Time")
plt.xlabel("Event Number")
plt.ylabel("Risk Level")
plt.grid(True)
plt.show()
