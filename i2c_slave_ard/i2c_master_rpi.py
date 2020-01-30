from smbus import SMBus

addr = 0x8 # bus address, same on rpi and arduino
bus = SMBus(1) # indicates /dev/ic2-1

user_input = " "
while user_input != "":
	user_input = input("New percent pwm cycle: ")
	try:
		user_input = int(user_input) + 2**8
	except:
		print("Not a valid number. Try again.")
		continue
	bus.write_byte(addr, user_input)
bus.write_byte(addr, 0)
