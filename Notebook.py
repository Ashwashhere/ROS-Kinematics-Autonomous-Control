# %% [markdown]
# <h1 style="color: blue;">Robotics Science and Systems: ROS Implementation (Personal Assignments 1-6)</h1>
# 
# This Jupyter Notebook contains the compiled code, execution commands, and visual observations for the practical implementation section of the Robotics Science and Systems assessment. 

# %% [markdown]
# # 1. PA-1
# ## a. Question 1
# ### i. Code Snippet:

# %%
# Terminal Commands to set up ROS workspace and create the Python script
# ash@mbpro:~/catkin_ws_rss$ source devel/setup.bash
# ash@mbpro:~/catkin_ws_rss$ cd ~/catkin_ws_rss/src/rss_linux_pkg/scripts
# ash@mbpro:~/catkin_ws_rss/src/rss_linux_pkg/scripts$ nano ash_nelson.py

# Sum of numbers from 0 to 99
total_sum = sum(range(100))

# Print the result 
print("The sum of numbers from 0 to 99 is:", total_sum) 

# Code to run the script
# ash@mbpro:~/catkin_ws_rss/src/rss_linux_pkg/scripts$ python3 ash_nelson.py

# Ouput:
# The sum of numbers from 0 to 99 is: 4950

# %% [markdown]
# # 1. PA-1
# ## a. Question 1
# ### ii. Response/Observations
# 
# To complete this task, I first navigated to the ROS package scripts directory (/catkin_ws_rss/src/rss_linux_pkg/scripts) within the workspace. I then used the nano text editor to create the required Python script.
# 
# The script uses Python's built-in sum() function combined with range(100) to efficiently calculate the total sum of all integers from 0 to 99. After saving the file, I executed it directly from the terminal using the python3 command.
# 
# Output: 
# The script executed without errors, outputting the correct total: 4950. 

# %% [markdown]
# # 1. PA-1
# ## b. Question 2
# 
# To successfully write and execute the Python script within the ROS environment, the following terminal commands were used:
# 
# * **source devel/setup.bash:**
#     * This is a fundamental ROS (Robot Operating System) command. It sources the setup script for your specific Catkin workspace. This updates your environment variables so the terminal knows exactly where to find the ROS packages, nodes, and commands you are working with. 
# * **cd ~/catkin_ws_rss/src/rss_linux_pkg/scripts:**
#     * The ***cd*** (change directory) command is used to navigate the file system. Here, it moves the terminals active directory into the  ***scripts*** folder of the ***rss_linux_pkg*** package where the executable Python files are stored. The ***~*** acts as a shortcut for the home directory.
# * **nano ash_nelson.py**
#     * ***nano*** is a text editor. This command opens the text editor and creates a new file named ***ash_nelson.py**** so the Python logic can be written directly within the terminal.
# * **python3 ash_nelson.py**
#     * This command calls the Python interpreter and tells it to execute the code in the ***ash_nelson.py*** file. This is what actually runs the logic and prints the final output (4950) to the screen.

# %% [markdown]
# # 2. PA-2
# ## a. Question 1
# ### i. Code Snippet:

# %%
# Create the move_square.py script make it executable and edit it in nano
# ash@mbpro:~/catkin_ws_rss/src/rss_linux_pkg/scripts$ touch move_square.py
# ash@mbpro:~/catkin_ws_rss/src/rss_linux_pkg/scripts$ chmod +x move_square.py
# ash@mbpro:~/catkin_ws_rss/src/rss_linux_pkg/scripts$ nano move_square.py

# Python script to move a robot in a square pattern 
#!/usr/bin/env python3
import rospy 
from geometry_msgs.msg import Twist
import math

def move_in_square():
        # Initialise the node
        rospy.init_node('square_mover_node')

        # Create the publisher to the /cmd_vel topic
        pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

        # Give ROS some time to register the publisher
        rospy.sleep(1)

        # Define the Twist message object
        move = Twist()

        # Define the speed parameters
        linear_speed = 0.2
        angular_speed = 0.2

        # Define the distance/angle to calculate duration
        side_length = 1.0
        turn_angle = math.pi/2 

        # Calculate durations
        move_duration = side_length/linear_speed
        turn_duration = turn_angle/angular_speed 

        # Loop 4 times to draw the 4 sides of the square 
        for _ in range(4):
                # Move forward
                rospy.loginfo("Moving forward")
                move.linear.x = linear_speed
                move.angular.z = 0.0
                pub.publish(move)
                rospy.sleep(move_duration)

                # Stop briefly
                move.linear.x = 0.0
                pub.publish(move)
                rospy.sleep(0.5)

                # Turn 90 degrees
                rospy.loginfo("Turning")
                move.linear.x = 0.0
                move.angular.z = angular_speed
                pub.publish(move)
                rospy.sleep(turn_duration)

                # Stop briefly
                move.angular.z = 0.0
                pub.publish(move)
                rospy.sleep(0.5)

        rospy.loginfo("Square completed!")

if __name__ == '__main__':
        try:
                move_in_square()
        except rospy.ROSInterruptException:
                pass

# Open second terminal to launch the Gazebo simulation with the TurtleBot3 in an empty world
# ash@mbpro:~/catkin_ws_rss$ source devel/setup.bash
# ash@mbpro:~/catkin_ws_rss$ export TURTLEBOT3_MODEL=burger
# ash@mbpro:~/catkin_ws_rss$ roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch

