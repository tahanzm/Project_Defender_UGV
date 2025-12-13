import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node

def generate_launch_description():
    pkg_name = 'defender_ugv_sim'
    urdf_file_name = 'defender_bot.urdf'
    
    # URDF dosya yolunu oluştur
    urdf_path = os.path.join(
        get_package_share_directory(pkg_name),
        'urdf',
        urdf_file_name)

    # URDF dosyasını oku
    with open(urdf_path, 'r') as inf:
        robot_desc = inf.read()

    return LaunchDescription([
        # 1. Robot State Publisher (BU EKSİKTİ)
        # Robotun modelini ROS ağına tanıtır
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': robot_desc, 'use_sim_time': True}]
        ),

        # 2. Gazebo'yu Başlat
        ExecuteProcess(
            cmd=['gazebo', '--verbose', '-s', 'libgazebo_ros_factory.so', '-s', 'libgazebo_ros_init.so'],
            output='screen'),

        # 3. Robotu Sahneye Koy (Spawn)
        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=['-topic', 'robot_description', '-entity', 'defender_bot', '-z', '0.5'],
            output='screen'),
    ])