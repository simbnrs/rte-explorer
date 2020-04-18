import os
import requests
from globals import *
from dotenv import load_dotenv

load_dotenv()

def get_token(auth_key):
    """
    Retrieves the token required to connect to the RTE API
    Args:
        auth_key (str): authentication key, in base64
    Returns (str): Token
    """
    r = requests.post(AUTH_URL, headers=dict(Authorization='Basic '+auth_key))
    if r.status_code == 200:
        token = r.json()["access_token"]
        token = "Bearer " + token
        return token
    else:
        raise PermissionError(
            "Invalid credentials"
        )

def get_pwr_gen_token(pwr_key=os.environ['PWR_GEN_KEY']):
    return get_token(pwr_key)