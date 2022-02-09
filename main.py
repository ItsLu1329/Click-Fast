#created by brenden (Lu) bachert, dec 12 2021
#name: Click-Fast
#what is it:
#it is a click game, similar to OSU but is just the clicking, 
#due to program restrictions
#
#please do not copy this code without my (brenden (Lu) bachert) concent
#if you do, at least credit me, id apreciate it
#
#im fine with you refrencing this code, but please credit me, or this program
#import pygame
#https://lbachert-cpavts-net.trinket.io/sites/click-fast

#https://trinket.io/pygame/bc5595f097?outputOnly=true

#v 2.7.8
#yes, this was made with a library\nfor graphing data


from graphics import *
from math import sqrt
import LuGraphicFunctions as lgf
import time
import random
circlelist = []

global clicktype, missmod


clicktype = None
fakes = 0
misses = 0
missmod = 0

mydiscord = 'Lu_#3743'

maincolor1 = '#4600a8' #dark purple
bgcolor1 = '#060f0f' #really dark gray
bgcolor2 = '#6035c4' #idk light purple?
maincolor2 = '#09d96d' #'#00a88c' #bright green
fakecolor = '#3c1178' #old color
startcolor = '#21A327' #old green
quitcolor = '#eb4034' #red
bonuscolor1 = '#14e0be'  #plasma blue
textcolor1 = bonuscolor1#'white'
textcolor2 = 'black'
darkmaincolor2 = '#06b85b'
fakebonuscolor = '#10c2a4'


#make start screen bg better
startcolor = maincolor2
versioninfo = 'v3.1.3'
#versioninfo = 'v3.1.3'

gametitle = 'Click-Fast'
subtitle = f'Graphics and Code by: \nLu Bachert\n{versioninfo}'
gameheadertext = f'Click-Fast {versioninfo}'


def createinfobtn(win, winSize, r, fontsize, x, y):
  infobtn = lgf.drawCircle(win, x, y, r, maincolor2, maincolor2, 1)
  infotxt = lgf.windowtext(win, x, y, 'Info', 'black')
  lgf.fancytext(infotxt, 'courier', fontsize, 'bold')
  return infobtn, infotxt

def createpabtn(win, winSize, pamenubtnSize, pamenutxtSize, pamenuY, pabtnX): #pa = playagain
  pabtn = lgf.drawCircle(win, pabtnX, pamenuY, pamenubtnSize, startcolor, startcolor, 1)
  patxt = lgf.windowtext(win, pabtnX, pamenuY, 'menu', textcolor2)
  lgf.fancytext(patxt, 'courier', pamenutxtSize, 'bold')
  
  return pabtn, patxt

def createquitbtn(win, winSize, pamenubtnSize, pamenutxtSize, pamenuY, quitbtnX, color):
  
  quitbtn = lgf.drawCircle(win, quitbtnX, pamenuY, pamenubtnSize, color, color, 1)
  quittxt = lgf.windowtext(win, quitbtnX, pamenuY, 'Quit', textcolor2)
  lgf.fancytext(quittxt, 'courier', pamenutxtSize, 'bold')
  return quitbtn, quittxt

def playorquitbtns(win, winSize):
  
  pamenubtnSize = 50
  pamenutxtSize = 20
  pamenuY = winSize * 0.63
  
  pabtnX = winSize * 0.40
  quitbtnX = winSize * 0.60
    
  pabtn, patxt = createpabtn(win, winSize, pamenubtnSize, pamenutxtSize, pamenuY, pabtnX)
  

  quitbtn, quittxt = createquitbtn(win, winSize, pamenubtnSize, pamenutxtSize, pamenuY, quitbtnX, quitcolor)


  return pabtn, patxt, quitbtn, quittxt


def otheroptions(win, winSize):
  #create buttons
  #fake toggler for now
  
  pass
  

def otherbuttons(win, winSize):
  
  startbutton = lgf.drawCircle(win, winSize * 0.85, winSize * 0.62, 70, startcolor, startcolor, 1)
  
  startbuttontext = lgf.windowtext(win, winSize * 0.85, winSize * 0.62, 'Start', textcolor2)
  lgf.fancytext(startbuttontext, 'courier', 25, 'bold')
  
  infobtn, infotxt = createinfobtn(win, winSize, 46, 20, winSize * 0.66, winSize * 0.66)

  return startbutton, startbuttontext, infobtn, infotxt
  


