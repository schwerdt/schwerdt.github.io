def decode():

  #A Python3 code 

  #For the Prairie Fest Medallion Hunt, we searched for clues around town.  Each clue provided several
  #numbers.  The numbers were a code for the name of a park where the medallion was hidden.
  #There were 5 clues, but we only found 3 of them.  For that reason, we only have a partial list
  #of numbers in the code (which is in masternums).  It seems that the numbers are to be converted
  #to letters via the keypad on a phone.  This code takes a list of all parks in the district, converts
  #them into their number equivalent and compares that number list to the numbers we do have (in
  #masternums).  Because we don't have all the numbers in the code, there may be extra numbers, but the
  #important thing is that possible solutions at least contain all the numbers we do have!
 
  #Make a dictionary to convert letters to numbers based on the phone keypad.
  phonedict = {'a':2,'b':2,'c':2, 'd':3,'e':3,'f':3, 'g':4,'h':4,'i':4, 'j':5, 'k':5,'l':5, 'm':6,'n':6,'o':6, 'p':7,'q':7,'r':7,'s':7, 't':8,'u':8,'v':8,'w':9,'x':9,'y':9,'z':9}
 
  #These are the numbers that I know are present in the list of numbers.
  #I am missing some numbers because we don't have all the clues.
  masternums = [6,7,4,6,2,7,2,3,6]
 
  #open the file with the name of the parks.  
  with open('parks') as f:
    content = f.readlines()
 
  for m in content:
    numarray = []; #stores the numbers obtained from converting text
    flag = 0
    #m is each entry in content.  remove any \n \t from entry
    m = m.strip()
    #convert to lowercase
    m = m.lower()
    #Break into a list of characters
    allchar = list(m)
    for piece in allchar:
      if piece in phonedict.keys(): #Check if the character is in the dictionary
        n = phonedict[piece]  #Convert letter to number
        numarray.append(n)  #Append the number to the list of numbers
    #Check to see if this numarray has all the same numbers as ours (there may be extras)
    for k in masternums: #Loop over known numbers
      if k in numarray:  #Check if it is in my list for the current park
        numarray.remove(k)  #Remove the number in the master list from the one associated with this park
      else:
        flag = 1  #If the number in the masternums is not present in this park's list, it cannot be a solution.
        break     #Set the flag to 1 to indicate this park is not a possibility.
    if flag == 0:
      print(m, ' is a possible solution')
      print('remaining numbers',numarray,'\n')
     
        

        
   
      



    
