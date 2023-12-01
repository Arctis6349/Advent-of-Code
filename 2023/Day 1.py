Number = 0
Words = ""
Word_List = []
Word = []
list = []
Total = 0

Dict = {"one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9"}

with open("input.txt","r") as file:
  list = file.readlines()
  
  for item in list:
    i = 0
    while i < len(item):
  
      char = item[i]
      count = i
      if char.isdigit():
         Word.append(int(char))
         i += 1
         continue


      if char == "o" or char == "t" or char == "s":
        try:  
          Words = item[count:count + 3]
        

          Word.append(int(Dict[Words]))
          i += 3
          continue 
        
        except:
          print()
      
      if char == "f" or char == "n":
        try:
          Words = item[count:count + 4]
          Word.append(int(Dict[Words]))
          i += 4
          continue
        except:
          print("")

      
      if char == "s" or char == "e" or char == "t":
       try:
        Words = item[count:count + 5]
        Word.append(int(Dict[Words]))
        i += 5
        continue
       except:
        print("")

      i += 1
    if Word:
      Number = Word[0]*10 + Word[len(Word) -1]
      print(Number)
      Total += Number
      
      Word.clear()
    

print(Total)