# Open third terminal to run the move_square.py script
# ash@mbpro:~/catkin_ws_rss$ rosrun rss_linux_pkg move_square.py
# [INFO] [1774975582.635891, 1734.821000]: Moving forward
# [INFO] [1774975588.183055, 1740.321000]: Turning
# [INFO] [1774975596.603479, 1748.676000]: Moving forward
# [INFO] [1774975602.120698, 1754.177000]: Turning
# [INFO] [1774975610.520534, 1762.531000]: Moving forward
# [INFO] [1774975616.028179, 1768.031000]: Turning
# [INFO] [1774975624.387570, 1776.385000]: Moving forward
# [INFO] [1774975629.892574, 1781.886000]: Turning
# [INFO] [1774975638.278290, 1790.240000]: Sqaure completed!


# %% [markdown]
# # 2. PA-2
# ## a. Question 1
# ### ii. Response/Observations:
# 
# ## Code Breakdown
# 
# ### 1. Initialisation and Setup
# * **rospy.init_node('square_mover_node')**: Registers the script as a ROS node, which is the foundational step for any ROS based robot control.
# * **rospy.Publisher('/cmd_vel', Twist, ...)**: Sets up a publisher to the ***/cmd_vel*** topic. This is the standard ROS topic used to send velocity commands (linear and angular) to a robot.
# 
# ### 2. Defining Movement Parameters
# The script uses basic physics to calculate how long the robot must perform a specific action:
# * **Linear/Angular Speed**: Sets how fast the robot moves (0.2 m/s) and turns (0.2 rad/s).
# * **Duration Calculation**: Uses the formula $time = \frac{distance}{speed}$. 
#     * **move_duration**: The time needed to cover the ***side_length***.
#     * **turn_duration**: The time needed to rotate 90 degrees ($\frac{\pi}{2}$ radians).
# 
# ### 3. The Control Loop
# The **for _ in range(4):** loop ensures the robot repeats the "move and turn" sequence four times to complete the square. Inside the loop, it follows these steps:
# * **Move Forward**: Sets ***linear.x*** to the desired speed and publishes it to the robot.
# * **Wait (***rospy.sleep***)**: Keeps the command active for the calculated duration.
# * **Turn**: Sets ***linear.x*** to 0 and ***angular.z*** to the turn speed to rotate the robot in place.
# * **Pause**: A brief 0.5 second stop between actions helps improve accuracy by reducing momentum-based errors.
# 
# **Robot Movement:**
# ![robotSquare.gif](attachment:robotSquare.gif)

# %% [markdown]
# # 3. PA-3
# ## a. Question 1
# ### i. Code Snippet:

# %%
# Copy the publisher script to create a new one for moving in a straight line and edit it in nano
# ash@mbpro:~/catkin_ws_rss$ cd src/rss_pubsub_pkg/scripts
# ash@mbpro:~/catkin_ws_rss/src/rss_pubsub_pkg/scripts$ cp ashnelson_publisher.py ashnelson_publisher_line.py
# ash@mbpro:~/catkin_ws_rss/src/rss_pubsub_pkg/scripts$ nano ashnelson_publisher_line.py

# Script to move in a straight line
#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

# Initialis script as a ROS  node
rospy.init_node('ashnelson_publisher_line')

# Define the publisher
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
rate = rospy.Rate(1)

# Create an empty Twist message
move = Twist()
# Set linear velocity to move forward
move.linear.x = 0.5
# Set angular velocity to 0 so it does not turn
move.angular.z = 0.0

# Keep running until stopped, send the movement command and pause
while not rospy.is_shutdown():
    pub.publish(move)
    rate.sleep()

# %% [markdown]
# # 3. PA-3
# ## a. Question 1
# ### ii. Respone Observations: 
# 
# To fulfill the requirement of moving the robot in a continuous straight line, I modified the velocity parameters within the ***Twist*** message. I set a continuous forward speed by assigning ***move.linear.x = 0.5*** (0.5m/s). Most importantly, to prevent the robot from deviating or turning, I  set ***move.angular.z = 0.0***. By ensuring there is zero angular velocity, the robot's trajectory is locked strictly to the x-axis.

# %% [markdown]
# # 3. PA-3
# ## a. Question 2
# ### i. Code Snippet:

# %%
# Naviate to the launch folder and create a launch file for the publisher node
# ash@mbpro:~/catkin_ws_rss$ cd src/rss_pubsub_pkg/launch
# ash@mbpro:~/catkin_ws_rss/src/rss_pubsub_pkg/launch$ touch ashnelson_publisher_line.launch
# ash@mbpro:~/catkin_ws_rss/src/rss_pubsub_pkg/launch$ nano ashnelson_publisher_line.launch

# Launch file to run the publisher node
# <launch>
#    <node name="ashnelson_publisher_line_node" pkg="rss_pubsub_pkg" type="ashnelson_publisher_line.py" output="screen"/>
# </launch>

# %% [markdown]
# # 3. PA-3
# ## a. Question 2
# ### ii. Respones/Observations:
# 
# To streamline the execution of the new straight-line movement script, I created a custom ROS launch file named ***ashnelson_publisher_line.launch*** within the package's ***launch*** directory. 
# 
# The XML structure defines a single ***<node>*** tag. I specified ***pkg="rss_pubsub_pkg"*** to tell ROS where to look, and ***type="ashnelson_publisher_line.py"*** to specify the exact executable script. Also, I included the ***output="screen"*** attribute; this ensures that any ***rospy.loginfo()*** messages or errors generated by the script will be printed directly to the active terminal, rather than being hidden in background log files. This setup allows the node to be started efficiently using the ***roslaunch*** command.