def drawgamemodeinfo(win, winSize, gamemode, text):
  
  if gamemode == 'Arcade':
    info = '''
infinite time
limited misses;
adds time;
time x miss 
modifier
(5)'''
  elif gamemode == 'Timed':
    info = '''
limited time;
(30 seconds)
infinit misses; 
reduces time 
you have left;
300 ms 
+ 
miss modifier
    '''
  else:
    info = ''
    
  if text == None:
    text = lgf.windowtext(win, winSize * 0.55, winSize * 0.22, info, textcolor1)
    lgf.fancytext(text, 'courier', 14, 'bold')# text for what each gamemode does
  else:
    text.setText(info)
  
  return text


def missedtextstats(win, winSize, difficulty, misses, fakes, circlemessage, gamemode, missmod, missestext):
  
  if gamemode == 'Arcade':
    newmisses = f'{misses}/5'
  
  else:
    newmisses = f'{misses}'
    
  missesfulltext = f'gamemode: {gamemode}    difficulty: {difficulty}\nmisses: {newmisses}     fakes: {fakes}     miss modifier: {missmod}\n{circlemessage}'

  if missestext == None:
    missestext = lgf.windowtext(win, winSize/2, 40, missesfulltext, textcolor1)
    lgf.fancytext(missestext, 'courier', 20, 'bold')
  else:
    missestext.setText(missesfulltext)
  
  return missestext



def possiblefake():
  num = random.randrange(0,10)
  if num > 7:
    return True
  else:
    return False



def makefake(win, r, winSize):
  if possiblefake():
    x, y = findrandompoint(winSize, r)
    pass
    
  else:
    x = y = -100
    pass
  
  fakecircle = lgf.drawCircle(win, x, y, r, fakecolor, fakecolor, 1)
  return fakecircle, x, y



def createinfotable(win, winSize):
  infoback = lgf.drawRectangle(win, winSize * 0.12, winSize * 0.15, bgcolor2, bgcolor1,  winSize * 0.73, winSize * 0.50)
  infoback.setWidth(5)
  info = lgf.windowtext(win, winSize * 0.47, winSize * 0.38, '''
  - goal -

  click the circles as fast as possible
  without missing any and without 
  hitting any fakes

  - fakes -
  
  fakes are darker versions of the 
  normal circles and you want to avoid
  hitting them at all costs because
  they will cause different negatives
  effect based on the gamemode''', textcolor1)  
  lgf.fancytext(info, 'courier', 20, 'bold')
  info.setStyle('bold')
  return [info, infoback]

def drawgamemodestatus(win, winSize, message):
    status = lgf.windowtext(win, winSize * 0.55, winSize * 0.092, message, textcolor2)
    lgf.fancytext(status, 'courier', 15, 'bold')
    return status

def drawgamemodebox(win, winSize):
  gamemodestatusbox = lgf.drawRectangle(win, winSize * 0.47, winSize * 0.075, maincolor2, maincolor2, winSize * 0.15, 30)
  return gamemodestatusbox


def drawdifficultystatus(win, winSize, message, df):
    if df == None:
      df = lgf.windowtext(win, winSize * 0.25, winSize * 0.092, message, textcolor2)
      lgf.fancytext(df, 'courier', 15, 'bold')
    else:
      df.setText(message)
    return df


    
def drawdifficultybox(win, winSize):
  difficultystatusbox = lgf.drawRectangle(win, winSize * 0.173, winSize * 0.075, maincolor2, maincolor2, winSize * 0.15, 30)
  return difficultystatusbox



def makebonuscircle(win, r,  x, y, winSize, color):
  r = r/3.5
  bonuscircle = lgf.drawCircle(win, x, y, r, color, color, 1)
  return bonuscircle



