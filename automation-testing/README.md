


# UI自动化框架总体设计思想

采用了分层结构来做到最大的复用与集成，有利于后期维护的扩展

1. Driver层：
采用了selenium Grid来做分布式管理，统一入口，所有端的测试都作为Node注册到一个Hub上，同时将appium和selenium集成到一起，通过设置环境变量
来做到driver的切换

默认的是用firefox来测试web后台case(type="web:Firefox")

切换到web端chrome浏览器 type="web:Chrome"

切换到H5   type="app:H5"

切换到Android测试   type="app:Android"

切换到IOS测试  type="app:IOS"


2. Element层：
所有的页面元素都封装成一个element(包含baseelment，asyncelement，select2element或是selectelment)，

里面封装了下面几类操作

__call__

这个对象自调用方法会同时实现set(sendkeys)和get(find_elements)功能

click,get_text等封装WebElement的操作

swipe

滑动，app测试特有的方法

包含了下面几类element

BaseElement

这个是element的最上层父类。里面封装了上述提到的方法

AsyncElement

异步式的element,__call__方法中包含智能等待元素功能

Select2Element, SelectElement

两类特殊的元素封装，可以将WebElement多种操作封装成一类，统一入口，便于调用

ElementCollection层

按照页面来组合元素，每个collection会包含某个页面或是某个模块所有的元素，封装的原因是利于将来复用

里面还会定义一个smoke_locators的list，用于指定冒烟测试的元素


3. Page层

封装了一个页面需要的基本操作，例如

get_url

通过url访问页面

start_activity

通过activity访问android应用的某个页面

等待页面加载操作

切换handle操作等

4. Case层

继承自unittest.TestCase，封装了case需要的操作

截图操作

虚拟登录操作

冒烟测试操作

5. Config层

里面会包含所有项目需要的配置信息



运行case
------------------------------------------------------------
我们需要进入UI层，将此作为当前目录，其实也是为了保证我们的截图功能顺利工作

1. run web backend cases--------pytest web/

2. run H5 investor cases--------pytest H5/

3. run app accountant cases--------pytest app/

Note:

要跨CPU来跑case, 加上 -n 参数

要重跑failed的case,加上 --reruns 参数

要生成测试报告，后面加上--junit-xml参数


服务器配置
--------------------------------------------------------------

一切都是基于selenium Grid

Hub: java -jar selenium-server-standalone-3.4.0.jar -role hub

Web node: java -jar selenium-server-standalone-3.4.0.jar -role webdriver -hub http://192.168.0.54:4444/grid/register/

App node(H5 included): appium -p 4723  -U 45EMGY49DMBM4LZS --nodeconfig='oppo.json' --no-reset




# API自动化框架总体设计思想


路径规划
---------------------------------------------------------------

接口按照开发controller的路径来进行设计

common：公共接口所在地

advisor：理财师端（APP端）接口所在地

investor：投资人端接口所在地

同时因为我们对外提供了接口，例如批量处理的部分接口在内部是不存在的，所以这部分被分配到了ex 文件夹下，其余的外部和内部公用的部分会被分散到
上面提到的文件夹中。

打Tag标签
-----------------------------------------------------------------

因为牵涉到了代码复用，所以我们会以打标签的形式来标记此case的类型

如果是内部接口  @attr('internal')

如果是外部open接口，主要是投资人的接口，主要用于客户可能需要自己开发自身H5系统之用，@attr('externalopen')

如果是外部接口，主要是企业后台使用，会包含一些批处理的接口， @attr('external')


运行case
-------------------------------------------------------------------

因为pytest的tag对于父子类关系那有bug，所以采用了nose来调度case运行

nosetests API/ -a internal --with-xunit --xunit-file="API/reports/API_tests.xml"
