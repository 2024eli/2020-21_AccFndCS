#Name: Evelyn Li
#Date: 02/10/2021

otp = """QFGWERTYPASDLZKBNMHJUIOXCV
WERNDLZKBOXCVQTSYPJUIAFGMH
FGLZKEPASRQTUIMXYBWDNCVOHJ
TLSDHOQFGWKBZYPAXNMERCVJUI
IOXCZVQFGYPDBNMLKWERTHJASU
HJUFAOXPQGWEMITYDLZKBNCVRS
QUIOXFDLZKBNMHERTYPAJCGWSV
VMPIYSDLAHJUCQFGWEZKBNRTOX
NMHJUIOASRTYPKBXDLZECVQFGW
GQEFWRTYULZKBICVPASJDOXNMH
MHJUQTYPGOWLASDZFBNIXCVERK
YPASDLZRKQFGOWEHJBXIMCUTNV
ERHPALIVQFXCGWZJOUTYDKBSNM
BYIASXDLZOQFGWHJNMRTUEPKCV
CLDHRTFGIQYPEOSWJABNMUVXZK"""

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

def splitOtp(otp, line): 
   lines = otp.splitlines()
   letters=[]
   line_num= 0
   for line in lines:
      letters.append(line[line_num])
      line_num = line_num+1
   letters = ''.join(letters)
   return letters

def encryptLetter(lines, ptLetter, num):
   otpLetter = lines[num]
   i = dict1[otpLetter]
   j = dict1[ptLetter]
   k = i + j
   if k > 26:
      k = k - 26
      ctLetter = dict2[k]
   else:
      ctLetter = dict2[k]
   return ctLetter

def encrypt(plainText, otp):
   ptLen = len(plainText)
   cipherText = ""
   j = 1
   for i in range(ptLen):
      if (j-1) % 5 == 0 and cipherText != "":
         cipherText += " " 
         #these three lines are the same as the else portion
         letter = splitOtp(otp, i)
         ctLetter = encryptLetter(letter, plainText[i], i)
         cipherText += ctLetter
      else:
         letter = splitOtp(otp, i)
         ctLetter = encryptLetter(letter, plainText[i], i)
         cipherText += ctLetter
      j+=1
   return cipherText

def main(): 
   message = raw_input("Encrypt: ")
   plainText = message.replace(" ", "") 
   cipherText = encrypt(plainText.upper(), otp)
   print cipherText

if __name__ == "__main__":
    main()