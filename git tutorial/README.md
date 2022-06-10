* 為何選擇使用github  
方便使用git版本控制系統
* 為何不使用gitlab  
gitlab需架設一台伺服器
---
## 前置作業
1. 安裝vscode(使用vscode可以更加輕易地使用git的基本動作，如果你很愛打commandline的話不用也行)
2. 安裝git
大致步驟可參照 : https://books.bod.idv.tw/2019/10/visual-studio-code-vs-code-git.html
---
## git與github入門教學(包含add commit push clone指令)

請參考 : https://www.youtube.com/watch?v=Zd5jSDRjWfA  

---  

### 若是第一次要commit，需要先設定好姓名和email(可隨意設定，但必要)  
getting start : https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup
1. cd到本地端的repository下，即你gitclone的資料夾  
2. 設定姓名和email
```
$ git config --global user.name "John Doe"
$ git config --global user.email johndoe@example.com
```  
---
## 基本指令  
* init(直接在本地端，建立好一個repository)，會發現出現一個.git資料夾，如果clone別人的repositoy就不用做這個動作
```
git init
```
* add
```
git add <檔案名稱> (add檔案)
git add . (add目前目錄下全部目錄與檔案)
```
* reset(此段可不需要使用command line，可用vscode的功能)
```
reset原本add的檔案
git reset -- <file name>

將某檔案回到前一個commit的狀態
git reset -- <file name>
git checkout -- <file name>

回到前一個commit的狀態(HEAD~"數字"，這個數字為前幾個commit，1代表前一個)
git reset --soft HEAD~1
```
* commit(請記得一定要留下欲commit的訊息)
```
git commit -m "some message"
```
* remote(設定github，不知道是不是要先去github建立專案)
```
git remote add <自訂名稱> <網址>
```
* push(推送推送至github)
```
git push -u <要push的名稱> <branch名稱> (帶-u參數可設定預設的git push)
前步驟設定完後，之後只需要git push即可

git push -f (-f => --force，會強制push，盡量不要用在多人開發的branch上，會影響到其他人)
```
* clone(同時下載前版本，clone完之後就可以做協同開發)
```
git clone <網址>
```

* checkout
```
git checkout 退出目前分支
git checkout <branch name> (切換分支，應該和git swhitch <branch name>一樣)
git checkout -b <branch name> 建立新branch並切換過去
```
* branch(分支)
```
git branch <branch name> (新增分支)
git branch -d (刪除branch)

```
* git pull(把新的commit抓下來)
```
conflict(因為在不同地方commit產生的版本不一致)
```
* git merge(分支整合)
```
git merge <要整合的branch(此branch在merge完會消失)> (將要整合的branch整合到現在所在的branch下，所以要注意有無切換到正確的branch)
```
* git rebase (把目前的分支的起始點一道最新的進度)
```
git rebase <要rebase到哪個分支>
若有衝突，則解決完後執行git rebase --continue
```
* 其他
```
git log (看日誌，按q離開瀏覽)
git remote (列出所有remote)
git status (看目前git狀態)
git branch (看所有branch，-a看包含remote上的所有branch)
```

可以參考簡單圖解 : https://backlog.com/git-tutorial/tw/stepup/stepup1_1.html
