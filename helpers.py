import time
import requests

class NetworkError(Exception):
    pass

def retry_request(url, max_retries=3, delay=2):
    attempts = 0
    while attempts < max_retries:
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            attempts += 1
            if attempts == max_retries:
                raise NetworkError(f'Failed to fetch {url} after {max_retries} attempts')
            time.sleep(delay)
