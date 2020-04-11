![fgosccalc1](https://user-images.githubusercontent.com/62515228/78868001-0ca71a80-7a7d-11ea-84b2-087f6b2466fc.png)
# fgosccalc
FGOのクエスト情報戦利品の周回前後のスクショを読み取り差分を計算

このプログラムをウェブ化したものをまっくすさんが公開しています https://fgosccalc.appspot.com/

## 必要なソフトウェア
Python 3.7以降

## ファイル
1. img2str.py : コマンドプロンプトでファイルを読み込みアイテムを出力
2. fgosccalc.py　: コマンドプロンプトでファイル2つを読み込み差分を出力
3. fgosccalc.cgi : fgosccalc.py の CGI版
4. calctweet.py : 周回報告のTweet URL から周回報告と画像差分をチェックする
5. item.csv : calctweet.py で使用するアイテム標準化ファイル
6. setting-dst.ini calctweet.py で使用する setting.ini の元ファイル
7. makeprop.py : property.xml を作成する
8. data/* : 文字学習用データ property.xml 作成後は必要無い

以下は4.実行時に作成される
9. property.xml : 文字認識のためのトレーニングファイル

## インストール
必要な Python ライブラリをインストールする

    $ pip install -r requirements.txt

makeprop.py を1度だけ実行

    $ python makeprop.py

### calctweet.py のインストールは以下の手順が必要
1. setting-dst.ini をコピーして setting.ini を作成
2. consumer_key　と　consumer_secret を手に入れる  
基本的に一般配布はしないので、https://developer.twitter.com/ からアプリケーション登録をして手に入れる  
※ここでaccess_token と access_secret を入手すると4の手順がとばせます
3. setting.ini に取得したconsumer_key と consumer_secretを入力する  
次のように入力します  

    consumer_key = 入手したconsumer_key  
    consumer_secret = 入手したconsumer_secret

4. calctweet.py を起動するとブラウザが立ち上がり、アプリ連携画面になるのでアプリ連携し、表示された PIN を入力する

## 使い方
### imgstr.py

    usage: img2str.py [-h] [-d] [--version] file
    
    戦利品画像を読み取る
    
    positional arguments:
      file         FGOの戦利品スクショ
    
    optional arguments:
      -h, --help   show this help message and exit
      -d, --debug  デバッグ情報を出力
      --version    show program's version number and exit

### fgosccalc.py

    $ fgosccalc.py ファイル名 ファイル名

    スクショから差分を計算する

### calctweet.py
    usage: calctweet.py [-h] [-a] [-s] [-r] [--version]
                        [tweet_url [tweet_url ...]]
    
    周回カウンタのスクショ付き報告をチェック
    
    positional arguments:
      tweet_url       Tweet URL
    
    optional arguments:
      -h, --help         show this help message and exit
      -u URL, --url URL  Tweet URL
      -a, --auto         #FGO周回カウンタ ツイの自動取得で連増実行
      -s, --suppress     差分のみ出力
      -i, --inverse      差分計算を逆にする
      -r, --resume       -a を前回実行した続きから出力
      -d, --debug        デバッグ情報を出力
      --version          show program's version number and exit