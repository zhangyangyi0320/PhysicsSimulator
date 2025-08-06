#ifndef QUATERNION_H
#define QUATERNION_H

#include "Vector3.h"

namespace PhysicsSimulator {

/**
 * @class Quaternion
 * @brief 四元数类，用于表示旋转
 */
class Quaternion {
public:
    /**
     * @brief 默认构造函数
     */
    Quaternion();
    
    /**
     * @brief 构造函数
     * @param x X分量
     * @param y Y分量
     * @param z Z分量
     * @param w W分量
     */
    Quaternion(float x, float y, float z, float w);
    
    /**
     * @brief 拷贝构造函数
     * @param other 其他四元数
     */
    Quaternion(const Quaternion& other);
    
    /**
     * @brief 赋值运算符
     * @param other 其他四元数
     * @return 自身引用
     */
    Quaternion& operator=(const Quaternion& other);
    
    /**
     * @brief 从欧拉角创建四元数
     * @param euler 欧拉角(弧度)
     * @return 四元数
     */
    static Quaternion fromEuler(const Vector3& euler);
    
    /**
     * @brief 从轴角创建四元数
     * @param axis 旋转轴
     * @param angle 旋转角度(弧度)
     * @return 四元数
     */
    static Quaternion fromAxisAngle(const Vector3& axis, float angle);
    
    /**
     * @brief 获取X分量
     * @return X分量
     */
    float getX() const;
    
    /**
     * @brief 获取Y分量
     * @return Y分量
     */
    float getY() const;
    
    /**
     * @brief 获取Z分量
     * @return Z分量
     */
    float getZ() const;
    
    /**
     * @brief 获取W分量
     * @return W分量
     */
    float getW() const;
    
    /**
     * @brief 设置X分量
     * @param x X分量
     */
    void setX(float x);
    
    /**
     * @brief 设置Y分量
     * @param y Y分量
     */
    void setY(float y);
    
    /**
     * @brief 设置Z分量
     * @param z Z分量
     */
    void setZ(float z);
    
    /**
     * @brief 设置W分量
     * @param w W分量
     */
    void setW(float w);
    
    /**
     * @brief 设置所有分量
     * @param x X分量
     * @param y Y分量
     * @param z Z分量
     * @param w W分量
     */
    void set(float x, float y, float z, float w);
    
    /**
     * @brief 四元数乘法
     * @param other 其他四元数
     * @return 结果四元数
     */
    Quaternion operator*(const Quaternion& other) const;
    
    /**
     * @brief 四元数点乘
     * @param other 其他四元数
     * @return 点乘结果
     */
    float dot(const Quaternion& other) const;
    
    /**
     * @brief 四元数长度
     * @return 四元数长度
     */
    float length() const;
    
    /**
     * @brief 四元数长度平方
     * @return 四元数长度平方
     */
    float lengthSquared() const;
    
    /**
     * @brief 归一化四元数
     * @return 归一化后的四元数
     */
    Quaternion normalized() const;
    
    /**
     * @brief 归一化自身
     * @return 自身引用
     */
    Quaternion& normalize();
    
    /**
     * @brief 四元数共轭
     * @return 共轭四元数
     */
    Quaternion conjugate() const;
    
    /**
     * @brief 四元数逆
     * @return 逆四元数
     */
    Quaternion inverse() const;
    
    /**
     * @brief 转换为欧拉角
     * @return 欧拉角(弧度)
     */
    Vector3 toEuler() const;
    
    /**
     * @brief 转换为轴角
     * @param axis 输出旋转轴
     * @param angle 输出旋转角度(弧度)
     */
    void toAxisAngle(Vector3& axis, float& angle) const;
    
private:
    float m_x;
    float m_y;
    float m_z;
    float m_w;
};

} // namespace PhysicsSimulator

#endif // QUATERNION_H