from datetime import datetime

from pydantic import BaseModel, Field


class UserBase(BaseModel):
    """
    Userスキーマのうち、読み取り・作成時に共通している属性を保持

    Attributes
    ----------
    name : str
        ユーザ名
    """
    name: str = Field(..., title="User ID")


class UserCreate(UserBase):
    """
    Userスキーマのうち、作成時に必要な属性を保持

    Attributes
    ----------
    password : str
        パスワード
    """
    password: str = Field(..., title="Password")


class User(UserBase):
    """
    Userスキーマのうち、読み取り時に必要な属性を保持

    Attributes
    ----------
    id : int, default 0
        ユーザID
    created_at : datetime, default datetime.now()
        作成日
    """
    id: int = Field(0, title="ID")
    created_at: datetime = Field(datetime.now(), title="Creation Date")

    class Config:
        orm_mode = True
