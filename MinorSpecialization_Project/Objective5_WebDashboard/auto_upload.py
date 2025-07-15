import requests
import schedule
import time
import datetime

# ✅ YOUR JWT TOKEN HERE
PINATA_JWT = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."

# ✅ File to upload
FILE_PATH = "alert.json"

def upload_to_pinata():
    url = "https://api.pinata.cloud/pinning/pinFileToIPFS"
    headers = {
        "Authorization": f"Bearer {PINATA_JWT}"
    }

    try:
        print("🚀 Uploading to Pinata...")

        with open(FILE_PATH, "rb") as f:
            files = {
                'file': (FILE_PATH, f)
            }
            response = requests.post(url, files=files, headers=headers)

        if response.status_code == 200:
            data = response.json()
            cid = data.get("IpfsHash")
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # ✅ Log CID to file
            log_line = f"{timestamp} | CID: {cid}\n"
            with open("upload_history.log", "a") as log_file:
                log_file.write(log_line)

            print("✅ Upload complete!")
            print("CID:", cid)
            print(f"🌐 View: https://gateway.pinata.cloud/ipfs/{cid}")

        else:
            print("❌ Error uploading to Pinata:")
            print(response.status_code, response.text)

    except FileNotFoundError:
        print(f"❌ File '{FILE_PATH}' not found.")
    except Exception as e:
        print("❌ Unexpected error:", str(e))

# ✅ Schedule: Every hour
schedule.every(1).hours.do(upload_to_pinata)

print("🕑 Automation script running. Uploading every hour...")
upload_to_pinata()  # Run once immediately

while True:
    schedule.run_pending()
    time.sleep(60)
