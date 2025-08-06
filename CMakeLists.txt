cmake_minimum_required(VERSION 3.10)
project(PhysicsSimulator)

# 设置C++标准
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# 添加可执行文件
add_executable(PhysicsSimulator
    src/core/PhysicsWorld.cpp
    src/dynamics/RigidBody.cpp
    src/utils/Vector3.cpp
    src/utils/Quaternion.cpp
    examples/basic_simulation.cpp
)

# 包含目录
include_directories(
    include
)

# 查找并链接必要的库
find_package(Threads REQUIRED)

target_link_libraries(PhysicsSimulator
    Threads::Threads
)