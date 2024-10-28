#!/usr/bin/env python3

import os
from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():

    pkg_dir = get_package_share_directory('my_first_package')
    pkg_launch_dir = os.path.join(pkg_dir, 'launch')

    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(pkg_launch_dir, 'turtle.launch.py')
            ),
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(pkg_launch_dir, 'turtle2.launch.py')
            ),
        ),
    ])