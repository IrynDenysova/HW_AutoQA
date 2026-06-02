import requests


class EmployeeApi:

    def __init__(self, url):
        self.url = url

    def create_employee(self, employee_data: dict):
        response = requests.post(
            self.url + "/employee/create",
            json=employee_data)
        return response

    def get_employee(self, employee_id):
        url = f"{self.url}/employee/info/{employee_id}"
        resp = requests.get(url)
        assert resp.status_code == 200, (
            f"Ошибка {resp.status_code}: {resp.text}"
        )
        return resp

    def update_employee(self, employee_id, client_token=None, **kwargs):
        url = f"{self.url}/employee/change/{employee_id}"
        params = {"client_token": client_token}
        return requests.patch(url, params=params, json=kwargs)
