def choiceConstruction(results):

     choice = []

     for lines in range(1, len(results)):
          
          line = (results[lines].rstrip("\n")).split(",")
          
     for choices in range(1,len(line)):
            
          tempDict = {
               "title": line[choices],
               "rating": 0
               }
          
          choice.insert(0, tempDict)

     return choice

def ranking(results, choice):

     for lines in range(1, len(results)): # iterating over each response
          
          line = (results[lines].rstrip("\n")).split(",")
          
          for choices in range(1,len(line)): # iterating over each element of response (titles of choices)

               currentTitle = line[choices]

               for title in choice: # iterating over each choice (dict)
                    
                    if title["title"] == currentTitle:
                        title["rating"] += choices

     return choice

def ratingSort(dicts):
     return dicts['rating']


def main():


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
          

main()