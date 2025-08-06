#include "Quaternion.h"
#include <cmath>

namespace PhysicsSimulator {

Quaternion::Quaternion() : m_x(0.0f), m_y(0.0f), m_z(0.0f), m_w(1.0f) {
}

Quaternion::Quaternion(float x, float y, float z, float w) : m_x(x), m_y(y), m_z(z), m_w(w) {
}

Quaternion::Quaternion(const Quaternion& other) : m_x(other.m_x), m_y(other.m_y), m_z(other.m_z), m_w(other.m_w) {
}

Quaternion& Quaternion::operator=(const Quaternion& other) {
    if (this != &other) {
        m_x = other.m_x;
        m_y = other.m_y;
        m_z = other.m_z;
        m_w = other.m_w;
    }
    return *this;
}

Quaternion Quaternion::fromEuler(const Vector3& euler) {
    float halfX = euler.getX() * 0.5f;
    float halfY = euler.getY() * 0.5f;
    float halfZ = euler.getZ() * 0.5f;
    
    float sinX = std::sin(halfX);
    float cosX = std::cos(halfX);
    float sinY = std::sin(halfY);
    float cosY = std::cos(halfY);
    float sinZ = std::sin(halfZ);
    float cosZ = std::cos(halfZ);
    
    return Quaternion(
        cosY * sinX * cosZ + sinY * cosX * sinZ,
        sinY * cosX * cosZ - cosY * sinX * sinZ,
        cosY * cosX * sinZ - sinY * sinX * cosZ,
        cosY * cosX * cosZ + sinY * sinX * sinZ
    );
}

Quaternion Quaternion::fromAxisAngle(const Vector3& axis, float angle) {
    float halfAngle = angle * 0.5f;
    float sinHalfAngle = std::sin(halfAngle);
    return Quaternion(
        axis.getX() * sinHalfAngle,
        axis.getY() * sinHalfAngle,
        axis.getZ() * sinHalfAngle,
        std::cos(halfAngle)
    );
}

float Quaternion::getX() const {
    return m_x;
}

float Quaternion::getY() const {
    return m_y;
}

float Quaternion::getZ() const {
    return m_z;
}

float Quaternion::getW() const {
    return m_w;
}

void Quaternion::setX(float x) {
    m_x = x;
}

void Quaternion::setY(float y) {
    m_y = y;
}

void Quaternion::setZ(float z) {
    m_z = z;
}

void Quaternion::setW(float w) {
    m_w = w;
}

void Quaternion::set(float x, float y, float z, float w) {
    m_x = x;
    m_y = y;
    m_z = z;
    m_w = w;
}

Quaternion Quaternion::operator*(const Quaternion& other) const {
    return Quaternion(
        m_w * other.m_x + m_x * other.m_w + m_y * other.m_z - m_z * other.m_y,
        m_w * other.m_y - m_x * other.m_z + m_y * other.m_w + m_z * other.m_x,
        m_w * other.m_z + m_x * other.m_y - m_y * other.m_x + m_z * other.m_w,
        m_w * other.m_w - m_x * other.m_x - m_y * other.m_y - m_z * other.m_z
    );
}

float Quaternion::dot(const Quaternion& other) const {
    return m_x * other.m_x + m_y * other.m_y + m_z * other.m_z + m_w * other.m_w;
}

float Quaternion::length() const {
    return std::sqrt(lengthSquared());
}

float Quaternion::lengthSquared() const {
    return m_x * m_x + m_y * m_y + m_z * m_z + m_w * m_w;
}

Quaternion Quaternion::normalized() const {
    float len = length();
    if (len > 0.0f) {
        float invLen = 1.0f / len;
        return Quaternion(m_x * invLen, m_y * invLen, m_z * invLen, m_w * invLen);
    }
    return *this;
}

Quaternion& Quaternion::normalize() {
    float len = length();
    if (len > 0.0f) {
        float invLen = 1.0f / len;
        m_x *= invLen;
        m_y *= invLen;
        m_z *= invLen;
        m_w *= invLen;
    }
    return *this;
}

Quaternion Quaternion::conjugate() const {
    return Quaternion(-m_x, -m_y, -m_z, m_w);
}

Quaternion Quaternion::inverse() const {
    float lenSq = lengthSquared();
    if (lenSq > 0.0f) {
        float invLenSq = 1.0f / lenSq;
        Quaternion result = conjugate();
    result.m_x *= invLenSq;
    result.m_y *= invLenSq;
    result.m_z *= invLenSq;
    result.m_w *= invLenSq;
    return result;
    }
    return *this;
}

Vector3 Quaternion::toEuler() const {
    Vector3 euler;
    
    // 计算俯仰角 (Y轴旋转)
    float sinP = 2.0f * (m_w * m_y - m_z * m_x);
    if (std::abs(sinP) >= 1.0f) {
        euler.setY(std::copysign(M_PI / 2.0f, sinP));
    } else {
        euler.setY(std::asin(sinP));
    }
    
    // 计算偏航角 (Z轴旋转)
    float sinY = 2.0f * (m_w * m_z + m_x * m_y);
    float cosY = 1.0f - 2.0f * (m_y * m_y + m_z * m_z);
    euler.setZ(std::atan2(sinY, cosY));
    
    // 计算滚转角 (X轴旋转)
    float sinR = 2.0f * (m_w * m_x + m_y * m_z);
    float cosR = 1.0f - 2.0f * (m_x * m_x + m_y * m_y);
    euler.setX(std::atan2(sinR, cosR));
    
    return euler;
}

void Quaternion::toAxisAngle(Vector3& axis, float& angle) const {
    float len = std::sqrt(m_x * m_x + m_y * m_y + m_z * m_z);
    if (len > 0.0f) {
        float invLen = 1.0f / len;
        axis.set(m_x * invLen, m_y * invLen, m_z * invLen);
        angle = 2.0f * std::acos(m_w);
    } else {
        axis.set(1.0f, 0.0f, 0.0f);
        angle = 0.0f;
    }
}

} // namespace PhysicsSimulator