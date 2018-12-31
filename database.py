import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
Base = automap_base()
engine = create_engine('mysql://root@localhost/regDB')

# reflect the tables
Base.prepare(engine, reflect=True)

students = Base.classes.students

session = Session(engine)



