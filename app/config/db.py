from sqlalchemy import create_engine,MetaData

engine = create_engine("mysql+pymysql://root:123456@localhost:3306/dbsql",
            pool_recycle=3600, echo=True)

meta = MetaData()
conn = engine.connect()