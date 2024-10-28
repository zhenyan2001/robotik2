#!/usr/bin/env python3

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='my_turtle',
            output='screen'),
        Node(
            package='turtlesim',
            executable='draw_square',
            name='draw_square',
            output='log'),
    ])