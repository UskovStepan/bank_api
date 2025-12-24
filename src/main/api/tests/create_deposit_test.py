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

    def test_positive_deposit(self, api_manager, create_user_request, account_deposit):
        response = api_manager.user_steps.create_deposit(create_user_request, account_deposit)
        assert response.balance == account_deposit.amount

    def test_negative_deposit(self, api_manager, create_user_request, account_negative_deposit):
        response = api_manager.user_steps.create_negative_deposit(create_user_request, account_negative_deposit)
        assert 'Amount must be between 1000 and 9000' in response.text

