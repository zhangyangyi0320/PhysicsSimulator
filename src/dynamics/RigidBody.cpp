#include "RigidBody.h"
#include "Quaternion.h"
#include <iostream>

namespace PhysicsSimulator {

class RigidBody::RigidBodyImpl {
public:
    RigidBodyImpl(ShapeType shapeType, float mass) 
        : m_shapeType(shapeType), m_mass(mass), m_bodyType(BodyType::DYNAMIC) {
        std::cout << "刚体实现已创建，形状类型: " << static_cast<int>(shapeType) 
                  << ", 质量: " << mass << std::endl;
    }
    
    ~RigidBodyImpl() {
        std::cout << "刚体实现已销毁" << std::endl;
    }
    
    void setPosition(const Vector3& position) {
        std::cout << "设置刚体位置: (" 
                  << position.getX() << ", " 
                  << position.getY() << ", " 
                  << position.getZ() << ")" << std::endl;
    }
    
    Vector3 getPosition() const {
        return Vector3(0.0f, 0.0f, 0.0f);
    }
    
    void setRotation(const Quaternion& rotation) {
        std::cout << "设置刚体旋转: (" 
                  << rotation.getX() << ", " 
                  << rotation.getY() << ", " 
                  << rotation.getZ() << ", " 
                  << rotation.getW() << ")" << std::endl;
    }
    
    Quaternion getRotation() const {
        return Quaternion(0.0f, 0.0f, 0.0f, 1.0f);
    }
    
    void applyForce(const Vector3& force) {
        std::cout << "应用力: (" 
                  << force.getX() << ", " 
                  << force.getY() << ", " 
                  << force.getZ() << ")" << std::endl;
    }
    
    void applyImpulse(const Vector3& impulse) {
        std::cout << "应用冲量: (" 
                  << impulse.getX() << ", " 
                  << impulse.getY() << ", " 
                  << impulse.getZ() << ")" << std::endl;
    }
    
    void setLinearVelocity(const Vector3& velocity) {
        std::cout << "设置线速度: (" 
                  << velocity.getX() << ", " 
                  << velocity.getY() << ", " 
                  << velocity.getZ() << ")" << std::endl;
    }
    
    Vector3 getLinearVelocity() const {
        return Vector3(0.0f, 0.0f, 0.0f);
    }
    
    void setAngularVelocity(const Vector3& velocity) {
        std::cout << "设置角速度: (" 
                  << velocity.getX() << ", " 
                  << velocity.getY() << ", " 
                  << velocity.getZ() << ")" << std::endl;
    }
    
    Vector3 getAngularVelocity() const {
        return Vector3(0.0f, 0.0f, 0.0f);
    }
    
    void setFriction(float friction) {
        std::cout << "设置摩擦系数: " << friction << std::endl;
    }
    
    void setRestitution(float restitution) {
        std::cout << "设置恢复系数: " << restitution << std::endl;
    }
    
    void setBodyType(BodyType type) {
        m_bodyType = type;
        std::cout << "设置刚体类型: " << static_cast<int>(type) << std::endl;
    }
    
    BodyType getBodyType() const {
        return m_bodyType;
    }
    
    ShapeType getShapeType() const {
        return m_shapeType;
    }
    
    float getMass() const {
        return m_mass;
    }
    
private:
    ShapeType m_shapeType;
    float m_mass;
    BodyType m_bodyType;
};

RigidBody* RigidBody::createBox(float mass, const Vector3& position, const Vector3& halfExtents) {
    RigidBody* body = new RigidBody(ShapeType::BOX, mass);
    body->setPosition(position);
    return body;
}

RigidBody* RigidBody::createSphere(float mass, const Vector3& position, float radius) {
    RigidBody* body = new RigidBody(ShapeType::SPHERE, mass);
    body->setPosition(position);
    return body;
}

RigidBody* RigidBody::createCylinder(float mass, const Vector3& position, const Vector3& halfExtents) {
    RigidBody* body = new RigidBody(ShapeType::CYLINDER, mass);
    body->setPosition(position);
    return body;
}

RigidBody* RigidBody::createPlane(const Vector3& normal, float constant) {
    RigidBody* body = new RigidBody(ShapeType::PLANE, 0.0f);
    body->setBodyType(BodyType::STATIC);
    return body;
}

RigidBody::RigidBody(ShapeType shapeType, float mass) 
    : m_impl(std::make_unique<RigidBodyImpl>(shapeType, mass)) {
    std::cout << "刚体已创建" << std::endl;
}

RigidBody::~RigidBody() {
    std::cout << "刚体已销毁" << std::endl;
}

void RigidBody::setPosition(const Vector3& position) {
    m_impl->setPosition(position);
}

Vector3 RigidBody::getPosition() const {
    return m_impl->getPosition();
}

void RigidBody::setRotation(const Quaternion& rotation) {
    m_impl->setRotation(rotation);
}

Quaternion RigidBody::getRotation() const {
    return m_impl->getRotation();
}

void RigidBody::applyForce(const Vector3& force) {
    m_impl->applyForce(force);
}

void RigidBody::applyImpulse(const Vector3& impulse) {
    m_impl->applyImpulse(impulse);
}

void RigidBody::setLinearVelocity(const Vector3& velocity) {
    m_impl->setLinearVelocity(velocity);
}

Vector3 RigidBody::getLinearVelocity() const {
    return m_impl->getLinearVelocity();
}

void RigidBody::setAngularVelocity(const Vector3& velocity) {
    m_impl->setAngularVelocity(velocity);
}

Vector3 RigidBody::getAngularVelocity() const {
    return m_impl->getAngularVelocity();
}

void RigidBody::setFriction(float friction) {
    m_impl->setFriction(friction);
}

void RigidBody::setRestitution(float restitution) {
    m_impl->setRestitution(restitution);
}

void RigidBody::setBodyType(BodyType type) {
    m_impl->setBodyType(type);
}

BodyType RigidBody::getBodyType() const {
    return m_impl->getBodyType();
}

ShapeType RigidBody::getShapeType() const {
    return m_impl->getShapeType();
}

float RigidBody::getMass() const {
    return m_impl->getMass();
}

} // namespace PhysicsSimulator