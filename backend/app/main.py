from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.exc import IntegrityError

from app.database import engine, SessionLocal, Base
from app.models import Topic
from app.schemas import TopicCreate, TopicRead
from app.scraper import scrape_wikipedia

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        # Permitir todas las orígenes
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/topics/", response_model=TopicRead)
def create_topic(topic: TopicCreate):
    db = SessionLocal()

    existing = db.query(Topic).filter(Topic.name == topic.name).first()
    if existing:
        db.close()
        return existing

    content = scrape_wikipedia(topic.name)
    if not content:
        db.close()
        raise HTTPException(status_code=404, detail="Topic not found on Wikipedia")

    db_topic = Topic(name=topic.name, content=content)
    db.add(db_topic)
    try:
        db.commit()
        db.refresh(db_topic)
    except IntegrityError:
        db.rollback()
        db_topic = db.query(Topic).filter(Topic.name == topic.name).first()
    finally:
        db.close()

    return db_topic


@app.get("/topics/{topic_id}", response_model=TopicRead)
def get_topic(topic_id: int):
    db = SessionLocal()
    topic = db.query(Topic).get(topic_id)
    db.close()
    if not topic:
        raise HTTPException(status_code=404, detail="Topic not found")
    return topic


@app.get("/")
def get_hola():
    return "Hola, mundo!"
