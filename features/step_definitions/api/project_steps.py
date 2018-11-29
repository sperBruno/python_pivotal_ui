from robot.libraries.BuiltIn import BuiltIn
from pivotal_api_services.projects import ProjectServices
from utils.json_schema_validator import validate_json_schema

project_service = ProjectServices()
CONTEXT = BuiltIn().get_variable_value('${CONTEXT}')


def i_create_a_project(project_data):
    CONTEXT.project_status, CONTEXT.project_response = project_service.create_project(project_data)


def i_verify_project_creation_status_is(status_code):
    assert CONTEXT.project_status is int(status_code), "Project Status code is {}".format(CONTEXT.project_status)


def i_verify_data_of_project_is_accurate(project_data):
    actual_response = project_service.get_project(id=str(CONTEXT.project_response["id"]))
    for key, value in project_data.items():
        assert actual_response[key] == value, "Project data {} != {}".format(actual_response[key], value)


def i_verify_project_schema():
    actual_response = project_service.get_project(id=str(CONTEXT.project_response["id"]))
    schema_failure_reason, is_schema_valid = validate_json_schema(project_service.get_project_schema(), actual_response)
    assert is_schema_valid, "Project Schema failed due to: {}".format(schema_failure_reason)
