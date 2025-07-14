from sqlalchemy import Column, ForeignKey, Table

from models.BaseModel import EntityMeta

group_user_association = Table(
    "group_user_association",
    EntityMeta.metadata,
    Column("group_id", ForeignKey("groups.id")),
    Column("user_id", ForeignKey("users.id")),
)