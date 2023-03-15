from sqlalchemy.orm import Session

from db import models
from db import schemas


def create_user(db: Session, user: schemas.UserCreate):
    """
    Userを作成する

    Parameters
    ----------
    db : Session
        データベースとの接続を行うための情報
    user : schemas.UserCreate
        ユーザ名とパスワードを含んだデータ

    Returns
    -------
    db_user : models.User
        Userモデル
    """
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def read_users(db: Session, offset: int = 0, limit: int = 100):
    """
    複数のUserを取得する

    Parameters
    ----------
    db : Session
        データベースとの接続を行うための情報
    offset : int, default 0
        取得するユーザIDの始点
    limit : int, default 100
        取得するユーザIDの数

    Returns
    -------
    users : list of models.User
        {offset}番目から{limit}個分のUserモデルのリスト
    """
    users = db.query(models.User).offset(offset).limit(limit).all()
    return users


def read_user_by_id(db: Session, user_id: int):
    """
    指定したidのUserを取得する

    Parameters
    ----------
    db : Session
        データベースとの接続を行うための情報
    id : int
        ユーザID

    Returns
    -------
    user : models.User
        ユーザIDが一致するUserモデル
    """
    user = db.query(models.User).filter(models.User.id == user_id).first()
    return user


def read_user_by_name(db: Session, user_name: str):
    """
    指定したnameのUserを取得する

    Parameters
    ----------
    db : Session
        データベースとの接続を行うための情報
    name : str
        ユーザ名

    Returns
    -------
    user : models.User
        ユーザ名が一致するUserモデル
    """
    return db.query(models.User).filter(models.User.name == user_name).first()
