from sqlalchemy import create_engine,Table,Column,String,MetaData
en="mysql://dipo:dipo@localhost/dipo"
engine=create_engine(en,echo=True)
metadata=MetaData()
essential_info=Table("webpage_info",metadata,Column("name",String(1000)),Column("desc",String(1000)),Column("link",String(1000)))
metadata.create_all(engine)
