#Name: Evelyn Li
#Date: 02/05/2021

#not using code for spaces
def undoVig(keyLetter, ctLetter):
   dict1 = {'A' : 0, 'B' : 1, 'C' : 2, 'D' : 3, 'E' : 4, 
        'F' : 5, 'G' : 6, 'H' : 7, 'I' : 8, 'J' : 9, 
        'K' : 10, 'L' : 11, 'M' : 12, 'N' : 13, 'O' : 14, 
        'P' : 15, 'Q' : 16, 'R' : 17, 'S' : 18, 'T' : 19, 
        'U' : 20, 'V' : 21, 'W' : 22, 'X' : 23, 'Y' : 24, 'Z' : 25}
   dict2 = {0 : 'A', 1 : 'B', 2 : 'C', 3 : 'D', 4 : 'E', 
        5 : 'F', 6 : 'G', 7 : 'H', 8 : 'I', 9 : 'J', 
        10 : 'K', 11 : 'L', 12 : 'M', 13 : 'N', 14 : 'O', 
        15 : 'P', 16 : 'Q', 17 : 'R', 18 : 'S', 19 : 'T', 
        20 : 'U', 21 : 'V', 22 : 'W', 23 : 'X', 24 : 'Y', 25: 'Z'}
   if ctLetter.isalpha():
      i = dict1[keyLetter]
      j = dict1[ctLetter]
      k = j - i
      if k < 0: 
         k = k + 26
         ptLetter = dict2[k]
      else:
         ptLetter = dict2[k]
   else: 
      ptLetter = ctLetter
   return ptLetter

def decryptVignere(key, cipherText):
   plainText = ""
   keyLen = len(key)
   i = 0
   for j in range (len(cipherText)): 
      if i > (len(key)-1):
         i = 0
      ptLetter = undoVig(key[i], cipherText[j])
      if ptLetter.isalpha():
         plainText += ptLetter
         i+=1
         j+=1 
      elif ptLetter == ' ':
         plainText += ptLetter
   return plainText

def main():
   key = "DAVINCI"
   cipherText = raw_input("Decrypt: ")
   result = decryptVignere(key, cipherText)
   print result
      
# Executes the main function 
if __name__ == '__main__': 
    main() 