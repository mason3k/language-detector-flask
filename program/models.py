from datetime import datetime

from flask_security.models import fsqla_v3 as fsqla
from sqlalchemy import BOOLEAN, DateTime, Float, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from . import db

fsqla.FsModels.set_db_info(db)


class Role(db.Model, fsqla.FsRoleMixin):
    ...


class User(db.Model, fsqla.FsUserMixin):
    ...

    def __repr__(self) -> str:
        return f"{self.email=}, {self.id=}"


class Entry(db.Model):
    __tablename__ = "entry"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement="auto")
    author_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    created: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    text: Mapped[str] = mapped_column(String(), nullable=False)
    language: Mapped[str] = mapped_column(String(), nullable=False)
    certainty: Mapped[float] = mapped_column(Float(precision=5), nullable=False)
    offline: Mapped[bool] = mapped_column(BOOLEAN, nullable=False)

    def __repr__(self) -> str:
        return f"{self.id=}, {self.text=}"
