import collections
import heapq


def euclidean_distance(array1, array2):
    """计算欧氏距离

    :param array1: [tuple/list] 第1个向量
    :param array2: [tuple/list] 第2个向量
    :return:
    """
    n1, n2 = len(array1), len(array2)
    if n1 == n2:
        return pow(sum(pow(array1[i] - array2[i], 2) for i in range(n1)), 1 / 2)
    else:
        raise ValueError("向量维度数不一致")


class LinearSweepKNN:
    """线性扫描实现的k近邻计算"""

    def __init__(self, x, y, k, distance_func):
        self.x, self.y, self.k, self.distance_func = x, y, k, distance_func

    def count(self, x):
        """计算实例x所属的类y
        时间复杂度：O(N+KlogN) 线性扫描O(N)；自底向上构建堆O(N)；每次取出堆顶元素O(logN)，取出k个共计O(KlogN)
        """
        distances = [(self.distance_func(x, self.x[i]), self.y[i]) for i in range(len(self.x))]
        heapq.heapify(distances)
        count = collections.Counter()
        for _ in range(self.k):
            count[heapq.heappop(distances)[1]] += 1
        return count.most_common(1)[0][0]


if __name__ == "__main__":
    dataset = [[(3, 3), (4, 3), (1, 1)], [1, 1, -1]]  # 训练数据集
    knn = LinearSweepKNN(dataset[0], dataset[1], k=2, distance_func=euclidean_distance)
    print(knn.count((3, 4)))  # 1
