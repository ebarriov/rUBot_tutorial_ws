#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from std_msgs.msg import Int64

#def callback_pong(msg):
#	if msg.data == 'ping':
#		output = String
#		output.data = 'pong'
#		pub.publish(output)
#		rospy.loginfo("data: %s", output)
#	else:
#		output.data = 'Fail'
#		pub.publish(output)
#		rospy.loginfo("data: %s", output)

#rospy.init_node('pong_node')
#pub = rospy.Publisher("/pong", String, queue_size=10)
#sub = rospy.Subscriber("/ping", String, callback_pong)
#rospy.spin()


output = 0

def callback_game(msg):
	global output
	if msg.data == "ping":
		output = "pong"
		new_msg = String()
		new_msg.data = output
		pub.publish(new_msg)
		rospy.loginfo("data: %s", output)
	else:
		output = "fail"
		new_msg = String()
		new_msg.data = output
		pub.publish(new_msg)
		rospy.loginfo("data: %s", output)		

rospy.init_node('pong_node')
pub = rospy.Publisher("/pong", String, queue_size=10)
sub = rospy.Subscriber("/ping", String, callback_game)
rospy.spin()
