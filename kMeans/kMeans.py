#coding: utf-8


"""
kMeans algorithm
"""

import numpy

def loadDataSet( filename ):
    dataMat = []
    fr = open( filename )
    for line in fr.readlines():
        curLine = line.strip().split( '\t' )
        fltLine = map( float, curLine )
        dataMat.append( fltLine )

    return dataMat




class kMeans( object ):
    """
    参数：
        n_clusters：聚类个数，即k
        initCent：质心初始化方式
        max_iter：最大迭代次数
    """
    def __init__( self, n_clusters=5, initCent='random', max_iter=300 ):

        if hasattr( initCent, '__array__' ):
            n_clusters = initCent.shape[0]
            self.centroids = numpy.asarray( initcent, dtype=numpy.float )
        else:
            self.centroids = None

        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.initCent = initCent
        self.clusterAssment = None
        self.labels = None
        self.sse = None


    def distEclud( self, vecA, vecB ):
        """
        计算两点的欧式距离
        """

        return numpy.linalg.norm( vecB - vecA )

    def randCent( self, X, k ):
        """
        随机选取k个质心，必须在数据集的边界内
        """

        # 特征维数
        n = X.shape[1]
        centroids = numpy.empty( ( k, n ) )
        for j in range(n):
            # 产生k个质心，一维一维地随机初始化
            minJ = min( X[:, j] )
            rangeJ = float( max ( X[:, j] ) - minJ )
            centroids[:, j] = ( minJ + rangeJ * numpy.random.rand( k, 1 ) ).flatten()

        return centroids

    def fit( self, X ):
        # 类型检查
        if not isinstance( X, numpy.ndarray ):
            try:
                X = numpy.asarray( X )
            except:
                raise TypeError( "numpy.ndarray required for X" )

        # 样本数量
        m = X.shape[0]

        # m*2的矩阵，第一列存储样本点所属的族的索引值，
        # 第二列存储该点与所属族的质心的平方误差
        self.clusterAssment = numpy.empty( ( m, 2 ) )


        if self.initCent == 'random':
            self.centroids = self.randCent( X, self.n_clusters )

        clusterChanged = True

        for _ in range( self.max_iter ):
            clusterChanged = False

            # 将每个样本点分配到离它最近的质心所属的族
            for i in range( m ):
                minDist = numpy.inf; minIndex = -1
                for j in range( self.n_clusters ):
                    distJI = self.distEclud( self.centroids[j, :], X[i, :] )
                    if distJI < minDist:
                        minDist = distJI; minIndex = j


                if self.clusterAssment[i, 0] != minIndex:
                    clusterChanged = True
                    self.clusterAssment[i, :] = minIndex, minDist**2

            if not clusterChanged:
                break

            for i in range( self.n_clusters ):
                ptsInClust = X[numpy.nonzero( self.clusterAssment[:, 0] == i )[0]]
                self.centroids[i, :] = numpy.mean( ptsInClust, axis=0 )

        self.labels = self.clusterAssment[:, 0]
        self.sse = sum( self.clusterAssment[:, 1] )


    def predict( self, X ):

        if not isinstance( X, numpy.ndarray ):
            try:
                X = numpy.asarray( X )
            except:
                raise TypeError( "numpy.ndarray required for X" )


        m = X.shape[0]

        preds = numpy.empty( (m, ) )

        for i in range( m ):
            minDist = numpy.inf
            for j in range( self.n_clusters ):
                distJI = self.distEclud( self.centroids[j, :], X[i, :] )
                if distJI < minDist:
                    minDist = distJI
                    preds[i] = j

        return preds