# %% [markdown]
# # 3. PA-3
# ## a. Question 3
# ### i. Code Snippet:

# %%
# Terminal 1, start ROS master
# ash@mbpro:~/catkin_ws_rss$ source devel/setup.bash
# ash@mbpro:~/catkin_ws_rss$ roscore

# Terminal 2, launch the publisher node
# ash@mbpro:~/catkin_ws_rss$ source devel/setup.bash
# ash@mbpro:~/catkin_ws_rss$ roslaunch rss_pubsub_pkg ashnelson_publisher_line.launch

# Terminal 3, run the subscriber node to see the published messages
# ash@mbpro:~/catkin_ws_rss$ source devel/setup.bash
# ash@mbpro:~/catkin_ws_rss$ rosrun rss_pubsub_pkg ashnelson_subscriber.py


# %% [markdown]
# # 3. PA-3
# ## a. Question 3
# ### i. Response/Observations
# 
# By running the ***ashnelson_subscriber.py*** node in a separate terminal, I was able to actively monitor the data being published to the topic by my straight-line script. 
# 
# The terminal output from the subscriber continuously printed the intercepted ***Twist*** messages. I observed that the velocity parameters remained constant with every logged message: the ***linear.x*** value was consistently locked at ***0.5***, while the ***angular.z*** value remained at ***0.0***. This continuous stream of data physically confirms the logic of the publisher script; because the angular velocity is strictly zero, the robot receives no rotational commands, proving mathematically that its resulting trajectory in a simulation will be a perfectly straight line.
# 
# **Subscriber Terminal Output: **
# ![PA3.3Output.png](attachment:PA3.3Output.png)

# %% [markdown]
# # 3. PA-3
# ## a. Question 4
# ### i. Code Snippet:

# %%
# Terminal, Launch empty world with TurtleBot3
# ash@mbpro:~/catkin_ws_rss$ source devel/setup.bash
# ash@mbpro:~/catkin_ws_rss$ export TURTLEBOT3_MODEL=burger
# ash@mbpro:~/catkin_ws_rss$ roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch

# %% [markdown]
# # 3. PA-3
# ## a. Question 4
# ### i. Response/Observations
# 
# After launching the ***turtlebot3_empty_world.launch*** file, the Gazebo opened with the TurtleBot3 spawned in the center of the grid. Because my custom ***ashnelson_publisher_line*** node was actively publishing to the ***/cmd_vel*** topic in the background, the simulated robot immediately began responding to those commands.
# 
# Visually, the robot drove continuously forward in a perfectly straight trajectory. This physical observation in the Gazebo environment directly corroborates the mathematical output observed in the terminal during Question 3, the strict ***angular.z = 0.0*** parameter successfully locks the robot's kinematics to a straight-line path.
# 
# **Robots Behaviour**: 
# ![ROSPA3Q4.gif](attachment:ROSPA3Q4.gif)

# %% [markdown]
# # 3. PA-3
# ## a. Question 5
# ### i. Code Snippet:

# %%
# Run the launch file, subscriber and gazebo to see the robot move in a circle
# Terminal 1, start ROS master
# ash@mbpro:~/catkin_ws_rss$ source devel/setup.bash
# ash@mbpro:~/catkin_ws_rss$ roscore

# Terminal 2, launch the circle publisher node
# ash@mbpro:~/catkin_ws_rss$ source devel/setup.bash
# ash@mbpro:~/catkin_ws_rss$ roslaunch rss_pubsub_pkg ashnelson_publisher.launch

# Terminal 3, run the subscriber node to see the published messages
# ash@mbpro:~/catkin_ws_rss$ source devel/setup.bash
# ash@mbpro:~/catkin_ws_rss$ rosrun rss_pubsub_pkg ashnelson_subscriber.py

# Terminal 4, run the publisher circle script 
# ash@mbpro:~/catkin_ws_rss$ source devel/setup.bash
# ash@mbpro:~/catkin_ws_rss$ export TURTLEBOT3_MODEL=burger
# ash@mbpro:~/catkin_ws_rss$ roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch


# %% [markdown]
# # 3. PA-3
# ## a. Question 5
# ### i. Response/Observations
# 
# Based on the execution of both scripts, the fundamental difference in the robot's physical behaviour stems directly from how each script handles the rotational parameters within the ***Twist*** message published to the ***/cmd_vel*** topic.
# 
# * **ashnelson_publisher.py (Original):** The original script supplies the robot with both a positive linear velocity (***linear.x***) and a non-zero angular velocity (***angular.z***). Because the robot is simultaneously driving forward and rotating, its kinematics force it into a continuous circular trajectory in the Gazebo simulation.
# * **ashnelson_publisher_line.py (Modified):** By explicitly defining ***move.angular.z = 0.0*** in the modified script, the rotational command is completely eliminated. As observed in the previous step, the robot only processes the forward momentum, locking its physical trajectory into a  straight line.
# 
# **Robot Behaviour:**
# ![robot_circle.gif](attachment:robot_circle.gif)

