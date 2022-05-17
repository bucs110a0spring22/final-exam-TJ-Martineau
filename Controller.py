import AnimeQuote
import AnimeFact

class Controller:
  def __init__(self):
    """
    Creates a session of the program
    """
    self.state = "RUNNING"
    self.stories = ""

  def GenerateText(self):
    """
    Generates text to be displayed on screen
    """
    self.text = ""

    anime_quote = AnimeQuote.AnimeQuote()
    anime_fact = AnimeFact.AnimeFact()

    fact = anime_fact.get(anime_quote.get('anime'))
    quote = anime_quote.get('quote')

    text = quote + '\n' + fact

    self.text = self.text + text
  
  def ProgramLoop(self):
    """
    The program loop that goes on until the user enters quit
    """
    while self.state == "RUNNING":
      self.input = input("Enter quit to quit, otherwise enter any key to continue: ")
      if self.input == "quit":
        self.state = "DONE"
      else:
        self.GenerateText()
        print(self.text)

    if self.state == "DONE":
      quit()


