一个github定时任务，将每天六点获取对应steamid下的库存饰品
- 如果想获取具体冷却时间需要携带Cookie，考虑到Cookie失效的问题。我这里没有携带。
- 没有携带Cookie获得所有饰品都是可以交易的（没有冷却），过滤规则在 want_list 和 want_gun 中
- 当前脚本使用的网页的接口，非官方接口


另一种调用官方Api的方法: 
- 获取steam-api-key:  https://steamcommunity.com/dev/apikey
- steamid: https://store.steampowered.com/account/
- appid: 730 csgo2的
- 接口文档: https://partner.steamgames.com/doc/webapi/IInventoryService#GetInventory

- https://partner.steamgames.com/doc/webapi/IInventoryService#GetInventory 使用这个接口可以获取库存，但是需要开发者级别的Key，需要购买，100美元。（我都白嫖github actions，自然买不起）
- 请求头Host/Refer 如果携带 github.com 会被Nginx拦截
