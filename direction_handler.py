import googlemaps
car_handler = googlemaps.Client("AIzaSyAH3qRKfcvNK-Jv3BFj3Rm2ggs91ElQOjE")


def get_direction_json(lat, longt, dlat, dlongt):
    path = car_handler.directions((lat, longt),(dlat, dlongt))
    print(type(path))
    return  path
