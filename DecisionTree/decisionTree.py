# -*- coding: utf-8 -*-


"""
Decision Tree
"""
import os
import pydotplus
from sklearn import tree


# 训练数据集
datasets = [[1, 2, 2, 1],
            [1, 2, 2, 2],
            [1, 1, 2, 3],
            [1, 1, 1, 1],
            [1, 2, 2, 1],
            [2, 2, 2, 1],
            [2, 2, 2, 2],
            [2, 1, 1, 2],
            [2, 2, 1, 3],
            [2, 2, 1, 3],
            [3, 2, 1, 3],
            [3, 2, 1, 2],
            [3, 1, 2, 2],
            [3, 1, 2, 3],
            [3, 2, 2, 1]]

# 特征空间
feature = [0, 0, 1, 1, 0,
           0, 0, 1, 1, 1,
           1, 1, 1, 1, 0]

# 对训练数据集以及特征空间进行拟合，这里用CART算法
DTC = tree.DecisionTreeClassifier()
DTC = DTC.fit( datasets, feature )

# 导出决策树
with open( "load.dot", "w" ) as f:
    f = tree.export_graphviz(DTC,out_file=f)
    
os.unlink('load.dot')

# 决策树以pdf格式的文件输出
dot_data = tree.export_graphviz( DTC, out_file=None )
graph = pydotplus.graph_from_dot_data( dot_data )
graph.write_pdf( "load.pdf" )
