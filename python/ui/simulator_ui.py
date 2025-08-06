#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import threading
import time
import numpy as np

# 添加项目根目录到路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from python.physics_binding import Vector3, Quaternion, RigidBody, PhysicsWorld, BodyType, ShapeType
from python.renderer.gl_renderer import GLRenderer

class PhysicsSimulatorUI:
    """物理模拟器UI类"""
    
    def __init__(self, root):
        """初始化UI"""
        self.root = root
        self.root.title("物理模拟器")
        self.root.geometry("1200x800")
        
        # 创建物理世界
        self.physics_world = PhysicsWorld()
        self.physics_world.initialize()
        
        # 创建渲染器
        self.renderer = None
        self.render_thread = None
        
        # 创建UI组件
        self.create_widgets()
        
        # 示例对象列表
        self.objects = []
    
    def create_widgets(self):
        """创建UI组件"""
        # 创建主框架
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # 创建左侧控制面板
        control_frame = ttk.LabelFrame(main_frame, text="控制面板")
        control_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)
        
        # 创建对象控制区域
        obj_frame = ttk.LabelFrame(control_frame, text="对象创建")
        obj_frame.pack(fill=tk.X, padx=5, pady=5)
        
        # 对象类型选择
        ttk.Label(obj_frame, text="对象类型:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.obj_type = tk.StringVar(value="盒子")
        obj_type_combo = ttk.Combobox(obj_frame, textvariable=self.obj_type, values=["盒子", "球体", "平面"])
        obj_type_combo.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)
        
        # 位置输入
        ttk.Label(obj_frame, text="位置 (x, y, z):").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        pos_frame = ttk.Frame(obj_frame)
        pos_frame.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)
        
        self.pos_x = tk.DoubleVar(value=0.0)
        self.pos_y = tk.DoubleVar(value=5.0)
        self.pos_z = tk.DoubleVar(value=0.0)
        
        ttk.Entry(pos_frame, textvariable=self.pos_x, width=5).pack(side=tk.LEFT, padx=2)
        ttk.Entry(pos_frame, textvariable=self.pos_y, width=5).pack(side=tk.LEFT, padx=2)
        ttk.Entry(pos_frame, textvariable=self.pos_z, width=5).pack(side=tk.LEFT, padx=2)
        
        # 尺寸/半径输入
        self.size_label = ttk.Label(obj_frame, text="尺寸 (x, y, z):")
        self.size_label.grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
        
        size_frame = ttk.Frame(obj_frame)
        size_frame.grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)
        
        self.size_x = tk.DoubleVar(value=1.0)
        self.size_y = tk.DoubleVar(value=1.0)
        self.size_z = tk.DoubleVar(value=1.0)
        
        self.size_x_entry = ttk.Entry(size_frame, textvariable=self.size_x, width=5)
        self.size_x_entry.pack(side=tk.LEFT, padx=2)
        self.size_y_entry = ttk.Entry(size_frame, textvariable=self.size_y, width=5)
        self.size_y_entry.pack(side=tk.LEFT, padx=2)
        self.size_z_entry = ttk.Entry(size_frame, textvariable=self.size_z, width=5)
        self.size_z_entry.pack(side=tk.LEFT, padx=2)
        
        # 质量输入
        ttk.Label(obj_frame, text="质量:").grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)
        self.mass = tk.DoubleVar(value=1.0)
        ttk.Entry(obj_frame, textvariable=self.mass, width=10).grid(row=3, column=1, sticky=tk.W, padx=5, pady=5)
        
        # 创建对象按钮
        ttk.Button(obj_frame, text="创建对象", command=self.create_object).grid(row=4, column=0, columnspan=2, pady=10)
        
        # 创建模拟控制区域
        sim_frame = ttk.LabelFrame(control_frame, text="模拟控制")
        sim_frame.pack(fill=tk.X, padx=5, pady=5)
        
        # 重力控制
        ttk.Label(sim_frame, text="重力 (x, y, z):").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        gravity_frame = ttk.Frame(sim_frame)
        gravity_frame.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)
        
        self.gravity_x = tk.DoubleVar(value=0.0)
        self.gravity_y = tk.DoubleVar(value=-9.81)
        self.gravity_z = tk.DoubleVar(value=0.0)
        
        ttk.Entry(gravity_frame, textvariable=self.gravity_x, width=5).pack(side=tk.LEFT, padx=2)
        ttk.Entry(gravity_frame, textvariable=self.gravity_y, width=5).pack(side=tk.LEFT, padx=2)
        ttk.Entry(gravity_frame, textvariable=self.gravity_z, width=5).pack(side=tk.LEFT, padx=2)
        
        # 时间步长控制
        ttk.Label(sim_frame, text="时间步长:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.time_step = tk.DoubleVar(value=1.0/60.0)
        ttk.Entry(sim_frame, textvariable=self.time_step, width=10).grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)
        
        # 模拟控制按钮
        button_frame = ttk.Frame(sim_frame)
        button_frame.grid(row=2, column=0, columnspan=2, pady=10)
        
        ttk.Button(button_frame, text="开始", command=self.start_simulation).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="暂停", command=self.pause_simulation).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="重置", command=self.reset_simulation).pack(side=tk.LEFT, padx=5)
        
        # 创建对象列表
        list_frame = ttk.LabelFrame(control_frame, text="对象列表")
        list_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.object_list = ttk.Treeview(list_frame, columns=("类型", "位置", "质量"), show="headings")
        self.object_list.heading("类型", text="类型")
        self.object_list.heading("位置", text="位置")
        self.object_list.heading("质量", text="质量")
        self.object_list.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # 删除对象按钮
        ttk.Button(list_frame, text="删除选中对象", command=self.delete_object).pack(pady=5)
        
        # 创建右侧渲染区域
        render_frame = ttk.LabelFrame(main_frame, text="渲染视图")
        render_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # 渲染控制按钮
        ttk.Button(render_frame, text="启动渲染器", command=self.start_renderer).pack(pady=10)
        
        # 对象类型变更事件
        obj_type_combo.bind("<<ComboboxSelected>>", self.on_obj_type_change)
    
    def on_obj_type_change(self, event):
        """对象类型变更处理"""
        obj_type = self.obj_type.get()
        
        if obj_type == "球体":
            self.size_label.config(text="半径:")
            self.size_y_entry.pack_forget()
            self.size_z_entry.pack_forget()
        elif obj_type == "平面":
            self.size_label.config(text="法向量:")
            self.size_y_entry.pack(side=tk.LEFT, padx=2)
            self.size_z_entry.pack(side=tk.LEFT, padx=2)
        else:  # 盒子
            self.size_label.config(text="尺寸 (x, y, z):")
            self.size_y_entry.pack(side=tk.LEFT, padx=2)
            self.size_z_entry.pack(side=tk.LEFT, padx=2)
    
    def create_object(self):
        """创建物理对象"""
        obj_type = self.obj_type.get()
        position = Vector3(self.pos_x.get(), self.pos_y.get(), self.pos_z.get())
        mass = self.mass.get()
        
        body = None
        
        if obj_type == "盒子":
            half_extents = Vector3(self.size_x.get(), self.size_y.get(), self.size_z.get())
            body = RigidBody.create_box(mass, position, half_extents)
            obj_info = {"type": "盒子", "position": position, "half_extents": half_extents, "mass": mass}
        
        elif obj_type == "球体":
            radius = self.size_x.get()
            body = RigidBody.create_sphere(mass, position, radius)
            obj_info = {"type": "球体", "position": position, "radius": radius, "mass": mass}
        
        elif obj_type == "平面":
            normal = Vector3(self.size_x.get(), self.size_y.get(), self.size_z.get())
            constant = 0.0  # 平面常数，通常为0
            body = RigidBody.create_plane(normal, constant)
            obj_info = {"type": "平面", "normal": normal, "constant": constant, "mass": 0.0}
        
        if body:
            self.physics_world.add_rigid_body(body)
            self.objects.append((body, obj_info))
            
            # 更新对象列表
            pos_str = f"({position.x:.1f}, {position.y:.1f}, {position.z:.1f})"
            self.object_list.insert("", "end", values=(obj_type, pos_str, mass))
    
    def delete_object(self):
        """删除选中的物理对象"""
        selected = self.object_list.selection()
        if selected:
            index = self.object_list.index(selected[0])
            if 0 <= index < len(self.objects):
                body, _ = self.objects[index]
                self.physics_world.remove_rigid_body(body)
                del self.objects[index]
                self.object_list.delete(selected[0])
    
    def start_renderer(self):
        """启动渲染器"""
        if self.render_thread and self.render_thread.is_alive():
            messagebox.showinfo("提示", "渲染器已经在运行")
            return
        
        # 创建并启动渲染线程
        self.render_thread = threading.Thread(target=self.run_renderer)
        self.render_thread.daemon = True
        self.render_thread.start()
    
    def run_renderer(self):
        """运行渲染器"""
        self.renderer = GLRenderer()
        self.renderer.set_physics_world(self.physics_world)
        self.renderer.run()
    
    def start_simulation(self):
        """开始模拟"""
        if self.renderer:
            self.renderer.paused = False
    
    def pause_simulation(self):
        """暂停模拟"""
        if self.renderer:
            self.renderer.paused = True
    
    def reset_simulation(self):
        """重置模拟"""
        # 清除所有对象
        for body, _ in self.objects:
            self.physics_world.remove_rigid_body(body)
        
        self.objects.clear()
        self.object_list.delete(*self.object_list.get_children())
        
        # 重新初始化物理世界
        gravity = Vector3(self.gravity_x.get(), self.gravity_y.get(), self.gravity_z.get())
        self.physics_world.initialize(gravity)

def main():
    """主函数"""
    root = tk.Tk()
    app = PhysicsSimulatorUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()