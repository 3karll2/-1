from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String

# Створюємо Base тут, щоб не залежати від інших файлів
class Base(DeclarativeBase):
    pass

# Приклад вашої моделі (замініть на свої поля)
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)