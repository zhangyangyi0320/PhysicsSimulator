#!/bin/bash

# 安装脚本 - 物理引擎模拟器依赖项
# 适用于Linux系统

echo "开始安装物理引擎模拟器依赖项..."

# 确保系统包是最新的
echo "更新系统包..."
sudo apt-get update
sudo apt-get upgrade -y

# 安装基本开发工具
echo "安装基本开发工具..."
sudo apt-get install -y build-essential cmake git pkg-config

# 安装C++物理库依赖
echo "安装Bullet Physics依赖..."
sudo apt-get install -y libbullet-dev

# 安装Python开发包
echo "安装Python开发包..."
sudo apt-get install -y python3-dev python3-pip python3-venv

# 安装OpenGL相关依赖
echo "安装OpenGL相关依赖..."
sudo apt-get install -y libgl1-mesa-dev libglu1-mesa-dev freeglut3-dev

# 创建Python虚拟环境
echo "创建Python虚拟环境..."
python3 -m venv venv
source venv/bin/activate

# 安装Python依赖
echo "安装Python依赖..."
pip install --upgrade pip
pip install numpy scipy matplotlib
pip install pyopengl pyopengl-accelerate
pip install pyvista vtk
pip install pybullet  # Python绑定的Bullet物理引擎

# 创建requirements.txt文件
echo "创建requirements.txt文件..."
cat > requirements.txt << EOL
numpy>=1.20.0
scipy>=1.7.0
matplotlib>=3.4.0
PyOpenGL>=3.1.5
PyOpenGL-accelerate>=3.1.5
pyvista>=0.32.0
vtk>=9.0.0
pybullet>=3.2.0
EOL

echo "依赖项安装完成！"
echo "请使用以下命令激活虚拟环境："
echo "source venv/bin/activate"