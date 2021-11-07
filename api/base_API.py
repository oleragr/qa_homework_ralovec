from configfiles.config import ConfigLoader
import requests


class BaseAPI:
    conf = ConfigLoader().get_configuration()
    base_url = conf['base_url_task1']
    session = None

    def __init__(self):
        pass

    def login(self, username, password):

        # login implementation

        self.session = requests.Session()
