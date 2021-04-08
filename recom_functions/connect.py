import psycopg2

def connection(database:str="huwebshop",ww:str="admin"):
    con = psycopg2.connect(
        host="localhost",
        database=database,
        user="postgres",
        password=ww,
    )
    cur = con.cursor()
    return con,cur