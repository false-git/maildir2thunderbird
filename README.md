# maildir2thunderbird

Courier-IMAP で使っていた Maildir を Thunderbird のローカルフォルダで使えるように変換する。

* Thunderbirdでローカルフォルダを作る
* アカウント設定でローカルフォルダを開き、ローカルフォルダの保存フォルダを調べる。(curとかnewがあるフォルダ)
* IMAPサーバから持ってきたMaildirの中身を上記フォルダに上書き。
* maildir2thunderbird を持ってきたMaildirを引数に実行する。
