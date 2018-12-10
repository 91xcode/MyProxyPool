import redis
REDIS_HOST = '127.0.0.1'
REDIS_PORT = '6379'
REDIS_PASSWORD = ''
INITIAL_SCORE = 10
REDIS_KEY = 'msk'

class RedisClient(object):
    def __init__(self, host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD):
        """
        初始化
        :param host: Redis 地址
        :param port: Redis 端口
        :param password: Redis密码
        """
        self.db = redis.StrictRedis(host=host, port=port, password=password, decode_responses=True)
        self.redis_version = redis.VERSION[0]

    def add(self, proxy, score=INITIAL_SCORE):
        """
        添加代理，设置分数为最高
        :param proxy: 代理
        :param score: 分数
        :return: 添加结果
        """
        print (self.db)
        return self.db.zadd(REDIS_KEY, {proxy: score})
        # return self.db.zadd(REDIS_KEY, proxy,)
        # if not self.db.zscore(REDIS_KEY, proxy):  # 如果代理没有分数就增加, 无也加入
        #     return self.db.zadd(REDIS_KEY, score, proxy)


if __name__=='__main__':
    # n = RedisClient()
    # # version = n.VERSION[0]
    # # print(n)
    # ss = {'https': 'http://119.139.198.151:18261'}
    # n.add(str(ss))
    # print(1)

    # n.zadd('grade', 100, 'Bob', 98, 'Mike')

    import redis

    print(redis.VERSION)

    # REDIS_HOST = '127.0.0.1'
    # REDIS_PORT = '6379'
    # REDIS_PASSWORD = ''
    # INITIAL_SCORE = 10
    # REDIS_KEY = 'msk'
    #
    import redis
    r = redis.Redis(...)
    if redis.VERSION[0] < 3:
        r.zadd('my-key', element1=score1)
    else:
        r.zadd('my-key', {element1: score1})


