import pytest

from src.main.api.generators.model_generator import RandomModelGenerator
from src.main.api.models.create_user_request import CreateUserRequest

@pytest.mark.api
class TestCreateUser:
    @pytest.mark.parametrize(
        'create_user_request',
        [RandomModelGenerator.generate(CreateUserRequest)],
    )
    def test_create_user_valid(self, api_manager, create_user_request):
        response = api_manager.admin_steps.create_user(create_user_request)
        print(response)
        assert create_user_request.username == response.username
        assert create_user_request.role == response.role

    @pytest.mark.parametrize(
        'username, password',
        [
            ('абв','Pas!sw0rd'),
            ('аб', 'Pas!sw0rd'),
            ('abv!', 'Pas!sw0rd'),
            ('Stepan002', 'Pas!sw0rд'),
            ('Stepan003', 'Pas!sw0'),
            ('Stepan004', 'pas!sw0rd'),
            ('Stepan005', 'PAS!SW0RD'),
            ('Stepan006', 'PASSSWORD'),
            ('Stepan007', 'PAS!SWRRD')
        ]
    )
    def test_create_user_invalid(self, username, password, api_manager):
        create_user_request = CreateUserRequest(username=username, password=password, role='ROLE_USER')
        api_manager.admin_steps.create_invalid_user(create_user_request)
