class BatchRecord:
    connection = None
    def __init__(self, connection): 
        self.connection = connection

    def close(self):
        self.connection.close()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    def deleteTable(self):
        self.connection.reconnect()
        cursor = self.connection.cursor()
        cursor.execute("""
            drop table if exists Batch_Records
                """)
        self.connection.commit()

    def createBatchRecordTable(self):
        self.connection.reconnect()
        cursor = self.connection.cursor()
        cursor.execute("""
            create table if not exists Batch_Records (
                    id int not null auto_increment,
                    batch_id int not null,
                    qty double not null,
                    division text not null,
                    log_date date not null,
                    notes text,
                    operator text not null,
                    constraint PK_Batch_Records primary key (id)
                )""")
        self.connection.commit()

    def insertBatchRecord(self, batch_id, qty, division, log_date, notes, operator):
        self.connection.reconnect()
        cursor = self.connection.cursor()
        cursor.execute("insert into Batch_Records (batch_id, qty, division, log_date, notes, operator) values (%s, %s, %s, %s, %s, %s)", (batch_id, qty, division, log_date, notes, operator))

        self.connection.commit()

        return cursor.rowcount == 1

    def getBatchRecord(self, batch_id):
        self.connection.reconnect()
        cursor = self.connection.cursor()
        cursor.execute("SELECT qty, division, DATE_FORMAT(log_date, '%d/%m/%Y') AS formatted_log_date, notes, operator FROM Batch_Records WHERE batch_id = %s", (batch_id,))
        return cursor.fetchall()
