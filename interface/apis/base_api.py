import requests

from interface.utils.logger_until import logger


class BaseApi:

    def __init__(self):
        pass

    def send(self,method,url,tool='requests',**kwargs):
        data = {
            'method':method,
            'url':url
        }
        data.update(kwargs)
        logger.info(kwargs)
        r = requests.request(**data)
        logger.info(r.text)
        return r