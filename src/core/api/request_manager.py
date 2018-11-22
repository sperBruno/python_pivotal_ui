from core.api.request_handler import RequestHandler


class RequestManager:

    @staticmethod
    def get_instance():
        return RequestHandler()