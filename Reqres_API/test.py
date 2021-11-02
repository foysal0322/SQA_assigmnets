class Api():

    def signup_post(self,url,json_data):
        import requests
        import json
        response=requests.post(url,json_data)
        print(json.dumps(response.json()))
        print(response.status_code)


    def signup_get(self,url,json_data):
        import requests
        import json
        response=requests.get(url,json_data)
        print(json.dumps(response.json()))
        print(response.status_code)

    def login_post(self,url,json_data):
        import requests
        import json
        response=requests.post(url,json_data)
        print(json.dumps(response.json()))
        print(response.status_code)

    def login_get(self,url,json_data):
        import requests
        import json
        response=requests.post(url,json_data)
        print(json.dumps(response.json()))
        print(response.status_code)

    def list_users_get(self,url):
        import requests
        import json
        response=requests.get(url)
        print(json.dumps(response.json()))
        print(response.status_code)

    def single_users_get(self,url):
        import requests
        import json
        response=requests.get(url)
        print(json.dumps(response.json()))
        print(response.status_code)

    def post_user(self,url,json_data):
        import requests
        import json
        response=requests.post(url,json_data)
        print(json.dumps(response.json()))
        print(response.status_code)

    def updated_user(self,url,json_data):
        import requests
        import json
        response=requests.post(url,json_data)
        print(json.dumps(response.json()))
        print(response.status_code)

    def delayed_response(self,url):
        import requests
        import json
        response=requests.get(url)
        print(json.dumps(response.json()))
        print(response.status_code)
        




        


