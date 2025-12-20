# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, declarative_base

# from sqlalchemy.orm import Session
# from fastapi import Depends

# DB_USER = "postgres"
# DB_PASSWORD = "123"
# DB_HOST = "localhost"
# DB_PORT = "5432"
# DB_NAME = "postgres"

# DATABASE_URL = (
#     f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}"
#     f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
# )

# engine = create_engine(DATABASE_URL)

# SessionLocal = sessionmaker(
#     autocommit=False,
#     autoflush=False,
#     bind=engine
# )

# Base = declarative_base()

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

# --------------------
# DATABASE CONFIG
# --------------------
DB_USER = "postgres"
DB_PASSWORD = "123"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "postgres"

DATABASE_URL = (
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

# --------------------
# MODEL
# --------------------
class User(Base):
    __tablename__ = "user_info"

    id = Column(Integer, primary_key=True, index=True)  # SERIAL in DB
    name = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)

# Create table if not exists
#Base.metadata.create_all(bind=engine)
