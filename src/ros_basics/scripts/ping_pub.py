#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from std_msgs.msg import Int64

#rospy.init_node("ping_node", anonymous=True)
#pub = rospy.Publisher("/ping", String, queue_size=10)
#rate = rospy.Rate(1)

#while not rospy.is_shutdown():
#	game = "ping"
#	rospy.loginfo(game)
#	pub.publish(game)
#	rate.sleep()


rospy.init_node("ping_node", anonymous=True)
pub = rospy.Publisher("/ping", String, queue_size=10)
rate = rospy.Rate(1)

while not rospy.is_shutdown():
	msg = String()
	msg.data = "ping"
	pub.publish(msg)
	
	rate.sleep()
