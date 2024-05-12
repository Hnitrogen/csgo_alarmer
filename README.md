一个github定时任务，将每天六点获取对应steamid下的库存饰品
- 如果想获取具体冷却时间需要携带Cookie，考虑到Cookie失效的问题。我这里没有携带。
- 没有携带Cookie获得所有饰品都是可以交易的（没有冷却），过滤规则在 want_list 和 want_gun 中


友情链接: 
- 获取steam-api-key:  https://steamcommunity.com/dev/apikey
- 接口文档: https://partner.steamgames.com/doc/webapi/IInventoryService#GetInventory

 TODO
[]我记得steamworks的api有通过个人steam——token获取饰品的接口，出差回来找不到了，有空找找把上面的缺陷修复了   --- https://partner.steamgames.com/doc/webapi/IInventoryService#GetInventory
