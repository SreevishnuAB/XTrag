from typing import List
from pydantic import BaseModel, Field
from pydantic.types import UUID4

class Tags(BaseModel):
  id: UUID4 = Field(..., title="Item ID")
  tags: List[str] = Field(..., title="List of extracted tags")