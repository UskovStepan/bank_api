import pytest
from src.main.api.fixtures.api_fixture import api_manager
from src.main.api.models.credit_request import CreditRequest

@pytest.mark.api
class TestCreateRequestCredit:
    # username = 'Stepans0211112'
    # def test_request_credit(self):
    #     login_admin_response = requests.post(
    #         url='http://localhost:4111/api/auth/token/login',
    #         json={
    #             'username': 'admin',
    #             'password': '123456'
    #         },
    #         headers={
    #             'Content-Type': 'application/json',
    #             'accept': 'application/json'
    #         }
    #     )
    #     assert login_admin_response.status_code == 200
    #     token = login_admin_response.json().get('token')
    #
    #     create_user_response = requests.post(
    #         url='http://localhost:4111/api/admin/create',
    #         json={
    #             'username': TestCreateRequestCredit.username,
    #             'password': 'Pas!sw0rd',
    #             'role': 'ROLE_CREDIT_SECRET',
    #         },
    #         headers={
    #             'Content-Type': 'application/json',
    #             'Authorization': f'Bearer {token}'
    #         }
    #     )
    #     assert create_user_response.status_code == 200
    #
    #     login_user_response = requests.post(
    #         url='http://localhost:4111/api/auth/token/login',
    #         json={
    #             'username': TestCreateRequestCredit.username,
    #             'password': 'Pas!sw0rd'
    #         },
    #         headers={
    #             'Content-Type': 'application/json',
    #             'accept': 'application/json',
    #         }
    #     )
    #     assert login_user_response.status_code == 200
    #     user_token = login_user_response.json().get('token')
    #
    #     create_from_deposit_response = requests.post(
    #         url='http://localhost:4111/api/account/create',
    #         headers={
    #             'accept': 'application/json',
    #             'Authorization': f'Bearer {user_token}'
    #         }
    #     )
    #     assert create_from_deposit_response.status_code == 201
    #     from_account_id = create_from_deposit_response.json().get('id')
    #
    #     create_credit_response = requests.post(
    #         url = 'http://localhost:4111/api/credit/request',
    #         json = {
    #             "accountId": from_account_id,
    #             "amount": 5000,
    #             "termMonths": 12
    #         },
    #         headers={
    #             'accept': 'application/json',
    #             'Authorization': f'Bearer {user_token}',
    #             'Content-Type': 'application/json'
    #         }
    #     )
    #
    #     assert create_credit_response.status_code == 201, f'Create credit failed: {create_credit_response.text}'
    #     assert create_credit_response.json().get('balance') == 5000
    #     assert create_credit_response.json().get('termMonths') == 12

    # def test_request_credit_middle(self):
    #     """Логинимся под администратора и создаем пользователя"""
    #     create_user_request = CreateUserRequest(username=TestCreateRequestCredit.username,
    #                                             password='Pas!sw0rd', role='ROLE_CREDIT_SECRET')
    #     create_user_response = CreateUserRequester(
    #         request_spec=RequestSpecs.auth_headers(username='admin', password='123456'),
    #         response_spec=ResponseSpecs.request_ok()
    #     ).post(create_user_request)
    #     print(create_user_response.model_dump())
    #
    #     """Логинимся пользователем и создаем счет"""
    #     create_account_response = CreateAccountRequest(
    #         request_spec=RequestSpecs.auth_headers(username=create_user_request.username,
    #                                                password=create_user_request.password),
    #         response_spec=ResponseSpecs.request_create()
    #     ).post()
    #     account_id = create_account_response.id
    #     print(create_account_response.model_dump())
    #
    #     """Подаем заявку на взятие кредита"""
    #     create_credit_request = CreditRequest(accountId=account_id, amount=10000, termMonths=6)
    #     create_credit_response = CreateCreditRequester(
    #         request_spec=RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
    #         response_spec=ResponseSpecs.request_create()
    #     ).post(create_credit_request)
    #
    #     print(f'response error: {create_credit_request.model_dump()}')
    #     assert create_credit_response.balance == 10000

    def test_request_credit_senior(self, api_manager,create_user_request_credit, account_with_credit_request):
        credit_request = CreditRequest(accountId=account_with_credit_request.id, termMonths=12, amount=5000)
        response = api_manager.user_steps.create_credit_request(create_user_request_credit, credit_request)

        assert response.balance == 5000


    @pytest.mark.parametrize('amount', [100, 4999, 15001, 20000])
    def test_board_sum_credit(self, api_manager, create_user_request_credit, account_with_credit_request, amount):
        credit_request = CreditRequest(accountId=account_with_credit_request.id, termMonths=12, amount=amount)
        response = api_manager.user_steps.negative_credit_request(create_user_request_credit, credit_request)

        assert 'Amount must be between 5000 and 15000' in response.text