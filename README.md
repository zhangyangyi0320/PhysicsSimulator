# PhysicsSimulator

一个高性能物理引擎模拟器，采用C++后端物理库开发，Python前端3D渲染。

## 项目概述

PhysicsSimulator是一个跨平台的物理模拟引擎，旨在提供高性能、高精度的物理模拟功能。该项目结合了C++的高性能计算能力和Python的灵活渲染能力，适用于游戏开发、科学研究、教育演示等多种场景。

### 核心特性

- **高性能计算**：C++编写的物理计算核心，支持多线程加速
- **精确模拟**：支持刚体动力学、软体动力学和流体动力学
- **实时渲染**：Python编写的3D可视化界面，基于OpenGL
- **跨平台支持**：支持Windows、macOS和Linux系统
- **可扩展API**：提供简洁易用的Python接口，方便集成到其他项目中

## 项目结构

```
PhysicsSimulator/
├── src/                  # C++源代码
│   ├── core/             # 核心物理引擎
│   ├── collision/        # 碰撞检测系统
│   ├── dynamics/         # 动力学模拟
│   └── utils/            # 工具函数
├── include/              # C++头文件
├── python/               # Python前端
│   ├── renderer/         # 3D渲染模块
│   └── ui/               # 用户界面
├── build/                # 构建目录
├── tests/                # 测试用例
└── docs/                 # 文档
```

## 技术栈

### 后端 (C++)
- 现代C++标准 (C++17)
- Eigen数学库
- Bullet物理引擎（可选集成）
- CMake构建系统

### 前端 (Python)
- Python 3.7+
- PyOpenGL
- NumPy
- PyQt5(GUI界面)

## 许可证

本项目采用MIT许可证 - 详情请参见 [LICENSE](LICENSE) 文件
