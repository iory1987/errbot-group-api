from fastapi import APIRouter, HTTPException, Depends
from typing import List, Optional
from schemas.GroupSchema import GroupSchema

GroupRoute = APIRouter(
    prefix="/v1/groups",
    tags=["group"],
)

@GroupRoute.get("/", response_model=List[GroupSchema])
def index():
    # Simulate fetching groups from a database
    return [{"id": 1}, {"id": 2}]

@GroupRoute.get("/{group_id}", response_model=GroupSchema)
def read_group(group_id: int):
    # Simulate fetching a group from a database by their ID
    return {"id": group_id}

@GroupRoute.post("/", response_model=GroupSchema)
def create_group(group: GroupSchema):
    # Simulate creating a group in a database
    return group

@GroupRoute.put("/{group_id}", response_model=GroupSchema)
def update_group(group_id: int, group: GroupSchema):
    # Simulate updating a group in a database by their ID
    return group

@GroupRoute.delete("/{group_id}")
def delete_group(group_id: int):
    # Simulate deleting a group from a database by their ID
    return {"detail": "Group deleted"}
