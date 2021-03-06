# coding=utf-8
"""
This file is for mysql database connection for user to use database operations as dataframe operations
"""

from .mysqltable import MySQLTable
from .mysqldatabase import MySQLDataBase


class MySQLOps(MySQLTable):
    
    def __init__(self, host: str, user: str, password: str, db_name: str) -> None:
        """
        This class is in development mode, not working yet. This class inherits
        MySQLTable and ListConversion. Purpose of this is to perform multiple
        table operations like join. But currently it is in development process,
        Not completed yet.
        
        Parameters
        ----------
        host : Host name of MySQL database.
        
        user : User name of MySQL database.
        
        password : Password for above user name of MySQL database.
        
        db_name : Any MySQL database name from MySQL database, which you want
        connect.
        """
        MySQLDataBase.__init__(self, host=host, user=user, password=password, db_name=db_name)
    
    def join_table(self):
        """
        This method is not working yet.
        TODO: create join table with foreign key, use yield to achieve iteration
        over object and commit changes into same table or create new table
        
        Returns
        -------
        pandas.DataFrame
        """
