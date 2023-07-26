# Clash规则列表

这是一个自用的Clash的规则列表,主要来源于[ShellClash](https://github.com/juewuy/ShellClash)和[ACL4SSR](https://github.com/ACL4SSR/ACL4SSR)的规则。

## 使用
```
https://api.dler.io/sub?target=clash&insert=true&new_name=true&exclude=8x|Traffic|Expire&include=&url=xxxxxxxx&config=https://raw.githubusercontent.com/zhf883680/ClashRules/main/Clash.ini
```

`exclude:过滤关键词  中文请转码`

`url:机场地址 多个用|分割`

`其他可保持不变`

`具体可访问 https://acl4ssr-sub.github.io/ 自行配置  把最后的config= 替换成https://raw.githubusercontent.com/zhf883680/ClashRules/main/Clash.ini`

## 差别

自行测试发现chatgpt无法访问,因此将claude.ai和bard作为独立的rule,其余ai相关的网址也独立成rule。  
具体请查看`ai.list` 与 `otherAi.list`

## 感谢

- [juewuy/ShellClash](https://github.com/juewuy/ShellClash): One-click deployment and management of Clash services using Shell scripts in Linux environment

- [ACL4SSR/ACL4SSR](https://github.com/ACL4SSR/ACL4SSR): SSR 去广告ACL规则/SS完整GFWList规则/Clash规则碎片,Telegram频道订阅地址
