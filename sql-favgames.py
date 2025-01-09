from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()


# create a class-based model for the "FavGames" table
class FavGames(base):
    __tablename__ = "FavGames"
    id = Column(Integer, primary_key=True)
    game_name = Column(String)
    platform_played = Column(String)
    year_released = Column(String)
    genre = Column(String)
    main_character = Column(String)
    

# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)


# creating records on our Programmer table
super_mario_bros = FavGames(
    game_name="Super Mario Bros",
    platform_played="NES",
    year_released="1985",
    genre="Platformer",
    main_character="Mario"
)

speedball_2 = FavGames(
    game_name="Speedball 2: Brutal Deluxe",
    platform_played="Atari ST",
    year_released="1990",
    genre="Sports/Action",
    main_character="Brutal Deluxe"
)

halo_3 = FavGames(
    game_name="Halo 3",
    platform_played="Xbox 360",
    year_released="2007",
    genre="First-Person Shooter",
    main_character="Master Chief"
)

the_last_of_us = FavGames(
    game_name="The Last of Us",
    platform_played="Playstation 4",
    year_released="2013",
    genre="Action-Adventure",
    main_character="Ellie"
)

fifa_96 = FavGames(
    game_name="FIFA 96",
    platform_played="Playstation 1",
    year_released="1995",
    genre="Sports",
    main_character="Aston Villa"
)

stray = FavGames(
    game_name="Stray",
    platform_played="Xbox Series X",
    year_released="2022",
    genre="Adventure",
    main_character="B-12"
)

powerwash_simulator = FavGames(
    game_name="Powerwash Simulator",
    platform_played="Xbox Series X",
    year_released="2022",
    genre="Simulation",
    main_character="You"
)

# add each instance of our programmers to our session
# session.add(super_mario_bros)
# session.add(speedball_2)
# session.add(halo_3)
# session.add(the_last_of_us)
# session.add(fifa_96)
# session.add(stray)
# session.add(powerwash_simulator)


# commit our session to the database
# session.commit()

# updating a single record
# favgame = session.query(FavGames).filter_by(id=7).first()
# favgame.main_character = "Powerwasher"




# updating multiple records
# games = session.query(FavGames)
# for game in games:
#     if game.platform_played == "Playstation 1":
#         game.platform = "PSOne"
#     else:
#         print("Platform not defined")
#     session.commit()


# deleting a single record
# title = input("Enter a game title: ")
# favgame = session.query(FavGames).filter_by(game_name=title).first()
# defensive programming
# if favgame is not None:
#     print("Game Found: ", favgame.game_name)
#     confirmation = input("Are you sure you want to delete this record? (y/n): ")
#     if confirmation.lower() == "y":
#         session.delete(favgame)
#         session.commit()
#         print("Game has been deleted")
#     else:
#         print("Game not deleted")
# else:
#     print("No records found")


# deleting multiple records (WARNING - this will delete all records)
# favgames = session.query(FavGames)
# for favgame in favgames:
#     session.delete(favgame)
#     session.commit()
    

# query the database to find all favgames
favgames = session.query(FavGames)
for favgame in favgames:
    print(
        favgame.id,
        favgame.game_name,
        favgame.platform_played,
        favgame.year_released,
        favgame.genre,
        favgame.main_character,
        sep=" | "
    )