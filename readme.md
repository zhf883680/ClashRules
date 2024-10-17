# Clash规则列表

这是一个自用的Clash的规则列表,主要来源于[ShellClash](https://github.com/juewuy/ShellClash)和[ACL4SSR](https://github.com/ACL4SSR/ACL4SSR)和[LM-Firefly](https://github.com/LM-Firefly/Rules)的规则。  
中国大陆规则以LM-Firefly为主,
每周会自动比较ACL4SSR和LM-Firefly的不一样的规则,添加进来,防止大量重复规则 
## 使用
```
https://api.dler.io/sub?target=clash&insert=true&new_name=true&exclude=8x|Traffic|Expire&include=&url=xxxxxxxx&config=https://raw.githubusercontent.com/zhf883680/ClashRules/main/Clash.ini
```

`exclude:过滤关键词  中文请转码`

`url:机场地址 多个用|分割`

`其他可保持不变`

`具体可访问 https://acl4ssr-sub.github.io/ 自行配置  把最后的config= 替换成https://raw.githubusercontent.com/zhf883680/ClashRules/main/Clash.ini`


## 感谢

- [juewuy/ShellClash](https://github.com/juewuy/ShellClash): One-click deployment and management of Clash services using Shell scripts in Linux environment

- [ACL4SSR/ACL4SSR](https://github.com/ACL4SSR/ACL4SSR): SSR 去广告ACL规则/SS完整GFWList规则/Clash规则碎片,Telegram频道订阅地址
- 
- [LM-Firefly/Rules](https://github.com/LM-Firefly/Rules): 自用Clash 策略组及规则 及Subconverter 相关资源备份