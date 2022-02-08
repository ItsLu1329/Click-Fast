
#created by Lu(Brenden) bachert
from graphics import *
import math
from math import sqrt

# ================= draw =================

def drawCircle(win, x, y, r, outline, fill, width):
  shape = Circle(Point(x,y), r)
  shape.setOutline(outline)
  shape.setFill(fill)
  shape.setWidth(width)
  shape.draw(win)
  return shape
  

def drawRectangle(win, startX, startY, outline, fill, endX, endY):
  shape = Rectangle(Point(startX,startY), Point(startX+endX,startY+endY))
  shape.setOutline(outline)
  shape.setFill(fill)
  shape.draw(win)
  return shape


def drawoval(win, startX, startY, outline, fill, size1, size2):
  p = win.getMouse()
  shapestart = Point(x,y)
  shapeend = Point(x + 50, y + 30)
  shape = Oval(shapestart,shapeend) 
  shape.setOutline(outline)
  shape.setFill(fill)
  shape.draw(win)
  return shape


def windowtext(win, x, y, text, color): #ADDED COLOR OF TEXT (1/12/22, 12:03)
    t = Text(Point(x,y), text)
    t.setOutline(color)

    t.draw(win)
    
    return t

def fancytext(textobj, font, size, texttype): #normal, bold, italic, bold italic
  textobj.setSize(size)
  textobj.setFace(font)
  textobj.setStyle(texttype)
  
'''


  try:
    
    if type(textobj) == 'list':
      
      for textobj in objlist:
        try:
          textobj.setSize(size)
          textobj.setFace(font)
          print('fancying')
        except:
          pass
        
    else:
      textobj.setSize(size)
      textobj.setFace(font)
      
  except:
    pass

'''

def drawmany(win, drawlist):
  for drawitem in drawlist:
    try:
      drawitem.draw(win)
    except:
      pass

#===================== checking if drawn shapes are clicked on (t/f) =================


def isClickedCircle(circle, point): # not made by me

  center = circle.getCenter()

  distance = ((point.getX() - center.getX()) ** 2 + (point.getY() - center.getY()) ** 2) ** 0.5

  return distance < circle.radius
  
  
def isClickedRectangle(rectangle, point):
  
  #if mouseX > rectangleX or mouseY > rectangleY:
  #  return True
  #else:
  #  return False
  '''
  center = rectangle.getCenter()

  distance = ((point.getX() - center.getX()) ** 2 + (point.getY() - center.getY()) ** 2) ** 0.5

  return distance < rectangle.radius
  '''
  print('isClickedRectangle is not currently working')
  return False
# ================== premade function groups ==========================================


  
  
  
# ============================ fun/random ===================


def bullseye(win, x, y, r, colorlist):
  subr = r * 0.2
  for color in colorlist:
    drawCircle(win, x, y, r, color)
    r = r - subr
    
    
    
    
    
# ============================= deleteing drawn objects =========================


def deleteddrawn(drawnlist):
  try:
    for drawn in drawnlist:
      drawn.undraw()
  except:
    try:
      drawnlist.undraw()
    except:
      print(f'error: {drawn} not undrawable')
      exit()
    
    
    
    
    
    
