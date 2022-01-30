#Name: Evelyn Li
#Date: 01/29/2021

question = raw_input("Encrypt or Decrypt?: ")

if question == "Encrypt": #Encrypt a message
   message = raw_input("Encrypt this message: ")
   i = 0
   j = 1
   xlist = []
   ylist = []
   while i < len(message):
      list1 = message[i]
      i+=2
      xlist += list1 
   xlist = ''.join(xlist)
   while j < len(message):
      list2 = message[j]
      j+=2
      ylist += list2 
   ylist = ''.join(ylist)
   list = xlist + ylist
   print list

if question == "Decrypt": #Decrypt a message
   message = raw_input("Decrypt this message: ")
   if len(message) % 2 == 1:
      xlist = message[0:(len(message)/2)+1]
      ylist = message[(len(message)/2)+1:]
   if len(message) % 2 == 0:
      xlist = message[0:(len(message)/2)]
      ylist = message[(len(message)/2):]
   i = 0
   j = 0
   list = []
   while i < (len(message)/2) and j < (len(message)/2):
      xlist[i]
      list.append(xlist[i])
      i+=1
      ylist[j]
      list.append(ylist[j])
      j+=1
   list = ''.join(list)
   print list