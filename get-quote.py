import random, sys

def primary():
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = len(quotes) - 1  # last variable to update automatically
  rnd = random.randint(0, last)
  rndm = random.randint(0, last)
  
  # print()
  # print(quotes[rnd], end=''),
  # print(quotes[rndm], end='')
  print()
  sys.stdout.write(quotes[rnd])
  sys.stdout.write(quotes[rndm]) 
  print()
 
if __name__== "__main__":
  primary()
