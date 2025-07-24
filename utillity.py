from configparser import ConfigParser
env = 'dev'

def read_config():
    config_file = './conf.ini'
    config = ConfigParser()
    config.read(config_file)
    return config[env]

def get_db_file():
    return read_config()['db_file']

if __name__ == '__main__':
    print(get_db_file())
