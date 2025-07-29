#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
依赖项检查脚本
用于验证所有必要的库是否已正确安装
"""

import sys
import importlib
import subprocess

def check_module(module_name, min_version=None):
    """检查Python模块是否已安装"""
    try:
        module = importlib.import_module(module_name)
        if hasattr(module, '__version__'):
            version = module.__version__
            print(f"✓ {module_name} 已安装 (版本: {version})")
            
            if min_version and version < min_version:
                print(f"  警告: {module_name} 版本 ({version}) 低于推荐版本 ({min_version})")
        else:
            print(f"✓ {module_name} 已安装 (无版本信息)")
        return True
    except ImportError:
        print(f"✗ {module_name} 未安装")
        return False

def check_bullet_installation():
    """检查Bullet物理引擎是否已安装"""
    try:
        result = subprocess.run(['pkg-config', '--exists', 'bullet'], check=False)
        if result.returncode == 0:
            version = subprocess.check_output(['pkg-config', '--modversion', 'bullet']).decode().strip()
            print(f"✓ Bullet Physics 已安装 (版本: {version})")
            return True
        else:
            print("✗ Bullet Physics 未安装或未找到")
            return False
    except Exception as e:
        print(f"✗ 检查Bullet Physics时出错: {e}")
        return False

def main():
    """主函数"""
    print("检查物理引擎模拟器依赖项...\n")
    
    # 检查Python版本
    python_version = sys.version.split()[0]
    print(f"Python 版本: {python_version}")
    if python_version < "3.7":
        print("警告: 推荐使用Python 3.7或更高版本")
    
    print("\n检查Python库:")
    # 检查核心Python库
    python_modules = [
        ("numpy", "1.20.0"),
        ("scipy", "1.7.0"),
        ("matplotlib", "3.4.0"),
        ("OpenGL", None),  # PyOpenGL
        ("pyvista", "0.32.0"),
        ("vtk", "9.0.0"),
        ("pybullet", "3.2.0")
    ]
    
    all_modules_installed = True
    for module, min_version in python_modules:
        if not check_module(module, min_version):
            all_modules_installed = False
    
    print("\n检查C++库:")
    bullet_installed = check_bullet_installation()
    
    print("\n总结:")
    if all_modules_installed and bullet_installed:
        print("✓ 所有依赖项已正确安装！")
    else:
        print("✗ 部分依赖项未安装，请运行 install_dependencies.sh 脚本安装缺失的依赖项。")

if __name__ == "__main__":
    main()