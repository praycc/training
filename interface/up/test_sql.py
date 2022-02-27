import requests


def test_register():
    json_data = {
            "phone": "13888888888",
            "password": "123456",
            "name": "张三"
    }
    r = requests.post(url='http://127.0.0.1:5000/register',json=json_data)
    print(r.json())