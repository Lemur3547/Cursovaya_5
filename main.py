from src.classes import DBManager

Db = DBManager('localhost', 'Cursovaya_4', 'postgres', 'Emik2507')
Db.create_tables()
Db.fill_db('Python')
