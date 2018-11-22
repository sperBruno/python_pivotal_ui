from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn

from core.api.request_manager import RequestManager
from utils.property_handler import PropertyHandler

CONTEXT = BuiltIn().get_variable_value('${CONTEXT}')
config_handler = PropertyHandler.get_instance()
request_handler = RequestManager.get_instance()


def i_send_a_post_request_to(endpoint, body):
    logger.info("CommonSteps:: sent %s and %s" % (endpoint, body))
    url = config_handler.get_base_url() + endpoint
    CONTEXT.last_response = request_handler.post_request(endpoint=url, body=body)


def i_expect_the_status_code(status_code):
    logger.info("CommonSteps:: Expect status code be %s" % status_code)
    assert CONTEXT.last_response.status_code == status_code, "Request Failed with status code %s" % CONTEXT.last_response.status_code


def i_stored_as(response_name):
    logger.info("CommonSteps:: Stored %s:" % (response_name))
    CONTEXT.responses = {response_name: CONTEXT.last_response}
