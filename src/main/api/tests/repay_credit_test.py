import pytest
from src.main.api.models.credit_request import CreditRequest
from src.main.api.models.repay_credit_request import RepayCreditRequest


@pytest.mark.api
class TestRepayCredit:
    # username = 'Stepans0611222'
    # def test_repay_credit(self):
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
    #             'username': TestRepayCredit.username,
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
    #             'username': TestRepayCredit.username,
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
    #     credit_id = create_credit_response.json().get('creditId')
    #
    #     repay_credit = requests.post(
    #         url='http://localhost:4111/api/credit/repay',
    #         json={
    #             "creditId": credit_id,
    #             "accountId": from_account_id,
    #             "amount": 5000
    #         },
    #         headers={
    #             'accept': 'application/json',
    #             'Authorization': f'Bearer {user_token}',
    #             'Content-Type': 'application/json'
    #         }
    #     )
    #     assert repay_credit.status_code == 200

    # def test_repay_credit_level_2(self):
    #     """Логинимся под администратора и создаем пользователя"""
    #     create_user_requester = CreateUserRequest(username=TestRepayCredit.username, password='Pas!sw0rd', role='ROLE_CREDIT_SECRET')
    #     create_user_response = CreateUserRequester(
    #         request_spec=RequestSpecs.auth_headers(username='admin', password='123456'),
    #         response_spec=ResponseSpecs.request_ok()
    #     ).post(create_user_requester)
    #
    #     '''Логинимся пользователем и создаем счет'''
    #     create_account_requester = CreateAccountRequest(
    #         request_spec=RequestSpecs.auth_headers(username=TestRepayCredit.username, password='Pas!sw0rd'),
    #         response_spec=ResponseSpecs.request_create(),
    #     ).post()
    #     account_id = create_account_requester.id
    #
    #     """Подаем заявку на креди"""
    #     create_credit_request = CreditRequest(accountId=account_id, amount=10000, termMonths=12)
    #     credit_response = CreateCreditRequester(
    #         request_spec=RequestSpecs.auth_headers(username=TestRepayCredit.username, password='Pas!sw0rd'),
    #         response_spec=ResponseSpecs.request_create()
    #     ).post(create_credit_request)
    #     credit_id = credit_response.creditId
    #
    #     """Погашаем кредит единоразовым палтежем"""
    #     create_repay_request = RepayCreditRequest(creditId=credit_id, accountId=account_id, amount=10000)
    #     create_repay_response = CreateRepayRequester(
    #         request_spec=RequestSpecs.auth_headers(username=TestRepayCredit.username, password='Pas!sw0rd'),
    #         response_spec=ResponseSpecs.request_ok()
    #     ).post(create_repay_request)
    #
    #     print(create_repay_response.model_dump())

    def test_repay_credit_senior(self, api_manager, create_user_request_credit, repay_account_with_credit_request):
        repay_credit = RepayCreditRequest(creditId=repay_account_with_credit_request.creditId, accountId=repay_account_with_credit_request.id, amount=9000)
        repay_response = api_manager.user_steps.repay_credit(create_user_request_credit, repay_credit)

