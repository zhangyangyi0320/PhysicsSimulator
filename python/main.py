#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import argparse

def main():
    """主函数"""
    parser = argparse.ArgumentParser(description="物理模拟器图形界面")
    parser.add_argument("--headless", action="store_true", help="无界面模式")
    parser.add_argument("--example", type=str, help="运行示例场景")
    args = parser.parse_args()
    
    # 添加项目根目录到路径
    project_root = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(project_root)
    
    if args.headless:
        # 无界面模式
        from python.physics_binding import PhysicsWorld, RigidBody, Vector3
        
        print("运行无界面模拟...")
        world = PhysicsWorld()
        world.initialize()
        
        # 创建地面
        ground = RigidBody.create_plane(Vector3(0, 1, 0), 0.0)
        world.add_rigid_body(ground)
        
        # 创建盒子
        box = RigidBody.create_box(1.0, Vector3(0, 10, 0), Vector3(1, 1, 1))
        world.add_rigid_body(box)
        
        # 模拟10秒
        time_step = 1.0 / 60.0
        for i in range(600):
            world.step_simulation(time_step)
            
            # 每60帧打印一次位置
            if i % 60 == 0:
                pos = box.get_position()
                print(f"第{i//60}秒: 盒子位置 ({pos.x}, {pos.y}, {pos.z})")
        
        # 清理
        world.remove_rigid_body(box)
        world.remove_rigid_body(ground)
    
    elif args.example:
        # 运行示例场景
        if args.example == "pendulum":
            from examples.pendulum import run_pendulum
            run_pendulum()
        elif args.example == "domino":
            from examples.domino import run_domino
            run_domino()
        else:
            print(f"未知示例: {args.example}")
    
    else:
        # 启动图形界面
        import tkinter as tk
        from python.ui.simulator_ui import PhysicsSimulatorUI
        
        root = tk.Tk()
        app = PhysicsSimulatorUI(root)
        root.mainloop()

if __name__ == "__main__":
    main()