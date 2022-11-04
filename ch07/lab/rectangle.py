
class Rectangle:
  def __init__(self,x,y,h,w):
    self.x = x
    self.y = y
    self.height = h
    self.width = w
    if (self.x < 0):
      self.x =0
    if (self.y < 0):
      self.y = 0
    if (self.height < 0):
       self.height = 0
    if (self.width < 0):
      self.width = 0
  def __str__(self):
    result_str = f"{self.x}[{self.y}]"
    result_str += f"\nheight:{self.height}"
    result_str += f"\nwidth:{self.width}"
    return result_str