def createselectionmenu(win, winSize):

  boxX1, boxY1, boxR = 70, 50, 50
  spacing = 110
  optionlist = []
  difficulty = ''
  difficultylist = ['Difficulty','Easy', 'Medium', 'Hard', 'Insane', 'Gamemode','Arcade', 'Timed']
  gamemodeX = winSize * 0.40
  gamemodeY = 50
  

  for difficulty in difficultylist:
    
    if difficulty == 'Difficulty':
      
      optionlist.append((lgf.drawRectangle(win, 0, boxY1, bgcolor2, bgcolor2, winSize, 40)))
      optionlist.append((lgf.windowtext(win, boxX1, boxY1 + 20, difficulty, textcolor1)))

      pass
    
        
    elif difficulty == 'Gamemode':
      optionlist.append((lgf.drawRectangle(win, 0, boxY1, maincolor1, bgcolor2, 100, 40)))
      optionlist.append((lgf.windowtext(win, gamemodeX, gamemodeY + 20, difficulty, textcolor1)))
      gamemodeY += spacing
    
    elif difficulty == 'Arcade' or difficulty == 'Timed':
      optionlist.append((lgf.drawCircle(win, gamemodeX, gamemodeY, boxR, maincolor2, maincolor2, 1)))
      optionlist.append((lgf.windowtext(win, gamemodeX, gamemodeY, difficulty, textcolor2)))
      gamemodeY += spacing

    else:
      optionlist.append((lgf.drawCircle(win, boxX1, boxY1, boxR, maincolor2, maincolor2, 1)))
      optionlist.append((lgf.windowtext(win, boxX1, boxY1, difficulty, textcolor2)))
      pass
    
    boxY1 += spacing
    
  for item in optionlist:
    try:
      lgf.fancytext(item, 'courier', 16, 'bold')
    except:
      pass
    
  return optionlist, optionlist[2], optionlist[4], optionlist[6], optionlist[8], optionlist[12], optionlist[14]



def dificultygraphics(win, winSize):
  difficultystatus = None
  gamemodeinfotext = None
  gamemode = 'None'
  start = False
  r = 0
  
  optionlist, easy, medium, hard, insane, arcade, timed = createselectionmenu(win, winSize)

  startbutton, startbuttontext, infobtn, infotxt = otherbuttons(win, winSize)
  infoandstartlist = [infobtn, infotxt, startbutton, startbuttontext]
  

  
  gamemodeinfotext = drawgamemodeinfo(win, winSize, gamemode, gamemodeinfotext)
  difficultystatusbox = drawdifficultybox(win, winSize)
  difficultystatus = drawdifficultystatus(win, winSize, 'None', difficultystatus)
  gamemodestatusbox = drawgamemodebox(win, winSize)
  gamemodestatus = drawgamemodestatus(win, winSize, gamemode)

  statuslist = [gamemodeinfotext, difficultystatusbox, difficultystatus, gamemodestatusbox, gamemodestatus]
  
  
  
  if 'dev' in versioninfo:
    gameheader = lgf.windowtext(win, winSize * 0.28, winSize * 0.73, gameheadertext, textcolor1)
  else:
    gameheader = lgf.windowtext(win, winSize * 0.16, winSize * 0.73, gameheadertext, textcolor1)

  lgf.fancytext(gameheader, 'courier', 20, 'italic')

  quitbtn, quittxt = createquitbtn(win, winSize, 36, 20, winSize * 0.54, winSize * 0.7, quitcolor)

  while r == 0 or start != True:
    
    p = win.getMouse()
    if lgf.isClickedCircle(easy, p):
      r = 80
      difficulty = 'Easy'

    elif lgf.isClickedCircle(medium, p):
      r = 65
      difficulty = 'Medium'
    elif lgf.isClickedCircle(hard, p):
      r = 50
      difficulty = 'Hard'
    elif lgf.isClickedCircle(insane, p):
      r = 25
      difficulty = 'Insane'
    
    elif lgf.isClickedCircle(arcade, p):
      gamemode = 'Arcade'
      
    elif lgf.isClickedCircle(timed, p):
      gamemode = 'Timed'
      
    elif lgf.isClickedCircle(quitbtn, p):
      exit()
    elif lgf.isClickedCircle(infobtn, p):
      infolist = createinfotable(win, winSize)
      win.getMouse()
      lgf.deleteddrawn(infolist)
      
      
    elif lgf.isClickedCircle(startbutton, p):
      if r != 0 and gamemode != '' and gamemode != 'None':
        start = True
        
      else:
        pass
      
    else:
      pass

    try:
      message = f'{difficulty}'
    except:
      message = 'None'
    
    difficultystatus = drawdifficultystatus(win, winSize, message, difficultystatus)
    gamemodeinfotext = drawgamemodeinfo(win, winSize, gamemode, gamemodeinfotext)

    gamemodestatus.setText(gamemode)
    
  lgf.deleteddrawn(infoandstartlist)
  lgf.deleteddrawn(statuslist)
  lgf.deleteddrawn([quitbtn, quittxt])
  lgf.drawmany(win, optionlist)
  lgf.deleteddrawn(optionlist)
  
  return r, difficulty, gamemode

