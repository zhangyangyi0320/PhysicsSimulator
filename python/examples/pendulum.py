#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import time
import numpy as np

# 添加项目根目录到路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from python.physics_binding import Vector3, Quaternion, RigidBody, PhysicsWorld
from python.renderer.gl_renderer import GLRenderer

def run_pendulum():
    """运行单摆示例"""
    # 创建物理世界
    world = PhysicsWorld()
    world.initialize()
    
    # 创建地面
    ground = RigidBody.create_plane(Vector3(0, 1, 0), 0.0)
    world.add_rigid_body(ground)
    
    # 创建固定点（静态球体）
    anchor = RigidBody.create_sphere(0.0, Vector3(0, 10, 0), 0.5)
    world.add_rigid_body(anchor)
    
    # 创建摆锤（动态球体）
    pendulum = RigidBody.create_sphere(1.0, Vector3(0, 5, 0), 1.0)
    world.add_rigid_body(pendulum)
    
    # 创建渲染器
    renderer = GLRenderer(title="单摆示例")
    renderer.set_physics_world(world)
    renderer.run()

if __name__ == "__main__":
    run_pendulum()