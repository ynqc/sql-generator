from typing import Any, Union
from method.utils import builder
from model.Column import Column
from model.Table import Table


class Query:
    @classmethod
    def _builder(cls, **kwargs: Any) -> "QueryBuilder":
        return QueryBuilder(**kwargs)

    @classmethod
    def from_(cls, *args: Union[Table, str, "QueryBuilder"], **kwargs: Any) -> "QueryBuilder":
        return cls._builder(**kwargs).from_(*args)

    
class QueryBuilder:
    def __init__(self):
        self._tables = []
        self._selects = []
        self._alias = ''
        # self._filters = []
        # self._groupbys = []
        # self._orderbys = []
        # self._joins = []
        # self._unions = []
        # self._limit = None
        # self._offset = None
    
    def __setattr__(self, key, value):
        return super().__setattr__(key, value)

    @builder
    def from_(self, *args: Union[Table, Query, str]) -> "QueryBuilder":
        for table in args:
            if isinstance(table, str):
                self._tables.append(Table(table))
            elif isinstance(table, QueryBuilder):
                self._tables.append("({str}) {alias}".format(str=table.get_sql(), alias=table._alias) if table._alias else "({str})".format(str=table.get_sql()))
            else:
                self._tables.append(table.instance(table))   
    @builder
    def as_(self, alias: str) -> "QueryBuilder":
        self._alias = alias
        
    @builder
    def select(self, *columns: Any) -> "QueryBuilder":
        for column in columns:
            if isinstance(column, str):
                if column == "*":
                    self._selects = ["*"]
                    return
                self._selects.append(Column(column))
            elif isinstance(column, Column):
                self._selects.append(column)
            else:
                raise 'Column error'
    
    def get_sql(self) -> str:
        query_str = ''
        if not self._selects:
            return ""
        query_str = self.__select_sql()

        if self._tables:
            query_str += self.__from_sql()

        return query_str

    def __select_sql(self) -> str:
        return "SELECT {str}".format(str=",".join([(column if isinstance(column, str) else column.sql_str) for column in self._selects]))
        
    def __from_sql(self) -> str:
        from_str = []
        for table in self._tables:
            if isinstance(table, Table):
                from_str.append(table.sql_str)
            elif isinstance(table, str):
                from_str.append(f"{table}")
                
        return " FROM {str}".format(str=",".join(from_str))
