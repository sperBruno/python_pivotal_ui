from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn

CONTEXT = BuiltIn().get_variable_value('${CONTEXT}')

def i_send_a_post_request_to(endpoint, body):
    logger.info("CommonSteps:: sent %s and %s" % (endpoint, body))


def i_expect_the_status_code(status_code):
    logger.info("CommonSteps:: Expect status code be %s" % status_code)
    CONTEXT.last_response = "Last Response"


def i_stored_as(response_name):
    logger.info("CommonSteps:: Stored %s:" % (response_name))
    CONTEXT.response_contex_name = {response_name: CONTEXT.last_response}
