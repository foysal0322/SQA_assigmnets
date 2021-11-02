from test import *
json_data={
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}

json_data_invalid_email={
    "email": "abcd",
    "password": "pistol"
}

json_data_empty_password={
    "email": "eve.holt@reqres.in",
    "password": ""
}

json_data_invalid_password={
    "email": "eve.holt@reqres.in",
    "password": "rifel"
}

login_data={
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
}
login_data_invalid_email={
    "email": "abc",
    "password": "cityslicka"
}
login_data_invalid_password={
    "email": "eve.holt@reqres.in",
    "password": "wrong_pass"
}
login_data_empty_email={
    "email": "",
    "password": "cityslicka"
}


login_data_empty_password={
    "email": "eve.holt@reqres.in",
    "password": ""
}

post_user={
    "name": "morpheus",
    "job": "leader"
  
}
post_user_invalid={
    "name": "",
    
}
updated_user={
    "name": "morpheus",
    "job": "zion resident"
}

obj=Api()

# obj.signup_post('https://reqres.in/api/register',json_data)
# obj.signup_post('https://reqres.in/api/register',json_data_empty_password)
# obj.signup_post('https://reqres.in/api/register',json_data_invalid_email)
# obj.signup_post('https://reqres.in/api/register',json_data_invalid_password)
# obj.signup_get('https://reqres.in/api/register',json_data)
# obj.login_post('https://reqres.in/api/login',login_data)
# obj.login_post('https://reqres.in/api/login',login_data_invalid_email)
# obj.login_post('https://reqres.in/api/login',login_data_invalid_password)
# obj.login_post('https://reqres.in/api/login',login_data_empty_email)
# obj.login_post('https://reqres.in/api/login',login_data_empty_password)
# try:
#     obj.login_post('abcd.com',login_data)
# except Exception as e:
#     print(e)

# obj.login_get('https://reqres.in/api/login',login_data)
# obj.list_users_get('https://reqres.in/api/users?page=2')
# obj.single_users_get('https://reqres.in/api/users/2')
# obj.single_users_get('https://reqres.in/api/users/23') # single user invalid
# obj.post_user('https://reqres.in/api/users',post_user)
# obj.post_user('https://reqres.in/api/users',post_user_invalid) #post invalid user
# obj.updated_user('https://reqres.in/api/users/2',updated_user)
obj.delayed_response('https://reqres.in/api/users?delay=3')