from tinydb import TinyDB, Query

from tinydb.storages import JSONStorage
from tinydb.middlewares import CachingMiddleware

class Database:
    serversdb = None
      
    def __init__(self):
        self.serversdb = TinyDB('/usr/local/mcupdate/db/servers.json', storage=CachingMiddleware(JSONStorage))

    def insertServer(self, srvtype, updatewait):
      self.serversdb.insert({'name': 1, 'char': 'a'})
   