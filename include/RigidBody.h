#ifndef RIGID_BODY_H
#define RIGID_BODY_H

#include "Vector3.h"
#include <memory>
#include <string>

namespace PhysicsSimulator {

// 前向声明
class Quaternion;

/**
 * @enum BodyType
 * @brief 刚体类型枚举
 */
enum class BodyType {
    STATIC,     ///< 静态刚体，不受物理影响
    DYNAMIC,    ///< 动态刚体，受物理影响
    KINEMATIC   ///< 运动学刚体，可以移动但不受物理影响
};

/**
 * @enum ShapeType
 * @brief 碰撞形状类型枚举
 */
enum class ShapeType {
    BOX,        ///< 盒体
    SPHERE,     ///< 球体
    CYLINDER,   ///< 圆柱体
    CAPSULE,    ///< 胶囊体
    CONE,       ///< 圆锥体
    PLANE       ///< 平面
};

/**
 * @class RigidBody
 * @brief 刚体类，表示物理世界中的刚体对象
 */
class RigidBody {
public:
    /**
     * @brief 创建一个盒体刚体
     * @param mass 质量
     * @param position 位置
     * @param halfExtents 半尺寸
     * @return 刚体指针
     */
    static RigidBody* createBox(float mass, const Vector3& position, const Vector3& halfExtents);
    
    /**
     * @brief 创建一个球体刚体
     * @param mass 质量
     * @param position 位置
     * @param radius 半径
     * @return 刚体指针
     */
    static RigidBody* createSphere(float mass, const Vector3& position, float radius);
    
    /**
     * @brief 创建一个圆柱体刚体
     * @param mass 质量
     * @param position 位置
     * @param halfExtents 半尺寸
     * @return 刚体指针
     */
    static RigidBody* createCylinder(float mass, const Vector3& position, const Vector3& halfExtents);
    
    /**
     * @brief 创建一个平面刚体
     * @param normal 法线
     * @param constant 常数
     * @return 刚体指针
     */
    static RigidBody* createPlane(const Vector3& normal, float constant);
    
    /**
     * @brief 析构函数
     */
    ~RigidBody();
    
    /**
     * @brief 设置位置
     * @param position 位置
     */
    void setPosition(const Vector3& position);
    
    /**
     * @brief 获取位置
     * @return 位置
     */
    Vector3 getPosition() const;
    
    /**
     * @brief 设置旋转
     * @param rotation 旋转四元数
     */
    void setRotation(const Quaternion& rotation);
    
    /**
     * @brief 获取旋转
     * @return 旋转四元数
     */
    Quaternion getRotation() const;
    
    /**
     * @brief 应用力
     * @param force 力
     */
    void applyForce(const Vector3& force);
    
    /**
     * @brief 应用冲量
     * @param impulse 冲量
     */
    void applyImpulse(const Vector3& impulse);
    
    /**
     * @brief 设置线速度
     * @param velocity 线速度
     */
    void setLinearVelocity(const Vector3& velocity);
    
    /**
     * @brief 获取线速度
     * @return 线速度
     */
    Vector3 getLinearVelocity() const;
    
    /**
     * @brief 设置角速度
     * @param velocity 角速度
     */
    void setAngularVelocity(const Vector3& velocity);
    
    /**
     * @brief 获取角速度
     * @return 角速度
     */
    Vector3 getAngularVelocity() const;
    
    /**
     * @brief 设置摩擦系数
     * @param friction 摩擦系数
     */
    void setFriction(float friction);
    
    /**
     * @brief 设置恢复系数
     * @param restitution 恢复系数
     */
    void setRestitution(float restitution);
    
    /**
     * @brief 设置刚体类型
     * @param type 刚体类型
     */
    void setBodyType(BodyType type);
    
    /**
     * @brief 获取刚体类型
     * @return 刚体类型
     */
    BodyType getBodyType() const;
    
    /**
     * @brief 获取形状类型
     * @return 形状类型
     */
    ShapeType getShapeType() const;
    
    /**
     * @brief 获取质量
     * @return 质量
     */
    float getMass() const;
    
private:
    /**
     * @brief 构造函数
     * @param shapeType 形状类型
     * @param mass 质量
     */
    RigidBody(ShapeType shapeType, float mass);
    
    class RigidBodyImpl;
    std::unique_ptr<RigidBodyImpl> m_impl;
};

} // namespace PhysicsSimulator

#endif // RIGID_BODY_H