def tittlebgcreate(win, winSize):
  
  titlecircle1 = lgf.drawCircle(win, winSize * 0.70, winSize * 0.17, 200, fakecolor, fakecolor, 5)
  titlecircle2 = lgf.drawCircle(win, winSize * 0.70, winSize * 0.17, 50, fakebonuscolor, fakebonuscolor, 5)
  
  titlecircle3 = lgf.drawCircle(win, winSize * 0.20, winSize * 0.45, 130, fakecolor, fakecolor, 5)
  titlecircle4 = lgf.drawCircle(win, winSize * 0.20, winSize * 0.45, 35, fakebonuscolor, fakebonuscolor, 5)
  
  titlecircle5 = lgf.drawCircle(win, winSize * 0.80, winSize * 0.60, 100, fakecolor, fakecolor, 5)
  titlecircle6 = lgf.drawCircle(win, winSize * 0.80, winSize * 0.60, 25, fakebonuscolor, fakebonuscolor, 5)
  
  return [titlecircle1, titlecircle2, titlecircle3, titlecircle4, titlecircle5, titlecircle6]
  
  
def tittlegraphics(win, winSize):
  drawnlist = []
  win.setBackground(bgcolor1)
  
  
  #add a background eventually
  titlebglist = tittlebgcreate(win, winSize)
  
  
  rectangle1 = lgf.drawRectangle(win, winSize * 0.20, winSize * 0.25, maincolor1, maincolor1, winSize * 0.60, winSize * 0.28)
  
  titletext = lgf.windowtext(win, winSize * 0.5, winSize * 0.38, gametitle, textcolor1)
  lgf.fancytext(titletext, 'courier', 36, 'bold')
  
  howtostart = lgf.windowtext(win, winSize * 0.5, winSize * 0.6, 'click to start', textcolor1)
  lgf.fancytext(howtostart, 'courier', 18, 'bold italic')
  
  subtitletext = lgf.windowtext(win, winSize * 0.5, winSize * 0.44, subtitle, fakebonuscolor)
  lgf.fancytext(subtitletext, 'courier', 16, 'italic')
  

  
  drawnlist = [subtitletext, titletext, rectangle1, howtostart]
  return drawnlist, titlebglist



def gamegraphics(win, winSize):
  win.setBackground(bgcolor1)
  headerbox = lgf.drawRectangle(win, -1, -1, maincolor1, maincolor1, winSize+1, 90)
  
  return headerbox


def getcurrentms(): #change to ms
  return int(time.time() * 1000)



def findrandompoint(windowsize, r):
  boarder = windowsize - (r*2)
  x = random.randrange(r + 100, boarder)
  y = random.randrange(r + 100, windowsize * 0.635)
  return x, y



