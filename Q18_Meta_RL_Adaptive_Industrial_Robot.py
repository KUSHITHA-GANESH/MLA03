# Q18: Meta-Reinforcement Learning for adaptive industrial robot
# Simplified MAML-style meta-learning.
# Each task has a different target position.
# The model learns a common initialization that adapts quickly.

import numpy as np
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense

def make_model():
    return Sequential([
        Dense(32, activation="relu", input_shape=(2,)),
        Dense(32, activation="relu"),
        Dense(2)
    ])

def task_loss(model, target):
    # Robot starts at (0,0); model predicts movement toward task target.
    x = tf.constant([[0.0, 0.0]], dtype=tf.float32)
    y = tf.constant([target], dtype=tf.float32)
    pred = model(x)
    return tf.reduce_mean(tf.square(pred - y))

meta_model = make_model()
meta_optimizer = tf.keras.optimizers.Adam(0.001)

tasks = [
    np.array([1.0, 1.0]),
    np.array([2.0, 0.0]),
    np.array([0.0, 2.0]),
    np.array([3.0, 3.0])
]

# Simplified first-order MAML:
for meta_step in range(1000):
    meta_gradients = [
        tf.zeros_like(v) for v in meta_model.trainable_variables
    ]

    for target in tasks:
        with tf.GradientTape() as tape:
            loss = task_loss(meta_model, target)

        grads = tape.gradient(loss, meta_model.trainable_variables)

        for i, g in enumerate(grads):
            meta_gradients[i] += g / len(tasks)

    meta_optimizer.apply_gradients(
        zip(meta_gradients, meta_model.trainable_variables)
    )

# Fast adaptation to a new task
new_task = np.array([4.0, 1.0])
adapt_optimizer = tf.keras.optimizers.SGD(0.05)

for _ in range(10):
    with tf.GradientTape() as tape:
        loss = task_loss(meta_model, new_task)
    grads = tape.gradient(loss, meta_model.trainable_variables)
    adapt_optimizer.apply_gradients(
        zip(grads, meta_model.trainable_variables)
    )

prediction = meta_model.predict(np.array([[0.0, 0.0]]), verbose=0)[0]

print("Q18 - Meta Reinforcement Learning")
print("New manufacturing task target:", new_task)
print("Robot adapted prediction:", np.round(prediction, 3))
print("Adaptation loss:", float(task_loss(meta_model, new_task)))
