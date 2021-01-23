from calculator import *
from verbose import verbose

def main(verbose):


     inFile = open("form.csv", 'r')

     results = inFile.readlines()
     choice = choiceConstruction(results)
     choice = ranking(results, choice)

     choice.sort(reverse = True, key = ratingSort)

     counter = 1
     
     for titles in choice:
          print("#%d" % counter + ":", titles["title"])
          counter+=1

     print("\nWINNER:", choice[0]["title"])

     if(verbose):
          verbose()
     
     inFile.close()
          
