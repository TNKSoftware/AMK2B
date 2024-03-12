AMK2B
=====
Kinect の スケルトンデータを Blender へ送信し、Blender の bone へ適用することで、簡単なモーションキャプチャを実現するツールです。

このプロジェクトでは、付属のアドオンがBlender 3.xでも動作するようにコードが修正されています。

実行環境
--------
* Microsoft Windows 10 以降
* [NET Framework 4 Client Profile](http://www.microsoft.com/ja-jp/net/netfx4/download.aspx "NET Framework 4 Client Profile") 以降
* [Kinect for Windows](http://www.microsoft.com/en-us/kinectforwindows/ "Kinect for Windows")
* [Kinect for Windows Runtime v1.8](http://www.microsoft.com/en-us/download/details.aspx?id=34810 "Kinect for Windows Runtime v1.8") 以降
* [Blender 3.6](http://www.blender.org/ "Blender") 以降

インストール
------------
1. [Release](https://github.com/TNKSoftware/AMK2B/releases "Release") からツールをダウンロードします。
1. 「KinectDataSender_x86」を任意のフォルダへ展開します。  
1. 「amk2b.zip」をBlender へアドオンとしてインストールします。
1. 編集画面でNキーを押し、右側のツールバーに「`AMK2B`」タブが追加されていればインストール完了です。

アンインストール
----------------
1. Blender へ追加した「`amk2b`」アドオンをBlenderから削除します。
1. ダウンロードした「`KinectDataSender`」を削除します。

使い方
------
1. 「`KinectDataSender.exe`」を起動します。  
   「`Kinect Data Sender`」画面が開きます。
1. 「`Kinect Data Sender`」画面の「`詳細設定`」で、Skeleton データを送信したい部位にチェックを入れます。
1. チェックを入れたチェックボックスに対応するテキストボックスへ、座標情報を適用する Blender のボーン名を入力します。  
   入力内容を保存する場合は、「`ファイル ＞ パラメータファイルを保存`」でファイル出力できます。
1. Blender を起動し、「`AMK2B/sample.blend`」を開いておきます。
1. 「`Kinect Data Sender`」画面の「`Kinect Start`」ボタンを押下します。  
   （Kinect が正常に作動した場合、左上にカメラ画像が表示されます。  
   表示されない場合、「`カメラ設定`」の「`カメラ画像描画`」がチェックされているか確認して下さい。）
1. 「`Kinect Data Sender`」画面の「`全体設定`」の「`自動設定`」ボタンを押下します。  
   カウントダウンが始まりますので、Kinect に向かって Blender 上のモデルと同じポーズをとります。  
   （"`前回設定時間`"が表示されれば成功です。）
   ここで設定されたジョイントの座標を基に相対座標で Blender の bone へ座標が適用されます。
1. Blender の「`AMK2B`」パネルの「`Receive Kinect Data`」ボタンを押下します。
1. Blender の「`AMK2B`」パネルの「`Apply Kinect Data`」ボタンを押下します。  
   これにより、Kinect の Skeleton 情報が Blender 上のモデルへ適用されます。  
   （体を動かすのと合わせてモデルも動けば成功です。）  
   なお、「Kinect Data Sender」の「ミラー」にチェックを入れると、  
   モデルに対して、鏡の前でポーズをとるように動かすことが出来るようになります。  
   他、「Kinect Data Sender」の設定や、モデルのボーンの設定などを見直し、  
   思うようなモーションキャプチャがとれるようになれるまで調整します。
1. Blender の「`AMK2B`」パネルの「`Recording`」ボタンを押下します。  
   カウントダウンが開始され、0 になるとモーションの録画が始まります。  
   録画は最初のフレームから最後のフレームまで行われ、停止します。
1. 出来上がったモデルとアニメーションデータはご自由にどうぞ。

Licensing
---------
Copyright &copy; 2012 asahiufo  
Licensed under the [GNU General Public License Version 3][GNU v3] 

Open Source Licensing
---------------------
* [Livet](http://ugaya40.net/livet "Livet")  
  Licensed under the [zlib/libpng][zlib/libpng]
* [Bespoke Open Sound Control Library](http://www.bespokesoftware.org/wordpress/?page_id=69 "Bespoke Open Sound Control Library")  
  Licensed under the [Microsoft Public License (MS-PL)][MS-PL]
* python-osc  
  Licensed under the [GNU General Public License][GNU]

[GNU v3]: http://www.gnu.org/licenses/gpl-3.0.txt
[zlib/libpng]: http://opensource.org/licenses/zlib-license.php
[MS-PL]: http://opensource.org/licenses/ms-pl.html
[GNU]: http://www.gnu.org/licenses/