# %% [markdown]
# # 3. PA-3
# ## a. Question 6
# ### i. Code Snippet:

# %%
# Stopping the robot by publishing zero velocities to the /cmd_vel topic
# rostopic pub /cmd_vel geometry_msgs/Twist "linear:
#  x: 0.0
#  y: 0.0
#  z: 0.0
# angular:
#  x: 0.0
#  y: 0.0
#  z: 0.0"

# %% [markdown]
# # 3. PA-3
# ## a. Question 6
# ### i. Response/Observations:
# 
# **Method 1:** the robot can be stopped by hitting ctrl+c in the publisher node terminal effectively stopping it from publishing commands.
# 
# **Method 2:** Manually publishing a zero-velocity command in a new terminal

# %% [markdown]
# # 4. PA-4
# ## a. Question 1&2
# ### i. Code Snippet:

# %%
# Write a publisher and subscriper script to move in a straight line and stop after a certain distance
# ash@mbpro:~$ cd catkin_ws_rss/src/rss_pubsub_pkg/scripts
# ash@mbpro:~/catkin_ws_rss/src/rss_pubsub_pkg/scripts$ touch ashnelson_pubsub.py
# ash@mbpro:~/catkin_ws_rss/src/rss_pubsub_pkg/scripts$ chmod +x ashnelson_pubsub.py
# ash@mbpro:~/catkin_ws_rss/src/rss_pubsub_pkg/scripts$ nano ashnelson_pubsub.py 

# Script to move in a straight line and stop after a certain distance
#!/usr/bin/env python3
import rospy
import math
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

# Global variables to track position
# Starting coordinates of the robot, initialised to None until the first /odom message is received
start_x = None
start_y = None
# Target distance to travel before stopping
target_distance = 1.0  
# Flag to indicate if the target distance has been reached
reached_target = False
# Publisher object to send velocity commands, initialised to None until the main function sets it up
pub = None

# The odom_callback function is called whenever a new message is published to the /odom topic. It calculates how far the robot has moved from its starting point and stops the robot once it reaches the target distance.
def odom_callback(msg):
    # Access the global variables to track position and control the robot
    global start_x, start_y, reached_target, pub

    # Flag to prevent further calculations and commands once the target distance has been reached
    if reached_target:
        return

    # Extract current X and Y position from the /odom message
    current_x = msg.pose.pose.position.x
    current_y = msg.pose.pose.position.y

    # Set the starting coordinates the first time the callback runs
    if start_x is None or start_y is None:
        start_x = current_x
        start_y = current_y

    # Calculate the Euclidean distance traveled
    distance_traveled = math.sqrt((current_x - start_x)**2 + (current_y - start_y)**2)

    # Check if the robot has reached or exceeded the target distance
    if distance_traveled >= target_distance:
        # The robot stops once it reaches the specified distance
        stop_msg = Twist()
        stop_msg.linear.x = 0.0
        stop_msg.angular.z = 0.0
        pub.publish(stop_msg)
        rospy.loginfo("Target distance reached! Robot stopped.")
        reached_target = True

