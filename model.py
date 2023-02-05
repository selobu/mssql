__all__ = ['Base']

from config import map_name_to_table
from datetime import datetime
from typing import Optional

from sqlalchemy import ForeignKey
from sqlalchemy import func
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class Base(DeclarativeBase):
    pass

@map_name_to_table
class Vehiculo(Base):
    __tablename__ = 'vehiculo'
    idVehiculo: Mapped[int] = mapped_column(Integer, primary_key=True)
    nombre: Mapped[str] = mapped_column(String(200))
    user_id = mapped_column(ForeignKey("persona.id"))
    persona: Mapped["Persona"] = relationship(back_populates="vehiculo")

@map_name_to_table
class Persona(Base):
    __tablename__ = 'persona'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    FirstName: Mapped[str] = mapped_column(String(200))
    LastName: Mapped[str] = mapped_column(String(200))
    vehiculo: Mapped[list["Vehiculo"]] = relationship(back_populates="persona")
   
   
if False:


    @map_name_to_table
    class Address(Base):
        __tablename__ = "address"

        id = mapped_column(Integer, primary_key=True)
        user_id = mapped_column(ForeignKey("user.id"))
        email_address: Mapped[str] = mapped_column(String(120))

        user: Mapped["User"] = relationship(back_populates="addresses")

        def __repr__(self) -> str:
            return f'Address({self.id}, {self.user_id}, {self.email_address})'

    @map_name_to_table
    class User(Base):
        __tablename__ = "user"

        id: Mapped[int] = mapped_column(Integer, primary_key=True)
        name: Mapped[str]
        fullname: Mapped[Optional[str]]
        nickname: Mapped[Optional[str]] = mapped_column(String(100))
        create_date: Mapped[datetime] = mapped_column(insert_default=func.now())

        addresses: Mapped[list["Address"]] = relationship(back_populates="user")
        def __repr__(self) -> str:
            return f'User({self.id}, {self.name}, {self.fullname}, {self.create_date})'