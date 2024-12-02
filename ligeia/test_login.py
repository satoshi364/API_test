import allure
import pytest
from auto_tests.common.login import login


@pytest.mark.parametrize("email, password, device_id, url, status_code", [
    ("alexanderku@test.com", "Street.dancer20!", "12345",
     "https://test.io/api/user/login", 200),
    ("incorrect_login", "Street.dancer20!", "12345",
     "https://test.io/api/user/login", 404),
    ("alexanderku@test.com", "incorrect password", "12345",
     "https://test.io/api/user/login", 404),
    ("alexanderku@test.com", "incorrect password", "12345",
     "https://test.io/api/user/login", 403)])
class TestAuth:
    @allure.description("Verify authorization")
    def test_login(self, email, password, device_id, url, status_code):
        with allure.step("Login"):
            response = login(email, password, device_id, url)

        with ((allure.step("Verify status code"))):
            assert response.status_code == status_code, (
                f"actual status code:{response.status_code}",
                f"{response.json()}",
                f"expected status code:{status_code}"
            )
        # api_session_token = response_body['apiSessionToken']

