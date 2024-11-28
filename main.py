from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
import schemas
from app.database import SessionLocal

app = FastAPI()


def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root() -> dict:
    return {"message": "Hello in my city!!!"}


@app.post("/cities", response_model=schemas.City)
def create_city(city: schemas.CityCreate, db: Session = Depends(get_db)):
    return crud.create_city(db=db, city=city)


@app.get("/cities", response_model=list[schemas.City])
async def get_cities(db: Session = Depends(get_db)):
    return crud.get_cities(db)


@app.get("/cities/{city_id}", response_model=schemas.City)
async def get_city(city_id: int, db: Session = Depends(get_db)):
    city = crud.get_city_by_id(db=db, city_id=city_id)
    if city is None:
        raise HTTPException(status_code=404, detail="City not found")
    return city


@app.put("/cities/{city_id}", response_model=schemas.City)
def update_city(city_id: int, city: schemas.CityCreate, db: Session = Depends(get_db)):
    db_city = crud.update_city(db=db, city_id=city_id, city=city)
    if db_city is None:
        raise HTTPException(status_code=404, detail="City not found")
    return db_city


@app.delete("/cities/{city_id}", response_model=schemas.City)
def delete_city(city_id: int, db: Session = Depends(get_db)):
    db_city = crud.delete_city(db=db, city_id=city_id)
    if db_city is None:
        raise HTTPException(status_code=404, detail="City not found")
    return db_city
