# python3.11.2-busterのイメージを使用
FROM python:3.11.2-buster

# コンテナの/serverを作業ディレクトリに指定
WORKDIR /server

# ./server(ホストマシン)から/server(コンテナ)にファイルをコピー
COPY ./server .

# コンテナ内でrequirements.txtに記述したパッケージをインストール
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

# コンテナ起動時にmain.pyを実行
CMD ["python", "main.py"]
