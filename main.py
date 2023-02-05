
from config import Config as conf
from sqlalchemy import create_engine

SQLALCHEMY_DATABASE_URI = conf.SQLALCHEMY_DATABASE_URI

engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True) # pool_recycle = 3600,
setattr(conf, 'engine', engine)




DECLARATIVE = True
if DECLARATIVE:
    from model import Base
    metadata = Base.metadata
    print('//---------------------------//')
    print('// CREATING TABLES //')
    metadata.create_all(engine)
    # setting engine to config

    import routes
    print('//---------------------------//')
    print('// CREATING USERS //')
    routes.create_users()

    print('//---------------------------//')
    print('// READING USERS ONE BY ONE //')
    #routes.read_users_one_by_one()

    print('//---------------------------//')
    print('// READING USERS ALL AT TIME //')
    #routes.read_users_all()

    print('//---------------------------//')
    print('// SELECT WITH JOIN //')
    # routes.select_join()
    import pruebazenith
    pruebazenith.select_join()
    print('//----------3---------------//')
    pruebazenith._3_select_personas()
    print('//----------4---------------//')
    pruebazenith._4_select_all_fields()
    print('//----------5---------------//')
    pruebazenith._5_filter_starting_by_a()
    print('//----------6---------------//')
    pruebazenith._6_changing_last_name()
    
else:
    # working with the database as unknown structure
    import  reflect
    print('//-----------------------------//')
    print('// READING USERS FROM REFLECT //')
    #reflect.read_users()
    
    print('//-----------------------------//')
    print('// CREATIN USERS//')
    #reflect.create_users()
    
    print('//-----------------------------//')
    print('// readign last 3 users//')
    #reflect.reading_last_3_users()
    
    print('//-----------------------------//')
    print('// reading all users //')
    # reflect.reading_all_users_join_email_address()
    a = 1
if DECLARATIVE:
    # verificando las relaciones
    from relationtypes import relationtypes
    #// ------------
    print('//-----------------------------//')
    print('// RELATIONSHIPS MANY TO MANY Test //')
    relationtypes.many2many()
    metadata = Base.metadata
    metadata.create_all(engine)
import depurar