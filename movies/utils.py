import requests
from django.conf import settings


def get_movie_from_api(title):
    url = f"http://www.omdbapi.com/?t={title}&apikey={settings.OMDBAPI_KEY}"
    res = requests.get(url)
    if res.status_code != 200:
        raise LookupError("Wrong answer from external API")

    data = res.json()
    if data.pop("Response") == "True":
        return {key.lower(): value for key, value in data.items()}
    raise LookupError("Movie with this title not found")
