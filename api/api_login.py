import requests
from parameterized import parameterized

import api
from api import BASE_URL


class ApiLogin():
    def __init__(self):
        self.url = BASE_URL+'/api/sys/login'


    def api_login(self,mobile,password):
        data = {"mobile":mobile,"password":password}
        return requests.post(url=self.url,json=data)