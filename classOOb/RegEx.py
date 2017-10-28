import re
safestr="132  21323   213 213   123"
safestrlast=re.sub("\\d+","ABC",safestr)
print(safestrlast)
print(safestrlast[0])
print(safestrlast[1])
print(safestrlast[2])

'''
safestr="132 21323 32323 2323 232"
safestrlast=re.subn("\\d+","ABC",safestr)# 第二个""删除,"ABC"替换
print(safestrlast)
print(safestrlast[0])
print(safestrlast[1])
'''
'''
safestr="全能神 全能神 全能神 全能神 "
safestrlast=re.subn("全能神","宇宙真理",safestr)#替换
# safestrlast=
print(safestrlast)
print(safestrlast[0])
print(safestrlast[1])
'''
'''
for data in re.finditer("\\d+","A11B22C33D44E55F61"): #筛选
    print(data.group())

print("---------------")
for data in re.finditer("[a-zA-Z]+","A11B22C33D44E55F61"): #筛选
    print(data.group())

print("---------------")
for data in re.finditer("[法轮功]","法轮功1234abcdefg法轮功"): #筛选
    print(data.group())

print("---------------")
for data in re.finditer("[^法轮功]","法轮功1234abcdefg法轮功"): #筛选,^取反
    print(data.group())
'''
'''
line1="a,b c;d"
mylist=re.split(r"[\s\,\;]",line1)#[\s\,\;] 三个符号选一个#正则表达式的 split
print(mylist)
'''
'''
# 正则表达式切割
line="127740 1小姐    22   166 本科  未婚   合肥 山羊座  编辑 普通话"
mylist=re.split("\\s+",line) # (\s表示空格 space) (+表示多个或者无数个)
print(mylist)
'''
'''
linelist=line.split(" ")#字符串切割,像这种无规则的字符串切割不正确
print(linelist)
'''
'''
# 字符串切割
line="363316626----3633166268190xl0"
linelist=line.split("----") # 字符串层面切割
print(linelist)
'''
'''
Emailstr="""
	caoxigang@baidu.com
曹　艳	Caoyan	6895	13811661805	caoyan@baidu.com
曹　宇	Yu Cao	8366	13911404565	caoyu@baidu.com
曹　越	Shirley Cao	6519	13683604090	caoyue@baidu.com
曹　政	Cao Zheng	8290	13718160690	caozheng@baidu.com
查玲莉	Zha Lingli	6259	13552551952	zhalingli@baidu.com
查　杉	Zha Shan	8580	13811691291	zhashan@baidu.com
查　宇	Rachel	8825	13341012971	zhayu@baidu.com
柴桥子	John	6262	13141498105	chaiqiaozi@baidu.com
常丽莉	lily	6190	13661003657	changlili@baidu.com
车承轩	Che Chengxuan	6358	13810729040	chechengxuan@baidu.com
陈　洁	Che	13811696984	chenxi_cs@baidu.com
陈　超	allen	8391	13810707562	chenchao@baidu.com
陈朝辉		13714189826	chenchaohui@baidu.com
陈　辰	Chen Chen	6729	13126735289	chenchen_qa@baidu.com
陈　枫	windy	8361	13601365213	chenfeng@baidu.com
陈海腾	Chen Haiteng	8684	13911884480	chenhaiteng@baidu.com
陈　红	Hebe	8614	13581610652	chenhong@baidu.com
陈后猛	Chen Houmeng	8238	13811753474	chenhoumeng@baidu.com
陈健军	Chen Jianjun	8692	13910828583	chenjianjun@baidu.com
陈　景	Chen Jing	6227	13366069932	chenjing@baidu.com
陈竞凯	Chen Jingkai	6511	13911087971	jchen@baidu.com
陈　坤	Isa13810136756	chenlei@baidu.com
陈　林	Lin Chen	6828	13520364278	chenlin@baidu.com
"""
# 匹配一个电话号码
print("匹配一个电话号码")
searchObj=re.findall("1[34578]\\d{9}",Emailstr)#找到所有的手机号并且把它挖出来.
print(searchObj)
print(type(searchObj))# 找到所有的电话号码,返回一个list列表

# 匹配所有的邮箱
print("匹配所有的邮箱")  # 要按套路来
regexmail=re.compile("([A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4})",re.IGNORECASE)#IGNORECASE忽略大小
maillist=regexmail.findall(Emailstr)
print(maillist)
'''
'''
QQstr="""
124528	男	14年	2012年5月以前	路人(0)	2017/02/21
2
顺便签约客服
940064306	男	9年	2016/07/12	宗师(1285)	2017/06/26
3
世间尽是妖魔鬼怪"(ºДº*)
90年代的新一辈_
1193887909	男	7年	2016/10/17	宗师(1084)	2017/06/26
4
萧十三楼
905519160	男	9年	2016/07/08	宗师(972)	2017/06/24
5
石头哥
北京-php-石头
2669288101	男	2年	2016/06/17	宗师(772)	2017/06/23
6
       缄默。
1393144035	未知	7年	2016/10/08	宗师(754)	2017/06/25
7
"""
findAllLine=re.findall("[1-9]\\d{4,10}",QQstr) # 查找全部,返回一个链表
print(findAllLine)
# searchObj=re.search("[1-9]\\d{4,10}",QQstr)#找到第一个符合条件的就可以了，没有查找全部.
# print(searchObj.group())
# print(searchObj.group(0))

'''
'''
searchObj=re.search(r"(.*)-is-(.*)","abc xyz-is-go")
#这里套路和match一样，唯一区别就是：
# print(re.match("xyz","abc xyz")) # 匹配从第一个开始
# re.search("abc","abc xyz"))# 查找 整个字符串包含就可以
print(searchObj)
print(searchObj.group())
print(searchObj.group(0))
print(searchObj.group(1))
print(searchObj.group(2))
'''
'''
print(re.match("abc","abc xyz"))
print(re.match("xyz","abc xyz")) # 匹配从第一个开始
#print(re.search())
print(re.search("abc","abc xyz"))# 查找 整个字符串包含就可以
print(re.search("xyz","abc xyz"))
'''
'''
# re 正则表达式在匹配大量数据的时候，使用预加载功能，提高效率
pat=re.compile("(.*)----(.*)")#预编译之后目的是加速（加快效率）,预加载正则表达式效率高
line="827007914----8421411penghueix"
matchObj=pat.match(line)
print(matchObj.group()) #matchobj.group()等价matchobj.group(0)
print(matchObj.group(0))
print(matchObj.group(1))
print(matchObj.group(2))
'''
'''
line="827007914----8421411penghueix"
matchObj=re.match(r"(.*)----(.*)",line) #切割
print(matchObj)
print(matchObj.group())
print(matchObj.group(0))
print(matchObj.group(1))
print(matchObj.group(2))

'''
'''
# match严格匹配，从第一个开始一个一个开始，"abc"在"abcdefgabc"出现的第一次
matchobj=re.match("abc","abcdefghabc")
print(matchobj)
print(type(matchobj))
print(matchobj.group(0))#挖掘的第一个匹配


#(.*) . 表示任意字符不包含换行，* 表示 0-N 次
line="gaoqinghua is a boy not a gril"
matchObj=re.match(r"(.*) is (.*) not (.*)",line)
print(matchObj)
print(matchObj.group())
print(matchObj.group(0))
print(matchObj.group(1))
print(matchObj.group(2))
print(matchObj.group(3))
# 3个正则表达式必须匹配 group(1)group(2)group(3)
'''
'''
# 3.match

import re
print(re.match("abc","abc")) #匹配，左边开始第一个算起
print(re.match("xabc","abc")) #匹配不成功返回None,匹配成功返回位置详细信息
print(re.match("abc","xabc"))
print(re.match("abc","abcx"))# 左边匹配右边，
'''
'''
# 2 正则判负案

import re
print(re.match("[1-9]\\d{4,10}","12341"))
print(re.match("[1-9]\\d{4,10}","12345678901"))
print(re.match("[1-9]\\d{4,10}","12341"))
print(re.match("[1-9]\\d{4,10}","1234"))
print(re.match("[1-9]\\d{4,10}","1234a"))
print(re.match("[1-9]\\d{4,10}","1234as"))
print(re.match("[1-9]\\d{4,10}","123412adsd213"))
print(re.match("[1-9]\\d{4,10}","a123412adsd213"))
'''

'''
# 1 为啥 regex.py
def checkQQ(QQstr):
    if len(QQstr)<5 or len(QQstr)>>11: #判断长度
        return False

    if QQstr[0]<'1' or QQstr[0]>'9': #判断第一个字符1-9
        return False

    for i in range(1,len(QQstr)): #剩下的每一个字符都在1-9
        if QQstr[i] < '0' or QQstr[i] >'9':
            return False

    return True

print(checkQQ("1892"))
print(checkQQ("112341232333"))
print(checkQQ("138fkf f"))
'''









































































