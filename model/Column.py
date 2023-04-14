from method import utils 

class Column:
    __slots__ = ('_name', '_alias', '_table_name', '_table_alias')
    def __init__(self, name, alias=None, **kwargs):
        super(Column, self).__init__()
        self._alias = alias
        self._name = name

    @property
    def name(self):
        return self._name
    
    @property
    def alias(self):
        return self._alias
    
    @property
    def sql_str(self):
        alias = self.alias
        column_name = self.__format_table_alias()
        if alias:
            return f"{column_name} as {alias}"
        else:
            return column_name
    
    def __get_key(self, index, value):
        key = '_table_name' if index==0 else '_table_alias'
        utils.set_class_attribute(self, key, value)
        
    def __format_table_alias(self):
        _table_alias = (self._table_alias if hasattr(self, '_table_alias') else '')  
        return f"{_table_alias}.{self.name}" if _table_alias else self.name

 
    def set_table(self,  *args):
        for index,i in enumerate(args):
            self.__get_key(index, i)
        
