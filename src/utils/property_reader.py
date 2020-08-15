import os

import configparser

PIVOTAL = "PIVOTAL"
USERNAME = "user"
PASS = "password"
TOKEN = "token"
BASE_UI_URL = "base_ui_url"
BASE_API_URL = "base_api_url"
BROWSER = "browser"


class PropertyReader:
    __instance = None

    def __init__(self, properties='..\..\config.properties'):
        self.__config = configparser.RawConfigParser()
        path_join = os.path.join(os.path.dirname(os.path.abspath(__file__)), properties)
        print(path_join)
        self.__properties = self.__config.read(path_join)
        print(self.__properties)
        assert len(self.__properties) > 0, "config.properties file must exist at root path"

    def get_env(self, variable):
        return self.__config.get(PIVOTAL, variable)

    def get_user(self):
        return self.get_env(USERNAME)

    def get_base_ui_url(self):
        return self.get_env(BASE_UI_URL)

    def get_base_api_url(self):
        return self.get_env(BASE_API_URL)

    def get_password(self):
        return self.get_env(PASS)

    def get_token(self):
        return self.get_env(TOKEN)

    def get_browser(self):
        return self.get_env(BROWSER)

    def get_implicit_time_wait(self):
        return int(self.get_env("implicitTimeWait"))

    def get_explicit_time_wait(self):
        return int(self.get_env("explicitTimeWait"))

    @staticmethod
    def get_property():
        if PropertyReader.__instance is None:
            PropertyReader.__instance = PropertyReader()
        return PropertyReader.__instance
