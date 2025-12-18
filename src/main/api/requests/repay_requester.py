from src.main.api.models.repay_credit_request import RepayCreditRequest
from src.main.api.models.repay_credit_response import RepayCreditResponse
from src.main.api.requests.requester import Requester
import requests
from requests import Response


class CreateRepayRequester(Requester):
    def post(self, create_repay_request:RepayCreditRequest) -> RepayCreditResponse | Response:
        url = f'{self.base_url}/credit/repay'
        response = requests.post(
            url = url,
            json = create_repay_request.model_dump(),
            headers=self.headers,
        )
        self.response_spec(response)
        return RepayCreditResponse(**response.json())
