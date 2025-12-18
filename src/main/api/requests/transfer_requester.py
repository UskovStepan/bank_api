import requests
from requests import Response
from src.main.api.models.transfer_response import TransferResponse
from src.main.api.models.transfer_request import TransferRequest
from src.main.api.requests.requester import Requester

class CreateTransferRequester(Requester):
    def post(self, create_transfer_request:TransferRequest) -> TransferResponse | Response:
        url = f'{self.base_url}/account/transfer'
        response = requests.post(
            url = url,
            json = create_transfer_request.model_dump(),
            headers=self.headers
        )
        self.response_spec(response)
        return TransferResponse(**response.json())