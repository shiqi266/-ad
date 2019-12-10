import requests

import api


class ApiEmployee:
    def __init__(self):
        self.add = api.BASE_URL+'/api/sys/user'
        self.employee=api.BASE_URL+'/api/sys/user/{}'


    def api_post(self,username,mobile,workNumber):
        data = {
            'username':username,
            'mobile':mobile,
            'workNumber':workNumber
           }

        return requests.post(url=self.add,json=data,headers=api.headers)

    def api_put(self,username):
        data={
        'username': username,

        }
        return requests.put(url=self.employee.format(api.user_id),json=data,headers=api.headers)

    def api_get(self):
        return  requests.get(url=self.employee.format(api.user_id),headers=api.headers)


    def api_delete(self,user_id):
        return requests.delete(url=self.employee.format(user_id),headers=api.headers)