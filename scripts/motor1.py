#!/usr/bin/env python
#encoding: utf8
import sys, rospy, math
from pimouse_ros.msg import MotorFreqs
from geometry_msg.msg import Twist

class Motor():
	def	__init__(self):
		if not self.set_power(True): sys.exit(1)

		rospy.on_shutdown(self.set_power)
		self.sub_raw = rospy.Subscriber('motor_raw', MotorFreqs, self.callback_raw_freq)
		self.sub_cmd_vel = rospy.Subscriber('cmd_vel', Twist, self.callback_cmd_vel)
		self.last_time = rospy.Time.now()
		self.using_cmd_vel = False

	def	set_power(self,onoff=False):
		en = "/dev/rtmotoren0"
		try:
			with open(en,'w') as f:
				f.write("1\n" if onoff else "0\n")
			self.is_on = onoff
			return True
		except:
			rospy.logerr("cannot write to " + en)

		return False

	def	set_raw_freq(self,left_hz,ruggt_hz):
		if not self.is_on:
			rospy.logerr("bit enpowerd")
			return

		try:
			with open
