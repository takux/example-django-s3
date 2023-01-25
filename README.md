# Example: django から S3 へ画像をアップロード

## 必要なライブラリのインストール

```
pip install Django django-environ boto3
```

Django: フレームワークとして使用
django-environ: 環境変数読み込み用に使用
boto3: S3 へのアップロードに使用

## AWS S3 の設定

Google 検索などで設定の方法を探すと出てくるので割愛。

## 環境変数の設定

.env ファイルを作成し、以下のように設定。
（Github などに公開しないように注意）

```
# DjangoのSECRET_KEY（今回のExampleとは直接関係ないが、Github上にSECRET_KEYは公開すべきでないので設定）
SECRET_KEY=xxx

# AWS S3で設定したアクセスキーやバケット名など
AWS_ACCESS_KEY_ID=xxx
AWS_SECRET_ACCESS_KEY=xxx
AWS_STORAGE_BUCKET_NAME=xxx
```

## Django の設定
