from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from setup.config import Config

engine = create_engine(
    url="mysql://{0}:{1}@{2}:{3}/{4}".format(
        Config.DB_USER,
        Config.DB_PASS,
        Config.DB_HOST,
        Config.DB_PORT,
        Config.DB_NAME
    )
)

Base = declarative_base()
Session = sessionmaker()