import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)



class Board:
	def __init__(self):
		self.pins = ""
		
	def setPin(self,pinNumber,onOff):
		if (onOff == "HIGH"):
			GPIO.output(pinNumber, GPIO.HIGH)
		else:
			GPIO.output(pinNumber, GPIO.LOW)
