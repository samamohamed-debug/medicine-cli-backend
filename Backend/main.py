from fastapi import FastAPI , HTTPException , status
from typing import List
from database import get_db
from schemas import MedicienCreate , MedicienResponse

app= FastAPI()

@app.get("/medicines",response_model=list[MedicienResponse])
def get_all_mediciens():
    return list(get_db.values())

@app.get("/medicines/{medicine_id}",response_model=MedicienResponse)
def get_medicine_by_id(medicine_id:int):
    if  medicine_id not  in get_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f" Medicine with id {medicine_id} was not found in our records"
        )
    return get_db[medicine_id]

@app.post("/medicines",response_model=MedicienResponse, status_code=status.HTTP_201_CREATED)
def create_medicien(payload: MedicienCreate):
    new_id=max(get_db.keys(), default=0) + 1
    new_medicien={
        "id": new_id,
        "name": payload.name,
        "price": payload.price,
        "in_stock": True
    }
    
    get_db[new_id] = new_medicien
    return new_medicien

@app.put ("/medicines/{medicien_id}",response_model=MedicienResponse)
def update_medicien(medicien_id: int, update_data:MedicienCreate):
    if medicien_id not in get_db:
        raise HTTPException(status_code=404 , detail="Medicien not Found")
    
    update_record={
        "id":medicien_id,
        "name": update_data.name,
        "price": update_data.price,
        "in_stock": get_db[medicien_id]
    }
    
    get_db[medicien_id]= update_record
    return update_record


@app.delete("/medicines/{medicien_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_medicien(medicien_id: int):
    if medicien_id not in get_db:
        raise HTTPException(status_code=404 , detail="Medicien not Found")
    
    del get_db[medicien_id]
    return None
