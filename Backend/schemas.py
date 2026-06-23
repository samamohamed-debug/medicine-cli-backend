from pydantic import BaseModel , Field

class MedicienBase(BaseModel):
    name: str = Field(min_length=3 , max_length=100)
    price: float=Field(ge=5 , le=300)
    
class MedicienCreate(MedicienBase):
    pass
    
class MedicienResponse(MedicienBase):
    id: int
    in_stock: bool
    