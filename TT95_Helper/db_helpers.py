import mysql.connector
from mysql.connector import Error

class MySQLConnector():
     
    def __init__(self, config=None):
        """Inititalize a connection to a database using a configuration file"""
        if config:
            try:
                self.connection = mysql.connector.connect(host=config['host'],
                                                          database=config['database'], 
                                                          user=config['user'],
                                                          password=config['password'])
                if self.connection.is_connected():
                    self.db_Info = self.connection.get_server_info()
                    print('Connected to MySQL database... MySQL Server version on ', self.db_Info)
                
            except Error as e:
                print('Error while connecting to MySQL', e)


    def upload_table(self, df, columns, table, verbose=False):
        """Upload a Dataframe to a table on the connected database, using the columns provided
        
            df: Dataframe to upload
            columns: The columns of the database table,
            table: The table of the database where the dataframe will be uploaded
            verbose: print SQL statements
        
        """
        
        values = list(df.itertuples(index=False, name=None))

        cursor = self.connection.cursor()
        
        success_state = None
        
        count = 0
        
        for row_value in values:
            sql = "INSERT INTO " + table +' '  + str(columns).replace("'","") + " VALUES " + str(row_value) + ';'
            if verbose:
                print(sql)
            try:
                cursor.execute(sql)
                success_state = 'Execution Succesful'
            
            except Error as e:
                success_state = 'SQL Execution failed ' + str(e)
            finally:    
                count+=1
                if count % 1000 == 0:
                    print('Uploaded data point ' + str(count));
                
        print(success_state)
    
    def commit(self):
        try:
            self.connection.commit()
            print('Commit succesful')
        except Error as e:
            print('Commit Unsuccesful ', e)
        
    def close(self):
        self.connection.close()
        
