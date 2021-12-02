import sqlite3


conn = sqlite3.connect('/web/DB/database.db')
cursor = conn.cursor()

Name=input("Digite o Nome: ")
Platform=input("Digite a Plataforma: ")
Developer=input("Digite o Desenvolvedor: ")
NA_Sales=input("Digite as vendas na região NA: ")
EU_Sales=input("Digite as vendas na região EU: ")
JP_Sales=input("Digite as vendas na região JP: ")
Other_Sales=input("Digite as vendas nas outras regiões: ")
Global_Sales=input("Digite as vendas Globais: ")

cursor.execute("""INSERT INTO videogamesales
                        (Name, Platform, Developer, NA_Sales, EU_Sales, JP_Sales, Other_Sales, Global_Sales)
                VALUES(?, ?, ?, ?, ?, ?, ?, ?);""", (Name, Platform, Developer, NA_Sales, EU_Sales, JP_Sales, Other_Sales, Global_Sales))

conn.commit()

print('Dados inseridos com sucesso.')

conn.close()