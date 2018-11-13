from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String(16))


engine = create_engine("mysql+mysqldb://root:root@127.0.0.1:3307/csv_data")
session = sessionmaker()
session.configure(bind=engine)
#Base.metadata.create_all(engine)
s = session()
p = Person(name="Mijja")
s.add(p)

q = s.query(Person).filter(Person.name == 'Mijja').one()

print(q.id,q.name)
