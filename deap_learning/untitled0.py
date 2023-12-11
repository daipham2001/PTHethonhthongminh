# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 09:26:04 2022

@author: ADMIN
"""
import tensorflow as tf
# import tensorflow.compat.v1 as tf
x = tf.constant(5,tf.float32)
y = tf.constant([5], tf.float32)
z = tf.constant([5,3,4], tf.float32)
t = tf.constant([[5,3,4,6],[2,3,4,7]], tf.float32)
u = tf.constant([[[5,3,4,6],[2,3,4,0]]], tf.float32)
v = tf.constant([[[5,3,4,6],[2,3,4,0]],
 [[5,3,4,6],[2,3,4,0]],
[[5,3,4,6],[2,3,4,0]]
 ], tf.float32)
print(y)