def circleClick(win, circle1, fakecircle, starttime, prevtime, p, misses, missmod, fakes, bonuscircle, fakebonuscircle, prevclicktype, gamemode, timelimit, quitbtn, menubtn, otherbtns):
  
  circlesdeletelist = [circle1, fakecircle, bonuscircle, fakebonuscircle]
  if lgf.isClickedCircle(bonuscircle, p):
    
    basepasttime = int(getcurrentms())
    predebuff = basepasttime - int(prevtime) 
    if gamemode == 'Arcade':
      timelimit += 100
      recordedtime = predebuff
    else:
      recordedtime = int(predebuff * 0.80)
    
    circlemessage = f'bonus! {recordedtime}'
    lgf.deleteddrawn(circlesdeletelist)
    misses += 0
    survival = True
    
  elif lgf.isClickedCircle(circle1, p): #if the circle clicked

    basepasttime = int(getcurrentms())
    recordedtime = basepasttime - int(prevtime) 
    if prevclicktype == False: #if the last hit was a miss, then do this, 
      if gamemode == 'Timed':
        recordedtime = round(recordedtime)

      else:
        recordedtime = round(recordedtime * missmod) #recorded time mod, mainly for arcade
    else:
      pass
    
    circlemessage = f'hit! {recordedtime}'
    lgf.deleteddrawn(circlesdeletelist)
    misses += 0
    survival = True
  
  elif lgf.isClickedCircle(quitbtn, p):
    exit()
  
  elif lgf.isClickedCircle(menubtn, p):
    misses, fakes, amountplayed, gamemode, difficulty, start = 0, 0, 0, None, '', False
    lgf.deleteddrawn(circlesdeletelist)
    lgf.deleteddrawn(otherbtns)
    main()
  
  elif lgf.isClickedCircle(fakecircle, p):
    basepasttime = int(getcurrentms())
    predebuff = basepasttime - int(prevtime)
    recordedtime = predebuff * 1.5
    circlemessage = f'fake! {recordedtime}'
    lgf.deleteddrawn(circlesdeletelist)
    misses += 1
    fakes += 1
    survival = True
  
  else:
    basepasttime = int(getcurrentms())
    predebuff = int(basepasttime - int(prevtime))
    recordedtime = predebuff * 2# < - instead use the miss modifier on hit
    lgf.deleteddrawn(circlesdeletelist)
    circlemessage = f'miss! (no points)' #{recordedtime}
    misses += 1
    survival = False
    
  if misses >= 5:
    if gamemode != 'Timed':
      circlemessage = f'{circlemessage}'
      gameEndmsg = True
      
    else:
      gameEndmsg = False
      pass
  else:
    gameEndmsg = False
    pass
  
  return recordedtime, basepasttime, misses, fakes, survival, circlemessage, missmod, gameEndmsg, timelimit



