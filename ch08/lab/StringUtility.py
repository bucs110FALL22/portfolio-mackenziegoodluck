class StringUtility:
  def __init__(self,string):
    self.string = string
  def __str__(self):
    return self.string
  def vowels(self):
    vowelCount = 0
    vowels = self.string
  
    for i in vowels:
      if(i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
        vowelCount +=1
      if (vowelCount >= 5):
        return "many"
    return str(vowelCount)
  def bothEnds(self):
    if (len(self.string) <= 2):
      return ""
    else:
      return self.string[:2]+self.string[-2:]
  
  def fixStart(self):
    if (len(self.string) <=1):
      return ""
    else:
      return self.string[0]+self.string[1:].replace(self.string[0],'*')
    
  def asciiSum(self):
    sum = 0
    for i in self.string:
     sum += ord(i)
    return sum
  def cipher(self):
    cipher = ""
    data = (len(self.string))
    for i in self.string:
      if (i.isupper()):
        cipher += chr((ord(i) + data - 65) % 26 + 65)
      elif (i.islower()):
        cipher += chr((ord(i) + data - 97) % 26 + 97)
      else:
        cipher += i
    
  
    return cipher
        