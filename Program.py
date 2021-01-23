from calculator import *

class Program:

     def __init__(self, verbose = None):
          self.v = verbose

     def main(self):

          choice, numResponses = choiceConstruction()
          choice.sort(reverse = True, key = ratingSort)

          counter = 1
          
          for titles in choice:
               print("#%d" % counter + ":", titles["title"])
               counter+=1

          print("\nMOST PREFERRED:", choice[0]["title"])

          peram = (self.v).lower()

          if(peram == "-v" or peram == "--verbose"):
               verbose(choice, numResponses)
