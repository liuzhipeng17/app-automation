import logging
import os


CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
ROOT_PATH = os.path.join(CURRENT_PATH, os.pardir)
LOG_PATH = os.path.join(ROOT_PATH, 'log')


class Log(logging.Logger):
    def __init__(self, name, level=logging.DEBUG, file=False, stream=True):
        self.name = name
        self.level = level
        logging.Logger.__init__(self, self.name, level=level)
        self.setLevel(level)
        if file:
            if not os.path.exists(LOG_PATH):
                os.mkdir(LOG_PATH)
            self.addHandler(logging.FileHandler(os.path.join(LOG_PATH, '%s.log'% self.name)))
            
        if stream:
            self.addHandler(logging.StreamHandler())
            
        for handler in self.handlers:
            formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
            handler.setFormatter(formatter)
        
        

        
if __name__ == '__main__':
    mylog = Log('Macaca', file=True)
    mylog.info('ddd')
    mylog.debug('hh')
