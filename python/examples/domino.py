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

def run_domino():
    """运行多米诺骨牌示例"""
    # 创建物理世界
    world = PhysicsWorld()
    world.initialize()
    
    # 创建地面
    ground = RigidBody.create_plane(Vector3(0, 1, 0), 0.0)
    world.add_rigid_body(ground)
    
    # 创建多米诺骨牌
    dominos = []
    for i in range(10):
        # 创建一个长方体作为多米诺骨牌
        domino = RigidBody.create_box(
            1.0,  # 质量
            Vector3(i * 2.0, 2.0, 0.0),  # 位置
            Vector3(0.1, 1.0, 0.5)  # 半尺寸
        )
        world.add_rigid_body(domino)
        dominos.append(domino)
    
    # 创建一个球体作为触发器
    ball = RigidBody.create_sphere(
        5.0,  # 质量
        Vector3(-3.0, 5.0, 0.0),  # 位置
        0.5  # 半径
    )
    world.add_rigid_body(ball)
    
    # 给球体一个初始速度
    # 在实际的物理引擎中应该有设置速度的方法
    # 这里只是示意，实际实现可能不同
    
    # 创建渲染器
    renderer = GLRenderer(title="多米诺骨牌示例")
    renderer.set_physics_world(world)
    renderer.run()

if __name__ == "__main__":
    run_domino()