import json
import hashlib

# ✅ Define SDN firewall rule
firewall_rule = {
    "rule_id": 1,
    "action": "BLOCK",
    "ip_address": "192.168.10.50"
}

# ✅ Save firewall rule to firewall_rule.json
with open('firewall_rule.json', 'w') as f:
    json.dump(firewall_rule, f, indent=4)

print("✅ Firewall rule saved to firewall_rule.json.")

# ✅ Compute SHA-256 hash of firewall_rule.json
with open('firewall_rule.json', 'rb') as f:
    file_data = f.read()
    rule_hash = hashlib.sha256(file_data).hexdigest()

print(f"✅ Local hash of firewall_rule.json:\n{rule_hash}")

# ✅ Simulate storing this hash on blockchain
blockchain_recorded_hash = rule_hash
print("✅ Hash recorded on blockchain (simulated).")

# ✅ Your Pinata IPFS CID for alert.json
alert_logs_cid = "QmVVfNZU2fm1skeKNjxS6AyDVpLpoihA1YAeQW559ccD8j"

# ✅ Save blockchain data to blockchain_hash.json
blockchain_data = {
    "blockchain_recorded_hash": blockchain_recorded_hash,
    "alert_logs_ipfs_cid": alert_logs_cid
}

with open('blockchain_hash.json', 'w') as f:
    json.dump(blockchain_data, f, indent=4)

print("✅ Blockchain data saved to blockchain_hash.json.")

# ✅ Simulate verifying the firewall rule
with open('firewall_rule.json', 'rb') as f:
    device_data = f.read()
    device_hash = hashlib.sha256(device_data).hexdigest()

print(f"✅ Device computed hash:\n{device_hash}")

if device_hash == blockchain_recorded_hash:
    print("✅ Verification passed: firewall rule is authentic.")
else:
    print("❌ Verification failed: firewall rule has been tampered with!")

# ✅ Show alert logs CID for linking in dashboard
print(f"✅ Alert logs stored on IPFS:")
print(f"🌐 https://gateway.pinata.cloud/ipfs/{alert_logs_cid}")
