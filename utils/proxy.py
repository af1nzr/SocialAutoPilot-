import random
import config

class ProxyManager:
    @staticmethod
    def get_random_proxy():
        return random.choice(config.PROXY_LIST)
