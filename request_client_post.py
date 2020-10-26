
import requests

import jwt

from datetime import date

#iat=date.today().strftime("%d/%m/%Y")
#Jti='MyID-001'

# define private secret
secret=('A9ddbcaba8c0ac1a0a812dc0c2f08514b23f2db0a68343cb8199ebb38a6d91e4ebfb378e22ad39c2d01 d0b4ec9c34aa91056862ddace3fbbd6852ee60c36acbf')

#payload = {"user": "username", "date": Iat , "iat" : Iat, "jti" : Jti}

# define client payload
payload = {"user": "username" }

# encode JWT token with payload
token = jwt.encode(payload, secret,algorithm='HS512')

print("Encoded token :")
print(token)


# format the token
auth_token = token.decode('UTF-8')

# define headers
hed = {'Authorization': 'Bearer ' +auth_token}


print("Client headers :")
print (hed)

# define other post data out of headers
data= {'app' : 'Other data'}


# define url to send post requests
url = 'http://localhost:8080/protected'

# send post request to server
response = requests.post(url, json=data, headers=hed )

# save the response JWT token from the server
save_JWT_token = response

print("The response from the server :")
print(response)

print("The server response in json format :")
print(response.json())

print("The server response headers")
print(response.headers)
