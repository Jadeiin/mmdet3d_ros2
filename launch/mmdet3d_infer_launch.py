from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='mmdet3d_ros2',
            executable='infer_node',
            name='mmdet3d_infer_node',
            parameters=[
                {'config_file': '/root/mmdetection3d/configs/tr3d/tr3d_scannet-3d-18class.py'},
                {'checkpoint_file': '/root/mmdetection3d/demo/checkpoints/tr3d_scannet.pth'},
                {'score_threshold': 0.75},
                {'infer_device': 'cuda:0'},
                {'nms_interval': 0.5},
                {'point_cloud_qos': 'best_effort'},
                {'point_cloud_frame': 'camera'},
                {'point_cloud_topic': '/camera_point'}
            ]
        )
    ])
