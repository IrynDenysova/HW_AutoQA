import pytest
from HW_7.Employees import EmployeeApi
from HW_7.Auth import AuthApi

base_url = "http://5.101.50.27:8000"
api = EmployeeApi(base_url)


def get_user_token():
    auth_api = AuthApi(base_url)

    response = auth_api.login("harrypotter", "expelliarmus")

    assert response.status_code == 200, (
        f"Ошибка авторизации. Статус: {response.status_code}, тело: {response.text}"
    )

    response_data = response.json()
    return response_data["user_token"]


@pytest.fixture
def sample_employee_data():
    """Статическая фикстура с валидными данными"""
    return {
        "first_name": "John",
        "last_name": "Doe",
        "middle_name": "Smith",
        "company_id": 3,
        "email": "john.doe@example.com",
        "phone": "+79991234567",
        "birthdate": "1995-05-20",
        "is_active": True
    }


def test_create_employee_success(sample_employee_data):
    response = api.create_employee(sample_employee_data)

    assert response.status_code in [200, 201]

    response_data = response.json()

    assert response_data == sample_employee_data


@pytest.mark.parametrize("employee_id", [1, 2, 3, 4, 5, 6])
def test_get_employee_info_success(employee_id):
    response = api.get_employee(employee_id)

    assert response.status_code == 200

    employee_info = response.json()

    assert "first_name" in employee_info
    assert "last_name" in employee_info
    assert "email" in employee_info
    assert "company_id" in employee_info


# def test_get_employee_info_success():
#     employee_id = 1
#
#     response = api.get_employee(employee_id)
#
#     assert response.status_code == 200
#
#     employee_info = response.json()
#
#     assert "first_name" in employee_info
#     assert "last_name" in employee_info
#     assert "email" in employee_info
#     assert "company_id" in employee_info


def test_patch_employee_success():
    user_token = get_user_token()
    employee_id = 1

    update_payload = {
        "phone": "+790012236567",
        "email": "vasia@example.com"
    }

    update_res = api.update_employee(
        employee_id,
        client_token=user_token,
        **update_payload
    )

    print(update_res.status_code)
    print(update_res.text)
    assert update_res.status_code == 200

    info_res = api.get_employee(employee_id).json()
    assert info_res["phone"] == "+790012236567"
    assert info_res["email"] == "vasia@example.com"
