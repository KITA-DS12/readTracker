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
    user_id : int
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
    user = db.query(models.User).filter(models.User.name == user_name).first()
    return user


def create_user_note(db: Session, note: schemas.NoteCreate, user_id: int):
    """
    Noteを作成する

    Parameters
    ----------
    db : Session
        データベースとの接続を行うための情報
    note : schemas.NoteCreate
        ノートのタイトルと本文を含んだデータ
    user_id : int
        ノートを所有するユーザのID

    Returns
    -------
    db_note : models.Note
        Noteモデル
    """
    db_note = models.Note(**note.dict(), owner_id=user_id)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note


def read_user_notes(db: Session,
                    user_id: int,
                    offset: int = 0,
                    limit: int = 100):
    """
    複数のUserを取得する

    Parameters
    ----------
    db : Session
        データベースとの接続を行うための情報
    user_id : int
        ノートを所有するユーザのID
    offset : int, default 0
        取得するユーザIDの始点
    limit : int, default 100
        取得するユーザIDの数

    Returns
    -------
    notes : list of models.Note
        {offset}番目から{limit}個分のNoteモデルのリスト
    """
    notes = db.query(models.Note).filter(models.Note.owner_id ==
                                         user_id).offset(offset).limit(limit).all()
    return notes


def read_note_by_id(db: Session, note_id: int):
    """
    指定したidのNoteを取得する

    Parameters
    ----------
    db : Session
        データベースとの接続を行うための情報
    note_id : int
        ノートのID

    Returns
    -------
    note : models.Note
        Note IDが一致するNoteモデル
    """
    note = db.query(models.Note).filter(models.Note.id == note_id).first()
    return note


def update_note(db: Session, note: schemas.Note):
    """
    指定したidのNoteを取得する

    Parameters
    ----------
    db : Session
        データベースとの接続を行うための情報
    note : schemas.Note
        Noteモデル

    Returns
    -------
    db_note : models.Note
        変更後のNoteモデル
    """
    db_note = db.query(models.Note).filter(models.Note.id == note.id).first()
    db_note.title = note.title
    db_note.content = note.content
    db.commit()
    return db_note


def delete_note_by_id(db: Session, note_id: int):
    """
    指定したidのNoteを取得する

    Parameters
    ----------
    db : Session
        データベースとの接続を行うための情報
    note_id : int
        ノートのID

    Returns
    -------
    note_id : int
        削除したNote ID
    """
    db.query(models.Note).filter(models.Note.id == note_id).delete()
    db.commit()
    return note_id
