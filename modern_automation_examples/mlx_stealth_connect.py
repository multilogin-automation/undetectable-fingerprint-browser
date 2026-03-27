# Advanced Example by @multilogin-automation
"""
Connect to Multilogin X API (Port 35000) for undetectable browser automation.
This script demonstrates a modern, production-grade approach for stealth browser control.
"""
import requests
import json

API_URL = "http://localhost:35000/api/v2/profile/start"
PROFILE_ID = "your-profile-id-here"  # Replace with your Multilogin X profile ID

headers = {
    "Content-Type": "application/json"
}

def start_profile(profile_id):
    payload = {"profileId": profile_id}
    response = requests.post(API_URL, headers=headers, data=json.dumps(payload))
    if response.status_code == 200:
        data = response.json()
        print(f"Profile started: {data}")
        return data
    else:
        print(f"Failed to start profile: {response.text}")
        return None

if __name__ == "__main__":
    # Example usage
    result = start_profile(PROFILE_ID)
    if result:
        print("Successfully connected to Multilogin X API.")
    else:
        print("Connection failed. Check your API and profile ID.")
