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


def get_planets(page=1):
    url = "https://swapi.co/api/planets/?page="
    if page is None:
        page = "1"
    response = requests.get(url+str(page))
    return response.json()


def get_page_nr(page_url):
    if page_url is not None:
        return page_url[-1:]
    return None
