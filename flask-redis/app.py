import os

import time

import redis
from flask import Flask

app = Flask(__name__)
REDIS_MASTER_HOST = os.environ.get('REDIS_MASTER_SERVICE_HOST')
cache = redis.Redis(host=REDIS_MASTER_HOST, port=6379)
import socket
my_ip = [l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1],
                   [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in
                     [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0]
def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    return 'Hello World! I have been seen {} times.\n my ip: {}'.format(count,my_ip)