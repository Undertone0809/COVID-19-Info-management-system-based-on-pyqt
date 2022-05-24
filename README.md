# 1.简介

python实验作业，正好回顾一下小学二年级学习的pyqt，优化一下以前写的框架。（大二还在写这些，有点惭愧，不想花太多时间写，于是一晚上肝完了）

> 1.本项目在pyqt的框架上进一步封装，基于springMVC架构和springboot架构进行二次架构设计，参考笔者之前写的：[【快速调用】基于mvc架构的pyqt架构封装](https://blog.csdn.net/linZinan_/article/details/112460133)
> 2.源代码链接：[https://gitee.com/zeeland/covid-19-based-on-pyqt](https://gitee.com/zeeland/covid-19-based-on-pyqt)



**相较于上篇博客，本次架构优化如下：**

- 优化了启动类的启动流程
- 添加了页面调度器，可以更加方便的进行页面调度
- 在启动类中添加了驱动注册中心，添加了相关的数据库驱动和连接池驱动，可以更加灵活的对数据库进行操作
- 进一步封装了mysql service，可以同时兼容connector和pool两种连接方式

# 2.运行环境

- python3.7.6
- 使用pip安装下面的环境

```shell
pip install PyQt5
pip install request
pip install pymysql
pip install mysql
pip install dbutils
```

- 目录结构

```shell
│  main.py
│  README.md
│
├─config # 配置文件
│  │  MysqlConfig.py
│  │  PoolConfig.py
│  │  __init__.py
│
├─controller # 页面控制器
│  │  HomeController.py
│  │  __init__.py
│
├─pojo  # model数据模型
│  │  epi_area.py
│  │  epi_province.py
│  │  __init__.py
│
├─service # 服务，包括爬虫服务和数据库CRUD服务
│  │  epi_area_service.py
│  │  epi_province_service.py
│  │  TodayEpiInfo.py
│  │  today_epi_info.json
│  │  __init__.py
│
├─static	# 静态文件
│  │  __init__.py
│  │
│  └─images
│          bg1.jpg
│          headPh.png
│  │
│  └─sql # 存放sql语句
│
├─utils
│      __init__.py
│
└─views
    │  home.py
    │  home.ui
    │  __init__.py
```

![image.png](https://img-blog.csdnimg.cn/img_convert/fac580a48fb9b9322fc69eaa08926d00.png)

# 3.需求分析

- 数据库存储所有的疫情信息，疫情信息包括：日期、城市名、新增病例、数量、确诊数量、疑似病例数据、治愈病例数量
- 可以用表格查看当前所有的疫情信息（定义排序规则）(**懒得做**)，并查询指定城市的疫情信息。
- 可以自动获取今日疫情信息也可以手动添加今日疫情信息
- 可以指定当前删除某个城市的信息

# 4.设计思路

啥也不管，先把架构搭起来，各个目录的文件夹先创建好，然后再做UI，把UI的大题样式确定下来。然后设计数据库模型，然后构建数据流逻辑，大体流程是这样。
![image.png](https://img-blog.csdnimg.cn/img_convert/c0299f9e4b41db0c47dfcf71cb6263ec.png)

- 需求上述已经确定好了。
- 框架搭建上述也做了一下大概描述，整个架构都是参考springMVC和springboot框架进行搭建的。
- UI设计过程省略。
- 解析疫情数据参考：[【爬虫+可视化】Python爬取疫情数据，并做可视化展示](https://blog.csdn.net/m0_48405781/article/details/121823049?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165235528016780366543939%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=165235528016780366543939&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_click~default-2-121823049-null-null.142^v9^control,157^v4^new_style&utm_term=%E7%88%AC%E5%8F%96%E7%96%AB%E6%83%85%E6%95%B0%E6%8D%AE&spm=1018.2226.3001.4187)，笔者参考了该博客的方法，自己爬了一个不同的API，解析里面的JSON数据，详细的信息在下面这两个文件，可以学习一下。

![image.png](https://img-blog.csdnimg.cn/img_convert/069af97eda6def246513841a1adeefc5.png)

- 根据解析的数据，数据库建成了下图的样子。一个省份疫情信息表，一个地区疫情信息表，地区外键指向省份id的主键。

![image.png](https://img-blog.csdnimg.cn/img_convert/f953b4cd9b636b539931f94f072d3954.png)
![image.png](https://img-blog.csdnimg.cn/img_convert/cdadfe96575c13c8d89e0455033246b6.png)

- model设计，两张表对应的实体类在pojo中，展示一个epi_province的代码

```python
class EpiProvince:
    def __init__(self,*args,**kwargs):
        # 地区名称
        self.province_name = None
        # 日期
        self.province_today_date = None
        # 更新时间
        self.province_total_update_time = None
        # 死亡人数
        self.province_total_dead = None
        # 治愈人数
        self.province_total_heal = None
        # 现有确诊
        self.province_total_now_confirm = None
        # 累积确诊
        self.province_total_confirm = None
        # 今日新增
        self.province_today_confirm = None
        # 逻辑删除
        self.is_delete = None
        # judge if the args is empty
        try:
            if len(args) == 0:
                self.province_name = kwargs['data']['province_name']
                self.province_today_date = kwargs['data']['province_today_date']
                self.province_total_update_time = kwargs['data']['province_total_update_time']
                self.province_total_dead = kwargs['data']['province_total_dead']
                self.province_total_heal = kwargs['data']['province_total_heal']
                self.province_total_now_confirm = kwargs['data']['province_total_now_confirm']
                self.province_total_confirm = kwargs['data']['province_total_confirm']
                self.province_today_confirm = kwargs['data']['province_today_confirm']
                self.is_delete = kwargs['data']['is_delete']
            else:
                args = args[0]
                self.province_name = args[1]
                self.province_today_date = args[2]
                self.province_total_update_time = args[3]
                self.province_total_dead = args[4]
                self.province_total_heal = args[5]
                self.province_total_now_confirm = args[6]
                self.province_total_confirm = args[7]
                self.province_today_confirm = args[8]
                self.is_delete = args[9]
        except Exception as e:
            print('[error]',e)

    def __str__(self):
        # print all info
        return 'province_name:%s,province_today_date:%s,province_total_update_time:%s,' \
               'province_total_dead:%s,province_total_heal:%s,province_total_now_confirm:%s,province_total_confirm:' \
               '%s,province_today_confirm:%s,is_delete:%s' % (self.province_name, self.province_today_date,
                self.province_total_update_time, self.province_total_dead,self.province_total_heal,
                self.province_total_now_confirm, self.province_total_confirm,
                self.province_today_confirm, self.is_delete)

```

- service实现：封装CRUD操作，可以更加方便的操作数据库实体（参考mybatis架构），节选代码如下所示。

```python
from config.MysqlConfig import MysqlConfig

class EpiProvinceService(MysqlConfig):
    def __init__(self,pool=None):
        super().__init__(pool=pool)

    def get_all(self):
        try:
            self.cursor.execute('select * from epi_province order by province_total_update_time desc')
            result = self.cursor.fetchall()
            return result
        except Exception as e:
            print('[error]',e)
            return None

    def get_count(self):
        try:
            self.cursor.execute('select count(*) from epi_province')
            result = self.cursor.fetchone()
            return result[0]
        except Exception as e:
            print('[error] EpiProvinceService get_count:',e)
            return None

    def get_by_name(self,province_name):
        try:
            # 查找里面含有有该字符串的数据
            self.cursor.execute('select * from epi_province where province_name like %s',(province_name+"%",))
            result = self.cursor.fetchall()
            return result
        except Exception as e:
            print('[error] EpiProvinceService get_by_name err:',e)
            return None

    def insert(self,epi_province):
        try:
            # find if has the same update time info, if has, then insert new one, if not, then do nothing
            self.cursor.execute('select * from epi_province where province_total_update_time = %s',
                                (epi_province.province_total_update_time,))
            result = self.cursor.fetchone()
            if result:
                # do nothing
                print('[info] EpiProvinceService insert: has the same data')
            else:
                # insert
                self.cursor.execute('insert into epi_province (province_name,province_today_date,'
                                    'province_total_update_time,province_total_dead,province_total_heal,'
                                    'province_total_now_confirm,province_total_confirm,province_today_confirm,'
                                    'is_delete) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)',(epi_province.province_name,
                                        epi_province.province_today_date, epi_province.province_total_update_time,
                                        epi_province.province_total_dead, epi_province.province_total_heal,
                                        epi_province.province_total_now_confirm, epi_province.province_total_confirm,
                                        epi_province.province_today_confirm, epi_province.is_delete))
                self.conn.commit()
                print('[info] insert successfully')
        except Exception as e:
            print('[error] EpiProvinceService insert err:',e)
            self.conn.rollback()

    def delete(self,province_name,update_time):
        try:
            self.cursor.execute('delete from epi_province where province_name = %s and province_total_update_time = %s',
                                (province_name,update_time))
            self.conn.commit()
        except Exception as e:
            print('[error] EpiProvinceService delete err:',e)
            self.conn.rollback()

    def __del__(self):
        try:
            self.cursor.close()
            self.conn.close()
        except Exception as e:
            print('[error] db close',e)
```

- controller实现的思想参考:[【快速调用】基于mvc架构的pyqt架构封装](https://blog.csdn.net/linZinan_/article/details/112460133)

程序设计到这里差不多就结束了，最后是主程序入口设计，如下：

```python
from PyQt5 import QtWidgets
from controller.HomeController import HomeController
from config.PoolConfig import PoolConfig

"""
@description: application gateways
"""
class SpireApplication:
    def __init__(self):
        # driver registration_list
        self.registration_list = {}
        # page dispatcher
        self.disp = None

        self.driver_registration()
        self.disp = PageDispatcher(self.registration_list)

    def driver_registration(self):
        self.pool_config = PoolConfig()
        self.registration_list['pool_config'] = self.pool_config
        print(self.registration_list)
        print('[sys] driver registered finish')
        

"""
@description: application page dispatcher,用作页面调度,控制不同的页面
@param      : registration_list驱动中心
"""
class PageDispatcher:
    def __init__(self,registration_list=None):
        self.registration_list = registration_list
        self.page_home_show(registration_list)
        print('[sys] page dispatcher finish')

    def page_home_show(self,registration_list=None):
        self.page_home = HomeController(registration_list=registration_list)
        self.page_home.show()

# main Application
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    a = SpireApplication()
    sys.exit(app.exec_())
```

# 5.运行效果

- **主界面**

![image.png](https://img-blog.csdnimg.cn/img_convert/a0203f0a44cb90cc152bc4c9e1cf9210.png)

- **切换页面**

![image.png](https://img-blog.csdnimg.cn/img_convert/fc7b5808ea904f5d0fb944aace47c2fb.png)

- **搜索城市or省份**

![image.png](https://img-blog.csdnimg.cn/img_convert/436b91f307f47f19f5d96d33f9934a70.png)

- **选中特定疫情数据删除**

![image.png](https://img-blog.csdnimg.cn/img_convert/8c9719f4d1bbe95542a7632175491076.png)
![image.png](https://img-blog.csdnimg.cn/img_convert/b918e995c0a6f5df2875e326dc8677b3.png)
![image.png](https://img-blog.csdnimg.cn/img_convert/6e7274f59eed68946c179d54fe1b183c.png)

# 6.参考资料

- [【爬虫+可视化】Python爬取疫情数据，并做可视化展示](https://blog.csdn.net/m0_48405781/article/details/121823049?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165235528016780366543939%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=165235528016780366543939&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_click~default-2-121823049-null-null.142^v9^control,157^v4^new_style&utm_term=%E7%88%AC%E5%8F%96%E7%96%AB%E6%83%85%E6%95%B0%E6%8D%AE&spm=1018.2226.3001.4187)
- [【快速调用】基于mvc架构的pyqt架构封装](https://blog.csdn.net/linZinan_/article/details/112460133)
- [python中形参*args和**args的区别](https://blog.csdn.net/linZinan_/article/details/114363592)
- [QTableWidget清空或删除内容及表头样式内容](https://blog.csdn.net/qq_16093323/article/details/79226349?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165244573916782248560921%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fall.%2522%257D&request_id=165244573916782248560921&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~first_rank_ecpm_v1~rank_v31_ecpm-4-79226349-null-null.142^v9^control,157^v4^new_style&utm_term=tabwidget+%E6%B8%85%E9%99%A4%E7%A9%BA%E7%9A%84%E5%86%85%E5%AE%B9&spm=1018.2226.3001.4187)

