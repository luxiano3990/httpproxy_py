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

The docker image container "aiohttp_server" is running just only one application server script : aiohttp_server.py in a Python 3 environment. The server script can also be run as standalone script for testing in a Python 3 environmant.

The client is another Python script which is not included in the docker image : request_client_post.py . We assume the client script to emulate HTTP post requests out of docker container. The client sends a http POST to the server running on port 8080. 

The client post is sending JWT headers and other JSON information. The server collect the client request and appends the JWT token with the new JWT claims JTI and IAT. Then it respond back to the clinet which save the new JWT token with x-my-jwt token recieved.

By launching the docker image, the server script aiohttp_server.py will start to work as HTTP proxy server binded on localhost on port 8080. By running the client script request_client_post.py on another terminal CLI, out of Docker container, a HTTP POST will be sent to http://localhost:8080/protected . An "Authorization : Bearer" header will be sent to the server plus a JSON payload. From the terminal output of the clinet script is possible to see the request sent and also the response from the server which is appending a new JWT token with JTI and IAT claims. The JWT token is added in to server response header as "x-my-jwt" field. 

By running the server script as a standalone application out of docker container, the terinal window will show more relevant information for testing and debugging purpose. (NOTE. A better testing environment can be setup by running client and server scripts from 2 diffrent terminal interface out of Docker container, in order to see the output from the terminal windows).




