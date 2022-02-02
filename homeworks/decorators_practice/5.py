from datetime import datetime


# HW
class Logger:

    def __init__(self, func_decorate, logfile='out.log'):
        self.logfile = logfile
        self.func_decorate = func_decorate

    def __call__(self):
        log = f'{self.func_decorate.__name__} with was executed at {datetime.now()}\n'
        print(log)
        with open(self.logfile, 'a') as file:
            file.write(log)


@Logger
def my_func():
    """
    This is my func
    """
    print(f"{my_func().__name__} is running")


my_func()
