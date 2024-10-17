# Environment
* ubuntu 20.04
* ros foxy
* tr3d with latest commit


## about server

mmdetection3d environment: https://mmdetection3d.readthedocs.io/zh-cn/latest/get_started.html

make sure this can run https://mmdetection3d.readthedocs.io/zh-cn/latest/get_started.html#id5


## about robot

robot and server communicate with wifi, using cyclone as dds

under untrustworthy network condition, strongly **recommend** using pcl to preprocess pointcloud using for 3d object detection, for example https://github.com/GitRepJo/pcl_example


## about mmdet3d
[model zoo](https://github.com/open-mmlab/mmdetection3d/blob/main/README_zh-CN.md#%E5%9F%BA%E5%87%86%E6%B5%8B%E8%AF%95%E5%92%8C%E6%A8%A1%E5%9E%8B%E5%BA%93)

download weight and config (if pulled mmdet3d repo, the configs in `mmdetection3d/projects` or `mmdetection3d/configs` )

# Build
```
colcon build --packages-select mmdet3d_ros2 --symlink
# modify the python interpreter path
sed -i 's,/usr/bin/python3,/root/miniconda3/bin/python,g' install/mmdet3d_ros2/lib/mmdet3d_ros2/infer_node
```


# Run
```
source install/setup.bash
ros2 launch mmdet3d_ros2 mmdet3d_infer_launch.py
```