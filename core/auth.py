import requests
from config.settings import TOKEN, USERNAME, PASSWORD


def get_tgt(token_url, username, password):
    try:
        response = requests.post(
            url=token_url,

            data={
                "username": username,
                "password": password
            },

            headers = {
                "Content-Type": "application/x-www-form-urlencoded",
                "Accept": "text/plain"
            },
        )
        return response.text
    except Exception as err:
        print(f"Error: {err}")
        return []

tgt = get_tgt(TOKEN, USERNAME, PASSWORD)
