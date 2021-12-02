from sqlite3.dbapi2 import Cursor

Cursor.execute("""CREATE TABLE IF NOT EXISTS videogamesales (
            id INT(11) PRIMARY KEY,
            Name VARCHAR(255),
            Platform VARCHAR(255),
            Developer VARCHAR(255),
            NA_Sales INT(255),
            EU_Sales INT(255),
            JP_Sales INT(255),
            Other_Sales INT(255),
            Global_Sales INT(255)
        );""")