def main():
    global pub, reached_target

    # Initialize the ROS node
    rospy.init_node('ashnelson_pubsub_node')

    # Subscribe to /odom and Publish to /cmd_vel
    rospy.Subscriber('/odom', Odometry, odom_callback)
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)

    rate = rospy.Rate(10) # 10 Hz

    # Set forward movement velocity
    move_msg = Twist()
    move_msg.linear.x = 0.2 
    move_msg.angular.z = 0.0

    while not rospy.is_shutdown():
        # Keep publishing the move command until the target is reached
        if not reached_target:
            pub.publish(move_msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass

# %% [markdown]
# # 3. PA-4
# ## a. Question 1&2
# ### i. Response/Observations:
# 
# **Distance Tracking and Control Logic:**
# To ensure the robot stops after a precise distance, I implemented a closed-loop control system using Odometry feedback. I set the ***target_distance*** variable to 1.0m. 
# 
# When the script initialises, the ***odom_callback*** function records the robot's initial x and y coordinates. As the robot moves, the callback continuously extracts the new coordinates and uses the Euclidean distance formula ($d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$) to calculate the exact distance traveled from the origin point. Once this calculated distance meets or exceeds 1.0m, the script triggers a boolean flag (***reached_target = True****) and publishes a final zero-velocity ***Twist*** message, safely stopping the robot.

# %% [markdown]
# # 4. PA-4
# ## a. Question 3
# ### i. Code Snippet:

# %%
# Terminal commands for creating launch script
# ash@mbpro:~/catkin_ws_rss/src/rss_pubsub_pkg/launch$ touch ashnelson_pubsub.launch
# ash@mbpro:~/catkin_ws_rss/src/rss_pubsub_pkg/launch$ nano ashnelson_pubsub.launch

# Launch file code to run the publisher and subscriber script
<launch>
    <node name="ashnelson_pubsub_node" pkg="rss_pubsub_pkg" type="ashnelson_pubsub.py" output="screen" />
</launch>

# %% [markdown]
# # 4. PA-4
# ## a. Question 3
# ### i. Response/Observations:
# 
# **Launch File Configuration:**
# To efficiently execute the new closed-loop control script, I created a custom launch file (***ashnelson_pubsub.launch***). 
# 
# The XML file defines the execution parameters for the node. I set the ***pkg*** attribute to ***rss_pubsub_pkg*** and the ***type*** attribute to my executable ***ashnelson_pubsub.py*** script. The inclusion of the ***output="screen"*** attribute is important for this assignment; because my Python script contains ***rospy.loginfo()*** commands to report when the target distance is reached, logging to the screen ensures I can actively monitor the odometry callbacks and the final stop notification directly in the terminal during the simulation.

# %% [markdown]
# # 4. PA-4
# ## a. Question 4
# ### i. Code Snippet:

# %%
# Open gazebo in terminal 1
# ash@mbpro:~/catkin_ws_rss$ cd ~/catkin_ws_rss
# ash@mbpro:~/catkin_ws_rss$ source devel/setup.bash
# ash@mbpro:~/catkin_ws_rss$ export TURTLEBOT3_MODEL=burger
# ash@mbpro:~/catkin_ws_rss$ roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch

# Terminal 2 run the publisher and subscriber node
# ash@mbpro:~/catkin_ws_rss$ source devel/setup.bash
# ash@mbpro:~/catkin_ws_rss$ roslaunch rss_pubsub_pkg ashnelsonpubsub.launch

# %% [markdown]
# # 4. PA-4
# ## a. Question 4
# ### i. Response/Observations:
# 
# **Description:**
# To test the script, I first launched the TurtleBot3 in an empty Gazebo world. Once the environment was fully loaded, I executed my custom ***ashnelson_pubsub.launch*** file in a secondary terminal. 
# 
# Immediately upon launch, the robot began moving forward in a straight line, responding to the ***0.2*** linear velocity commands being published to ***/cmd_vel***. Meanwhile, the terminal actively displayed the logging output from my script. 
# 
# Because the script was subscribed to the ***/odom*** topic, it continuously calculated the Euclidean distance from the starting coordinates. Once the robot visually covered what appeared to be exactly 1 meter in the simulation, it came to a complete stop. Simultaneously, the terminal printed the final log: ***[INFO] Target distance reached! Robot stopped.*** This physical observation in Gazebo perfectly validates the closed-loop logic of the script; the robot successfully used real-time odometry feedback to dictate its physical movement. 
# 
# **Terminal Output Confriming the Robot Stopped:**
# ![terminOutput.png](attachment:image.png)
# **Observation:**
# ![PA44.gif](attachment:PA44.gif)

# %% [markdown]
# # 5. PA-5
# ## a. Question 1
# ### i. Code Snippet:

# %%
# Naviagate to launch folder and create the publisher and subscriber launch file
# ash@mbpro:~/catkin_ws_rss/src$ cd rss2_msgsrv_pkg
# ash@mbpro:~/catkin_ws_rss/src/rss2_msgsrv_pkg$ cd launch
# ash@mbpro:~/catkin_ws_rss/src/rss2_msgsrv_pkg/launch$ touch ashnelson_pubsub.launch
# ash@mbpro:~/catkin_ws_rss/src/rss2_msgsrv_pkg/launch$ nano ashnelson_pubsub.launch

# Launch file code for publisher and subscriber nodes
<launch>
    <node name="msg_pub_node" pkg="rss2_msgsrv_pkg" type="msg_pub.py" output="screen" />

    <node name="msg_sub_node" pkg="rss2_msgsrv_pkg" type="msg_sub.py" output="screen" />
</launch>

# %% [markdown]
# # 5. PA-5
# ## a. Question 1
# ### i. Response/Observations:
# 
# **Launch File Description:**
# For this task, I created a single launch file (***ashnelson_pubsub.launch***) designed to startup of multiple ROS nodes simultaneously. 
# 
# Instead of manually opening separate terminals and executing ***rosrun*** for the publisher and subscriber individually, this XML configuration allows the ROS master to initialise both ***msg_pub.py*** and ***msg_sub.py*** from the ***rss2_msgsrv_pkg*** package with a single command. I included the ***output="screen"*** attribute for both nodes, ensuring that the terminal executing the ***roslaunch*** command displays the combined log messages from both the publishing and subscribing processes, allowing for easy verification that they are communicating correctly.

# %% [markdown]
# # 5. PA-5
# ## a. Question 2
# ### i. Code Snippet:

# %%
# Naviagte to and create the server_client launch file
# ash@mbpro:~/catkin_ws_rss/src/rss2_msgsrv_pkg/launch$ touch ashnelson_server_client.launch
# ash@mbpro:~/catkin_ws_rss/src/rss2_msgsrv_pkg/launch$ nano ashnelson_server_client.launch

# Launch file code for server and client nodes
<launch>
    <node name="turtlebot_move_server" pkg="rss2_msgsrv_pkg" type="pw_srv_server.py" output="screen" />

    <node name="turtlebot_move_client" pkg="rss2_msgsrv_pkg" type="pw_srv_client.py" output="screen" />
</launch>

# %% [markdown]
# # 5. PA-5
# ## a. Question 2
# ### i. Response/Observations:
# 
# **Client-Server Launch File Description:**
# Following the same multi-node structure as the previous question, I created ***ashnelson_server_client.launch*** file to launch the server and client nodes. 
# 
# This launch file initialises the ***turtlebot_move_server*** node, which spins up and waits to receive requests, and the ***turtlebot_move_client*** node, which will send a specific movement request. Launching both simultaneously via a single XML file ensures that the server is active in the ROS environment at the exact moment the client sends its service call. Including ***output="screen"*** allows me to monitor the request sent by the client and the success/failure boolean response returned by the server directly in the terminal window.

# %% [markdown]
# # 5. PA-5
# ## a. Question 3, 4, 5, 6
# ### i. Code Snippet:

# %%
# Python script for the service server to move the TurtleBot in a specific pattern when the service is called 
#!/usr/bin/env python3
import rospy
from rss2_msgsrv_pkg.srv import srv_turtlebot_move, srv_turtlebot_moveResponse
from geometry_msgs.msg import Twist

# Global variable for the publisher to send velocity commands, initialised to None until the main function sets it up
pw_pub = None

# Exectues when service client makes a request
def my_callback(request):
    rospy.loginfo('Turtlebot_move_service has been called. Starting 30-second sequence.')
    
    # Twist message to hold velocity commands
    vel = Twist()
    
    # Set rate to 1 per second
    rate = rospy.Rate(1) 

    # Move in a circle by setting angular and linear for 20 seconds
    rospy.loginfo('Phase 1: Moving in a circle (20 seconds)')
    vel.linear.x = 0.2 
    vel.angular.z = 0.2 
    
    # Loop 20 times
    for i in range(20):
        pw_pub.publish(vel)
        rospy.loginfo(f'Circle time: {i+1}/20')
        rate.sleep()

    # Stop for 5 seconds
    rospy.loginfo('Phase 2: Stopping (5 seconds)')
    vel.linear.x = 0.0
    vel.angular.z = 0.0
    
    # Loop 5 times 
    for i in range(5):
        pw_pub.publish(vel)
        rospy.loginfo(f'Stop time: {i+1}/5')
        rate.sleep()

    # Move along the x axis by zeroing angular speed
    rospy.loginfo('Phase 3: Moving straight along x-axis (5 seconds)')
    vel.linear.x = 0.2  
    vel.angular.z = 0.0 
    
    # Loop 5 times 
    for i in range(5):
        pw_pub.publish(vel)
        rospy.loginfo(f'Straight time: {i+1}/5')
        rate.sleep()

    # Stop completely
    rospy.loginfo('Phase 4: Sequence complete. Stopping completely.')
    vel.linear.x = 0.0
    vel.angular.z = 0.0
    pw_pub.publish(vel)

    # Return the response 
    return srv_turtlebot_moveResponse(True)


if __name__ == '__main__':
    try:
        # Initialise the ROS node
        rospy.init_node('turtlebot_move_server')
        
        # Set up the publisher to send velocity commands to the Turtlebot
        pw_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        
        # Set up the service server
        pw_service = rospy.Service('/turtlebot_move_service', srv_turtlebot_move, my_callback)
        
        rospy.loginfo('Service /turtlebot_move_service is ready and waiting for requests!')
        
        # Keep the node running and listening for client requests
        rospy.spin()
        
    except rospy.ROSInterruptException:
        pass

# Testing the code 
# Terminal 1, start ROS master
# ash@mbpro:~/catkin_ws_rss$ source devel/setup.bash
# ash@mbpro:~/catkin_ws_rss$ roscore

# Terminal 2, launch the server and client nodes
# ash@mbpro:~/catkin_ws_rss$ source devel/setup.bash
# ash@mbpro:~/catkin_ws_rss$ rosrun rss2_msgsrv_pkg pw_srv_server.py

# Terminal 3, run the client to call the service and trigger the robot movement
# ash@mbpro:~/catkin_ws_rss$ source devel/setup.bash
# ash@mbpro:~/catkin_ws_rss$ rosrun rss2_msgsrv_pkg pw_srv_client.py

# %% [markdown]
# # 5. PA-5
# ## a. Question 3, 4, 5, 6
# ### i. Response/Observations:
# 
# **Robot Dance Code Description:**
# To achieve the exact 30-second sequence across Questions 3 through 6, I modified the server callback function to execute a time-based open-loop control strategy. By establishing a ***rospy.Rate(1)*** (1 Hz), I ensured that each iteration of a ***for*** loop lasted exactly one second. 
# 
# * **Phase 1 (Circle - 20s):** I supplied the ***Twist*** message with both linear 0.2m/s and angular 0.2 rad/s velocities, publishing this command 20 times to force the robot into a continuous circular trajectory.
# * **Phase 2 (Pause - 5s):** I zeroed out all velocities and published the stop command 5 times, effectively halting the robot for exactly 5 seconds.
# * **Phase 3 (Straight - 5s):** I re-engaged the linear velocity to 0.2 m/s but kept angular velocity at 0.0, moving the robot straight along the x-axis for 5 loops. 
# * **Phase 4 (Final Stop):** Once the loops resolved, a final zero-velocity message was published to safely terminate the robot's momentum, and the server successfully returned a ***True*** response to the client. The terminal logging correctly documented each second of the sequence.
# 
# **Terminal Output:**
# ![TerminalOutputPA5.png](attachment:image.png)
# 
# **Robot Dance:**
# ![RobotDance.gif](attachment:PA53456RobotDance.gif)

# %% [markdown]
# # 6. PA-6
# ## a. Question 1
# ### i. Code Snippet:

# %%
# Create the service file for the turtlebot move service
# ash@mbpro:~/catkin_ws_rss cd ~/catkin_ws_rss/src/rss2_msgsrv_pkg
# ash@mbpro:~/catkin_ws_rss/src/rss2_msgsrv_pkg$ mkdir srv
# ash@mbpro:~/catkin_ws_rss/src/rss2_msgsrv_pkg/srv$ nano turtlebot_move_square.srv

# Service file definition for the turtlebot move service
float64 sideLength
int32 repetitions
---
bool success

# %% [markdown]
# # 6. PA-6
# ## a. Question 1
# ### i. Response/Observations:
# 
# **Custom Service Message Definition:**
# To establish a custom communication protocol between a new client and server, I created a dedicated ***srv*** directory within the ***rss2_msgsrv_pkg*** workspace. Inside this directory, I defined the custom message structure in the ***turtlebot_move_square.srv*** file.
# 
# Following ROS conventions, I separated the message into two distinct parts using  ***---***. The top section defines the ***Request*** parameters (***float64 sideLength*** and ***int32 repetitions***), which dictate the physical dimensions and duration of the robot's task. The bottom section defines the ***Response*** parameter (***bool success***), which the server will use to notify the client whether the sequence was completed without errors.

# %% [markdown]
# # 6. PA-6
# ## a. Question 2
# ### i. Code Snippet:

# %%
# Modify CMakeLists.txt and package.xml to include the new service definition and dependencies
# Modify the package.xml file to include the new service dependencies
<buildtool_depend>catkin</buildtool_depend>
<build_depend>geometry_msgs</build_depend>
<build_depend>nav_msgs</build_depend>
<build_depend>rospy</build_depend>
<build_depend>std_msgs</build_depend>
# Message generation dependencies
<build_depend>message_generation</build_depend>
<build_export_depend>geometry_msgs</build_export_depend>
<build_export_depend>nav_msgs</build_export_depend>
<build_export_depend>rospy</build_export_depend> 
# Message runtime dependencies
<build_export_depend>message_runtime</build_export_depend>
<build_export_depend>std_msgs</build_export_depend>
<exec_depend>geometry_msgs</exec_depend>
<exec_depend>nav_msgs</exec_depend>
<exec_depend>rospy</exec_depend>
<exec_depend>std_msgs</exec_depend>
# Runtime dependencies for the service
<exec_depend>message_runtime</exec_depend>

# Modify the CMakeLists.txt file to include the new service definition and dependencies
find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  nav_msgs
  rospy
  std_msgs
  message_generation
)

