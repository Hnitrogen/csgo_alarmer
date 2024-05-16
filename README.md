一个github定时任务，将每天六点获取对应steamid下的库存饰品
- 当前脚本使用的buff网页的接口，非官方接口


另一种调用官方Api的方法: 
- 获取steam-api-key:  https://steamcommunity.com/dev/apikey
- steamid: https://store.steampowered.com/account/
- appid: 730 csgo2的
- 接口文档: https://partner.steamgames.com/doc/webapi/IInventoryService#GetInventory

- https://partner.steamgames.com/doc/webapi/IInventoryService#GetInventory 使用这个接口可以获取库存，但是需要开发者级别的Key，需要购买，100美元。（我都白嫖github actions，自然买不起）
- 请求头Host/Refer 如果携带 github.com 会被Nginx拦截

##### 配置repo
在Settings中配置Actions执行的secrets项
- EMAIL_PASSWORD        发送人邮箱密码
- EMAIL_USERNAME        发送人邮箱账号
- COOKIE                buff上的cookie ，记的用''包裹cookie的值
