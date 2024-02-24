import sqlalchemy

db_url = 'postgresql://hackerboy:2dEi7eG8ltppoLSiIrZk@localhost:5432/bets'
engine = sqlalchemy.create_engine(db_url, echo=True)

with engine.connect() as conn:
    result = conn.execute(sqlalchemy.text("select 'hello world'"))
    print(result.all())