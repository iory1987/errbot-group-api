import datetime
from sqlalchemy.orm import relationship
from models.BaseModel import EntityMeta
from sqlalchemy import Column, Integer, String, PrimaryKeyConstraint, DateTime, Boolean
from models.GroupUserAssociation import (
    group_user_association,
)


class User(EntityMeta):
    __tablename__ = "users"
    id = Column(Integer)
    name = Column(String9=(100), nullable=False)
    groups = relationship("Group", lazy="dynamic", secondary=group_user_association)
    email = Column(String, unique=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    is_active = Column(Boolean, default=True)

    PrimaryKeyConstraint("id")

    def normalize(self):
        return {
            "id": self.id.__str__(),
            "name": self.name.__str__(),
        }
