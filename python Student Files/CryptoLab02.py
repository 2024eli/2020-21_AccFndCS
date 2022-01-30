#Name: Evelyn Li
#Date: 02/03/2021 
  
# Dictionary to lookup the index of alphabets (I found this idea online and decided
# to implement the dictionary)
dictionary1 = {'A' : 1, 'B' : 2, 'C' : 3, 'D' : 4, 'E' : 5, 
        'F' : 6, 'G' : 7, 'H' : 8, 'I' : 9, 'J' : 10, 
        'K' : 11, 'L' : 12, 'M' : 13, 'N' : 14, 'O' : 15, 
        'P' : 16, 'Q' : 17, 'R' : 18, 'S' : 19, 'T' : 20, 
        'U' : 21, 'V' : 22, 'W' : 23, 'X' : 24, 'Y' : 25, 'Z' : 26} 
  
dictionary2 = {0 : 'Z', 1 : 'A', 2 : 'B', 3 : 'C', 4 : 'D', 5 : 'E', 
        6 : 'F', 7 : 'G', 8 : 'H', 9 : 'I', 10 : 'J', 
        11 : 'K', 12 : 'L', 13 : 'M', 14 : 'N', 15 : 'O', 
        16 : 'P', 17 : 'Q', 18 : 'R', 19 : 'S', 20 : 'T', 
        21 : 'U', 22 : 'V', 23 : 'W', 24 : 'X', 25 : 'Y'} 
  
def encrypt(plainText, num): 
   cipher = ""
   for ctLetter in message: 
      # checks if in dictionary or not 
      if ctLetter.isalpha(): 
         num = ( dictionary1[ctLetter] + num ) % 26
         cipher += dictionary2[num] 
      else:
         cipher += ctLetter
   return cipher
    
def decrypt(cipherText, num): 
   decipher = "" 
   for ptLetter in message: 
      # checks if in dictionary or not 
      if ptLetter.isalpha(): 
         num = ( dictionary1[ptLetter] - num + 26) % 26
         decipher += dictionary2[num] 
      else:
         decipher += ptLetter
   return decipher 
  
def main(): 
   question = raw_input("Encrypt or Decrypt?: ") 
   if question == "Encrypt": #Encrypt a message
      plainText = raw_input("Encrypt: ")
      num = 13
      cipherText = encrypt(message.upper(), num) 
      print (cipherText) 
      
   if question == "Decrypt": #Decrypt a message
      cipherText = raw_input("Decrypt: ")
      num = 13
      plainText = decrypt(message.upper(), num) 
      print (plainText) 
   # Friendly note that Encrypt and Decrypt are practically the same thing
   # but it's cool to separate the two functions to make it more usable to the public!

# Executes the main function 
if __name__ == '__main__': 
    main() 