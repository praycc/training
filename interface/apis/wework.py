from interface.apis.base_api import BaseApi
from interface.utils.file_tools import FileTools


class WeWork(BaseApi):

    def get_token(self,corpid,corpsecret):
        # corpid = 'ww92a70d6031c9bd2f'
        # corpsecret = 'MG3TfgdsS29DKy_KNHBCb7hXx3wf5fOVLR3a3ix6pEI'
        url = f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}'
        r = self.send('GET',url)
        return r.json().get('access_token')
