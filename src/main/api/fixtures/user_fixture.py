
import pytest

from src.main.api.generators.model_generator import RandomModelGenerator
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.credit_request import CreditRequest
from src.main.api.models.deposit_request import DepositRequest
from src.main.api.models.repay_credit_request import RepayCreditRequest
from src.main.api.models.transfer_request import TransferRequest


@pytest.fixture
def create_user_request(api_manager):
    user_request = RandomModelGenerator.generate(CreateUserRequest)
    api_manager.admin_steps.create_user(user_request)
    return user_request

@pytest.fixture(params=[1000, 1500, 7777.7, 8999.99, 9000])
def account_deposit(api_manager, create_user_request, request):
    account = api_manager.user_steps.create_account(create_user_request)
    return DepositRequest(accountId=account.id, amount=request.param)

@pytest.fixture(params=[100, 999, 9001, 10000])
def account_negative_deposit(api_manager, create_user_request, request):
    account = api_manager.user_steps.create_account(create_user_request)
    return DepositRequest(accountId=account.id, amount=request.param)

@pytest.fixture(scope='function')
def from_account(api_manager, create_user_request):
    account = api_manager.user_steps.create_account(create_user_request)
    deposit_request = DepositRequest(accountId=account.id, amount=5000)
    from_account = api_manager.user_steps.create_deposit(create_user_request, deposit_request)
    return from_account

@pytest.fixture(scope='function')
def to_account(api_manager, create_user_request):
    return api_manager.user_steps.create_account(create_user_request)

@pytest.fixture(params=[100, 4999, 15001, 20000])
def credit_test_data(request, account_with_credit_request):
    amount = request.param
    credit_request = CreditRequest(
        accountId=account_with_credit_request.id,
        termMonths=12,
        amount=amount
    )
    expected_error = 'Amount must be between 5000 and 15000'
    return {
        'credit_request': credit_request,
        'expected_error': expected_error
    }

@pytest.fixture(scope='function')
def create_user_request_credit(api_manager):
    user_request = RandomModelGenerator.generate(CreateUserRequest)
    user_request.role = "ROLE_CREDIT_SECRET"
    api_manager.admin_steps.create_user(user_request)
    return user_request

@pytest.fixture(scope='function')
def account_with_credit_request(api_manager, create_user_request_credit):
    account = api_manager.user_steps.create_account(create_user_request_credit)
    return account

@pytest.fixture(params=[5000, 7000, 10000, 14999.99, 15000])
def repay_account_with_credit_request(api_manager, request, create_user_request_credit, account_with_credit_request):
    credit_request = CreditRequest(accountId=account_with_credit_request.id, termMonths=12, amount=request.param)
    response = api_manager.user_steps.create_credit_request(create_user_request_credit, credit_request)
    return RepayCreditRequest(
        creditId=response.creditId,
        accountId=response.id,
        amount=request.param
    )

@pytest.fixture(scope='function')
def get_transaction(api_manager, create_user_request, to_account, from_account):
    create_transfer_request = TransferRequest(fromAccountId=from_account.id, toAccountId=to_account.id, amount=1000)
    transfer_response = api_manager.user_steps.create_transfer(create_user_request, create_transfer_request)
    return transfer_response

@pytest.fixture(scope='function')
def transfer_request(from_account, to_account, amount):
    return TransferRequest(fromAccountId=from_account.id, toAccountId=to_account.id, amount=amount)

@pytest.fixture(params=[
    {'amount': 6000, 'expected_error': 'Insufficient funds'},
    {'amount': 0, 'expected_error': 'Amount must be greater than'}
])
def negative_transfer_data(request):
    return request.param

@pytest.fixture
def negative_transfer_request(from_account, to_account, negative_transfer_data):
    return TransferRequest(
        fromAccountId=from_account.id,
        toAccountId=to_account.id,
        amount=negative_transfer_data['amount']
    )