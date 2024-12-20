import sqlite3


class Banco_de_produtos():
    def __init__(self, bd):
        self.__conn = sqlite3.connect(bd)
        self.__cursor = self.__conn.cursor()

    def create_table(self, table, columns):
    
        key = ''
        for i in columns:
            key += f'{i} {columns[i]}, '

        query = f'''
            CREATE TABLE IF NOT EXISTS {table}(
                {key[:-2]}
            )
        '''
        
        if self.__cursor.execute(query):
            self.__conn.commit()
            return True
        return False
    
    def get_all(self, table):
        self.__cursor.execute(f'''
            Select * from {table}
        ''')
        return self.__cursor.fetchall()
    
    def get_value_id(self, table, id):
        self.__cursor.execute(f'''
            Select * from {table} where id = "{id}"
        ''')

        return self.__cursor.fetchall()

    def get_value(self, table, condition):
        
        where = ''
        for i in condition:
            where += f'WHERE {condition[i]}' if i == 'where' else ''

        query = f'''
            Select * from {table} {where}
        '''

        self.__cursor.execute(query)
        return self.__cursor.fetchall()

    def insert_values(self, table, values):
        key = ''
        value = ''

        for i in values:
            key += f'{i}, '
            value += f'"{values[i]}", '

        query = f'''
            INSERT INTO {table}({key[:-2]}) VALUES ({value[:-2]});
        '''

        if self.__cursor.execute(query):
            self.__conn.commit()
            return True
        return False

    def update_values(self, table, values, condition):
        key = ''
        where = ''

        for i in values:
            key += f'{i} = "{values[i]}", '

        for i in condition:
            where += f'WHERE {condition[i]}' if i == 'where' else ''

        query = f'''
            UPDATE {table} SET {key[:-2]} {where}
        '''

        print(query)


        if self.__cursor.execute(query):
            self.__conn.commit()
            return True
        return False
    
    def delete_values(self, table, condition):
        where = ''
        for i in condition:
            where += f' where {condition[i]}' if i == 'where' else ''

        query = f'''
            DELETE FROM {table} {where}
        '''

        if self.__cursor.execute(query):
            self.__conn.commit()
            return True
        return False