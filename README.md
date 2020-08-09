ECHO-text
## 回声发送文字消息
> 手机搜狗输入法的开挂回声模式启发了我，遂在电脑上编写了一款功能类似的程序，权当练手
理论上只要支持enter键发送消息的聊天平台都可使用
（经测试Windows PCQQ可用）

<br>**像下面这样**
</br>

> 阿巴阿巴阿巴阿巴
阿巴阿巴阿巴阿
阿巴阿巴阿巴
阿巴阿巴阿
阿巴阿巴
阿巴阿
阿巴
阿

<br>来张图片帮助理解</br>
![例图](https://img-blog.csdnimg.cn/20200809154008513.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ2OTIyNzky,size_16,color_FFFFFF,t_70 "例图")


------------

Python语言，依赖库keyboard，pynput，pyperclip，time
`pip install keyboard pynput pyperclip`即可便捷安装

------------

### 使用方法：
1. 输入框输入文字
2. 按shift+enter
3. 即可自动发送回声内容
4. 按ctrl+q退出，（发送过程中不能强行退出）
- 不建议发送过长文字消息，可能会被判定刷屏
<br>

#### PS:若有英文字母输入，则需要将输入法调成英文模式，否则会出各种奇奇怪怪的错误
</br>