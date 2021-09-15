from sqlalchemy import Boolean, Column, Integer, String


from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(Integer)
    email = Column(String)
    password = Column(String)



    
    


