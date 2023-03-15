from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from db.database import Base


class User(Base):
    """
    Userテーブルの定義

    Attributes
    ----------
    id : Column(Integer)
        ユーザID
    name : Column(String)
        ユーザ名
    password : Column(String)
        パスワード
    created_at : Column(DateTime)
        作成日
    """

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    password = Column(String)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)

    notes = relationship("Note", back_populates="owner")


class Note(Base):
    """
    Noteテーブルの定義

    Attributes
    ----------
    id : Column(Integer)
        ノートのID
    title : Column(String)
        ノートのタイトル
    content : Column(String)
        ノートの本文
    created_at : Column(DateTime)
        作成日
    """

    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    content = Column(String)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="notes")
