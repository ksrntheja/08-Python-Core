from abc import *


class DBInterface(ABC):
    @abstractmethod
    def connect(self): pass

    @abstractmethod
    def disconnect(self): pass


class Oracle(DBInterface):
    def connect(self):
        print('Connecting to Oracle Database...')

    def disconnect(self):
        print('Disconnecting to Oracle Database...')


class Sybase(DBInterface):
    def connect(self):
        print('Connecting to Sybase Database...')

    def disconnect(self):
        print('Disconnecting to Sybase Database...')


dbname = input('Enter Database Name:')
classname = globals()[dbname]
x = classname()
x.connect()
x.disconnect()

# Enter Database Name:Oracle
# Connecting to Oracle Database...
# Disconnecting to Oracle Database...

# Enter Database Name:Sybase
# Connecting to Sybase Database...
# Disconnecting to Sybase Database...
