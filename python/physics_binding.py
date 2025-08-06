#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ctypes
import os
import sys
import numpy as np
from typing import Tuple, List, Optional

# 加载共享库
def load_library():
    """加载物理引擎共享库"""
    # 确定库文件路径
    if sys.platform.startswith('linux'):
        lib_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../build/libPhysicsSimulator.so'))
    elif sys.platform == 'darwin':
        lib_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../build/libPhysicsSimulator.dylib'))
    elif sys.platform == 'win32':
        lib_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../build/PhysicsSimulator.dll'))
    else:
        raise RuntimeError(f"不支持的平台: {sys.platform}")
    
    # 检查库文件是否存在
    if not os.path.exists(lib_path):
        raise FileNotFoundError(f"找不到物理引擎库文件: {lib_path}")
    
    try:
        return ctypes.CDLL(lib_path)
    except Exception as e:
        raise RuntimeError(f"加载物理引擎库失败: {e}")

# 向量类
class Vector3:
    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0):
        self.x = x
        self.y = y
        self.z = z
    
    def __repr__(self):
        return f"Vector3({self.x}, {self.y}, {self.z})"
    
    def to_numpy(self) -> np.ndarray:
        """转换为NumPy数组"""
        return np.array([self.x, self.y, self.z], dtype=np.float32)
    
    @classmethod
    def from_numpy(cls, array: np.ndarray) -> 'Vector3':
        """从NumPy数组创建Vector3"""
        return cls(array[0], array[1], array[2])

# 四元数类
class Quaternion:
    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0, w: float = 1.0):
        self.x = x
        self.y = y
        self.z = z
        self.w = w
    
    def __repr__(self):
        return f"Quaternion({self.x}, {self.y}, {self.z}, {self.w})"
    
    def to_numpy(self) -> np.ndarray:
        """转换为NumPy数组"""
        return np.array([self.x, self.y, self.z, self.w], dtype=np.float32)
    
    @classmethod
    def from_numpy(cls, array: np.ndarray) -> 'Quaternion':
        """从NumPy数组创建Quaternion"""
        return cls(array[0], array[1], array[2], array[3])

# 刚体类型
class BodyType:
    DYNAMIC = 0
    STATIC = 1
    KINEMATIC = 2

# 形状类型
class ShapeType:
    BOX = 0
    SPHERE = 1
    CAPSULE = 2
    CYLINDER = 3
    CONE = 4
    PLANE = 5

# 刚体类
class RigidBody:
    def __init__(self, ptr):
        self.ptr = ptr
    
    def get_position(self) -> Vector3:
        """获取刚体位置"""
        # 这里应该调用C++库中的函数，这里用模拟实现
        # 实际应该通过ctypes调用C++函数
        return Vector3(0, 0, 0)  # 模拟返回值
    
    def get_rotation(self) -> Quaternion:
        """获取刚体旋转"""
        return Quaternion()  # 模拟返回值
    
    def set_position(self, position: Vector3) -> None:
        """设置刚体位置"""
        pass  # 模拟实现
    
    def set_rotation(self, rotation: Quaternion) -> None:
        """设置刚体旋转"""
        pass  # 模拟实现
    
    def apply_force(self, force: Vector3, rel_pos: Optional[Vector3] = None) -> None:
        """施加力"""
        pass  # 模拟实现
    
    def apply_impulse(self, impulse: Vector3, rel_pos: Optional[Vector3] = None) -> None:
        """施加冲量"""
        pass  # 模拟实现
    
    @staticmethod
    def create_box(mass: float, position: Vector3, half_extents: Vector3) -> 'RigidBody':
        """创建盒子刚体"""
        # 模拟实现
        return RigidBody(None)
    
    @staticmethod
    def create_sphere(mass: float, position: Vector3, radius: float) -> 'RigidBody':
        """创建球体刚体"""
        # 模拟实现
        return RigidBody(None)
    
    @staticmethod
    def create_plane(normal: Vector3, constant: float) -> 'RigidBody':
        """创建平面刚体"""
        # 模拟实现
        return RigidBody(None)

# 物理世界类
class PhysicsWorld:
    def __init__(self):
        self.ptr = None
        self.bodies = []
    
    def initialize(self, gravity: Vector3 = Vector3(0, -9.81, 0)) -> None:
        """初始化物理世界"""
        # 模拟实现
        pass
    
    def add_rigid_body(self, body: RigidBody) -> None:
        """添加刚体到物理世界"""
        self.bodies.append(body)
    
    def remove_rigid_body(self, body: RigidBody) -> None:
        """从物理世界移除刚体"""
        if body in self.bodies:
            self.bodies.remove(body)
    
    def step_simulation(self, time_step: float, max_sub_steps: int = 10) -> None:
        """步进模拟"""
        # 模拟实现
        pass
    
    def get_rigid_bodies(self) -> List[RigidBody]:
        """获取所有刚体"""
        return self.bodies