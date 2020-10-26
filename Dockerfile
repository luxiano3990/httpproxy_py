FROM python:3
EXPOSE 8080
WORKDIR /app
COPY requirements.txt /app/
COPY aiohttp_server.py /app

RUN pip install -r requirements.txt
CMD python3 aiohttp_server.py
LABEL org.opencontainers.image.source https://github.com/luxiano3990/httpproxy_py