## Generate services in the 'srv' folder
add_service_files(
   FILES
   srv_turtlebot_move.srv
   ashnelson_turtlebot3_move_square.srv
 )

## Generate added messages and services with any dependencies listed here
generate_messages(
   DEPENDENCIES
   geometry_msgs  
   nav_msgs  
   std_msgs
 )

catkin_package(
#  INCLUDE_DIRS include
  LIBRARIES rss2_msgsrv_pkg
  CATKIN_DEPENDS geometry_msgs nav_msgs rospy std_msgs message_runtime
#  DEPENDS system_lib
)

# %% [markdown]
# # 6. PA-6
# ## a. Question 2
# ### i. Response/Observations:
# 
# **Edit CMakeLists.txt and Package.xml:**
# Creating a custom ***.srv*** file is not enough on its own; the ROS build system must be explicitly instructed on how to compile it. To achieve this, I modified the two core configuration files of the package. 
# 
# In ***package.xml***, I added ***message_generation*** as a build dependency and ***message_runtime*** as an execution dependency. This ensures the package has the necessary tools to process the custom message structure.
# 
# In ***CMakeLists.txt***, I added ***message_generation*** to the ***find_package*** macro. Crucially, I updated the ***add_service_files*** block to explicitly include the newly created ***ashnelson_turtlebot_move_square.srv*** file, and ensured ***generate_messages()*** was uncommented. Finally, I added ***message_runtime*** to the ***CATKIN_DEPENDS*** in ***catkin_package()***. When ***catkin_make*** is run in the workspace, these configurations command ROS to parse the ***.srv*** text file and generate the corresponding Python classes (***ashnelson_turtlebot_move_squareRequest*** and ***ashnelson_turtlebot_move_squareResponse***) so they can be imported into my scripts.

