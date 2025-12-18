import pytest

from src.main.api.models.deposit_request import DepositRequest
from src.main.api.models.transfer_request import TransferRequest

@pytest.mark.api
class TestCreateTransfer:
    # username = 'Stepans041122'
    # def test_transfer_deposit(self):
    #     login_admin_request = LoginUserRequest(username='admin', password='123456')
    #     login_admin_response = requests.post(
    #         url='http://localhost:4111/api/auth/token/login',
    #         json=login_admin_request.model_dump(),
    #         headers={
    #             'Content-Type': 'application/json',
    #             'accept': 'application/json'
    #         }
    #     )
    #     assert login_admin_response.status_code == 200
    #     token = login_admin_response.json().get('token')
    #
    #     create_user_request = CreateUserRequest(username=TestCreateTransfer.username, password='Pas!sw0rd', role='ROLE_USER')
    #     create_user_response = requests.post(
    #         url = 'http://localhost:4111/api/admin/create',
    #         json = create_user_request.model_dump(),
    #         headers={
    #             'Content-Type': 'application/json',
    #             'Authorization': f'Bearer {token}'
    #         }
    #     )
    #     assert create_user_response.status_code == 200
    #
    #     login_user_request = LoginUserRequest(username=TestCreateTransfer.username, password='Pas!sw0rd')
    #     login_user_response = requests.post(
    #         url='http://localhost:4111/api/auth/token/login',
    #         json=login_user_request.model_dump(),
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
    #     create_to_deposit_response = requests.post(
    #         url='http://localhost:4111/api/account/create',
    #         headers={
    #             'accept': 'application/json',
    #             'Authorization': f'Bearer {user_token}'
    #         }
    #     )
    #     assert create_to_deposit_response.status_code == 201
    #     to_account_id = create_to_deposit_response.json().get('id')
    #
    #     create_deposit_request = DepositRequest(accountId=from_account_id, amount=5000.5)
    #     deposit_response = requests.post(
    #         url='http://localhost:4111/api/account/deposit',
    #         json=create_deposit_request.model_dump(),
    #         headers={
    #             'accept': 'application/json',
    #             'Authorization': f'Bearer {user_token}',
    #             'Content-Type': 'application/json',
    #         }
    #     )
    #     assert deposit_response.status_code == 200, f'Deposit failed: {deposit_response.text}'
    #     balance = deposit_response.json().get('balance')
    #     assert balance == 5000.5
    #
    #     create_transfer_request = TransferRequest(fromAccountId=from_account_id, toAccountId=to_account_id, amount=1250.38)
    #     response = requests.post(
    #         url='http://localhost:4111/api/account/transfer',
    #         json=create_transfer_request.model_dump(),
    #         headers={
    #             'accept': 'application/json',
    #             'Authorization': f'Bearer {user_token}',
    #             'Content-Type': 'application/json',
    #         }
    #     )
    #     assert response.status_code == 200, f'Transfer failed: {response.text}'
    #     create_transfer_response = TransferResponse(**response.json())
    #     assert create_transfer_response.fromAccountIdBalance == balance - create_transfer_request.amount


    # def test_transfer_deposit_middle(self):
    #     """Логинимся под администратора и создаем пользователя"""
    #     create_user_request = CreateUserRequest(username=TestCreateTransfer.username,
    #                                             password='Pas!sw0rd', role='ROLE_USER')
    #     create_user_response = CreateUserRequester(
    #         request_spec=RequestSpecs.auth_headers(username='admin', password='123456'),
    #         response_spec=ResponseSpecs.request_ok()
    #     ).post(create_user_request)
    #
    #     """Логинимся пользователем и создаем первый счет который будет пополняться"""
    #     create_account_from_response = CreateAccountRequest(
    #         request_spec=RequestSpecs.auth_headers(username=create_user_request.username,
    #                                                password=create_user_request.password),
    #         response_spec=ResponseSpecs.request_create()
    #     ).post()
    #     account_id_from = create_account_from_response.id
    #
    #     """Создаем втророй счет на который будем переводить деньги с первого"""
    #     create_account_to_response = CreateAccountRequest(
    #         request_spec=RequestSpecs.auth_headers(username=create_user_request.username,
    #                                                password=create_user_request.password),
    #         response_spec=ResponseSpecs.request_create()
    #     ).post()
    #     account_id_to = create_account_to_response.id
    #
    #     """Пополняем первый счет"""
    #     deposit_request = DepositRequest(accountId=account_id_from, amount = 3000)
    #     create_deposit_response = CreateDepositRequester(
    #         request_spec=RequestSpecs.auth_headers(username=create_user_request.username,
    #                                                password=create_user_request.password),
    #         response_spec=ResponseSpecs.request_ok()
    #     ).post(deposit_request)
    #     balance = create_deposit_response.balance
    #
    #     """Переводим деньги с первого счета на второй, проверяем балан второго счета"""
    #     create_transfer_request = TransferRequest(fromAccountId=account_id_from, toAccountId=account_id_to, amount=1250.38)
    #     create_transfer_response = CreateTransferRequester(
    #         request_spec=RequestSpecs.auth_headers(username = create_user_request.username, password = create_user_request.password),
    #         response_spec=ResponseSpecs.request_ok()
    #     ).post(create_transfer_request)
    #
    #     assert create_transfer_response.fromAccountIdBalance == balance - create_transfer_request.amount
    #     print(create_transfer_response.fromAccountIdBalance)

    def test_transfer_deposit(self, api_manager, create_user_request):
        from_account_id = api_manager.user_steps.create_account(create_user_request).id
        deposit_request = DepositRequest(accountId=from_account_id, amount=5000)
        deposit = api_manager.user_steps.create_deposit(create_user_request, deposit_request)

        to_account_id = api_manager.user_steps.create_account(create_user_request).id
        create_transfer = TransferRequest(fromAccountId=from_account_id, toAccountId=to_account_id, amount=3000)

        transfer_response = api_manager.user_steps.create_transfer(create_user_request, create_transfer)

        assert transfer_response.fromAccountIdBalance == 2000