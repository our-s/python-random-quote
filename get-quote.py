import random

def primary():
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  # last = 13
  last = len(quotes) - 1  # last variable to update automatically
  rnd = random.randint(0, last)
  print(quotes[rnd])

if __name__== "__main__":
  primary()
