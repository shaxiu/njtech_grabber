# 南京工业大学抢课小助手

本脚本暂时处于测试版阶段，示例代码可用于通识选修课选课退课等，仅支持自用，禁止用于个人盈利。

🎈代码修改，以及请求参数配置具体详见:<a href='https://github.com/shaxiu/ZF_API'>正方教务选课系统API分析文档</a>

---------------------------------------------------------------------------------------------------------------------------------------

## 功能

由于2021-2022第二学期选课改为分年级分时段
因此本抢课助手有了用武之地，具体功能如下:

- [x] 跨越时段限制选课，即当高年级可以选课的时候，低年级也可进行选课
- [x] 跨越限制进行退课，即页面不允许退课时，也可进行正常退课
- [x] 已选课程查询
- [x] 自动获取cookie
- [x] 自动获取`njdm_id`、` xkkz_id`、`xkxnm`、`xkxqm`
- [x] 支持主修课选课
- [x] 支持拓展英语课选课(写是写了，管不管用俺就不知道了)
- [ ] 支持体育课选课
- [ ] 支持多线程暴力抢课


## 效果图

![result](./images/1.png)

![result](./images/2.png)

![result](./images/3.png)

## 环境配置

- Python3

- configparser

- requests

- rsa

- bs4

### 安装

默认已安装好python3

#### 安装库

`pip3 install configparser`

`pip3 install requests`

`pip3 install rsa`

`pip3 install bs4`

## 脚本配置

```
[accountConfig]
userName=用户名(学号)
passWord=密码
[baseConfig]
baseUrl = https://jwgl.njtech.edu.cn
xkkz_id = null
kklxdm=null
xkxnm=null
xkxqm=null
njdm_id=null
zyh_id=null
isEnglishCourse=false
```

**基础玩法**

- 将 `config.ini` 与软件脚本放于同一目录下
- 将配置文件中的 `userName` `passWord`  改为自己的用户名和密码
- 将 `baseUrl` 改为学校教学管理平台对应域名地址
- 若是拓展英语课程，将 `isEnglishCourse` 参数改为 `true`（未经测试，俺也不知道管不管用）
- 其他参数无需更改

**进阶玩法**

- 若学校进行分年级分时段选 选修课，例如 19级可以进行选课而作为20级的你无法选课/只可以选主修课
- 你可以通过修改参数~~欺骗后台~~ ，~~假装自己是19级的~~
- 修改 `njdm_id` 如 `2020`  -> ` 2019`
- 修改 `kklxdm` ：`01`为主修课 `10` 为选修课 `07`为拓展英语课      ps:每个学校不同，仅供参考
- 修改 `xkkz_id`：该参数可以找对应有权限选课的高年级/低年级同学要，每一轮次选课固定
- 其他参数配置具体详见:<a href='https://github.com/shaxiu/ZF_API'>正方教务选课系统API分析文档</a>

## <span id="jump">卡bug的简易方法</span>

注：方法主要针对分年级分时段选课，未到时间的用户无法进入通识选修课的界面的问题(前提是用户可正常进入主修课选课界面)

- F12查看网页代码，将 `id='kklxdm'` 的input框的 `value` 改为 `10`

  其中`10`对应通识选修课，`01`对应主修课选课

- 修改完成后点击搜索，发现课程列表出现通识选修课，但无法正常点击展开课程进行选课

- 将 `id='xkkz_id'` 的input框的value改为 `D8243C19A3C0239AE0530264A8C00F27`(动态值,以具体情况为准)

- 将`id='njdm_id'`的input框的value值改为允许现在选网课的年级如`2018`

- 再次点击课程，发现可以正常展开并进行选课
