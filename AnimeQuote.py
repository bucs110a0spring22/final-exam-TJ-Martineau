import requests
import json

class AnimeQuote:
  def __init__(self):
    """
    Sets up the api url to get anime quotes
    """
    self.api_url = 'https://animechan.vercel.app/api/random'

  def get(self, arg):
    """
    Calls the api to gather anime quote data

    arg: specifies the information needed from the quote data (string)

    Returns the specified content from the api
    """
    response = requests.get(self.api_url)
    data = response.text
    content = json.loads(data)
    return content[arg]

  def __str__(self):
    return "AnimeQuote"


  