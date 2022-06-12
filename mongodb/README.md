## mongodb 一些小東西  
集合(Collection)相當於RD(Relational Database)裡的table

# 基本指令  
1. 進入DB  
```
mongo
```
2. 列出所有資料庫  
```
show dbs;
```
3. 切換資料庫(# 如果資料庫不存在會直接創建一個)
```
# use + 資料庫名稱
use komablog;
```
4. 刪除資料庫  
```
db.dropDatabase();
```
## 操作集合(Collection)
1. 看collection
```
show collections;
```
2. 新增collection
```
db.createCollection("users");
```
3. 修改collection名稱
```
db.users.renameCollection("staff");
```
4. 刪除collection
```
db.staff.drop();
```
---

# CRUD 基本語法  


## C  

新增一列 db.posts.insert({})
```
> db.posts.insert(
... {
...     title:"我的第一篇博客",
...     content:"已經開始寫博客了,太感動了。"
... }
... );
```
以for新增多個列
```
> for(var i = 3;  i <= 10; i++ ){
        db.posts.insert(
         {title: "我的第" + i + "篇博客"} 
         );
    }
WriteResult({ "nInserted" : 1 })
```
把結果秀出來會像這樣
```
> db.posts.find();
{ "_id" : ObjectId("62a59b1073a3122a54e29213"), "title" : "我的第一篇博客", "content" : "已經開始寫博客了,太感動了。" }
{ "_id" : ObjectId("62a59bc473a3122a54e29214"), "title" : "我的第二篇博客", "content" : "寫點甚麼好呢?", "tag" : [ "未分類" ] }
{ "_id" : ObjectId("62a59d8273a3122a54e29215"), "title" : "我的第3篇博客" }
{ "_id" : ObjectId("62a59d8273a3122a54e29216"), "title" : "我的第4篇博客" }
{ "_id" : ObjectId("62a59d8273a3122a54e29217"), "title" : "我的第5篇博客" }
{ "_id" : ObjectId("62a59d8273a3122a54e29218"), "title" : "我的第6篇博客" }
{ "_id" : ObjectId("62a59d8273a3122a54e29219"), "title" : "我的第7篇博客" }
{ "_id" : ObjectId("62a59d8273a3122a54e2921a"), "title" : "我的第8篇博客" }
{ "_id" : ObjectId("62a59d8273a3122a54e2921b"), "title" : "我的第9篇博客" }
{ "_id" : ObjectId("62a59d8273a3122a54e2921c"), "title" : "我的第10篇博客" }
```
## R  
秀出有幾列
```
> db.posts.count();
10
```
查詢collection中的全部資料 db.posts.find();
相等於RD的 select * from posts  
```
> db.posts.find();
{ "_id" : ObjectId("62a59b1073a3122a54e29213"), "title" : "我的第一篇博客", "content" : "已經開始寫博客了,太感動了。" }
```
## 帶條件的查詢

條件列表  
```
db.[collection_name].find({"":""})
$gte
$gt
$lte
$lt
$eq
$ne
正規表達式:/k/, /^k/
db.[collection_name].distinct("field_name");
```

首先先建幾列資料
```
> db.posts.insert({title:"怪物獵人世界平測","rank":2,"tag":"game"});
WriteResult({ "nInserted" : 1 })
> db.posts.insert({title:"紙片馬里奧是玩體驗","rank":1,"tag":"game"});
WriteResult({ "nInserted" : 1 })
> db.posts.insert({title:"Ubuntu16LTS的安裝","rank":3,"tag":"it"});;;;
WriteResult({ "nInserted" : 1 })
> db.posts.insert({title:"信長之野望大致銷量突破10000","rank":4,"tag":"game"});
WriteResult({ "nInserted" : 1 })
> db.posts.insert({title:"ruby的開發效率真的很高","rank":7,"tag":"it"});;;;;;;;
WriteResult({ "nInserted" : 1 })
> db.posts.insert({title:"賽爾達傳說最近出了DLC","rank":4,"tag":"game"});
WriteResult({ "nInserted" : 1 })
```
將條件放入({})中，即可根據條件查詢
```
> db.posts.find({"tag":"game"});
{ "_id" : ObjectId("62a59f3773a3122a54e2921d"), "title" : "怪物獵人世界平測", "rank" : 2, "tag" : "game" }
{ "_id" : ObjectId("62a59f5e73a3122a54e2921e"), "title" : "紙片馬里奧是玩體驗", "rank" : 1, "tag" : "game" }
{ "_id" : ObjectId("62a59fb773a3122a54e29220"), "title" : "信長之野望大致銷量突破10000", "rank" : 4, "tag" : "game" }
{ "_id" : ObjectId("62a59ff973a3122a54e29222"), "title" : "賽爾達傳說最近出了DLC", "rank" : 4, "tag" : "game" }
```
```
> db.posts.find({"rank": {$gte: 4}});
{ "_id" : ObjectId("62a59fb773a3122a54e29220"), "title" : "信長之野望大致銷量突破10000", "rank" : 4, "tag" : "game" }
{ "_id" : ObjectId("62a59fd773a3122a54e29221"), "title" : "ruby的開發效率真的很高", "rank" : 7, "tag" : "it" }
{ "_id" : ObjectId("62a59ff973a3122a54e29222"), "title" : "賽爾達傳說最近出了DLC", "rank" : 4, "tag" : "game" }
```
```
> db.posts.find({"rank": {$gt: 4}});
{ "_id" : ObjectId("62a59fd773a3122a54e29221"), "title" : "ruby的開發效率真的很高", "rank" : 7, "tag" : "it" }
```
```
> db.posts.find({"rank": {$lte: 4}});
{ "_id" : ObjectId("62a59f3773a3122a54e2921d"), "title" : "怪物獵人世界平測", "rank" : 2, "tag" : "game" }
{ "_id" : ObjectId("62a59f5e73a3122a54e2921e"), "title" : "紙片馬里奧是玩體驗", "rank" : 1, "tag" : "game" }
{ "_id" : ObjectId("62a59f8e73a3122a54e2921f"), "title" : "Ubuntu16LTS的安裝", "rank" : 3, "tag" : "it" }
{ "_id" : ObjectId("62a59fb773a3122a54e29220"), "title" : "信長之野望大致銷量突破10000", "rank" : 4, "tag" : "game" }
{ "_id" : ObjectId("62a59ff973a3122a54e29222"), "title" : "賽爾達傳說最近出了DLC", "rank" : 4, "tag" : "game" }
```
```
> db.posts.find({"rank": {$lt: 4}});
{ "_id" : ObjectId("62a59f3773a3122a54e2921d"), "title" : "怪物獵人世界平測", "rank" : 2, "tag" : "game" }
{ "_id" : ObjectId("62a59f5e73a3122a54e2921e"), "title" : "紙片馬里奧是玩體驗", "rank" : 1, "tag" : "game" }
{ "_id" : ObjectId("62a59f8e73a3122a54e2921f"), "title" : "Ubuntu16LTS的安裝", "rank" : 3, "tag" : "it" }
```
```
> db.posts.find({"title": /u/});
{ "_id" : ObjectId("62a59f8e73a3122a54e2921f"), "title" : "Ubuntu16LTS的安裝", "rank" : 3, "tag" : "it" }
{ "_id" : ObjectId("62a59fd773a3122a54e29221"), "title" : "ruby的開發效率真的很高", "rank" : 7, "tag" : "it" }
```
```
> db.posts.find({"title": /^R/});
> db.posts.find({"title": /^r/});
{ "_id" : ObjectId("62a59fd773a3122a54e29221"), "title" : "ruby的開發效率真的很高", "rank" : 7, "tag" : "it" }
```
```
> db.posts.find({"title": /^U/});
{ "_id" : ObjectId("62a59f8e73a3122a54e2921f"), "title" : "Ubuntu16LTS的安裝", "rank" : 3, "tag" : "it" }
```
```
> db.posts.distinct("tag");
[ "game", "it" ]
```
多個條件
```
> db.posts.find({"title": /u/,"rank":{$gte:5}});
{ "_id" : ObjectId("62a59fd773a3122a54e29221"), "title" : "ruby的開發效率真的很高", "rank" : 7, "tag" : "it" }
```
```
> db.posts.find({$or:[{"title": /u/},{"rank":{$gte:4}}] });
{ "_id" : ObjectId("62a59f8e73a3122a54e2921f"), "title" : "Ubuntu16LTS的安裝", "rank" : 3, "tag" : "it" }
{ "_id" : ObjectId("62a59fb773a3122a54e29220"), "title" : "信長之野望大致銷量突破10000", "rank" : 4, "tag" : "game" }
{ "_id" : ObjectId("62a59fd773a3122a54e29221"), "title" : "ruby的開發效率真的很高", "rank" : 7, "tag" : "it" }
{ "_id" : ObjectId("62a59ff973a3122a54e29222"), "title" : "賽爾達傳說最近出了DLC", "rank" : 4, "tag" : "game" }
```
```
> db.posts.find({"rank": {$in: [3, 4]}})
{ "_id" : ObjectId("62a59f8e73a3122a54e2921f"), "title" : "Ubuntu16LTS的安裝", "rank" : 3, "tag" : "it" }
{ "_id" : ObjectId("62a59fb773a3122a54e29220"), "title" : "信長之野望大致銷量突破10000", "rank" : 4, "tag" : "game" }
{ "_id" : ObjectId("62a59ff973a3122a54e29222"), "title" : "賽爾達傳說最近出了DLC", "rank" : 4, "tag" : "game" }
```
```
> db.posts.insert({"title":"經!騎士發生重大交易", "istop": true });
WriteResult({ "nInserted" : 1 })
> db.posts.find();
{ "_id" : ObjectId("62a59f3773a3122a54e2921d"), "title" : "怪物獵人世界平測", "rank" : 2, "tag" : "game" }
{ "_id" : ObjectId("62a59f5e73a3122a54e2921e"), "title" : "紙片馬里奧是玩體驗", "rank" : 1, "tag" : "game" }
{ "_id" : ObjectId("62a59f8e73a3122a54e2921f"), "title" : "Ubuntu16LTS的安裝", "rank" : 3, "tag" : "it" }
{ "_id" : ObjectId("62a59fb773a3122a54e29220"), "title" : "信長之野望大致銷量突破10000", "rank" : 4, "tag" : "game" }
{ "_id" : ObjectId("62a59fd773a3122a54e29221"), "title" : "ruby的開發效率真的很高", "rank" : 7, "tag" : "it" }
{ "_id" : ObjectId("62a59ff973a3122a54e29222"), "title" : "賽爾達傳說最近出了DLC", "rank" : 4, "tag" : "game" }
{ "_id" : ObjectId("62a5a79873a3122a54e29223"), "title" : "經!騎士發生重大交易", "istop" : true }
> db.posts.find({"istop" : {$exists:true}});
{ "_id" : ObjectId("62a5a79873a3122a54e29223"), "title" : "經!騎士發生重大交易", "istop" : true }
```
## U
```

```

## D
刪除全部資料
```
> db.posts.remove({});
WriteResult({ "nRemoved" : 10 })
```