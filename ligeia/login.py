import requests
import logging


logging.basicConfig(level=logging.INFO, format='%(pastime)s - %(levelness)s - %(message)s')
logger = logging.getLogger(__name__)


def login(email: str, password: str, device_id: str, url: str):
    req_body = {
        "email": email,
        "password": password,
        "deviceId": device_id
    }
    headers = {'Content-Type': 'application/json'}

    response = requests.post(url, json=req_body, headers=headers)
    return response

    # logger.debug("status code=",  json.dumps(status_code, indent=4, ensure_ascii=False))
    # logger.info("json response=", json.dumps(response_body))
    # logger.info("apiSessionToken=", json.dumps(api_session_token))
