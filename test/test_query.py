from model.Column import Column
from model.Query import Query
from model.Table import Table
# class A(Table):
#     _table_alias='a'
#     _table_name="a"
#     id = Column('id')
#     name = Column('name')
#     age = Column('age', "AGE")
# class B(Table):
#     _table_alias='b'
#     _table_name="b"
#     id = Column('id')
#     name = Column('name')
#     age = Column('age', "AGE")
# a = Query.from_("a").select("*") 
# b = Query.from_("a").select("id", "name") 
# c = Query.from_("a").select(Column("name"), Column("id")) 
# d = Query.from_(A).select(A.id, A.name) 
# e = Query.from_(A).select("*")
# f = Query.from_(A).select(A.age) 
# g = Query.from_(A, B).select(A.age, B.age)
# print(a.get_sql()) # SELECT * FROM a
# print(b.get_sql()) # SELECT id,name FROM a
# print(c.get_sql()) # SELECT name,id FROM a
# print(d.get_sql()) # SELECT a.id,a.name FROM a a
# print(e.get_sql()) #SELECT * FROM a
# print(f.get_sql()) #SELECT age as AGE FROM a -> no _table_alias
# print(f.get_sql()) # SELECT a.age as AGE FROM a a -> has _table_alias
# print(g.get_sql()) # SELECT a.age as AGE,b.age as AGE FROM a a,b b

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

a = Query.from_(A).select(A.age) 
b = Query.from_(a).select("*")

print(b.get_sql()) # SELECT * FROM (SELECT a.age as AGE FROM a a)


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

a = Query.from_(A).select(A.age)
c = Query.from_(A).select(A.age).as_("C")
b = Query.from_(a).select("*")
e = Query.from_(a, c).select("*")

print(b.get_sql()) # SELECT * FROM (SELECT a.age as AGE FROM a a)
print(e.get_sql()) #SELECT * FROM (SELECT a.age as AGE FROM a a),(SELECT a.age as AGE FROM a a) C

