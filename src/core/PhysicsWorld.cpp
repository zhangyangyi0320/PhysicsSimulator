#include "PhysicsWorld.h"
#include "RigidBody.h"
#include <iostream>

namespace PhysicsSimulator {

class PhysicsWorld::PhysicsWorldImpl {
public:
    PhysicsWorldImpl() {
        std::cout << "物理世界实现已创建" << std::endl;
    }
    
    ~PhysicsWorldImpl() {
        std::cout << "物理世界实现已销毁" << std::endl;
    }
    
    void initialize(float gravityX, float gravityY, float gravityZ) {
        std::cout << "初始化物理世界，重力: (" 
                  << gravityX << ", " 
                  << gravityY << ", " 
                  << gravityZ << ")" << std::endl;
    }
    
    void stepSimulation(float timeStep, int maxSubSteps) {
        std::cout << "步进模拟，时间步长: " << timeStep 
                  << ", 最大子步数: " << maxSubSteps << std::endl;
    }
    
    void addRigidBody(RigidBody* body) {
        std::cout << "添加刚体到物理世界" << std::endl;
    }
    
    void removeRigidBody(RigidBody* body) {
        std::cout << "从物理世界移除刚体" << std::endl;
    }
    
    void setGravity(float x, float y, float z) {
        std::cout << "设置重力: (" << x << ", " << y << ", " << z << ")" << std::endl;
    }
    
    Vector3 getGravity() const {
        return Vector3(0.0f, -9.81f, 0.0f);
    }
};

PhysicsWorld::PhysicsWorld() : m_impl(std::make_unique<PhysicsWorldImpl>()) {
    std::cout << "物理世界已创建" << std::endl;
}

PhysicsWorld::~PhysicsWorld() {
    std::cout << "物理世界已销毁" << std::endl;
}

void PhysicsWorld::initialize(float gravityX, float gravityY, float gravityZ) {
    m_impl->initialize(gravityX, gravityY, gravityZ);
}

void PhysicsWorld::stepSimulation(float timeStep, int maxSubSteps) {
    m_impl->stepSimulation(timeStep, maxSubSteps);
}

void PhysicsWorld::addRigidBody(RigidBody* body) {
    m_impl->addRigidBody(body);
}

void PhysicsWorld::removeRigidBody(RigidBody* body) {
    m_impl->removeRigidBody(body);
}

void PhysicsWorld::setGravity(float x, float y, float z) {
    m_impl->setGravity(x, y, z);
}

Vector3 PhysicsWorld::getGravity() const {
    return m_impl->getGravity();
}

} // namespace PhysicsSimulator