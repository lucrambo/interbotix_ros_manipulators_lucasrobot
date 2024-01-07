import math
import rospy
from threading import Thread
from interbotix_xs_modules.arm import InterbotixManipulatorXS

def robot_1():
    robot_1 = InterbotixManipulatorXS(robot_model="vx300", robot_name="arm_1", moving_time=1.0, gripper_pressure=1.0, init_node=False)
    robot_1.arm.set_ee_pose_components(x=0.3, z=0.2)
    robot_1.arm.go_to_home_pose()
    robot_1.gripper.open()
    robot_1.gripper.close()
    robot_1.arm.set_single_joint_position("waist", -math.pi/4.0)
    robot_1.arm.set_single_joint_position("waist", 0)
    robot_1.arm.go_to_sleep_pose()

def robot_2():
    robot_2 = InterbotixManipulatorXS(robot_model="lucasrobot", robot_name="arm_2", moving_time=1.0, gripper_pressure=1.0, init_node=False)
    robot_2.arm.set_ee_pose_components(x=0.3, z=0.2)
    robot_2.arm.go_to_home_pose()
    robot_2.gripper.open()
    robot_2.gripper.close()
    robot_2.arm.set_single_joint_position("waist", math.pi/4.0)
    robot_2.arm.set_single_joint_position("waist", 0)
    robot_2.arm.go_to_sleep_pose()

def main():
    rospy.init_node("xsarm_dual")
    Thread(target=robot_1).start()
    Thread(target=robot_2).start()

if __name__=='__main__':
    main()
