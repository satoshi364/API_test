import allure
import pytest
from auto_tests.common.logout import logout
from auto_tests.common.login import login


@pytest.mark.parametrize("email,"
                         "password,"
                         "device_id,"
                         "login_url,"
                         "logout_url,"
                         "status_code",
                         [
                             ("alexanderku@test.com",
                              "Street.dancer20!!",
                              "12345",
                              "https://test.io/api/user/login",
                              "https://test.io/api/user/logout", 200)
                         ])
class TestLogout:
    @allure.description("Verify logout")
    def test_logout(self, email, password, device_id, login_url, logout_url, status_code):
        with allure.step("Do login"):
            response = login(email, password, device_id, login_url)
            api_session_token = response.json().get('apiSessionToken')

        with allure.step("Do logout"):
            logout_response = logout(logout_url, api_session_token)
            assert status_code == logout_response.status_code
