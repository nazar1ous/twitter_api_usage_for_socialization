
from __future__ import print_function
import twitter
import geocoder
import folium


def get_users_from_screen_name(screen_name: str) -> object:
    """
    :param screen_name: user's id of account
    :return: users object with their location inside and other features
    """
    CONSUMER_KEY = "teBhfDcfcysTGgmJfmB6VJisw"
    CONSUMER_SECRET = "3gipTPBbsvNB7In294RMISGKP6oASfpjlHiWCzyyeTUskUI0cy"
    ACCESS_TOKEN = "840484607392915457-e9qearc2z8r1bOd88nI4lsYad38Wl8f"
    ACCESS_TOKEN_SECRET = "43PcVh7tLrLHueFiOBAveemYPV76OSAv5zoldE4J6r2xE"

    api = twitter.Api(consumer_key=CONSUMER_KEY,
                      consumer_secret=CONSUMER_SECRET,
                      access_token_key=ACCESS_TOKEN,
                      access_token_secret=ACCESS_TOKEN_SECRET)

    users = api.GetFriends(screen_name=screen_name)
    return users


def get_coordinates_from_location(location: str) -> list:
    """
    Return coordinates from location
    :param location: user's location in str
    :return: list of coordinates([latitude, longitude])

    >>> get_coordinates_from_location("Arena Lviv Lviv Ukraine")
    [49.8055205, 23.973569165549602]
    """
    g = geocoder.osm(location)
    return g.latlng


def get_coordinates_from_users_data(users: object) -> dict:
    """
    Return data with coordinates of each user
    :param users: object
    :return: dict with a key as a coord and value is a list of names
    """
    detailed_location = {}
    for user in users:
        coordinates = get_coordinates_from_location(user.location)
        if coordinates:
            coordinates = tuple(coordinates)
            if coordinates not in detailed_location:
                detailed_location[coordinates] = [user.name]
            else:
                detailed_location[coordinates].append(user.name)
    return detailed_location


def create_web_map_from_user_friends_location(screen_name: str,
                                              name_of_file: str):
    """
    Create web map from users friends location
    :param screen_name: id of user's twitter account
    :param name_of_file: name of html file
    :return: html file
    """
    map = folium.Map(location=[49.841952, 24.0315921], zoom_start=6)
    main_layer = folium.FeatureGroup(name="Twitter friends locations")
    users_coordinates = get_coordinates_from_users_data(
        get_users_from_screen_name(screen_name))
    for coord in users_coordinates:
        users_names = users_coordinates[coord]
        text = "List of friends with this location: {}"\
            .format(','.join(users_names))
        main_layer.add_child(folium.Marker(location=coord,
                                           popup=text,
                                           color='green',
                                           icon=folium.Icon()))
    map.add_child(main_layer)
    map.save(name_of_file)


if __name__ == "__main__":
    create_web_map_from_user_friends_location('nazariy_kuspys', 'new1_one.html')
