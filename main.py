from config.configreader import ConfigReader
from config.settings import Settings


def start():
    settings = Settings(ConfigReader.read())
    print(settings.connectionString)


if __name__ == '__main__':
    start()
