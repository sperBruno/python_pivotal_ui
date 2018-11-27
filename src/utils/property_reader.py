import ConfigParser

PIVOTAL = "PIVOTAL"


class PropertyReader:
    property_reader = None

    def __init__(self, properties='../config.properties'):
        self.__config = ConfigParser.RawConfigParser()
        self.__properties = self.__config.read(properties)
        print properties
        assert len(self.__properties) > 0, "config.properties file must exist at root path"

    def get_user(self):
        return self.__config.get(PIVOTAL, "user")

    def get_base_url(self):
        return self.__config.get(PIVOTAL, "base_url")

    def get_password(self):
        return self.__config.get(PIVOTAL, "password")

    def get_token(self):
        return self.__config.get(PIVOTAL, "token")
