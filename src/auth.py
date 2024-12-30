import requests

def get_bearer_token(base_url, client_id, client_secret, grant_type, username, password):
    """Fetch bearer token using OAuth."""
    url = f"{base_url}/oauth/issueToken"
    payload = {
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": grant_type,
        "username": username,
        "password": password
    }
    response = requests.post(url, data=payload)
    response.raise_for_status()
    return response.json().get("access_token")
