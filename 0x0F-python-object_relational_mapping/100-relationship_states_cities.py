#!/usr/bin/python3
"""creates the State “California” with the City “San Francisco”
"""

import sqlalchemy
import sys
from relationship_city import City
from relationship_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           username, password, database))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    sesh = Session()

    add = State(name="California")
    add.cities = [City(name="San Francisco")]

    sesh.add(add)
    sesh.commit()

    sesh.close()
