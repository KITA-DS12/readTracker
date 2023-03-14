from fastapi import FastAPI
import uvicorn

# FastAPIのインスタンスを作成
app = FastAPI()


# ルートパス("/")へアクセスした場合
@app.get("/")
async def root():
    # JSON形式で"message": "Hello World"というメッセージを返す
    return {"message": "Hello World"}

# このpyファイルが実行された場合
if __name__ == "__main__":
    # WSGI(Web Server Gateway Interface)であるuvicornで
    # サーバーを起動する
    uvicorn.run(
        # main.pyファイルのappオブジェクトを使用する
        app="main:app",
        # ホストに0.0.0.0を指定
        host="0.0.0.0",
        # ファイル変更時に自動でリロードをする
        reload=True,
        # ポート番号8888を指定
        port=8888,
        # デバッグログを出力
        log_level="debug"
    )
