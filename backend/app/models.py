from sqalchemy import Column, Integer, String, Text
from .database import Base


class Topic(Base):
    __tablename__ = "topics"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, index=True)
    content = Column(Text, nullable=False)

    def __repr__(self):
        return f"<Topic(name={self.name}, content={self.content[:50]}...)>"