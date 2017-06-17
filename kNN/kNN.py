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
import os


def createDataSet():

    """
    Create data set group, labels
    """

    #Define group and labels
    group = numpy.array( [[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]] )
    labels = ['A', 'A', 'B', 'B']
    return group, labels


def classify0( inX, dataSet, labels, k ):

    """
    Input:
        inX: testSet that used to be given a label
        dataSet: data that already have labels
        labels: type
        k: the k least distances

    Output: the label of inX
    """
    
    #Compute the distances of inX and dataSet
    #dataSetSize = len( dataSet )
    dataSetSize = dataSet.shape[0]
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



def file2matrix( filename ):

    """
    filename: filename.txt
    """

    returnVect = numpy.zeros( (1, 1024) )

    #open filename.txt
    f = open( filename )

    #Since the data in filename have the structure 32 * 32
    for i in range(32):
        lineStr = f.readline()
        for j in range(32):
            returnVect[0, 32*i+j] = int( lineStr[j] )

    return returnVect

def handwritingClassTest():

    """
    Train the data from trainingDigits and test the data from testDigits
    """
    
    hwLabels = []
    #trainingFileList: name of txt files in trainingDigits files
    trainingFileList = os.listdir( 'trainingDigits' )
    m = len( trainingFileList )

    #Store the training data which is equal to dataSet
    trainingMat = numpy.zeros( (m, 1024) )

    for i in range( m ):

        #fileNameStr is to obtain the name of txt files
        #classNumStr is to obtain the real number of the txt files' img
        #for example: the txt files' name is 1_2.txt, then
        #fileNameStr.split('.') = ['1_2', 'txt'], fileStr = '1_2'
        #fileStr.split('_') = ['1', '2'], classNumStr = 1
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int( fileStr.split('_')[0] )

        #labels
        hwLabels.append( classNumStr )
        trainingMat[i, :] = file2matrix( 'trainingDigits/%s' % fileNameStr )

    testFileList = os.listdir( 'testDigits' )

    errorCount = 0.0
    mTest = len( testFileList )
    for i in range( mTest ):
        #In the same way as trainingDigits
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int( fileStr.split('_')[0] )
        vectorUnderTest = file2matrix( 'testDigits/%s', % fileNameStr )

        #classify testDigits files by function classify0
        classifierResult = classify0( vectorUnderTest, trainingMat, hwLabels, 3 )


        print "the classifier came back with: %d, the real answer is: %d" % (classifierResult, classNumStr)
        if ( classifierResult != classNumStr ): errorCount += 1.0

    print "\nthe total number of errors is: %d" % errorCount
    print "\nthe total error rate is: %f" %( errorCount / float( mTest ) )
