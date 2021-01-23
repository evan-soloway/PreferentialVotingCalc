
  
def choiceConstruction():
     
     choice = []

     inFile = open("form.csv", 'r')
     results = inFile.readlines()

     for lines in range(1, len(results)): # iterating over each response
          
          line = (results[lines].rstrip("\n")).split(",")
          
     for choices in range(1,len(line)):
            
          tempDict = {
               "title": line[choices],
               "rating": 0
               }
          
          choice.insert(0, tempDict)

     choice = ranking(results, choice)

     return choice, len(results)-1;

def ranking(results, choice): # cannot be called before choiceConstruction

     for lines in range(1, len(results)): # iterating over each response
          
          line = (results[lines].rstrip("\n")).split(",")
          
          for choices in range(1,len(line)): # iterating over each element of response (titles of choices)

               currentTitle = line[choices]

               for title in choice: # iterating over each choice (dict)
                    
                    if title["title"] == currentTitle:
                        title["rating"] += choices

     return choice
     
def verbose(choice, numResponses):

     print()# newline
     
     for titles in choice:
          print(titles["title"], "received", titles["rating"], "points")

     print("\n" + "There were", numResponses, "responses")

def ratingSort(dicts):
     return dicts['rating']
