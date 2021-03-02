from fastapi import APIRouter
import yake
from sqlalchemy.sql import select

from config.db import DB
from utils.logger import get_logger
from model.request.item import Item
from model.db.tag import tag

router = APIRouter()

LOGGER = get_logger(__name__)

@router.post("/")
async def create_tag(item: Item):
  db = DB.get_instance().database
  text = item.text
  kw_extractor = yake.KeywordExtractor(n=1, top=2)
  keywords = kw_extractor.extract_keywords(text)
  LOGGER.error(keywords)
  top_tags = [{"id": item.id, "tag": _keyword[0]} for _keyword in keywords]
  query = tag.insert()
  await db.execute_many(query=query, values=top_tags)
  LOGGER.error(top_tags)
  return item

@router.get("/{id}")
async def get_tags(id):
  db = DB.get_instance().database
  query = select([tag]).where(tag.c.id == id)
  result = await db.fetch_all(query)
  LOGGER.error(result)
  return result
