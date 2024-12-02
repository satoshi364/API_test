import requests


def logout(logout_url: str, api_session_token: str):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_session_token}'
    }
    response = requests.get(logout_url, headers=headers)
    return response
