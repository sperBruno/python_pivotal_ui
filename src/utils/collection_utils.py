from robot.libraries.BuiltIn import BuiltIn
from robot.api import logger


def create_a_dictionary(**kwargs):
    logger.info("Collection_utils;;create_dictionary::{}".format(kwargs))
    BuiltIn.create_dictionary(kwargs)