def main():
  clicktype = True
  missestext = None
  endorcontinue = False
  timelimit = 30000
  missmod = 1.2
  prevtime = 0
  misses = 0
  fakes = 0
  amountplayed = 0
  timestamps = []
  
  titlebglist = tittlebgcreate(win, winSize)
  gglist = gamegraphics(win, winSize)

  win.setBackground(bgcolor1)
  r, difficulty, gamemode = dificultygraphics(win, winSize)
  
  currenttime = getcurrentms()
  
  lgf.deleteddrawn(titlebglist)
  
  missestext = missedtextstats(win, winSize, difficulty, misses, fakes, 'no clicks', gamemode, missmod, missestext)
  startingtime = getcurrentms()

  
  
  quitbtnlist= createquitbtn(win, winSize, 20, 13, winSize * 0.08, winSize * 0.10, quitcolor)
  pabtnlist = createpabtn(win, winSize, 30, 15, winSize * 0.05, winSize * 0.053)
  menubtn = pabtnlist[0]
  quitbtn = quitbtnlist[0]
  otherbtns = [menubtn, pabtnlist[1], quitbtn, quitbtnlist[1]]
  
  while endorcontinue == False:
    
    if amountplayed < 1:
      prevtime = getcurrentms()
    else:
      pass
    
    x, y = findrandompoint(winSize, r)
    fake, fakeX, fakeY = makefake(win, r, winSize)
    fakebonuscircle = makebonuscircle(win, r, fakeX, fakeY, winSize, fakebonuscolor)
    circle1 = lgf.drawCircle(win, x, y, r, maincolor1, maincolor1, 1)
    bonuscircle = makebonuscircle(win, r, x, y, winSize, bonuscolor1)

    p = win.getMouse()

    prevclicktype = clicktype
    currenttime, prevtime, misses, fakes, clicktype, circlemessage, missmod, gameEndmsg, timelimit = circleClick(win, circle1, fake, currenttime, prevtime, p, misses, missmod, fakes, bonuscircle, fakebonuscircle, prevclicktype, gamemode, timelimit, quitbtn, menubtn, otherbtns)
    
    if gamemode == 'Timed' and getcurrentms() - startingtime >= timelimit:
        gameEndmsg = True
        lgf.deleteddrawn([circle1, fake, fakebonuscircle, bonuscircle])
        endorcontinue = True

    if clicktype:
      timestamps.append(currenttime)
      amountplayed += 1
    else:
      if prevclicktype == False and clicktype == False:
        if gamemode == 'Arcade':
          missmod = round(missmod + 0.1, 1)

        elif gamemode == 'Timed':
          timelimit = timelimit - missmod
          missmod += 100
          
        else:
          pass
        
      else:
        if gamemode == 'Arcade':
          missmod = 1.2
        else:
          missmod = 300

    if gameEndmsg:
      if gamemode == 'Timed':
        endtypemsg = 'time'
        
      elif gamemode == 'Arcade':
        endtypemsg = 'clicks'
      else:
        endtypemsg = 'error'
      
      outofclicks = lgf.windowtext(win, winSize * 0.5, winSize * 0.4, f'out of {endtypemsg}\nclick to continue', bonuscolor1)
      lgf.fancytext(outofclicks, 'courier', 20, 'bold')
    else:
      pass
    
    missestext = missedtextstats(win, winSize, difficulty, misses, fakes, circlemessage, gamemode, missmod, missestext) 
    if misses >= 5 and gamemode != 'Timed':
      endorcontinue = True
    elif gamemode == 'Time':
      pass
    else:
      pass

  overalltime = 0
  
  for timestamp in timestamps:
    overalltime += timestamp
  try:
    averagetime = round(overalltime / len(timestamps))
  except:
    averagetime = None
  
  win.getMouse()
  
  try:
    outofclicks.undraw()
  except:
    pass
  
  lgf.deleteddrawn(otherbtns)
  
  gamestatbox = lgf.drawRectangle(win, winSize*0.25, winSize * 0.18, bonuscolor1, bonuscolor1, winSize/2, winSize * 0.3)
  timeamount = (str(timelimit)[:-3]) + ' sec' #'30 seconds'
  
  if gamemode == 'Arcade':
    
    endgamestats = f'in {gamemode} mode\non {difficulty} difficulty\nyou hit {amountplayed} circles, {fakes} fake(s)\noverall time(ms): {overalltime}\naverage time(ms): {averagetime}'
    
  else:
    endgamestats = f'in {gamemode} mode\non {difficulty} difficulty in {timeamount}\nyou hit {amountplayed} circles, {fakes} fake(s)\naverage time(ms): {str(timelimit)[:-2]}'
  
  t = lgf.windowtext(win, winSize/2, winSize/3, endgamestats, textcolor2)
  t.setSize(25)

  pabtn, patxt, quitbtn, quittxt = playorquitbtns(win, winSize)
  playagainlist = [pabtn, patxt, quitbtn, quittxt, gamestatbox, t]
  lgf.drawmany(win, playagainlist)

  playagaindecision = False
  while playagaindecision == False:
      
    point_playagainoptions = win.getMouse()
    
    if lgf.isClickedCircle(pabtn, point_playagainoptions):
      playagaindecision = 'play'
      
    elif lgf.isClickedCircle(quitbtn, point_playagainoptions):
      playagaindecision = 'quit'
      
    else:
      playagaindecision = False
  
  if playagaindecision == 'quit':
    lgf.deleteddrawn(playagainlist)
    win.close
    
  elif playagaindecision == 'play':
    misses, fakes, amountplayed, gamemode, difficulty, start = 0, 0, 0, None, '', False
    lgf.deleteddrawn(playagainlist)
    main()
  else:
    print('error')
    win.close
  
  
  #also make a leaderboard
  # maybe have a user input
  
  win.close


if __name__ == '__main__':
  
  global win, winSize
  
  #device = input('what device are you on?\nmobile(m) or computer(c): ')

  
  winSize = 800
  
  # ================ window fix ============================
  '''try:
    windowsize = input('website(w) or downlaod/window(d): ')
    if windowsize == 'w':
      #external window;
      win = GraphWin(width=winSize, height=winSize * 0.75)
    else:
      #trinket window
      win = GraphWin(width=winSize, height=winSize)
  except:
    pass
  '''
  win = GraphWin(title= f'{gameheadertext}',width=winSize, height=winSize * 0.75)
  # ==========================================================

  titlegraphicslist, titlebglist = tittlegraphics(win, winSize)
  win.getMouse()
  lgf.deleteddrawn(titlebglist)
  lgf.deleteddrawn(titlegraphicslist)
  
  main()


        
