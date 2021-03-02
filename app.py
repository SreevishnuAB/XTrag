import databases
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from config.db import DB
from routes import health
from routes.v1 import tag


app = FastAPI(
  title="Xtrag",
  version="0.1"
)

origins = [
    "http://localhost:5000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

database = DB.get_instance().database

@app.on_event("startup")
async def startup():
  await database.connect()
  create_query = """CREATE TABLE IF NOT EXISTS xtrag_tag(id uuid NOT NULL, tag VARCHAR NOT NULL, PRIMARY KEY (id, tag))"""
  await database.execute(create_query)


@app.on_event("shutdown")
async def shutdown():
  await database.disconnect()


app.include_router(
  health.router,
  tags=["health"],
  responses={
    200: {"details": "OK"},
    500: {"error": "Internal server error"}
  }
)

app.include_router(
  tag.router,
  prefix="/api/v1/tag",
  tags=["tag"],
  responses={
    201: {"details": "Tags created"},
    400: {"error": "ID and description cannot be empty"},
    500: {"error": "Internal server error"}
  }
)