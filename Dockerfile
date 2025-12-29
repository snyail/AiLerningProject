FROM python:3

# アプリケーションディレクトリを作成する
WORKDIR /usr/src/Project

# pipのアップデート
RUN pip install --upgrade pip

# pipでインストールしたいモジュールをrequirements.txtに記述しておいて、
# コンテナ内でpipにインストールさせる
# requirements.txtの書き方は[pip freeze]コマンドから参考に出来る
COPY ./Project/requirements.txt ./
RUN pip install -r requirements.txt

# アプリケーションコードをコンテナにコピー
COPY . .

CMD ["tail", "-f", "/dev/null"]
