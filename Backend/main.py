from fastapi import FastAPI , HTTPException , status
from typing import List
from Backend.database import MEDICINES_DB
from Backend.schemas import MedicienCreate , MedicienResponse

app= FastAPI()

@app.get("/medicines",response_model=list[MedicienResponse])
def get_all_mediciens():
    return list(MEDICINES_DB.values())

@app.get("/medicines/{medicine_id}",response_model=MedicienResponse)
def get_medicine_by_id(medicine_id:int):
    if  medicine_id not  in MEDICINES_DB:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f" Medicine with id {medicine_id} was not found in our records"
        )
    return MEDICINES_DB[medicine_id]

@app.post("/medicines",response_model=MedicienResponse, status_code=status.HTTP_201_CREATED)
def create_medicien(payload: MedicienCreate):
    new_id=max(MEDICINES_DB.keys(), default=0) + 1
    new_medicien={
        "id": new_id,
        "name": payload.name,
        "price": payload.price,
        "in_stock": True
    }
    
    MEDICINES_DB[new_id] = new_medicien
    return new_medicien

@app.put ("/medicines/{medicien_id}",response_model=MedicienResponse)
def update_medicien(medicien_id: int, update_data:MedicienCreate):
    if medicien_id not in MEDICINES_DB:
        raise HTTPException(status_code=404 , detail="Medicien not Found")
    
    update_record={
        "id":medicien_id,
        "name": update_data.name,
        "price": update_data.price,
        "in_stock": MEDICINES_DB[medicien_id]["in_stock"]
    }
    
    MEDICINES_DB[medicien_id]= update_record
    return update_record


@app.delete("/medicines/{medicien_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_medicien(medicien_id: int):
    if medicien_id not in MEDICINES_DB:
        raise HTTPException(status_code=404 , detail="Medicien not Found")
    
    del MEDICINES_DB[medicien_id]
    return None