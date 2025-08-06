#ifndef VECTOR3_H
#define VECTOR3_H

namespace PhysicsSimulator {

/**
 * @class Vector3
 * @brief 三维向量类
 */
class Vector3 {
public:
    /**
     * @brief 默认构造函数
     */
    Vector3();
    
    /**
     * @brief 构造函数
     * @param x X坐标
     * @param y Y坐标
     * @param z Z坐标
     */
    Vector3(float x, float y, float z);
    
    /**
     * @brief 拷贝构造函数
     * @param other 其他向量
     */
    Vector3(const Vector3& other);
    
    /**
     * @brief 赋值运算符
     * @param other 其他向量
     * @return 自身引用
     */
    Vector3& operator=(const Vector3& other);
    
    /**
     * @brief 获取X坐标
     * @return X坐标
     */
    float getX() const;
    
    /**
     * @brief 获取Y坐标
     * @return Y坐标
     */
    float getY() const;
    
    /**
     * @brief 获取Z坐标
     * @return Z坐标
     */
    float getZ() const;
    
    /**
     * @brief 设置X坐标
     * @param x X坐标
     */
    void setX(float x);
    
    /**
     * @brief 设置Y坐标
     * @param y Y坐标
     */
    void setY(float y);
    
    /**
     * @brief 设置Z坐标
     * @param z Z坐标
     */
    void setZ(float z);
    
    /**
     * @brief 设置所有坐标
     * @param x X坐标
     * @param y Y坐标
     * @param z Z坐标
     */
    void set(float x, float y, float z);
    
    /**
     * @brief 向量加法
     * @param other 其他向量
     * @return 结果向量
     */
    Vector3 operator+(const Vector3& other) const;
    
    /**
     * @brief 向量减法
     * @param other 其他向量
     * @return 结果向量
     */
    Vector3 operator-(const Vector3& other) const;
    
    /**
     * @brief 向量数乘
     * @param scalar 标量
     * @return 结果向量
     */
    Vector3 operator*(float scalar) const;
    
    /**
     * @brief 向量数除
     * @param scalar 标量
     * @return 结果向量
     */
    Vector3 operator/(float scalar) const;
    
    /**
     * @brief 向量点乘
     * @param other 其他向量
     * @return 点乘结果
     */
    float dot(const Vector3& other) const;
    
    /**
     * @brief 向量叉乘
     * @param other 其他向量
     * @return 叉乘结果
     */
    Vector3 cross(const Vector3& other) const;
    
    /**
     * @brief 向量长度
     * @return 向量长度
     */
    float length() const;
    
    /**
     * @brief 向量长度平方
     * @return 向量长度平方
     */
    float lengthSquared() const;
    
    /**
     * @brief 归一化向量
     * @return 归一化后的向量
     */
    Vector3 normalized() const;
    
    /**
     * @brief 归一化自身
     * @return 自身引用
     */
    Vector3& normalize();
    
private:
    float m_x;
    float m_y;
    float m_z;
};

} // namespace PhysicsSimulator

#endif // VECTOR3_H