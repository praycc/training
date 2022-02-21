from faker import Faker


class Untils:

    @classmethod
    def get_name(self):
        return Faker('zh_CN').name()

    @classmethod
    def get_phonenumber(self):
        return Faker('zh_CN').phone_number()