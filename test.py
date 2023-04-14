# 类的实例只能拥有slots中定义的变量，不能再增加新的变量。注意：定义了slots后，就不再有dict
# 如果类变量与slots中的变量同名，则该变量被设置为 readonly！！！

# class base:
#     var=9 #类变量
#     __slots__=('x')
#     def __init__(self):
#         pass
 
# if __name__ == "__main__":    
#     b=base()
#     print (b.__dict__)
#     b.x=2 #添加实例变量
#     # print (b.__dict__)

# 如果要把一个类的实例变成 str，就需要实现特殊方法__str__()：
# 我们可以使用@property装饰器来创建只读属性，@property装饰器会将方法转换为相同名称的只读属性,
# 访问存在的属性时，会正常返回值，若该值不存在，则会进入最后的兜底函数__getattr__。
# 在对一个属性设置值的时候，会调用到这个函数，每个设置值的方式都会进入这个方法。
# super().__setattr__(key, value) # python 添加实例属性 因为类不能掉用实例属性

from model.Column import Column
from model.Query import Query
from model.Table import Table

if __name__ == "__main__":   
    class A(Table):
        _table_alias='a'
        _table_name="a"
        id = Column('id')
        name = Column('name')
        age = Column('age', "AGE")
    class B(Table):
        _table_alias='b'
        _table_name="b"
        id = Column('id')
        name = Column('name')
        age = Column('age', "AGE")
    a = Query.from_("a").select("*") 
    b = Query.from_("a").select("id", "name") 
    c = Query.from_("a").select(Column("name"), Column("id")) 
    d = Query.from_(A).select(A.id, A.name) 
    e = Query.from_(A).select("*")
    f = Query.from_(A).select(A.age) 
    g = Query.from_(A, B).select(A.age, B.age)
    print(a.get_sql()) # SELECT * FROM a
    print(b.get_sql()) # SELECT id,name FROM a
    print(c.get_sql()) # SELECT name,id FROM a
    print(d.get_sql()) # SELECT a.id,a.name FROM a a
    print(e.get_sql()) #SELECT * FROM a
    print(f.get_sql()) #SELECT age as AGE FROM a -> no _table_alias
    print(f.get_sql()) # SELECT a.age as AGE FROM a a -> has _table_alias
    print(g.get_sql()) # SELECT a.age as AGE,b.age as AGE FROM a a,b b