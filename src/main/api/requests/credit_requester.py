from src.main.api.models.credit_request import CreditRequest
from src.main.api.models.credit_response import CreditResponse
from src.main.api.requests.requester import Requester
import requests
from requests import Response


class CreateCreditRequester(Requester):
    def post(self, create_credit_requester:CreditRequest) -> CreditResponse | Response:
        url = f'{self.base_url}/credit/request'
        response = requests.post(
            url = url,
            json = create_credit_requester.model_dump(),
            headers = self.headers
        )
        self.response_spec(response)
        return CreditResponse(**response.json())