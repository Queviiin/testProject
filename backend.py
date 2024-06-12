import requests
import time

#Stage Env (test)
BASE_URL = "https://stage.v1.api.pdax.ph/caas-mw/cognito"


class API:

    def login():
        path = '/login'
        base_url = BASE_URL
        payload = {
            "username": "dev1.dev@pdax.ph",
            "password": "caasTestingP@ssw0rd"
        }
        headers = {
                'accept': 'application/json'
        }
        URL = base_url + path
        result = requests.post(URL, json=payload, headers=headers)
        return result

## TEST CASES ##

def test_user_is_able_to_login():
    resp = API.login()
    resp_json = resp.json()
    status = resp_json["email"]
    access_token = resp_json["accessToken"]

    assert status == "dev1.dev@pdax.ph"
    assert access_token != ""

    print("TEST CASE PASSED")


test_user_is_able_to_login()