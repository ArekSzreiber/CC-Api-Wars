import requests

root = "https://swapi.co/api/"
planets_header = [
        "Name",
        "Diameter",
        "Climate",
        "Terrain",
        "Surface Water Percentage",
        "Population",
        "Residents",
    ]


def get_elements(type="planets", page="1"):
    response = requests.get(root + type + "/?page="+page)
    return response.json()


def get_planets(url="https://swapi.co/api/planets/?page=1"):
    response = requests.get(url)
    return response.json()