# %% [markdown]
# # 6. PA-6
# ## a. Question 3, 4, 5
# ### i. Code Snippet:

# %%
# Python script to move the robot in a square pattern based on service request
#!/usr/bin/env python3

# Terminal commands to create the service server and client scripts
# ash@mbpro:~/catkin_ws_rss/src$ cd rss2_msgsrv_pkg/scripts
# ash@mbpro:~/catkin_ws_rss/src/rss2_msgsrv_pkg/scripts$ touch ashnelson_square_server.py ashnelson_square_client.py

# Edit the server script in nano
# ash@mbpro:~/catkin_ws_rss/src/rss2_msgsrv_pkg/scripts$ nano ashnelson_square_server.py

import rospy
import math
from rss2_msgsrv_pkg.srv import ashnelson_turtlebot3_move_square, ashnelson_turtlebot3_move_squareResponse
from geometry_msgs.msg import Twist

# Execturd when square movement service is called
def move_square_callback(request):
    rospy.loginfo('Square movement service called.')
    vel = Twist()
    
    # Define movement speeds
    linear_speed = 0.2
    angular_speed = 0.2
    
    # Calculate maneuver durations
    straight_duration = request.sideLength / linear_speed
    # 90-degree turn
    turn_duration = (math.pi / 2) / angular_speed  
    
    # Execute the requested number of complete squares
    for _ in range(request.repetitions):
        # Loop for each side of the square
        for _ in range(4):
            # Drive straight along the edge
            vel.linear.x = linear_speed
            vel.angular.z = 0.0
            pw_pub.publish(vel)
            rospy.sleep(straight_duration)
            
            # Brief pause to stabilise robot 
            vel.linear.x = 0.0
            pw_pub.publish(vel)
            rospy.sleep(0.5)

            # turn 90 degrees 
            vel.linear.x = 0.0
            vel.angular.z = angular_speed
            pw_pub.publish(vel)
            rospy.sleep(turn_duration)
            
            # Brief pause to stabilise
            vel.angular.z = 0.0
            pw_pub.publish(vel)
            rospy.sleep(0.5)

    # Ensure the robot when finished
    vel.linear.x = 0.0
    vel.angular.z = 0.0
    pw_pub.publish(vel)

    rospy.loginfo('Square movement completed successfully.')
    return ashnelson_turtlebot3_move_squareResponse(True)

