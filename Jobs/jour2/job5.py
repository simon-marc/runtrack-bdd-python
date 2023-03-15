import mysql.connector


config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'LaPlateforme',

}

cnx = mysql.connector.connect(**config)
cnx.connect()

cursorSel = cnx.cursor()
selectionAction = ("SELECT SUM(superficie) FROM etage")

cursorSel.execute(selectionAction)
req = cursorSel.fetchone()

print(f"La superficie de la Plateforme est de {req[0]} m2")

cursorSel.close()
