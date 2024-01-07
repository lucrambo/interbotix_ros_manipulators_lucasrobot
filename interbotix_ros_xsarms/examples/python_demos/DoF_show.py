from interbotix_xs_modules.arm import InterbotixManipulatorXS
import numpy as np

# This script makes the end-effector perform pick, pour, and place tasks
#
# To get started, open a terminal and type 'roslaunch interbotix_xsarm_control xsarm_control.launch robot_model:=wx250'
# Then change to this directory and type 'python bartender.py  # python3 bartender.py if using ROS Noetic'

def main():
    bot = InterbotixManipulatorXS("lucasrobot", "arm", "gripper")
    bot.arm.go_to_home_pose()
    bot.arm.set_single_joint_position("waist", np.pi/2.0)
    bot.gripper.open()
    bot.gripper.close()
    bot.arm.set_single_joint_position("waist", -np.pi/2.0)
    bot.arm.set_single_joint_position("waist", np.pi/2.0)
    bot.gripper.open()

if __name__=='__main__':
    main()
