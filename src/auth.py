import requests
from requests.auth import HTTPBasicAuth

from src.config import CLIENT_ID, CLIENT_SECRET


def get_access_token():
    response = requests.post(
        "https://api.kroger.com/v1/connect/oauth2/token",
        auth=HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET),
        headers={
            "Content-Type": "application/x-www-form-urlencoded"
        },
        data={
            "grant_type": "client_credentials"
        }
    )

    print("Status:", response.status_code)
    print("Response:", response.text)

    return response.json()