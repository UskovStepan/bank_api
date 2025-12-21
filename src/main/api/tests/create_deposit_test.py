from src.main.api.models.deposit_request import DepositRequest
import pytest

@pytest.mark.api
class TestCreateDepositTest:
    # username = 'Stepans031122'
    # def test_replenishment_deposit(self):
    #     create_user_request = CreateUserRequest(username=TestCreateDepositTest.username, password='Pas!sw0rd', role='ROLE_USER')
    #     CreateUserRequester(
    #         request_spec=RequestSpecs.auth_headers(username='admin', password='123456'),
    #         response_spec=ResponseSpecs.request_ok()
    #     ).post(create_user_request)
    #
    #     create_account_response = CreateAccountRequest(
    #         request_spec=RequestSpecs.auth_headers(username=create_user_request.username, password='Pas!sw0rd'),
    #         response_spec=ResponseSpecs.request_create()
    #     ).post()
    #
    #     account_id = create_account_response.id
    #     assert create_account_response.balance == 0
    #
    #
    #     deposit_request = DepositRequest(accountId=account_id, amount=3000)
    #     create_deposit_response = CreateDepositRequester(
    #         request_spec=RequestSpecs.auth_headers(create_user_request.username, create_user_request.password),
    #         response_spec=ResponseSpecs.request_ok()
    #     ).post(deposit_request)
    #     assert create_deposit_response.balance == 3000
    #     print(create_deposit_response)

    def test_deposit(self, api_manager, create_user_request):
        account_id = api_manager.user_steps.create_account(create_user_request).id
        deposit_request = DepositRequest(accountId=account_id, amount=5500)
        create_deposit = api_manager.user_steps.create_deposit(create_user_request, deposit_request)

        assert create_deposit.balance == 5500

    @pytest.mark.parametrize('amount', [100, 999, 9001, 10000])
    def test_border_deposit(self, api_manager, create_user_request, from_account, amount):
        deposit_request = DepositRequest(accountId=from_account.id, amount=amount)
        response = api_manager.user_steps.create_negative_deposit(create_user_request, deposit_request)

        assert 'Amount must be between' in response.text

