from pydantic import BaseModel, Field

class TopicCreate(BaseModel):
    name: str
    
class TopicRead(BaseModel):
    id: int
    content: str
    
    class Config:
        orm_mode = True
