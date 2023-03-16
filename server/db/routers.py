from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from db import crud
from db import schemas
from db.database import get_db

router = APIRouter()


@router.get("/users", response_model=list[schemas.User], tags=['user'])
def read_users(offset: int = 0,
               limit: int = 100,
               db: Session = Depends(get_db)):
    """
    複数のUserを取得する

    Parameters
    ----------
    offset : int, default 0
        取得するユーザIDの始点
    limit : int, default 100
        取得するユーザIDの数
    db : Session
        データベースとの接続を行うための情報

    Returns
    -------
    users : list of models.User
        {offset}番目から{limit}個分のUserモデルのリスト
    """

    users = crud.read_users(db=db, offset=offset, limit=limit)
    return users


@router.get("/user/{user_id}", response_model=schemas.User, tags=['user'])
def read_user_by_id(user_id: int, db: Session = Depends(get_db)):
    """
    指定したidのUserを取得する

    Parameters
    ----------
    user_id : int
        ユーザID
    db : Session
        データベースとの接続を行うための情報

    Returns
    -------
    user : models.User
        ユーザIDが一致するUserモデル
    """

    user = crud.read_user_by_id(db=db, user_id=user_id)
    return user


@router.post("/user/signup", response_model=schemas.User, tags=['user'])
def signup(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """
    Userを作成する

    Parameters
    ----------
    user : schemas.UserCreate
        ユーザ名とパスワードを含んだデータ
    db : Session
        データベースとの接続を行うための情報

    Returns
    -------
    new_user : models.User
        Userモデル
    """

    db_user = crud.read_user_by_name(db=db, user_name=user.name)
    # 既にユーザ名が存在する場合は400エラーを返す
    if db_user:
        raise HTTPException(
            status_code=400, detail="Username already registered")

    new_user = crud.create_user(db=db, user=user)
    return new_user


@router.post("/user/signin", response_model=schemas.User, tags=['user'])
def signin(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """
    アカウント認証を行う

    Parameters
    ----------
    user : schemas.UserCreate
        ユーザ名とパスワードを含んだデータ
    db : Session
        データベースとの接続を行うための情報

    Returns
    -------
    user : models.User
        Userモデル
    """

    db_user = crud.read_user_by_name(db=db, user_name=user.name)
    # パスワードが一致しない場合は401エラーを返す
    if user.password != db_user.password:
        raise HTTPException(
            status_code=401, detail="Password is incorrect")

    return db_user


@router.post("/note/{user_id}", response_model=schemas.Note, tags=['note'])
def create_note(note: schemas.NoteCreate,
                user_id: int,
                db: Session = Depends(get_db)):
    """
    Noteを作成する

    Parameters
    ----------
    note : schemas.NoteCreate
        ノートのタイトルと本文を含んだデータ
    user_id : int
        ノートを所有するユーザのID
    db : Session
        データベースとの接続を行うための情報

    Returns
    -------
    new_note : models.Note
        Noteモデル
    """

    new_note = crud.create_user_note(db=db, note=note, user_id=user_id)
    return new_note


@router.get("/notes/{user_id}", response_model=list[schemas.Note], tags=['note'])
def read_notes(user_id: int,
               offset: int = 0,
               limit: int = 100,
               db: Session = Depends(get_db)):
    """
    複数のNoteを取得する

    Parameters
    ----------
    user_id : int
        ノートを所有するユーザのID
    offset : int, default 0
        取得するユーザIDの始点
    limit : int, default 100
        取得するユーザIDの数
    db : Session
        データベースとの接続を行うための情報

    Returns
    -------
    users : list of models.Note
        {offset}番目から{limit}個分のNoteモデルのリスト
    """

    notes = crud.read_user_notes(
        db=db, user_id=user_id, offset=offset, limit=limit)
    return notes


@router.put("/note/update", response_model=schemas.Note, tags=['note'])
def update_note(note: schemas.Note, db: Session = Depends(get_db)):
    """
    Noteを更新する

    Parameters
    ----------
    note : schemas.Note
        Noteモデル
    db : Session
        データベースとの接続を行うための情報

    Returns
    -------
    new_note : models.Note
        Noteモデル
    """

    db_note = crud.read_note_by_id(db=db, note_id=note.id)
    # ノートが存在しない場合は400エラーを返す
    if not db_note:
        raise HTTPException(
            status_code=400, detail="Note does not exist")

    new_note = crud.update_note(db=db, note=note)
    return new_note


@router.delete("/note/{note_id}", response_model=schemas.Note, tags=['note'])
def delete_note(note_id: int, db: Session = Depends(get_db)):
    """
    Noteを削除する

    Parameters
    ----------
    note_id : int
        ノートのID
    db : Session
        データベースとの接続を行うための情報

    Returns
    -------
    delete_note : models.Note
        空のNoteモデル
    """

    db_note = crud.read_note_by_id(db=db, note_id=note_id)
    # ノートが存在しない場合は400エラーを返す
    if not db_note:
        raise HTTPException(
            status_code=400, detail="Note does not exist")

    delete_note = crud.delete_note_by_id(db=db, note_id=note_id)
    return delete_note
