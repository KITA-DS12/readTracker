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
    name: str = Field(..., title="User Name")


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

    Attributes ----------
    id : int, default 0
        ユーザID
    created_at : datetime, default datetime.now()
        作成日
    """
    id: int = Field(0, title="User ID")
    created_at: datetime = Field(datetime.now(), title="Creation Date")

    class Config:
        orm_mode = True


class NoteBase(BaseModel):
    """
    Noteスキーマのうち、読み取り・作成時に共通している属性を保持

    Attributes
    ----------
    title : str
        ノートのタイトル
    content : str | None, default None
        ノートの本文
    """
    title: str = Field("", title="Note Title")
    content: str | None = Field(None, title="Note Content")


class NoteCreate(NoteBase):
    """
    Noteスキーマのうち、作成時に必要な属性を保持

    Attributes
    ----------
    """
    pass


class Note(NoteBase):
    """
    Noteスキーマのうち、読み取り時に必要な属性を保持

    Attributes
    ----------
    id : int, default 0
        タイトルのID
    created_at : datetime, default datetime.now()
        作成日
    owner_id : int, default 0
        ユーザID
    """
    id: int = Field(0, title="Note ID")
    created_at: datetime = Field(datetime.now(), title="Creation Date")
    owner_id: int = Field(0, title="User ID")

    class Config:
        orm_mode = True
