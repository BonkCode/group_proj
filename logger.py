class BonkLogger:
    __instance = None

    def __init__(self, path: str):
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
