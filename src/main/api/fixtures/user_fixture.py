
import pytest

from src.main.api.generators.model_generator import RandomModelGenerator
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.credit_request import CreditRequest
from src.main.api.models.deposit_request import DepositRequest
from src.main.api.models.transfer_request import TransferRequest


@pytest.fixture
def create_user_request(api_manager):
    user_request = RandomModelGenerator.generate(CreateUserRequest)
    api_manager.admin_steps.create_user(user_request)
    return user_request

@pytest.fixture(scope='function')
def create_user_request_credit(api_manager):
    user_request = RandomModelGenerator.generate(CreateUserRequest)
    user_request.role = "ROLE_CREDIT_SECRET"
    api_manager.admin_steps.create_user(user_request)
    return user_request

@pytest.fixture(scope='function')
def from_account(api_manager, create_user_request):
    account = api_manager.user_steps.create_account(create_user_request)
    deposit_request = DepositRequest(accountId=account.id, amount=5000)
    from_account = api_manager.user_steps.create_deposit(create_user_request, deposit_request)
    return from_account

@pytest.fixture(scope='function')
def to_account(api_manager, create_user_request):
    return api_manager.user_steps.create_account(create_user_request)

@pytest.fixture(scope='function')
def account_with_credit_request(api_manager, create_user_request_credit):
    account = api_manager.user_steps.create_account(create_user_request_credit)
    return account

@pytest.fixture(scope='function')
def repay_account_with_credit_request(api_manager, create_user_request_credit, account_with_credit_request):
    account = api_manager.user_steps.create_account(create_user_request_credit)
    credit_request = CreditRequest(accountId=account_with_credit_request.id, termMonths=12, amount=9000)
    response = api_manager.user_steps.create_credit_request(create_user_request_credit, credit_request)
    return response

@pytest.fixture(scope='function')
def get_transactions(api_manager, create_user_request, to_account, from_account):
    create_transfer_request = TransferRequest(fromAccountId=from_account.id, toAccountId=to_account.id, amount=1000)
    transfer_response = api_manager.user_steps.create_transfer(create_user_request, create_transfer_request)
    return transfer_response