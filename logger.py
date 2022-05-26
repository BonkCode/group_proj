class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class BonkLogger(metaclass=Singleton):
    __instance = None

    def __init__(self, path: str):
        if path.split('.')[-1] != 'log':
            self.path = 'default.log'
            self.error(f'Wrong file extension: .log expected. filename provided:{path}')
        else:
            self.path = path

    @classmethod
    def get_instance(cls, path='default.log'):
        if not cls.__instance:
            cls.__instance = BonkLogger(path)
        return cls.__instance

    def info(self, message: str):
        with open(self.path, 'a') as log_file:
            log_file.write(f'INFO: {message}\n')

    def error(self, message: str):
        with open(self.path, 'a') as log_file:
            log_file.write(f'ERROR: {message}\n')
