from src.main.api.models.deposit_response import DepositResponse
from src.main.api.requests.requester import Requester
from src.main.api.models.deposit_request import DepositRequest
from requests import Response
import requests


class CreateDepositRequester(Requester):
    def post(self, create_deposit_request:DepositRequest) -> DepositResponse | Response:
        url = f'{self.base_url}/account/deposit'
        response = requests.post(
            url = url,
            json=create_deposit_request.model_dump(),
            headers= self.headers
        )
        self.response_spec(response)
        return DepositResponse(**response.json())

