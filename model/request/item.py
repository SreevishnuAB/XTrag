from pydantic import BaseModel, Field
from pydantic.types import UUID4

class Item(BaseModel):
  id: UUID4 = Field(..., title="Item ID")
  text: str = Field(..., title="Source text for tag extraction")
