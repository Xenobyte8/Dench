import pandas as pd
from sqlalchemy import create_engine, text
engine = create_engine("sqlite:///data/database.db", echo=True)


with engine.begin() as conn:
    query = text("""SELECT * FROM player""")
    df = pd.read_sql_query(query, conn)
    print(df)