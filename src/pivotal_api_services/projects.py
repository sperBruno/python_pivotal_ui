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

    def get_projects(self):
        project_list = self.request_handler.get_request(endpoint=self.__project).json()
        print project_list
        for project in project_list:
            print "Asas"
            print type(project)
            print project
            if not project['name'] in self.projects:
                print project['name']
                print project['id']
                self.projects[project['name']] = project['id']
                print 12
        return self.projects

    def get_project(self, id):
        current_url = self.__project + "/" + id
        project = self.request_handler.get_request(endpoint=current_url).json()
        if not project['name'] in self.projects:
            print project['name']
            print project['id']
            self.projects[project['name']] = project['id']
            print 12
        return project

    def get_project_schema(self):
        #TODO: Read and return project json schema
        pass
