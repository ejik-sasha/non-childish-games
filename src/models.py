from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from database import Base
from typing import Optional, Annotated
import enum


intpk = Annotated[int, mapped_column(primary_key=True)]

class UsersOrm(Base):
    __tablename__ = "users"
    id: Mapped[intpk]
    username: Mapped[str] = mapped_column(String(50))
    email: Mapped[Optional[str]] = mapped_column(String(100))

class CharacterClass(enum.Enum):
    A = "A"
    B = "B"
    C = "C"

class CharactersOrm(Base):
    __tablename__ = "characters"
    id: Mapped[intpk]
    username: Mapped[str] = mapped_column(String(50))
    characterClass: Mapped[CharacterClass]
    characterId: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    skill: Mapped[int] = mapped_column(Integer, server_default="0")


metadata_obj = MetaData()