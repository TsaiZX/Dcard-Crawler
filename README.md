# Dcard-crawler
學術使用，抓取 Dcard 特定版、特定文章

## 參數名
---
時事版:trending

popular = true 為熱門文章 / false 為最新文章

## Dcard Api
---
- https://www.dcard.tw/_api/forums/[*版名]/posts?popular=true

- https://www.dcard.tw/_api/forums/[*版名]/posts?popular=false&before=[*文章id]


透過ID 可以找到文章:
- https://www.dcard.tw/_api/posts/[*id]

文章留言
- https://www.dcard.tw/_api/posts/[*id]/comments?limit=50
- https://www.dcard.tw/_api/posts/[*id]/comments?after=50

搜尋
- https://www.dcard.tw/_api/search/posts?highlight=true&query=[*搜尋字串]
- https://www.dcard.tw/_api/search/posts?highlight=true&query=[*搜尋字串]&offset=

