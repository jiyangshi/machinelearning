#!/usr/bin/env python
#coding: utf-8


"""
k-近邻算法的一般流程：

（1）收集数据：可以使用任何方法。
（2）准备数据：距离计算所需要的数值，最好是结构化的数据格式。
（3）分析数据：可以使用任何方法。
（4）训练算法：此步骤不适用k-近邻算法。
（5）测试算法：计算错误率。
（6）使用算法：首先需要输入样本数据和结构化的输出结果，然后运行k-近邻算法判定输入数据分别属于那个分类，最后应用对计算出的分类执行后续的处理。
"""

import numpy
import operator


def createDataSet():

    #Define group and labels
    group = numpy.array( [[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]] )
    labels = ['A', 'A', 'B', 'B']
    return group, labels


def classify0( inX, dataSet, labels, k ):

    
    #Compute the distances of inX and dataSet
    dataSetSize = len( dataSet )
    diffMat = numpy.tile( inX, (dataSetSize, 1) ) - dataSet
    sqdiffMat = diffMat**2
    sqDistances = sqdiffMat.sum( axis = 1 )
    distances = sqDistances**0.5
    sortedDistIndeices = distances.argsort()


    #Choose the k points which have the least distances
    classCount = {}
    for i in range( k ):
        voteIlabel = labels[sortedDistIndeices[i]]
        classCount[voteIlabel] = classCount.get( voteIlabel, 0 ) + 1

    #sorted
    sortedClassCount = sorted( classCount.iteritems(),key = operator.itemgetter( 1 ), reverse = True )

    return sortedClassCount[0][0]



if __name__ == '__main__':

    group, labels = createDataSet()

    print classify0( [0, 0], group, labels, 3 )
