#ifndef PHYSICS_WORLD_H
#define PHYSICS_WORLD_H

#include <vector>
#include <memory>

namespace PhysicsSimulator {

// 前向声明
class RigidBody;
class Vector3;

/**
 * @class PhysicsWorld
 * @brief 物理世界类，管理所有物理对象和模拟
 */
class PhysicsWorld {
public:
    /**
     * @brief 构造函数
     * @param gravity 重力向量，默认为(0,-9.81,0)
     */
    PhysicsWorld();
    
    /**
     * @brief 析构函数
     */
    ~PhysicsWorld();
    
    /**
     * @brief 初始化物理世界
     * @param gravityX X轴重力
     * @param gravityY Y轴重力
     * @param gravityZ Z轴重力
     */
    void initialize(float gravityX = 0.0f, float gravityY = -9.81f, float gravityZ = 0.0f);
    
    /**
     * @brief 步进模拟
     * @param timeStep 时间步长
     * @param maxSubSteps 最大子步数
     */
    void stepSimulation(float timeStep, int maxSubSteps = 10);
    
    /**
     * @brief 添加刚体到物理世界
     * @param body 刚体指针
     */
    void addRigidBody(RigidBody* body);
    
    /**
     * @brief 从物理世界移除刚体
     * @param body 刚体指针
     */
    void removeRigidBody(RigidBody* body);
    
    /**
     * @brief 设置重力
     * @param x X轴重力
     * @param y Y轴重力
     * @param z Z轴重力
     */
    void setGravity(float x, float y, float z);
    
    /**
     * @brief 获取重力
     * @return 重力向量
     */
    Vector3 getGravity() const;
    
private:
    class PhysicsWorldImpl;
    std::unique_ptr<PhysicsWorldImpl> m_impl;
};

} // namespace PhysicsSimulator

#endif // PHYSICS_WORLD_H