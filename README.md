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
├── examples/             # 示例程序
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
- PyQt5/PySide2 (GUI界面)

## 安装与使用

### 依赖项
- C++17兼容的编译器 (GCC 7+, Clang 5+, MSVC 2017+)
- Python 3.7+
- CMake 3.10+
- Git

### 构建步骤

```bash
# 克隆仓库
git clone https://github.com/yourusername/PhysicsSimulator.git
cd PhysicsSimulator

# 构建C++库
mkdir -p build && cd build
cmake ..
make

# 安装Python依赖
cd ../python
pip install -r requirements.txt
```

### 运行示例

```bash
# 从项目根目录
python examples/basic_simulation.py
```

## 使用示例

```python
from physics_simulator import Simulator, RigidBody, Vector3

# 创建模拟器实例
sim = Simulator()

# 添加一个刚体
box = RigidBody.create_box(1.0, 1.0, 1.0)
box.position = Vector3(0, 5, 0)
sim.add_body(box)

# 添加地面
ground = RigidBody.create_plane()
ground.is_static = True
sim.add_body(ground)

# 运行模拟
sim.run_with_visualization()
```

## 贡献指南

欢迎贡献代码、报告问题或提出新功能建议。请遵循以下步骤：

1. Fork本仓库
2. 创建您的特性分支 (`git checkout -b feature/amazing-feature`)
3. 提交您的更改 (`git commit -m 'Add some amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 打开Pull Request

## 许可证

本项目采用MIT许可证 - 详情请参见 [LICENSE](LICENSE) 文件

## 联系方式

项目维护者 - [您的姓名](mailto:your.email@example.com)

项目链接: [https://github.com/yourusername/PhysicsSimulator](https://github.com/yourusername/PhysicsSimulator)