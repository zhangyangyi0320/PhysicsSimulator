#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import time
from typing import List, Tuple, Dict, Any, Optional

# 导入物理引擎绑定
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from physics_binding import Vector3, Quaternion, RigidBody, PhysicsWorld, ShapeType

class GLRenderer:
    """OpenGL渲染器类"""
    
    def __init__(self, width: int = 800, height: int = 600, title: str = "物理模拟器"):
        """初始化渲染器"""
        self.width = width
        self.height = height
        self.title = title
        
        # 物理世界
        self.physics_world = None
        
        # 渲染对象
        self.render_objects = {}
        
        # 相机参数
        self.camera_distance = 20.0
        self.camera_azimuth = 45.0
        self.camera_elevation = 30.0
        self.camera_target = [0.0, 0.0, 0.0]
        
        # 鼠标状态
        self.mouse_buttons = [False, False, False]
        self.mouse_pos = [0, 0]
        
        # 帧率控制
        self.last_time = 0
        self.frame_count = 0
        self.fps = 0
        
        # 物理模拟参数
        self.time_step = 1.0 / 60.0
        self.paused = False
    
    def init_gl(self):
        """初始化OpenGL"""
        glClearColor(0.2, 0.2, 0.2, 1.0)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glEnable(GL_COLOR_MATERIAL)
        
        # 设置光照
        light_position = [10.0, 10.0, 10.0, 1.0]
        light_ambient = [0.2, 0.2, 0.2, 1.0]
        light_diffuse = [0.8, 0.8, 0.8, 1.0]
        light_specular = [1.0, 1.0, 1.0, 1.0]
        
        glLightfv(GL_LIGHT0, GL_POSITION, light_position)
        glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
        glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)
    
    def resize(self, width: int, height: int):
        """窗口大小改变回调"""
        self.width = width
        self.height = height
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45.0, width / height, 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)
    
    def set_camera(self):
        """设置相机位置"""
        glLoadIdentity()
        
        # 计算相机位置
        x = self.camera_distance * np.cos(np.radians(self.camera_elevation)) * np.cos(np.radians(self.camera_azimuth))
        y = self.camera_distance * np.sin(np.radians(self.camera_elevation))
        z = self.camera_distance * np.cos(np.radians(self.camera_elevation)) * np.sin(np.radians(self.camera_azimuth))
        
        # 设置相机
        gluLookAt(
            x, y, z,  # 相机位置
            *self.camera_target,  # 目标点
            0.0, 1.0, 0.0  # 上方向
        )
    
    def draw_grid(self, size: int = 10, step: float = 1.0):
        """绘制网格"""
        glDisable(GL_LIGHTING)
        glBegin(GL_LINES)
        glColor3f(0.5, 0.5, 0.5)
        
        for i in range(-size, size + 1):
            glVertex3f(i * step, 0, -size * step)
            glVertex3f(i * step, 0, size * step)
            
            glVertex3f(-size * step, 0, i * step)
            glVertex3f(size * step, 0, i * step)
        
        glEnd()
        glEnable(GL_LIGHTING)
    
    def draw_axes(self, length: float = 5.0):
        """绘制坐标轴"""
        glDisable(GL_LIGHTING)
        glBegin(GL_LINES)
        
        # X轴 (红色)
        glColor3f(1.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(length, 0.0, 0.0)
        
        # Y轴 (绿色)
        glColor3f(0.0, 1.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, length, 0.0)
        
        # Z轴 (蓝色)
        glColor3f(0.0, 0.0, 1.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, length)
        
        glEnd()
        glEnable(GL_LIGHTING)
    
    def draw_box(self, half_extents: Vector3):
        """绘制盒子"""
        glPushMatrix()
        glScalef(half_extents.x * 2, half_extents.y * 2, half_extents.z * 2)
        glutSolidCube(1.0)
        glPopMatrix()
    
    def draw_sphere(self, radius: float):
        """绘制球体"""
        glutSolidSphere(radius, 20, 20)
    
    def draw_plane(self):
        """绘制平面"""
        glPushMatrix()
        glScalef(10.0, 0.01, 10.0)
        glutSolidCube(1.0)
        glPopMatrix()
    
    def draw_rigid_body(self, body: RigidBody):
        """绘制刚体"""
        # 获取刚体位置和旋转
        pos = body.get_position()
        rot = body.get_rotation()
        
        # 设置变换
        glPushMatrix()
        glTranslatef(pos.x, pos.y, pos.z)
        
        # 应用旋转 (四元数转换为旋转矩阵)
        # 简化实现，实际应该使用四元数转换为旋转矩阵
        
        # 根据刚体类型绘制不同形状
        shape_type = ShapeType.BOX  # 假设为盒子，实际应从刚体获取
        
        if shape_type == ShapeType.BOX:
            glColor3f(0.8, 0.2, 0.2)
            self.draw_box(Vector3(1.0, 1.0, 1.0))  # 假设尺寸，实际应从刚体获取
        elif shape_type == ShapeType.SPHERE:
            glColor3f(0.2, 0.8, 0.2)
            self.draw_sphere(1.0)  # 假设半径，实际应从刚体获取
        elif shape_type == ShapeType.PLANE:
            glColor3f(0.5, 0.5, 0.5)
            self.draw_plane()
        
        glPopMatrix()
    
    def display(self):
        """显示回调"""
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        # 设置相机
        self.set_camera()
        
        # 绘制网格和坐标轴
        self.draw_grid()
        self.draw_axes()
        
        # 绘制所有刚体
        if self.physics_world:
            for body in self.physics_world.get_rigid_bodies():
                self.draw_rigid_body(body)
        
        # 显示帧率
        self.calculate_fps()
        self.display_text(f"FPS: {self.fps:.1f}", 10, 20)
        
        glutSwapBuffers()
    
    def calculate_fps(self):
        """计算帧率"""
        current_time = time.time()
        self.frame_count += 1
        
        if current_time - self.last_time >= 1.0:
            self.fps = self.frame_count / (current_time - self.last_time)
            self.frame_count = 0
            self.last_time = current_time
    
    def display_text(self, text: str, x: int, y: int):
        """显示文本"""
        glDisable(GL_LIGHTING)
        glMatrixMode(GL_PROJECTION)
        glPushMatrix()
        glLoadIdentity()
        glOrtho(0, self.width, 0, self.height, -1, 1)
        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()
        glLoadIdentity()
        
        glColor3f(1.0, 1.0, 1.0)
        glRasterPos2i(x, self.height - y)
        
        for c in text:
            glutBitmapCharacter(GLUT_BITMAP_9_BY_15, ord(c))
        
        glMatrixMode(GL_PROJECTION)
        glPopMatrix()
        glMatrixMode(GL_MODELVIEW)
        glPopMatrix()
        glEnable(GL_LIGHTING)
    
    def idle(self):
        """空闲回调"""
        if self.physics_world and not self.paused:
            self.physics_world.step_simulation(self.time_step)
        glutPostRedisplay()
    
    def keyboard(self, key, x, y):
        """键盘回调"""
        if key == b' ':
            self.paused = not self.paused
        elif key == b'r':
            # 重置模拟
            pass
        elif key == b'q' or key == b'\x1b':  # ESC键
            sys.exit(0)
    
    def mouse(self, button, state, x, y):
        """鼠标回调"""
        if button < 3:
            self.mouse_buttons[button] = (state == GLUT_DOWN)
        
        self.mouse_pos = [x, y]
    
    def motion(self, x, y):
        """鼠标移动回调"""
        dx = x - self.mouse_pos[0]
        dy = y - self.mouse_pos[1]
        
        if self.mouse_buttons[0]:  # 左键拖动
            self.camera_azimuth += dx * 0.5
            self.camera_elevation += dy * 0.5
            
            # 限制仰角
            if self.camera_elevation > 89.0:
                self.camera_elevation = 89.0
            if self.camera_elevation < -89.0:
                self.camera_elevation = -89.0
        
        if self.mouse_buttons[2]:  # 右键拖动
            self.camera_distance += dy * 0.1
            
            # 限制距离
            if self.camera_distance < 1.0:
                self.camera_distance = 1.0
            if self.camera_distance > 100.0:
                self.camera_distance = 100.0
        
        self.mouse_pos = [x, y]
    
    def set_physics_world(self, world: PhysicsWorld):
        """设置物理世界"""
        self.physics_world = world
    
    def run(self):
        """运行渲染循环"""
        # 初始化GLUT
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
        glutInitWindowSize(self.width, self.height)
        glutCreateWindow(self.title)
        
        # 设置回调
        glutDisplayFunc(self.display)
        glutReshapeFunc(self.resize)
        glutKeyboardFunc(self.keyboard)
        glutMouseFunc(self.mouse)
        glutMotionFunc(self.motion)
        glutIdleFunc(self.idle)
        
        # 初始化OpenGL
        self.init_gl()
        
        # 开始主循环
        glutMainLoop()