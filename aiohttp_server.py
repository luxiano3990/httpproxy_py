

import jwt

from aiohttp import web

from aiohttp_jwt import JWTMiddleware

from datetime import date

from datetime import datetime  


# Assign new JWT claims
current_date=datetime.now().time()                                                                                    
Iat=str(current_date)    

Jti='MyID-001'

# Define encoding private secret
secret=('A9ddbcaba8c0ac1a0a812dc0c2f08514b23f2db0a68343cb8199ebb38a6d91e4ebfb378e22ad39c2d01 d0b4ec9c34aa91056862ddace3fbbd6852ee60c36acbf')


# Define handler to manage post requetsts
async def protected_handler(request):


    print('Payload request sent by the client :')

    print(request['payload'])

    print('Request sent by the client :')

    print(request)

    print('Response by the server : ')

    print(web.json_response({'IAT': Iat, 'JTI' : Jti ,'user': request['payload']}) )

    print('Headers sent from the client :')

    print(request.headers)

    print('Appending JWT token with new claims...')

    # assign new playload with appended JWT clains
    payload =  {'IAT': Iat, 'JTI' : Jti ,'user': request['payload']}

    print ('New payload appended with IAT and JTI claims : ')

    print(payload)

    # encoding new JWT token
    token = jwt.encode(payload , secret,algorithm='HS512')

    print('New appended JWT token with IAT and JTI claims : ')

    print(token)

    # fromat the token
    auth_token = token.decode('UTF-8')

    # defining new headers for respomse
    hed = {'Authorization': 'Bearer ' }

    # appending new headers with JWT claims
    hed['x-my-jwt'] = auth_token

    print ('New JWT appended heders :')

    print (hed)

    # Return response to client
    return web.json_response(request['payload'],headers=hed)



# Define app
app = web.Application(
    middlewares=[
        JWTMiddleware(secret),
    ]
)


# Define action on post
app.router.add_route('POST', '/protected', protected_handler)

#launch app

if __name__ == '__main__':
    web.run_app(app)
