from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        parsed_poetry_content = toml.loads(content)['tool']['poetry']

        project_name = parsed_poetry_content['name']
        project_description = parsed_poetry_content['description']
        project_dependencies = parsed_poetry_content['dependencies']
        project_dev_dependencies = parsed_poetry_content['group']['dev']['dependencies']

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(project_name,
                       project_description,
                       project_dependencies,
                       project_dev_dependencies)
