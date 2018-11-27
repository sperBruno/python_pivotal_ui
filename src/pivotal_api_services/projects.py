from pivotal_api_services.pivotal_services import PivotalServices


class ProjectServices(PivotalServices):

    def __init__(self):
        super(ProjectServices, self).__init__()
        self.__project = "{}/projects".format(self.request_handler.main_url)
        self.project = {}
        self.projects = {}

    def create_project(self, data):
        response = self.request_handler.post_request(endpoint=self.__project, body=data)
        # print response.json()["id"]
        return response.status_code, response.json()

    def get_projects(self, id=""):

        current_url = "{}/{}".format(self.__project, id) if id is not "" else self.__project
        project_list = self.request_handler.get_request(endpoint=current_url).json()
        # print project_list
        for project in project_list:
            # print project
            self.projects[project['name']] = project['id']
        return self.projects
