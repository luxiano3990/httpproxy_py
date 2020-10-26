docker push ghcr.io/luxiano3990/aiohttp_server:latest

sudo docker build -t aiohttp_server .

docker run -d -p 8080:8080 --name=my_http aiohttp_server

docker start my_http


# docker stop my_http
# docker rm my_http
