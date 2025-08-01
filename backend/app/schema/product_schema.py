class ProductImageResponse(BaseModel):
    path: str
    color_name: Optional[str]
    class Config:
        orm_mode = True

class ProductResponse(BaseModel):
    id: int
    name: str
    sku: str
    cost_price: float
    sale_price: float
    quantity: int
    is_active: bool
    images: List[ProductImageResponse]
    class Config:
        orm_mode = True
