from board import SCL, SDA
import busio
import time

from adafruit_pca9685 import PCA9685

i2c_bus = busio.I2C(SCL, SDA)

pca = PCA9685(i2c_bus)

pca.frequency = 800

user_input = 0

while user_input != "":
	user_input = input("New percent pwm cycle: ")
	try:
		pca.channels[0].duty_cycle = int(65535*float(user_input))
	except Exception as e:
		print("Error", e)
	if user_input == "s1":
		for i in range(50):
			pca.channels[0].duty_cycle = 0xefff
			time.sleep(0.05)
			pca.channels[0].duty_cycle = 0x0fff
pca.channels[0].duty_cycle = 0x0000
