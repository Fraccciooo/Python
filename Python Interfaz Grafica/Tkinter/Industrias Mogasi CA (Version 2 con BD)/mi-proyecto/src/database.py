from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Venta(Base):
    __tablename__ = 'ventas'
    id = Column(Integer, Sequence('venta_id_seq'), primary_key=True)
    numero_factura = Column(String(50), nullable=False)
    sucursal = Column(String(100), nullable=False)

DATABASE_URL = "sqlite:///mi_base_de_datos.db"  # Cambiar según la base de datos utilizada

def init_db():
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)
    return sessionmaker(bind=engine)()

def agregar_venta(session, numero_factura, sucursal):
    nueva_venta = Venta(numero_factura=numero_factura, sucursal=sucursal)
    session.add(nueva_venta)
    session.commit()

def obtener_ventas(session):
    return session.query(Venta).all()

def actualizar_venta(session, venta_id, numero_factura, sucursal):
    venta = session.query(Venta).filter(Venta.id == venta_id).first()
    if venta:
        venta.numero_factura = numero_factura
        venta.sucursal = sucursal
        session.commit()

def eliminar_venta(session, venta_id):
    venta = session.query(Venta).filter(Venta.id == venta_id).first()
    if venta:
        session.delete(venta)
        session.commit()