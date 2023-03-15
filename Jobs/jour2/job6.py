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
selectionAction = ("SELECT SUM(capacite) FROM salle")

cursorSel.execute(selectionAction)
req = cursorSel.fetchall()

print(f"La capacité de toutes les salles est de {req[0][0]} personnes")

cursorSel.close()
