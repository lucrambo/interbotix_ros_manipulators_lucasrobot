from interbotix_xs_modules.arm import InterbotixManipulatorXS

# This script closes and opens the gripper twice, changing the gripper pressure half way through
#
# To get started, open a terminal and type 'roslaunch interbotix_xsarm_control xsarm_control.launch robot_model:=wx200'
# Then change to this directory and type 'python gripper_control.py  # python3 bartender.py if using ROS Noetic'

def main():
    arm = InterbotixManipulatorXS("lucasrobot", "arm", "gripper")
    arm.gripper.close()
    arm.gripper.open()
    arm.gripper.set_pressure(1.0)
    arm.gripper.close()
    arm.gripper.open()

if __name__=='__main__':
    main()
