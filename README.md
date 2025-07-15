<img width="1202" height="750" alt="image" src="https://github.com/user-attachments/assets/84af527a-8610-492f-a2de-d406bb430c03" /># blockchain-based-cyber-defense-system


Project Overview

This Minor Specialization Project implements a blockchain-based cyber defense system integrating:

> SDN Firewall Rules  
> Honeypot simulation  
> Decentralized alert storage via IPFS  
> Reinforcement learning risk prediction  
> Interactive cybersecurity dashboard  
> Blockchain hash integrity verification  

It aims to ensure tamper-proof cyber threat monitoring and enhance the trustworthiness of security logs and rules.



 Technologies Used

- Python 3 (Flask, Requests, Matplotlib, etc.)
- JavaScript (Chart.js)
- HTML/CSS
- Pinata & IPFS
- SHA-256 hashing
- Solidity (Optional)
- JSON files as a lightweight DB
- Vercel / GitHub Pages (for hosting the dashboard)



Objectives

| Objective | Description | Status |
|-----------|-------------|--------|
| 1 | Upload honeypot alert logs to IPFS via Pinata |  Done |
| 2 | Simulate risk prediction using reinforcement learning |  Done |
| 3 | Create a honeypot server to trap intrusions | Done |
| 4 | Store SDN firewall rule hashes on blockchain-like simulation | Done |
| 5 | Build a dashboard visualizing alerts, hashes, and IPFS data |  Done |


 Project Structure


MinorSpecialization_Project/
 ├── Objective1_Upload_IPFS/
 │ ├── pinata_upload.py
 │ ├── alert.json
 ├── Objective2_RiskPrediction/
 │ └── rl_risk_predictor.py
 ├── Objective3_FlaskHoneypot/
 │ └── honeypot_flask.py
 ├── Objective4_SDN_Filter_Sim/
 │ ├── firewall_rule.json
 │ ├── blockchain_hash.json
 │ └── sdn_blockchain_simulation.py
 ├── Objective5_WebDashboard/
 │ ├── index.html
 │ ├── login.html
 │ ├── firewall_rule.json
 │ ├── blockchain_hash.json
 │ ├── alert.json
 │ └── images/
 ├── auto_upload.py
 └── README.md



 Objective 1 — Upload Alerts to IPFS

Implemented using Pinata to store logs in a decentralized way.

 Files

- `alert.json` → stores logs
- `pinata_upload.py` → uploads to Pinata via JWT

How to Run

bash
pip install requests
python3 pinata_upload.py
 Returns a public IPFS CID to share logs securely:
 Uploading to Pinata...
 File uploaded to Pinata successfully!
 IPFS CID: QmVVfNZU2fm1skeKNjxS6AyDVpLpoihA1YAeQW559ccD8j

View your logs publicly:
https://gateway.pinata.cloud/ipfs/QmVVfNZU2fm1skeKNjxS6AyDVpLpoihA1YAeQW559ccD8j


Objective 2 — Cyber Risk Prediction
A simple Reinforcement Learning simulation models rising or falling risk levels.
File
rl_risk_predictor.py


How to Run
pip install numpy matplotlib
python3 rl_risk_predictor.py

Displays a risk-level graph showing:
Spikes = attacks detected


Drops = calm periods



 Objective 3 — Honeypot Simulation
A Flask honeypot server logs unauthorized hits to the //trap endpoint.
File
honeypot_flask.py


How to Run
pip install flask
python3 honeypot_flask.py

Then visit:
http://127.0.0.1:5000/trap

 Response:
{
  "message": "Trap triggered! Intrusion logged.",
  "alert": {
    ...
  }
}

 Log automatically added to alert.json.

Objective 4 — SDN Firewall Rule Hashing
Stores firewall rules, along with their SHA-256 hash, for blockchain-style integrity.
Files
firewall_rule.json


blockchain_hash.json


sdn_blockchain_simulation.py


How to Run
python3 sdn_blockchain_simulation.py

Example output:
 >Saved firewall rule to firewall_rule.json
>SHA-256 Hash of Rule: d78482ac9a4e3e3f6c23326a...
> Saved hash to blockchain_hash.json
 The hash ensures firewall rules have not been tampered with.
 Objective 5 — Cyber Defense Dashboard
A beautiful web dashboard visualizing:
> SDN firewall rules
> Blockchain hash
> IPFS CID viewer
> Pie chart of risk levels
> Bar chart of attacks over time
Files
index.html


login.html


JSON files for data


How to Run
Run a local server:
python3 -m http.server

Visit:
http://127.0.0.1:8000/login.html

Login → Dashboard displays all:
Blockchain data


IPFS link


Real-time charts


Default Login
Username: admin
Password: 1234


🖼️ Screenshots
Dashboard View

Pinata Upload Success

Risk Prediction Plot




 Bonus — Automation
auto_upload.py automatically uploads your alert.json to IPFS every hour and logs CIDs for permanent records.

Smart Contract Integration (Optional)
An optional Solidity smart contract stores your CID on Mumbai Testnet for on-chain verification.

🌐 Deployment
You can host your dashboard on:
Vercel

GitHub Pages

Netlify

Learning Outcomes
 Decentralized log storage (IPFS)
  Blockchain hash integrity
  Reinforcement learning risk modeling
  Web dashboards and data visualization
  Flask honeypot simulation
  Full integration of SDN, AI, IPFS, and blockchain

Project Status
 >All Objectives Completed
 >Dashboard Working
 >Blockchain Hashing Functional
 >IPFS Upload Confirmed
 > Hosting Ready for Deployment

 Author
Yuvraj Yadav
 B.Tech Computer Science & Engineering
 MIT Manipal
Under the Guidance of
Ms. Namrata Marium Chacko
 Assistant Professor
 Department of CSE, MIT Manipal

