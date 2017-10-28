class 王建林:
    def __init__(self):
        self.money=20000e8 # 2000*10^8
        self.mystr="定一个小目标，赚它一个亿"

    @classmethod  # 标识符，可以省略，类的内部方法
    def doing(self):
        #print("疯狂工作")
        return "疯狂工作"

    def buy(self):
        #print("有钱花")
        return "有钱花"

def getmoney(wjl): # 把类当作参数，通过参数调用类的内部方法（外部方法）
   return wjl.buy()
   # return wjl.money

dawang = 王建林()
print(getmoney(dawang))
dawang.doing()

''' #静态方法
class People:
    def __init__(self,tall):
        self.tall=tall

    @staticmethod #静态方法，是关键字
    def gereyes():
        return 2

    def gettall(self):
        return self.gereyes()

# 静态方法不用实例就能访问，通过(类名.静态方法)就可以调用
print(People.gereyes())#通用的东西，静态方法，不同实例就可以使用的方法

p1=People(123)
print(p1.gereyes()) # 实例化也可以使用
print(type(People.gereyes))
print(type(People.gettall))

'''







'''
class MyOBJ:
    pass


class MyOBJK(object): # 所有的类是 object 的子孙
    pass



my1 = MyOBJ()
print(dir(my1))
print("-----------")
my2 = MyOBJK()
print(dir(my2))
print("-----------")
my3 = object()
print(dir(my3))
'''
'''
class Person(object):
    def __init__(self,tall,name):
        self.eye = 2
        self.tall=tall
        self.name=name
        # print("My name is Person")

    def polymorphismFunc(self):
        return ("My name is %s"%(self.name))

class Student(Person):
    def __init__(self,tall,name):
        super(Student,self).__init__(tall,name)
        # print("My name is Student")

    def polymorphismFunc(self):
        return ("My name is %s"%(self.name))


class Teacher(Person):
    def __init__(self,tall,name):
        super(Teacher,self).__init__(tall,name)
        # print("My name is Teacher")

    def polymorphismFunc(self):
        return ("My name is %s"%(self.name))


def display(p):  # 多态 体现函数
    print(p.polymorphismFunc())

p=Person(1,"Person")
s=Student(12,"Student")
t=Teacher(123,"Teacher")

display(p)
display(s)
display(t)
'''





















































