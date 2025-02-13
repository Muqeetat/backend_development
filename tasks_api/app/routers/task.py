from fastapi import FastAPI, HTTPException, Response, status, Depends, APIRouter,Query
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import models, schemas,oauth2
from ..database import get_db


router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@router.get("/" ,response_model=List[schemas.TaskResponse])
def get_tasks(db: Session = Depends(get_db),current_user: dict = Depends(oauth2.get_current_user),
    limit: int = Query(10, le=100),skip: int = Query(0, ge=0),search: Optional[str] = ""):

    tasks= db.query(models.Task).filter(
        models.Task.owner_id == current_user.id,
        models.Task.title.contains(search)).limit(limit).offset(skip).all()
    return tasks


@router.get("/{id}",response_model=schemas.TaskResponse)
def get_task_by_id(id: int, db: Session = Depends(get_db),current_user: dict = Depends(oauth2.get_current_user)):

    task = db.query(models.Task).filter(models.Task.id == id).first()  
    if not task:
        raise HTTPException(status_code=404, detail=f"Task with id {id} not found")     # If task not found, raise a 404 error
    
    if task.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail=f"Not authorized to perform action")
    return task

@router.get("/category/{category}", response_model=List[schemas.TaskResponse])  # Fetching tasks by category
def get_tasks_by_category(category: str, db: Session = Depends(get_db), current_user: dict = Depends(oauth2.get_current_user),
    limit: int = Query(10, le=100),skip: int = Query(0, ge=0)):
    
    tasks = db.query(models.Task).filter(
        models.Task.owner_id == current_user.id,
        models.Task.category == category
        ).limit(limit).offset(skip).all()     # Query the Task table to get all tasks by category

    if not tasks:
        raise HTTPException(status_code=404, detail=f"No tasks found in category '{category}'")
    return tasks  # Return the list of tasks


@router.get("/user/{username}", response_model=List[schemas.TaskResponse])  # Fetching tasks by username
def get_tasks_by_username(username: str, db: Session = Depends(get_db),current_user: dict = Depends(oauth2.get_current_user),
    limit: int = Query(10, le=100),skip: int = Query(0, ge=0)):
    user = db.query(models.User).filter(models.User.name == username).first()     # Query the User table to get the user by their username
    if not user:
        raise HTTPException(status_code=404, detail=f"User with username '{username}' not found")
    tasks = db.query(models.Task).filter(models.Task.owner_id == user.id).limit(limit).offset(skip).all()    # Query the Task table to get all tasks associated with the user by their user_id

    if not tasks:
        raise HTTPException(status_code=404, detail=f"No tasks found for user '{username}'") 
    return tasks  # Return the list of tasks


@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.TaskResponse)
def create_task(task: schemas.Task,db: Session = Depends(get_db),current_user: dict = Depends(oauth2.get_current_user)):
    print(current_user)
    new_task = models.Task(owner_id=current_user.id,**task.dict())
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


@router.put("/{id}", response_model=schemas.TaskResponse2)
def update_task(id: int, updated_task: schemas.TaskUpdate,db: Session = Depends(get_db),current_user: dict = Depends(oauth2.get_current_user)):
    task = db.query(models.Task).filter(models.Task.id == id).first()
    if task == None:
        raise HTTPException(status_code=404, detail=f"Task with id {id} not found")

    if task.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail=f"Not authorized to perform action")

    update_data  = updated_task.dict(exclude_unset=True)  # Only update provided fields
    for key, value in update_data.items():
        setattr(task, key, value)  

    db.commit()
    db.refresh(task)
    return task


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(id: int, db: Session = Depends(get_db),current_user: dict = Depends(oauth2.get_current_user)):

    task_query = db.query(models.Task).filter(models.Task.id == id)
    task = task_query.first()
    if task == None:
        raise HTTPException(status_code=404, detail=f"Task with id {id} not found")

    if task.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail=f"Not authorized to perform action")
    
    task_query.delete(synchronize_session=False)
    db.commit()
    return {"message": "Task deleted"}