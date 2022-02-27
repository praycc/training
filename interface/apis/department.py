import requests

from interface.apis.wework import WeWork
from interface.utils.file_tools import FileTools


class Department(WeWork):
    def __init__(self):
        crop_data = FileTools.read_yaml('secrets')
        corpid = crop_data.get('corpid').get('pray')
        corpsecret = crop_data.get('corpsecret').get('department')
        self.access_token = self.get_token(corpid,corpsecret)

    def creat(self,data):
        url = f'https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={self.access_token}'
        r = self.send('POST',url,tool='requests',json=data)
        return r

    def update(self,data):
        url = f'https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={self.access_token}'
        r = self.send('POST',url,json=data)
        return r

    def delete_department(self,id):
        url = f'https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={self.access_token}&id={id}'
        r = self.send('GET',url)
        return r

    def get_list(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.access_token}"
        r = self.send('GET',url)
        return r