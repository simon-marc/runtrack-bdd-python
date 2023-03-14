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
selectionAction = ("SELECT nom, capacite FROM salle")

cursorSel.execute(selectionAction)
req = cursorSel.fetchall()

print(req)

cursorSel.close()
