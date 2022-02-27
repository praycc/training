import json

from genson import SchemaBuilder
from jsonschema import validate,ValidationError,SchemaError

from interface.utils.logger_until import logger


def schmea_validate(obj,schema):
    try:
        validate(instance=obj,schema=schema)
    except ValidationError as e:
        path = " ".join(i for i in e.path)
        logger.error(f"验证出错，错误地址：{path},错误的信息：{e.message}")
        return False
    except Exception as e:
        logger.error(f"验证出错，错误信息：{e.message}")
        return False
    else:
        logger.info("验证成功")
        return True


def test_genson():
    builder = SchemaBuilder()
    builder.add_object({"a": 1, "b": "222", "c": '', "d": None})
    builder.add_object({"a": "1", "b": "2", "c": 3})
    json.dump(builder.to_schema(), open("schema_demo.json", 'w', encoding='utf8'))

def test_schema():
    _schema = json.load(open("schema_demo.json", encoding='utf8'))
    assert schmea_validate({"a":1,"b":"2","c":123},schema=_schema)