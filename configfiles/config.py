import yaml, os
from pathlib import Path
import argparse
from dotenv import load_dotenv
load_dotenv()

path = Path(__file__).parent


class ConfigLoader:
    def __init__(self):
        with open(os.path.join(path, 'config.yml')) as file:
            self.config = yaml.load(file, Loader=yaml.SafeLoader)
        # Get cmd command --env and use this for loading configuration file
        self.parser = argparse.ArgumentParser(description="run test using --env configuration")
        self.parser.add_argument('--env', help='host to run tests on (default: %(default)s)', default='test')
        args, notknownargs = self.parser.parse_known_args()
        self.env = args.env

    def get_configuration(self):
        assert self.env in self.config.keys()
        self.config[self.env]['env'] = self.env
        for item in self.config[self.env]:
            env_var = self.read_env_variables('ENV_' + item)
            if env_var:
                self.config[self.env][item] = env_var
        self.config[self.env]["ROOT_DIR"] = path.parent
        return self.config[self.env]

    @staticmethod
    def read_env_variables(variable):
        return os.environ.get(variable)