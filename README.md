# ROS Kinematics & Autonomous Control (TurtleBot3)

[![ROS Noetic](https://img.shields.io/badge/ROS-Noetic-22314E?style=flat-square&logo=ros&logoColor=white)](http://wiki.ros.org/noetic)
[![Gazebo Sim](https://img.shields.io/badge/Simulator-Gazebo-FF9900?style=flat-square&logo=gazebo&logoColor=white)](https://gazebosim.org/)
[![Python 3](https://img.shields.io/badge/Language-Python%203-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)

This repository contains the practical implementation suite of autonomous robot control strategies, kinematics scripts, and custom distributed communication protocols developed for the **Robotics Science and Systems** course at Manchester Metropolitan University. 

The codebase targets a **TurtleBot3 Burger** differential drive mobile robot simulated within an empty **Gazebo world**, executing both open-loop velocity profiles and high-precision closed-loop control leveraging odometry feedback layers.

---

## 🚀 Key Technical Architectures

### 1. Closed-Loop Odometry Tracking (`ashnelson_pubsub.py`)
* Implements a feedback control mechanism utilizing the robot's onboard sensor fusion streams.
* Subscribes asynchronously to the `/odom` navigation topic and extracts real-time $X$ and $Y$ spatial coordinates.
* Calculates current displacement from the starting origin using a continuous Euclidean distance tracking formula ($d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$).
* Publishes high-frequency `geometry_msgs/Twist` velocity matrices to the `/cmd_vel` multiplexer, executing a hard software stop commands the micro-moment a specified target threshold is achieved.

### 2. Custom Service Message Compilation (`.srv` Protocol)
* Configures custom remote procedure call structures inside the Catkin compilation pipeline by setting explicit data parameters (`float64 sideLength` and `int32 repetitions`) backed by a return state (`bool success`).
* Establishes workspace package generation parameters by explicitly integrating dependencies across `CMakeLists.txt` (`message_generation`, `generate_messages`) and `package.xml` (`message_runtime`) properties.

### 3. Client-Server Velocity Sequencers (`ashnelson_square_server.py`)
* Handles parameter-driven open-loop geometry trajectories.
* Translates desired dimension properties into explicit velocity timelines via duration-matching parameters ($time = \frac{distance}{speed}$).
* Employs time-sliced state steps managed via precise `rospy.sleep()` schedules and isolated dampening pauses to clear residual hardware inertia and tracking drift between rotational pivots.

---

## 🛠️ Tech Stack & Dependencies

* **Core OS Environment:** Ubuntu 20.04 LTS / Linux Bash
* **Middleware Middleware:** Robot Operating System (ROS Noetic Architecture)
* **Simulation Engine:** Gazebo 11 Physics Simulator
* **Target Hardware Profile:** TurtleBot3 Burger Configuration
* **Primary Language Framework:** Python 3 (including `rospy`, `math`, `geometry_msgs`, `nav_msgs`)

---

## 📂 Repository Structure

```text
rss_linux_pkg/
├── launch/
│   └── ashnelson_publisher_line.launch   # Streamlines straight-line node startup
├── scripts/
│   ├── ash_nelson.py                    # Workspace sanity execution test node
│   └── ashnelson_publisher_line.py       # Hard-locked linear axis movement logic
rss2_msgsrv_pkg/
├── launch/
│   ├── ashnelson_pubsub.launch           # Synchronous pub/sub node initializer
│   └── ashnelson_server_client.launch    # Multi-node server-client bootstrap script
├── scripts/
│   ├── ashnelson_pubsub.py               # Real-time closed-loop tracking engine
│   ├── ashnelson_square_client.py        # Custom message request generator
│   ├── ashnelson_square_server.py        # Target geometry velocity engine
│   ├── pw_srv_client.py                  # Service client initiator
│   └── pw_srv_server.py                  # 30-second multi-phase action profile server
└── srv/
    └── ashnelson_turtlebot3_move_square.srv # Custom compiled message structure
