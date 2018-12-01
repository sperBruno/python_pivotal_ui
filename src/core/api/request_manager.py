from core.api.request_handler import RequestHandler
from utils.property_handler import PropertyHandler


class RequestManager:
    __instance = None

    @staticmethod
    def get_instance():
        if RequestManager.__instance is None:
            RequestManager.__instance = RequestHandler()
            RequestManager.__instance.session.headers.update(
                {"X-TrackerToken": PropertyHandler.get_instance().get_token(),
                 "Content-Type": "application/json"})
        return RequestManager.__instance
