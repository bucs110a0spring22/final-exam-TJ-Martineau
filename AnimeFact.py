import requests
import random
import json

class AnimeFact:
  def __init__(self):
    """
    Sets up the api url for getting anime facts, and creates an AnimeFact object
    """
    self.api_url = "https://anime-facts-rest-api.herokuapp.com/api/v1/"
    self.response = ""

  def fixTitle(self, anime):
    """
    Takes in a title and changes it so that it can be added to a url

    Arguments: anime (string) is the original title

    Returns the fixed title (string)
    """
    anime_temp = ""
    for letter in anime:
      if ord(letter) == 32:
        anime_temp = anime_temp + chr(95)
      elif ord(letter) < 91:
        anime_temp = anime_temp + chr(ord(letter) + 32)
      else:
        anime_temp = anime_temp + letter
        
    return anime_temp
    
  def get(self, anime):
    """
    Asks the api for a fact given an anime. If it fails, get a fact about Full Metal Alchemist

    Arguments: anime (string) is the anime title

    Returns either a fact about the given anime or a fact about Full Metal Alchemist
    """
    title = self.fixTitle(anime)
    
    if requests.get(self.api_url + title):
      response = requests.get(self.api_url + title)
      success = True
    else:
      response = requests.get(self.api_url + "fma_brotherhood")
      success = False

    data = response.text
    content = json.loads(data)
    fact = content['data'][0]

    if success:
      fact = "One fact about this anime: " + fact['fact']
    else:
      fact = "Couldn't find facts about this anime, but did you know that "+ fact['fact']
      
    return fact

  def __str__(self):
    return "AnimeFact"