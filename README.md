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

### コミットをなかったことにしたいとき

#### 削除コミット

~~~
# コミット済みのファイルをリポジトリから消す
$ git rm --cached <file_name>

# gitignoreに追記
$ echo '<file_name>' >> .gitignore
~~~

### コミット自体なしにしたいとき

- pushしていないときは``rest``で対応

- pushしているとき

~~~
$ git revert <commit>
~~~

### コミットをまとめたいとき

- rebase + squashでコミットをまとめる

~~~
$ HEADを含む過去のnコミット分をrebase
$ git rebase -i HEAD~n

# エディタが開くので変更して保存
# fixup, fは1つ前のコミットにまとめられる
~~~

### 間違って違うブランチにコミットしちゃったとき

~~~
# コミットが残った状態で別ブランチを作る
$ git branch <other-branch>

# masterのHEAD、インデックス、ワーキングツリーを全て1つ前に戻す
$ git reset --hard HEAD~

# コミットが残っている別ブランチをチェックアウト
$ git checkout other-branch
~~~

### コミットをうっかり消しちゃった時

~~~
# 過去のコミット一覧をみる
$ git reflog

# コミットを選択して復元
$ git reset --hard <commit>
~~~

### ブランチを復元したい時

- branch nameにコミットが復元される

~~~
$ git reflog

$ git branch <branch name> <commit>
~~~

### コミットの内容を一部変更

~~~
$ git rebase -i <commit>

# 対象コミットのpickをeditに変更

$ git commit --amend
$ git rebase --continue
~~~

## リモート編

### 何個か前のコミットを消したい場合

~~~
$ git rebase -i <対象コミット>

$ git push -f origin master
~~~
