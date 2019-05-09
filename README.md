# GitHub練習用リポジトリ

## ブランチを切ってREADMEを更新
- hoge
    - hogehoge
- foo
    - foofoo

## rebaseを練習するためにわざとスペルミス
- hogehoge
    - foo

## hoge

### hogehoge
- hogehoge
- hoge

### hogehoge
- hogehoge
- hoge


### 直前のコミットメッセージを修正

~~~
$ git commit --amend
~~~

エディタが開かれるので自由にコミットメッセージを修正

### 数個前のコミットを変更したい場合

~~~
$ git rebase -i <commit>
# エディタが開くので変更して保存
~~~

| コマンド | 説明 |
| --- | --- |
| p, pick | コミットをそのまま採用する |
| r, reword | コミットを採用するが、メッセージのみ書き換える |
| e, edit | コミットを採用するが修正のために立ち止まる |
| s, squash | コミットを採用するが、前のコミットと合体する |
| f, fixup | squashと同様だが、コミットログメッセージは捨てる |
| x, exec | シェルを使ってコマンドを実行する |
