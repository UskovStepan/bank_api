import requests
from requests import Response
from src.main.api.models.login_user_response import LoginUserResponse
from src.main.api.requests.requester import Requester
from src.main.api.models.login_user_request import LoginUserRequest

class LoginUserRequester(Requester):
    def post(self, login_user_request:LoginUserRequest) -> LoginUserResponse|Response:
        url = f'{self.base_url}/auth/token/login'
        response = requests.post(
            url=url,
            json=login_user_request.model_dump(),
            headers=self.headers
        )
        self.response_spec(response)
        if response.status_code == 200:
            return LoginUserResponse(**response.json())
        return response