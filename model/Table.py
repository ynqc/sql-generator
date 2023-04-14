from typing import List
from model.Column import Column
from method import utils 


class Table:
    _table_name: str
    _table_alias: str
    _columns: List[Column]

    def __init__(self, name=None, alisa=None):
        super(Table, self).__init__()
        if name:
            utils.set_class_attribute(self, "_table_name", name)
        if alisa:
            utils.set_class_attribute(self, "_table_alias", alisa)

    def __setattr__(self, key, value):
        return super().__setattr__(key, value)
    
    @property
    def name(self):
        return self._table_name
    
    @property
    def alias(self):
        return self._table_alias
    
    @property
    def columns(self):
        return self._columns
    
    @property
    def sql_str(self):
        alias = (self._table_alias if hasattr(self, '_table_alias') else '')
        return f"{self._table_name} {alias}" if alias else self._table_name
        
    def __set_props(self):
        props = self.__dict__
        setattr(self, "_columns", [])
        for i in props:
            if isinstance(props[i], Column):
                if hasattr(self, '_table_alias') and hasattr(self, '_table_name'):
                    props[i].set_table(self._table_name, self._table_alias)
                self.__set_columns(self, props[i])
                
    def __set_columns(self, column):
        self._columns.append(column)   
    
    def instance(self):
        self.__set_props(self)
        return self()