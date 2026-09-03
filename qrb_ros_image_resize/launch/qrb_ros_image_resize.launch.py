# Copyright (c) 2024 Qualcomm Innovation Center, Inc. All rights reserved.
# SPDX-License-Identifier: BSD-3-Clause-Clear

import os
from ament_index_python.packages import get_package_share_directory
import launch
from launch_ros.actions import ComposableNodeContainer
from launch_ros.descriptions import ComposableNode

# this is an example to launch resize node.
# if you want to run the test node you should build test node,
# and as the follow creat two new launch files to launch the #TestPubNode and #TestSubNode.

def generate_launch_description():
    composable_nodes = [
        ComposableNode(
            package='qrb_ros_image_resize',
            plugin='qrb_ros::resize::ResizeNode',
            name='qrb_ros_image_resize',
            parameters=[{
                'use_scale': False,
                'height': 400,
                'width': 400,
                #'use_scale': True,
                #'scale_height': 0.25,
                #'scale_width': 0.25,
            }]),
    ]

    container = ComposableNodeContainer(
        name='resize',
        namespace='container',
        package='rclcpp_components',
        executable='component_container',
        composable_node_descriptions=composable_nodes,
        output='screen'
    )

    return launch.LaunchDescription([container])
