import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="tokaido.proxy.rlwy.net",
        port=36470,
        user="root",
        password="EkEmFVwYTMPjKHBqOGbvHlrGROWhpMDo",
        database="railway"
    )
