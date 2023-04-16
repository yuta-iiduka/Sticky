#インストール
py -m pip install Flask

#初期化
#py -m venv --clear .venv
#deactivate

#起動１
cd C:\Users\aaa\OneDrive\ドキュメント\学習用\Python\sticky
.venv\Scripts\activate
SET FLASK_APP=controller_sticky:app
py controller_sticky.py

#起動２
py -m flask run

#DB
cd C:\Users\aaa\OneDrive\ドキュメント\学習用\Python\sticky
.venv\Scripts\activate
SET FLASK_APP=controller_sticky:app
py -m flask db init
py -m flask db migrate
py -m flask db upgrade
#py -m flask db downgrade


//sample.htmlをブラウザで開きF12で開発者ツールを使い，以下を実行
//50x50のグリッドに沿ってJQueryオブジェクトが配置され，リサイズ，マウスによる再配置が可能になる。
to = new TreeObject("obj");
toheader = new TreeObject("header");
toheader.set_child(to);
g = new Grid(50,50);
g.set_jquery_obj(to.jquery_obj);
g.set_jquery_obj(toheader.jquery_obj);
g.fit();
g.reposition(to.jquery_obj,1,1,4,20)
g.reposition(toheader.jquery_obj,8,2,10,14)