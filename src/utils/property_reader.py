import ConfigParser

PIVOTAL = "PIVOTAL"
USERNAME = "user"
PASS = "password"
TOKEN = "token"
BASE_UI_URL = "base_ui_url"
BASE_API_URL = "base_api_url"
BROWSER = "browser"


class PropertyReader:
    property_reader = None

    def __init__(self, properties='..\config.properties'):
        self.__config = ConfigParser.RawConfigParser()
        self.__properties = self.__config.read(properties)
        print properties
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
