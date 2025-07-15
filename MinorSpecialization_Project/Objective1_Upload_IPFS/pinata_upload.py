import requests

# ✅ Your active JWT token with correct scopes
PINATA_JWT = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySW5mb3JtYXRpb24iOnsiaWQiOiJlYTM1MDFhNC1kMjM1LTQyOTQtOWY0MC1kMDZjMDkzZDMyODAiLCJlbWFpbCI6Inl1dnJhanlhZGF2NzM0QGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJwaW5fcG9saWN5Ijp7InJlZ2lvbnMiOlt7ImRlc2lyZWRSZXBsaWNhdGlvbkNvdW50IjoxLCJpZCI6IkZSQTEifSx7ImRlc2lyZWRSZXBsaWNhdGlvbkNvdW50IjoxLCJpZCI6Ik5ZQzEifV0sInZlcnNpb24iOjF9LCJtZmFfZW5hYmxlZCI6ZmFsc2UsInN0YXR1cyI6IkFDVElWRSJ9LCJhdXRoZW50aWNhdGlvblR5cGUiOiJzY29wZWRLZXkiLCJzY29wZWRLZXlLZXkiOiJhODg2OGEyZTQzMmJmMDA4MjllZCIsInNjb3BlZEtleVNlY3JldCI6IjAxZGE5NzdlY2VmODA4ZGFkOWE4YjE4MDM1Yjg4ZjFkZGMwYzg1NDdiNjUyNzM1NGI0NTlhZTA5YzQzNWNmMTYiLCJleHAiOjE3ODM2OTY4NDJ9.EvxszQPRlsU3cyE61vBGBX9_TutiXRvZ69ubqfhH9i4"

# ✅ File you want to upload
FILE_PATH = "alert.json"

def upload_to_pinata(file_path):
    url = "https://api.pinata.cloud/pinning/pinFileToIPFS"

    headers = {
        "Authorization": f"Bearer {PINATA_JWT}"
    }

    print("🚀 Uploading to Pinata...")

    try:
        with open(file_path, "rb") as f:
            files = {
                'file': (file_path, f)
            }
            response = requests.post(url, files=files, headers=headers)

        print("🛰️  Pinata response code:", response.status_code)

        if response.status_code == 200:
            data = response.json()
            cid = data.get("IpfsHash")
            if cid:
                print("✅ File uploaded to Pinata successfully!")
                print("🔗 IPFS CID:", cid)
                print(f"🌐 View on: https://gateway.pinata.cloud/ipfs/{cid}")
            else:
                print("❌ Upload succeeded but no CID returned.")
                print("Response:", data)
        else:
            print("❌ Error uploading to Pinata:")
            print(response.status_code, response.text)

    except FileNotFoundError:
        print(f"❌ File '{file_path}' not found. Please check your filename.")
    except Exception as e:
        print("❌ An unexpected error occurred:", str(e))

if __name__ == "__main__":
    upload_to_pinata(FILE_PATH)
