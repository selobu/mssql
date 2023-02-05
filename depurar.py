from reflect import read_users
from config import Config as Tb
from config import Tb, Config as conf
from sqlalchemy import select
from sqlalchemy.orm import Session
from pprint import pprint
import re
engine = conf.engine

with Session(engine) as session:
    results = session.query(Tb.User)
    newres = []
    for row in results.all():
        curr_name = row
        # deleting spaces at the beggining, at the end and double spaces 
        temp_name = re.sub('[0-9]*','',curr_name.name)
        curr_name.name = re.sub('\s+',' ',temp_name.strip())
        newres.append( curr_name)
    session.add_all(newres)
    session.commit()
a=1
