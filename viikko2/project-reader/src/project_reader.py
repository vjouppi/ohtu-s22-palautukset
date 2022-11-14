from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        #print(content)
        parsed_content = toml.loads(content)
        name = parsed_content['tool']['poetry']['name']
        desc = parsed_content['tool']['poetry']['description']
        if desc == '':
            desc = '-'
        deps = parsed_content['tool']['poetry']['dependencies'].keys()
        dev = parsed_content['tool']['poetry']['dev-dependencies'].keys()

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, desc, deps, dev)
