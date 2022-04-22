from sqlalchemy.engine.url import URL
from yaml import load, FullLoader
from base64 import b64decode

class DB_Config :
    
    def __init__ (self) :
        with open('./tweet_api/app/db-config.yml') as f :
            db_config = load(f, Loader=FullLoader)['database']

        self.__db_drivername = db_config['drivername']
        self.__db_host = self.decode(db_config['host'])
        self.__db_port = db_config['port']
        self.__db_database = db_config['database']
        self.__db_username = db_config['username']
        self.__db_password = self.decode(db_config['password'])
    
    def decode (self, encryted_text) :
        bytes_text = b64decode(encryted_text)
        return bytes_text.decode('ascii')
        
    def get_url (self) :
        return URL.create(
            drivername = self.__db_drivername,
            host = self.__db_host,
            port = self.__db_port,
            database = self.__db_database,
            username = self.__db_username,
            password = self.__db_password
        )

db_confing = DB_Config()