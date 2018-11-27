from robot.libraries.BuiltIn import BuiltIn

from pivotal_api_services.projects import ProjectServices


project_service = ProjectServices()
CONTEXT = BuiltIn().get_variable_value('${CONTEXT}')

def i_create_a_project(project_data):
    CONTEXT.project_status, CONTEXT.project_response = project_service.create_project(project_data)
    print CONTEXT.project_response

def i_verify_project_creation_is_succesfull():
    print "**************************************"
    print CONTEXT.project_response["id"]
    print project_service.get_projects(id=str(CONTEXT.project_response["id"]))
    actual_status_code = CONTEXT.project_status
    assert actual_status_code is 200, "Project Status code is {}".format(actual_status_code)

def i_verify_data_of_project_is_accurate(project_data):
    actual_response = CONTEXT.project_response
    for key, value in project_data.items():
        assert actual_response[key] is value, "Project Status code is {}".format(actual_response)