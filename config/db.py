import os
from os.path import join, dirname

import databases
from dotenv import load_dotenv

from utils.logger import get_logger

_dotenv_path = join(dirname(dirname(__file__)), '.env')
load_dotenv(_dotenv_path)

LOGGER = get_logger(__name__)

class DB:
  __instance = None
  def __init__(self) -> None:

    if DB.__instance == None:
      LOGGER.info("Creating Database instance")
      self.database = databases.Database(os.environ.get("DB_URL"))
      DB.__instance = self
    else:
        LOGGER.error("Explcit call to Database constructor")
        raise Exception("Singleton class. Use get_instance method")

  @staticmethod
  def get_instance():
    LOGGER.info("Getting Database instance")
    if DB.__instance == None:
      DB()
    return DB.__instance
  
