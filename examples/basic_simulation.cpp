#include "PhysicsWorld.h"
#include "RigidBody.h"
#include <iostream>

int main() {
    std::cout << "=== 物理引擎演示 ===" << std::endl;
    
    // 创建物理世界
    PhysicsSimulator::PhysicsWorld world;
    world.initialize();
    
    // 创建地面(静态平面)
    PhysicsSimulator::RigidBody* ground = PhysicsSimulator::RigidBody::createPlane(
        PhysicsSimulator::Vector3(0, 1, 0), 0.0f);
    world.addRigidBody(ground);
    
    // 创建一个盒子
    PhysicsSimulator::RigidBody* box = PhysicsSimulator::RigidBody::createBox(
        1.0f, 
        PhysicsSimulator::Vector3(0, 10, 0), 
        PhysicsSimulator::Vector3(1, 1, 1));
    world.addRigidBody(box);
    
    // 模拟10秒
    float timeStep = 1.0f / 60.0f;
    for (int i = 0; i < 600; ++i) {
        world.stepSimulation(timeStep);
        
        // 每60帧打印一次位置
        if (i % 60 == 0) {
            PhysicsSimulator::Vector3 pos = box->getPosition();
            std::cout << "第" << i/60 << "秒: 盒子位置 (" 
                      << pos.getX() << ", " 
                      << pos.getY() << ", " 
                      << pos.getZ() << ")" << std::endl;
        }
    }
    
    // 清理
    world.removeRigidBody(box);
    world.removeRigidBody(ground);
    delete box;
    delete ground;
    
    return 0;
}