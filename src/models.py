import os
import sys
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
from sqlalchemy import create_engine, String, ForeignKey
from eralchemy2 import render_er

Base = declarative_base()

class Pokedex(Base):
    __tablename__ = 'pokedex'

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column()
    numero: Mapped[int] = mapped_column()
    tipo: Mapped[str] = mapped_column()

class Evolucion(Base):
    __tablename__ = 'evolucion'

    id: Mapped[int] = mapped_column(primary_key=True)
    nameEvo: Mapped[str] = mapped_column()
    evolucion1: Mapped[str] = mapped_column()
    evolucion2: Mapped[str] = mapped_column()
    evolucion3: Mapped[str] = mapped_column()
    pokemon_id:Mapped[int]=mapped_column(ForeignKey('pokedex.id'))

class Ataque(Base):
    __tablename__ = 'ataque'

    id: Mapped[int] = mapped_column(primary_key=True)
    defensa:Mapped[str] = mapped_column()
    velocidad: Mapped[int] = mapped_column()
    ataque_especial:Mapped[str] = mapped_column()
    poke_id: Mapped[int]=mapped_column(ForeignKey('pokedex.id'))
    evolucion: Mapped[int]=mapped_column(ForeignKey('evolucion.id'))

class Debilidad(Base):
    __tablename__= 'debilidad'

    id:Mapped[int] = mapped_column(primary_key=True)
    devilidad1:Mapped[str] = mapped_column()
    devilidad2:Mapped[str] = mapped_column()
    devilidad3:Mapped[str] = mapped_column()

class Caracteristica(Base):
    __tablename__ = 'caracteristica'

    id: Mapped[int]=mapped_column(primary_key=True)
    altura: Mapped[int] = mapped_column()
    peso:Mapped[int] = mapped_column()
    sexo: Mapped[str] = mapped_column()
    habilidad:Mapped[str] = mapped_column()
    devilidad:Mapped[int] = mapped_column(ForeignKey('debilidad.id'))
    pokemon:Mapped[int] = mapped_column(ForeignKey('pokedex.id'))
    evo_id:Mapped[int] = mapped_column(ForeignKey('evolucion.id'))



## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
