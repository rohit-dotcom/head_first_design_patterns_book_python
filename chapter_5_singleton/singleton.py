class ExistingConnectionError(Exception):
    pass

class db_connection():
    __conn=None
    _allow_creation=False

    def __new__(cls,*args,**kwargs):
        if not cls._allow_creation:
            raise RuntimeError("Direct instantionion forbidden: Please db_connection.get_instance()")
        return super().__new__(cls)

    def  __init__(self): 
        if getattr(self,'_initialized',False):
            pass
        self._initialized=True

    @classmethod
    def get_instance(cls):
        if cls.__conn==None:
            cls._allow_creation=True
            try:
                cls.__conn=cls()
            finally:
                cls._allow_creation=False

        return cls.__conn


    def get_connection(self):
        return 'this is db connection'
