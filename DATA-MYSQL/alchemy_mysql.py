# >uv add sqlalchemy
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine, Column, Integer, String

#1. Luodaan yhteys tietokantaan
#sqlite
#engine = create_engine("sqlite://movies.db", echo = True)

#mysql.connector        // create connection from 'connection string'
engine = create_engine("mysql+mysqlconnector://joulupukki:joulu!@localhost/harjoitus", echo = True)

#2. Määritetään 'model':it /"mallit"
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key = True)
    name = Column(String(50))
    email = Column(String(100))

#Luodaan luodoista malleista talulu(t):
Base.metadata.create_all(engine)

#3. Luodaan sessio, yhdistetään sessio luotuun engineen ja luodaan sql-query:ssa
Session = sessionmaker(bind=engine)
session = Session()

#Luodaan uusi käyttäjaä User():
new_user = User(name="joulupukki", email="pukki@korvatunturi.lol")
session.add(new_user)
session.commit()

#tulostetaan luodut userit
for user in session.query(User).all():
    print(user.id, user.name, user.email)
