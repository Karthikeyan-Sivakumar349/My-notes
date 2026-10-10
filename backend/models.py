from sqlalchemy import Column, Integer, String, Text
from database import Base


class File(Base):
    __tablename__ = "files"

    id = Column(Integer, primary_key=True, index=True)
    file_name = Column(String, unique=True, nullable=False)
    content = Column(Text, nullable=False)