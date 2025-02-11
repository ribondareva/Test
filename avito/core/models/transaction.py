from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from .base import Base


class Transaction(Base):
    id = Column(Integer, primary_key=True, index=True)
    from_user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    to_user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    amount = Column(Integer)

    from_user = relationship(
        "User", foreign_keys=[from_user_id], backref="outgoing_transactions"
    )
    to_user = relationship(
        "User", foreign_keys=[to_user_id], backref="incoming_transactions"
    )