if __name__ == '__main__':
    # Initialize the ROS node
    rospy.init_node('square_move_server')
    
    # Setup publisher for velocity commands
    pw_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    
    # Register the service server
    rospy.Service('/turtlebot_move_square_service', ashnelson_turtlebot3_move_square, move_square_callback)
    
    # Keep the node active to listen for service requests
    rospy.loginfo('Service /turtlebot_move_square_service is ready!')
    rospy.spin() 


# Edit the client script in nano
# ash@mbpro:~/catkin_ws_rss/src/rss2_msgsrv_pkg/scripts$ nano ashnelson_square_client.py

# Python script to call the square movement service and send parameters
#!/usr/bin/env python3
import rospy
import sys
from rss2_msgsrv_pkg.srv import ashnelson_turtlebot3_move_square, ashnelson_turtlebot3_move_squareRequest

if __name__ == '__main__':
    # Initialise the client node
    rospy.init_node('square_move_client')
    
    rospy.loginfo("Waiting for /turtlebot_move_square_service to become available...")
    
    # Prevent client from crashing
    rospy.wait_for_service('/turtlebot_move_square_service')
    
    try:
        # Create a proxy to the service
        square_service_client = rospy.ServiceProxy('/turtlebot_move_square_service', ashnelson_turtlebot3_move_square)
        
        # Create an instance of the request object
        request_obj = ashnelson_turtlebot3_move_squareRequest()
        
        # Set the parameters for the movement
        request_obj.sideLength = 1.0 
        request_obj.repetitions = 2 
        
        rospy.loginfo(f"Sending Request -> sideLength: {request_obj.sideLength}, repetitions: {request_obj.repetitions}")
        
        # Send the request and wait for the response
        response = square_service_client(request_obj)
        
        # Check the success boolean that the server sends back
        if response.success:
            rospy.loginfo("Success! The robot completed the squares.")
        else:
            rospy.loginfo("Failed! Something went wrong during execution.")
            
        rospy.loginfo("End of service call.")
        
    except rospy.ServiceException as e:
        rospy.logerr(f"Service call failed: {e}")

# Terminal commands to run the server and client
# Terminal 1, start ROS master
# ash@mbpro:~/catkin_ws_rss$ source devel/setup.bash
# ash@mbpro:~/catkin_ws_rss$ roscore

# Terminal 2, launch the server node
# ash@mbpro:~/catkin_ws_rss$ source devel/setup.bash
# ash@mbpro:~/catkin_ws_rss$ rosrun rss2_msgsrv_pkg ashnelson_square_server.py

# Terminal 3, run the client to call the service and trigger the robot movement
# ash@mbpro:~/catkin_ws_rss$ source devel/setup.bash
# ash@mbpro:~/catkin_ws_rss$ rosrun rss2_msgsrv_pkg ashnelson_square_client.py

# %% [markdown]
# # 6. PA-6
# ## a. Question 3, 4, 5
# ### i. Code Snippet:
# 
# **Square client and server code description:**
# To fulfill the requirements of Q3, Q4, and Q5, I developed complementary server and client scripts utilising the custom ***turtlebot_move_square.srv*** message. 
# 
# When the client script is executed, it sends a request object containing ***sideLength = 1.0*** and ***repetitions = 2*** to the server. 
# 
# * **Q3:** The server dynamically extracts the ***request.sideLength*** parameter and divides it by the set ***linear_speed*** 0.2 m/s*** to calculate the exact duration the robot needs to drive forward. This ensures the square scales perfectly to the client's request.
# * **Q4:** The 4-sided movement logic is wrapped inside an outer ***for _ in range(request.repetitions):*** loop. This successfully dictates that the entire square sequence loops exactly as many times as the client dictates.
# * **Q5:** Once all loops resolve cleanly, the final line of the callback explicitly returns ***ashnelson_turtlebot_move_squareResponse(True)***. The client script intercepts this boolean response and logs a success message to the terminal. By testing these scripts together, I observed the robot successfully navigate two 1.0m squares sequentially before halting.
# 
# **Server Output:**
# ![serverOutput.png](attachment:image-2.png)
# 
# **Client Output:**
# ![clientOutput.png](attachment:image.png)
# 
# **Robot Square:**
# ![robotSquarePA6.gif](attachment:robotSquarePA6.gif)


