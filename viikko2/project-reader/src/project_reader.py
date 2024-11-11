from urllib import request
import toml
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        content = request.urlopen(self._url).read().decode("utf-8")

        parsed_content = toml.loads(content)

        project_name = parsed_content['tool']['poetry']['name']
        project_description = parsed_content['tool']['poetry']['description']
        project_license = parsed_content['tool']['poetry']['license']
        project_authors = parsed_content['tool']['poetry']['authors']
        dependencies = parsed_content['tool']['poetry']['dependencies']
        development_dependencies = parsed_content['tool']['poetry']['group']['dev']['dependencies']

        return Project(
            project_name,
            project_description,
            project_license,
            project_authors,
            dependencies,
            development_dependencies
        )
