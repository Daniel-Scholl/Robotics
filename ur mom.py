from __future__ import print_function
import time
import sys
import math
import qwiic_scmd
import pi_servo_hat

myMotor = qwiic_scmd.QwiicScmd()

def runExample():
	print("Motor Test.")
	R_MTR = 0
	L_MTR = 1
	FWD = 0
	BWD = 1

	if myMotor.connected == False:
		print("Motor Driver not connected. Check connections.", \
			file=sys.stderr)
		return
	myMotor.begin()
	print("Motor initialized.")
	time.sleep(.250)
	
	# Zero Motor Speeds
	myMotor.set_drive(0,0,0)
	myMotor.set_drive(1,0,0)
	
	myMotor.enable()
	print("Motor enabled")
	time.sleep(.250)



	myMotor.set_drive(R_MTR,FWD,250)
	myMotor.set_drive(L_MTR,BWD,-125)

if __name__ == '__main__':
	try:
		runExample()
	except (KeyboardInterrupt, SystemExit) as exErr:
		print("Ending example.")
		myMotor.disable()
		sys.exit(0)