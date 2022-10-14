import pygame
import random

#Part A
def threenp1(n):
  count = 0
  while n != 1:
    if (n%2) == 0:
     n = n//2
    else:
     n = (n * 3)+ 1
    count +=1
  
  return count


pygame.init()
display = pygame.display.set_mode()
font = pygame.font.Font(None, 5)


n = 101
sequence = {} #dictionary 
print(sequence)
max_so_far = 0
max_val = 20
upper_limit = 20
e= 8 
pygame.font.init()
font = pygame.font.Font(None,100)
for n in range(2,upper_limit + 1, 1):
   display.fill("White")
   count = threenp1(n)
   sequence[n*e] = count*e
   coordinates = list(sequence.items())
print(coordinates)
for value in range(2, upper_limit + 1):
  display.fill("white")
  count = 0
  n = value
  if(len(coordinates) > 1):
   pygame.draw.lines(display, "Pink", False, (coordinates ))
   display.blit(pygame.transform.flip(display,False,True),(0,0))
  
  if count < max_so_far:
   count = max_so_far
   print(count)#count = 2 if i=2
     
word = "The greatest values is "+ str(max_val)
msg = font.render(word,True, "Blue")
display.blit(msg, (10,10))
pygame.time.wait(1000)
pygame.display.flip()
print(sequence)

pygame.time.wait(1000)

 
