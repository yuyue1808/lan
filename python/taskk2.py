from keras.datasets import imdb

# 参数 num_words=10000 的意思是仅保留训练数据中前 10 000 个最常出现的单词
# 数据集被分为用于训练的 25 000 条评论与用于测试的 25 000 条评论，训练集和测试
# 集都包含 50% 的正面评论和 50% 的负面评论
(train_data, train_labels), (test_data, test_labels) = imdb.load_data(num_words=10000)
print(train_data.shape)
print(train_data)
print(train_labels.shape)
print(train_labels)
print(test_data.shape)
print(test_labels.shape)

# 获取对应的单词word_index
word_index = imdb.get_word_index()
# word_index字典里 键值对是  单词是key 数字是value  我们交换一下
reverse_word_index = dict([(value, key) for (key, value) in word_index.items()])
# 合成出train_data[0]代表的语句
decoded_review = ' '.join([reverse_word_index.get(i - 3, '?') for i in train_data[0]])
print(decoded_review)

import numpy as np


def vectorize_sequences(sequences, dimension=10000):
    results = np.zeros((len(sequences), dimension))
    for i, sequence in enumerate(sequences):
        results[i, sequence] = 1.
    return results


# 处理输入数据
x_train = vectorize_sequences(train_data)
print(x_train.shape)
x_test = vectorize_sequences(test_data)
y_train = np.asarray(train_labels).astype('float32')
y_test = np.asarray(test_labels).astype('float32')

# 验证数据集取一些
x_val = x_train[:10000]
partial_x_train = x_train[10000:]
y_val = y_train[:10000]
partial_y_train = y_train[10000:]

from keras import models
from keras import layers

model = models.Sequential()
model.add(layers.Dense(16, activation='relu', input_shape=(10000,)))
model.add(layers.Dense(16, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))
# loss函数可选binary_crossentropy二元交叉熵或者mse
model.compile(optimizer='rmsprop', loss='binary_crossentropy',
              metrics=['accuracy'])

model.fit(partial_x_train, partial_y_train, epochs=4,
          batch_size=512, verbose=0)
# results得到的是loss值和metric值
results = model.evaluate(x_test, y_test)
print(results)

# 测试数据集看看效果
# 如你所见，网络对某些样本的结果非常确信（大于等于 0.99，或小于等于 0.01），但对其他
# 结果却不那么确信（0.6 或 0.4）。
print(model.predict(x_test))

