# httpproxy_py

This is a Python programming task to build a HTTP proxy that takes a POST request from a client and appends a JSON Web Token (JWT) with following claims :

1) iat - Timestamp of the request as specified by the specification

2) jti- A cryptographic nonce that should be unique

3) payload - A json payload of the structure: {"user": "username", "date": "todays date"}

The JWT os signed with the following hex string secret using the HS512 alogrithm as in the JWT spec:

a9ddbcaba8c0ac1a0a812dc0c2f08514b23f2db0a68343cb8199ebb38a6d91e4ebfb378e22ad39c2d01 d0b4ec9c34aa91056862ddace3fbbd6852ee60c36acbf

The JWT is appended to the x-my-jwt header into the upstream post request sent from client.

The upstream post endpoint is http://localhost:8080/protected 

This tasks implements the following requirements:

- Use Python3.6+
- Use the follwing Python  libraries : aiohttp, PyJWT, requests, datetime
- Use Docker to build a Python 3 image
- It provides a docker-compose.yml version 3.8 to specify the web service which binds on port 8080
- It providse a Makefile with following build and run targets
- Yhe HTTP_PORT variable is 8080 
- The project is delivered via a public GitHub repository
- The status page is included in the script aiohttp_server.py which show at execution time all information about the current connection , status, headers, encoding , jwt, etc. It logs each requests.
- It Usse asyncronous programming
- Test functionality is built in the server output once run the server script and clinet scripts from CLI : aiohttp_server.py and  request_client_post.py

The docker image is just only one application server script : aiohttp_server.py which can also be run as standalone in a Python 3 environmant for testing.

The client is another Python script :  request_client_post.py which sends a http POST to the server running on port 8080. The post is sending JWT headers and other JSON information. The server collect the clinet request and appends the JWT token with the new JWT claims JTI and IAT. Then it respond back to the clinet which save the new JWT token with x-my-jwt token recieved.



