#!/usr/bin/env python
#encoding: utf8
import sys, rospy, math
from pimouse_ros.msg import MotorFreqs
from geometry_msg.msg import Twist

class Motor():
	def	__init__(self):
		if not self.set_power(True): sys.exit(1)

		rospy.on_shutdown(self.setpower)
