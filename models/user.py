from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer,String
from config.db import meta,engine

gabetass=Table("Cajeros", meta, Column(
    "id",Integer, primary_key=True, nullable=False),
    Column("name",String(50)),
    Column("cantidadBilletes",Integer),
    Column("dineroTotal",Integer),
    Column("gabetas",Integer),
    Column("sucursal",String(255)),
    Column("idCajero",Integer),)

meta.create_all(engine)



