import tensorflow as tf

# 텐서 = tf.constant([3.0,4.5,5])
# 텐서2 = tf.constant([6,7,8])
# 텐서3 = tf.constant([[1,2],
#                     [3,4]])

# w = tf.Variable(1.0)
# print(w.numpy())
# w.assign(2)
# print(w)

키 = [170,180,175,160]
신발 = [260,270,265,255]

def 손실함수():
    예측값 = 키 * a + b
    return tf.square(260 - 예측값)
a = tf.Variable(0.1)
b = tf.Variable(0.2)
opt = tf.keras.optimizers.Adam(learning_rate=0.1)

for i in range(300):
    opt.minimize(손실함수, var_list=[a,b])
    print(a.numpy(),b.numpy())