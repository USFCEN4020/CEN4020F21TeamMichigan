import os
import redis
import sys

class Database:
    def __init__(self, zset_name):
        redis_host = os.environ.get('REDIS_HOST', '127.0.0.1')
        redis_port = os.environ.get('REDIS_PORT', 6379)

        self.db = redis.StrictRedis(host=redis_host, port=redis_port)
        self.zset_name = zset_name

    def add(self, key):
        try:
            self.db.zadd(self.zset_name, {key: 0})
        except redis.exceptions.ConnectionError:
            print("Unable to connect to redis host.")
            sys.exit(0)