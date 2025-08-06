#include "Vector3.h"
#include <cmath>

namespace PhysicsSimulator {

Vector3::Vector3() : m_x(0.0f), m_y(0.0f), m_z(0.0f) {
}

Vector3::Vector3(float x, float y, float z) : m_x(x), m_y(y), m_z(z) {
}

Vector3::Vector3(const Vector3& other) : m_x(other.m_x), m_y(other.m_y), m_z(other.m_z) {
}

Vector3& Vector3::operator=(const Vector3& other) {
    if (this != &other) {
        m_x = other.m_x;
        m_y = other.m_y;
        m_z = other.m_z;
    }
    return *this;
}

float Vector3::getX() const {
    return m_x;
}

float Vector3::getY() const {
    return m_y;
}

float Vector3::getZ() const {
    return m_z;
}

void Vector3::setX(float x) {
    m_x = x;
}

void Vector3::setY(float y) {
    m_y = y;
}

void Vector3::setZ(float z) {
    m_z = z;
}

void Vector3::set(float x, float y, float z) {
    m_x = x;
    m_y = y;
    m_z = z;
}

Vector3 Vector3::operator+(const Vector3& other) const {
    return Vector3(m_x + other.m_x, m_y + other.m_y, m_z + other.m_z);
}

Vector3 Vector3::operator-(const Vector3& other) const {
    return Vector3(m_x - other.m_x, m_y - other.m_y, m_z - other.m_z);
}

Vector3 Vector3::operator*(float scalar) const {
    return Vector3(m_x * scalar, m_y * scalar, m_z * scalar);
}

Vector3 Vector3::operator/(float scalar) const {
    if (scalar != 0.0f) {
        float invScalar = 1.0f / scalar;
        return Vector3(m_x * invScalar, m_y * invScalar, m_z * invScalar);
    }
    return *this;
}

float Vector3::dot(const Vector3& other) const {
    return m_x * other.m_x + m_y * other.m_y + m_z * other.m_z;
}

Vector3 Vector3::cross(const Vector3& other) const {
    return Vector3(
        m_y * other.m_z - m_z * other.m_y,
        m_z * other.m_x - m_x * other.m_z,
        m_x * other.m_y - m_y * other.m_x
    );
}

float Vector3::length() const {
    return std::sqrt(lengthSquared());
}

float Vector3::lengthSquared() const {
    return m_x * m_x + m_y * m_y + m_z * m_z;
}

Vector3 Vector3::normalized() const {
    float len = length();
    if (len > 0.0f) {
        float invLen = 1.0f / len;
        return Vector3(m_x * invLen, m_y * invLen, m_z * invLen);
    }
    return *this;
}

Vector3& Vector3::normalize() {
    float len = length();
    if (len > 0.0f) {
        float invLen = 1.0f / len;
        m_x *= invLen;
        m_y *= invLen;
        m_z *= invLen;
    }
    return *this;
}

} // namespace PhysicsSimulator