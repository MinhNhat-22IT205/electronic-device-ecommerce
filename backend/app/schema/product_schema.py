
from pydantic import BaseModel
from typing import List, Optional

class ImageColor(BaseModel):
    id:int
    name:str

    class Config:
        orm_mode = True    

class ProductImageResponse(BaseModel):
    path: str
    color:ImageColor

    class Config:
        orm_mode = True


class ProductResponse(BaseModel):
    id: int
    name: str
    sku: str
    description: Optional[str]
    camera: Optional[str]
    cpu: Optional[str]
    ram: Optional[int]
    rom: Optional[int]
    pin: Optional[int]
    cost_price: Optional[float]
    sale_price: float
    quantity: int
    weight: Optional[float]
    width: Optional[float]
    height: Optional[float]
    thick: Optional[float]
    is_activated: bool
    is_deleted: Optional[bool]
    images: List[ProductImageResponse]

    class Config:
        orm_mode = True
