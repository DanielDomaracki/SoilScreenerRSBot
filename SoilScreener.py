import pyautogui
import time
import random
from pyclick import HumanClicker

#sets up camera by making north face up and move screen all the way up
def setup ():
	# initialize HumanClicker object
	hc = HumanClicker()
	loc = [0,0]
	print("Setting up screen")

	#Focus screen
	##hc.move((300,2),1)
	##hc.click()
	##time.sleep(random.uniform(0.1,.2))


	#find "minimap" on screen and then click the compass
	location = pyautogui.locateCenterOnScreen('images\Minimap.PNG', confidence=0.8)

	if location is None:
		return 1

	loc[0] = location[0] - 32
	loc[1] = location[1] + 39
	locf = fuzzyClick(loc,10)
	hc.move((int(locf[0]),int(locf[1])),.8)
	hc.click()

	time.sleep(random.uniform(0.3,0.6))

	#move screen up fully
	pyautogui.keyDown('up')
	time.sleep(random.uniform(1.3,1.7))
	pyautogui.keyUp('up')
	time.sleep(random.uniform(0.2,0.4))

	return 1

#Main loop
def soilLoop (counter):
	setupCheck = 0
	LoopCounter = 0

	#main loop of bot
	while True:

		#Runs first time
		if setupCheck == 0:
			setupCheck = setup()

			#Tele to digsite with preset 2 of "arch journal"
			location = pyautogui.locateCenterOnScreen('images\\archBank.PNG',confidence=0.75)
			if location is None: 
				print("Teleporting to Digsite")
				pyautogui.press('2')
				time.sleep(random.uniform(4,5))

			goToBank()

		goToMeshArea(counter)
		goToBank()
		LoopCounter += 1
		print("The bot has completed: " + str(LoopCounter) + " inventories")
	return

#Goes to bank chest and gets full inv of soils
def goToBank ():
	loc = [0,0]
	hc = HumanClicker()
	print("Going to bank")

	#Walk to bank at Digsite
	location = pyautogui.locateCenterOnScreen('images\\archBank.PNG',confidence=0.65)

	if location is None:
		print ("Cant find bank chest on Minimap")
		pyautogui.press("2")
		time.sleep(4)
		goToBank()
		return

	loc [0] = location[0]
	loc [1] = location[1] + 6
	locf = fuzzyClick(loc,3)
	hc.move((int(locf[0]),int(locf[1])),1.8)
	hc.click()

	time.sleep(random.uniform(11,13))

	#Clicks on bank chest
	location = locateLoop("digsite",'BankChest',4,0.65)

	if location is None:
		print ("Cant find bank chest")
		goToBank()

	loc [0] = location[0]
	loc [1] = location[1]
	locf = fuzzyClick(loc,2)
	hc.move((int(locf[0]),int(locf[1])),1.6)
	hc.click()
	#pyautogui.click(locf[0], locf[1])

	time.sleep(random.uniform(4,5))

	#Deposit all times
	pyautogui.press('3')
	time.sleep(random.uniform(0.3,0.5))

	#Takes soil box
	location = pyautogui.locateCenterOnScreen('images\soilBoxBank.PNG', confidence=0.9)

	loc[0] = location[0]
	loc[1] = location[1]
	locf = fuzzyClick(loc,2)
	hc.move((int(locf[0]),int(locf[1])),1)
	hc.click()

	time.sleep(random.uniform(0.5,0.7))

	#RC soil box
	location = pyautogui.locateCenterOnScreen('images\soilBox.PNG', confidence=0.9)

	loc[0] = location[0]
	loc[1] = location[1]
	locf = fuzzyClick(loc,2)
	hc.move((int(locf[0]),int(locf[1])),1)
	pyautogui.click(button = 'right')

	time.sleep(random.uniform(0.2,0.4))
	hc.move((int(locf[0]),int(locf[1])+45),1)
	hc.click()
	time.sleep(random.uniform(0.3,0.6))

	pyautogui.press('1')
	time.sleep(random.uniform(0.5,1))

#Goes to mesh area
def goToMeshArea (counter):
	x = 0
	counter1 = int(counter)
	hc = HumanClicker()
	loc = [0,0]
	print("Going to screen soil")

	#Walk to bank at Digsite
	location = pyautogui.locateCenterOnScreen('images\SoilMeshArea.PNG',confidence=0.6)

	if location is None:
		print ("Cant find mesh area")
		goToMeshArea()
		return

	loc [0] = location[0]
	loc [1] = location[1]
	locf = fuzzyClick(loc,8)
	hc.move((int(locf[0]),int(locf[1])),2)
	hc.click()

	time.sleep(random.uniform(5.2,5.8))

	while x < counter1:
		#Click Screen
		print ("Screening soil for the: " + str(counter) + " time")
		location = locateLoop("","Mesh",10,0.82)

		loc [0] = location[0]
		loc [1] = location[1]
		locf = fuzzyClick(loc,3)
		hc.move((int(locf[0]),int(locf[1])),2)
		hc.click()

		x += 1

		time.sleep(random.uniform(3,3.5))

		location = pyautogui.locateOnScreen('images\ScreenFail.PNG',confidence=0.95)
		if location is True:
			return 

		pyautogui.press("space")
		time.sleep(random.uniform(1,4))

		while actionCheck() is True:
			time.sleep(2)

#Finds object from a series of pictures
def locateLoop (mat,abrev,maxCount,conf):

	for x in range(1,maxCount+1):

		location = pyautogui.locateCenterOnScreen('images\\' + mat+abrev + str(x) + '.PNG', confidence=conf)
		if location is not None:
			break

	if location is None:
		for x in range(1,maxCount+1):

			location = pyautogui.locateCenterOnScreen('images\\' + mat+abrev + str(x) + '.PNG', confidence=conf-0.15)
			if location is not None:
				break

	return location

#Randomizes click
def fuzzyClick (loc, fuz):
	loc[0] = loc[0] + random.uniform(-fuz,fuz)
	loc[1] = loc[1] + random.uniform(-fuz,fuz)
	return loc

#Checks to see if player is actively digging. Returns a True or False
def actionCheck ():
	xpCheck = pyautogui.locateOnScreen('images\Screening.PNG', confidence = 0.8)
	
	if xpCheck is None:
		return False
	else:
		return True 

print ("Type in #, how many times can you screen soil before needing to bank: ")
counter = input()
soilLoop(counter)

# initialize HumanClicker object
hc = HumanClicker()
