#!/usr/bin/python

#
# Clevo LightFX
#

# Importing Lightpack and WMI for Win driver interaction

import lightpack, time, wmi, msvcrt, subprocess, itertools, threading, sys


# Progress bar animation

def animate(end_val, bar_length=60):
    for i in xrange(0, end_val):
		percent = float(i) / end_val
		hashes = chr(219) * int(round(percent * bar_length))
		spaces = ' ' * (bar_length - len(hashes))
		sys.stdout.write("\rLoading... {0} {1}%".format(hashes + spaces, int(round(percent * 101))))
		time.sleep(0.01)
		sys.stdout.flush()

# string to rgb

def str2rgb(s,num):

 if num == 1 :
  rgba = s[2:13].split(",")
 elif num == 2 :
  rgba = s[2:13].split(",")
 elif num == 3 :
  rgba = s[2:13].split(",")
 
 #if len(rgba) not in (3, 4):
 # return (0, 0, 0)
 
 brg = (rgba[2],rgba[0],rgba[1])
 return tuple(map(int, brg))
 
# rgb to hex	

def tohex(rgb):
	return "%02X%02X%02X" % rgb
 
def illuminate():

# Interacting with the clevo driver

 c = wmi.WMI(namespace="root\WMI")
 clevo = "select * from CLEVO_GET"

 delay = 0.3
 
# find prismatik

 lpack = lightpack.lightpack('127.0.0.1', 3636, [5,4,3,1,2,6,7,8,9,10])
 lpack.connect()
 print ('')
 print ('                                 Press ESC to end')
 print ('')
 print ('')
 while True :
	
	led1 = tohex(str2rgb(lpack.getColors()[0],1))
	led2 = tohex(str2rgb(lpack.getColors()[1],2))
	led3 = tohex(str2rgb(lpack.getColors()[2],3))
	#print led1 + " " + led2 + " " + led3
	
	
	ark = int("F0"+led1,16)
	ark2 = int("F1"+led2,16)
	ark3 = int("F2"+led3,16)
	
	#print ark,led1
	
	for doy in c.query(clevo):
	 doy.SetKBLED(ark)
	 doy.SetKBLED(ark2)
	 doy.SetKBLED(ark3)
	 
	if msvcrt.kbhit():
	 if ord(msvcrt.getch()) == 27:
		openapp('reset')
		break
		
 
def openapp(app):
	SW_MINIMIZE = 6
	info = subprocess.STARTUPINFO()
	info.dwFlags = subprocess.STARTF_USESHOWWINDOW
	info.wShowWindow = SW_MINIMIZE
	
	if app == 'prismat':
		animate(105)
		resetapp = subprocess.Popen(r'C:\Program Files (x86)\Hotkey\GameFeet.exe', startupinfo=info)
		time.sleep(1)
		resetapp.terminate()
		global pfx
		pfx = subprocess.Popen(r'p\lightfx.exe', startupinfo=info, shell=False)
		illuminate()
		#animate('done')
	elif app == 'reset':
		print ('Resetting keyboard...')
		resetapp = subprocess.Popen(r'C:\Program Files (x86)\Hotkey\GameFeet.exe', startupinfo=info)
		time.sleep(1)
		resetapp.terminate()
		pfx.terminate()
		print ('')
		print ('Goodbye!')
		
print ('')
print ('Clevo LightFX')
print ('')
openapp('prismat')





