import sqlalchemy as sa

engine = sa.create_engine("mysql+mysqldb://root:root@127.0.0.1:3307/gonextjob")
conn = engine.connect()
result = conn.execute("select * from users")
for row in result:
    print("row:" + row["username"])
conn.close()

def create_flights_table():
    pass