from db.connection import Base, engine
from db.models import EmailStore

Base.metadata.create_all(bind=engine)