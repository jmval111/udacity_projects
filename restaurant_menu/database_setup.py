import sys

from sqlalchemy import Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

Base = declarative_base()

# end of SQLAlchemy configuration #



class Restaurant(Base):

    __tablename__ = 'restaurant'

    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)

    @property
    def Serialize(self):
        # create a JSON style object for an API endpoint
        return {
            'name': self.name,
            'id': self.id
        }




class MenuItem(Base):

    __tablename__ = 'menu_item'

    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    course = Column(String(250))
    description = Column(String(250))
    price = Column(String(8))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)

    @property
    def Serialize(self):
        # create a JSON style object for an API endpoint
        return {
            'name': self.name,
            'id': self.id,
            'course': self.course,
            'description': self.description,
            'price': self.price,
        }


engine = create_engine('sqlite:///restaurantmenu.db')

Base.metadata.create_all(engine)
