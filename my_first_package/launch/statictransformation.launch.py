from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='static_transform_publisher',
            output='screen',
            parameters=[],
            arguments=['1', '2', '3', '0.5', '0.1', '-1.0', 'camera_link', 'laser']
        ),
    ])