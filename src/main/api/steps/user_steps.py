

from src.main.api.fixtures.user_fixture import create_user_request
from src.main.api.foundation.endpoint import Endpoint
from src.main.api.foundation.requesters.validate_crud_requester import ValidateCrudeRequester
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.credit_request import CreditRequest
from src.main.api.models.deposit_request import DepositRequest
from src.main.api.models.repay_credit_request import RepayCreditRequest
from src.main.api.models.transactions_request import TransactionRequest
from src.main.api.models.transactions_response import TransactionResponse
from src.main.api.models.transfer_request import TransferRequest
from src.main.api.specs.request_specs import RequestSpecs
from src.main.api.specs.response_specs import ResponseSpecs
from src.main.api.steps.base_steps import BaseSteps


class UserSteps(BaseSteps):
    def create_account(self, create_user_request: CreateUserRequest):
        response = ValidateCrudeRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.CREATE_ACCOUNT,
            ResponseSpecs.request_create()
        ).post()
        return response

    def create_deposit(self, create_user_request: CreateUserRequest, deposit_request:DepositRequest):
        response = ValidateCrudeRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.DEPOSIT_ACCOUNT,
            ResponseSpecs.request_ok()
        ).post(deposit_request)
        return response
    def create_negative_deposit(self, create_user_request: CreateUserRequest, deposit_request:DepositRequest):
        response = ValidateCrudeRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.DEPOSIT_ACCOUNT,
            ResponseSpecs.request_bad()
        ).crud_requester.post(deposit_request)
        return response

    def create_transfer(self, create_user_request: CreateUserRequest, transfer_request:TransferRequest):
        response = ValidateCrudeRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.TRANSFER_ACCOUNT,
            ResponseSpecs.request_ok()
        ).post(transfer_request)
        return response
    def create_negative_transfer(self, create_user_request: CreateUserRequest, transfer_request:TransferRequest):
        response = ValidateCrudeRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.TRANSFER_ACCOUNT,
            ResponseSpecs.request_bad()
        ).crud_requester.post(transfer_request)
        return response
    def get_transactions(self,create_user_request: CreateUserRequest, user_id:int):
        response = ValidateCrudeRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.GET_TRANSACTIONS,
            ResponseSpecs.request_ok()
        ).get(user_id)
        return response

    def create_credit_request(self, create_user_request_credit:CreateUserRequest, credit_request:CreditRequest):
        response = ValidateCrudeRequester(
            RequestSpecs.auth_headers(username=create_user_request_credit.username, password=create_user_request_credit.password),
            Endpoint.CREDIT_REQUEST,
            ResponseSpecs.request_create()
        ).post(credit_request)
        return response
    def negative_credit_request(self, create_user_request_credit:CreateUserRequest, credit_request:CreditRequest):
        response = ValidateCrudeRequester(
            RequestSpecs.auth_headers(username=create_user_request_credit.username, password=create_user_request_credit.password),
            Endpoint.CREDIT_REQUEST,
            ResponseSpecs.request_bad()
        ).crud_requester.post(credit_request)
        return response

    def repay_credit(self, create_user_request_credit: CreateUserRequest, repay_credit:RepayCreditRequest):
        response = ValidateCrudeRequester(
            RequestSpecs.auth_headers(username=create_user_request_credit.username, password=create_user_request_credit.password),
            Endpoint.REPAY_CREDIT,
            ResponseSpecs.request_ok()
        ).post(repay_credit)
        return response


