import requests


def get_motivational_quote():
    response = requests.get("https://zenquotes.io/api/random")
    data = response.json()
    motivational_quote = data[0]['q'] if not data[0]['q'].startswith("Too") else ""
    return motivational_quote
