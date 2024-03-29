import numpy as np
from sklearn import preprocessing

data = np.array([
    [0, 2, 1, 12], 
    [1, 3, 5, 3], 
    [2, 3, 2, 12],
    [1, 2, 4, 3]
])

# 独热编码(One-Hot Encoding)
# 通常需要处理的数值都是稀疏地, 散乱地分布在空间中, 然而我们并不需要存储这些大数值, 这时就需要使用独热编码.
# 可以把独热编码看做是一种收紧(tighten)特征向量的工具. 他把特征向量的每个特征与特征的非重复总数相对应, 通过one-of-k的形式对每个值进行编码.
# 特征向量的每个特征值都按照这种方式编码, 这样可以更加有效地表示空间.

# 例如, 当需要处理四维向量空间, 当给一个特征向量的第n个特征进行编码时, 编辑器会遍历每个特征向量的第n个特征, 然后进行非重复计数.
# 如果非重复计数的值是K, 那么就把这个特征转换为只用一个值是1, 其他值都是0的K维向量.

encoder = preprocessing.OneHotEncoder()
encoder.fit(data)   # fit来学习编码
encoded_vector = encoder.transform([[2, 3, 5, 3],]).toarray()   # 将[2, 3, 5, 3]进行编码
print("Encoded vector\n", encoded_vector)

# 观察每个特征向量的第三个特征, 分别是1, 5, 2, 4这四个不重复的值, 也就是说独热编码的长度为4.
# 如果你需要对5进行编码, 那么向量就是[0, 0, 0, 1]. 向量中只有一个值是1, 第二个元素是1, 对应的值是5.


# 假如有三种颜色特征：红、黄、蓝。 
# 在利用机器学习的算法时一般需要进行向量化或者数字化。
# 那么你可能想令 红=1，黄=2，蓝=3. 那么这样其实实现了标签编码，即给不同类别以标签。
# 然而这意味着机器可能会学习到“红<黄<蓝”，但这并不是我们的让机器学习的本意，只是想让机器区分它们，并无大小比较之意。
# 所以这时标签编码是不够的，需要进一步转换。
# 因为有三种颜色状态，所以就有3个比特。
# 即红色：1 0 0 ，黄色: 0 1 0，蓝色：0 0 1 。
# 如此一来每两个向量之间的距离都是根号2，在向量空间距离都相等，所以这样不会出现偏序性，基本不会影响基于向量空间度量算法的效果。
# 自然状态码为：000,001,010,011,100,101
# 独热编码为：000001,000010,000100,001000,010000,100000