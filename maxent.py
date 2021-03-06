''' Maximum entropy classifier '''
import numpy as np
import feature_func as ff

class MaxEntClassifier( object ):
    def __init__( self, history_list, tag_set, feat_functs  ):
        self.history_list = history_list
        self.tag_set = tag_set
        self.feat_functs = feat_functs
        self.train_set = self.create_dataset()
        #self.model =  np.zeros( self.train_set.shape )
        self.model =  np.random.random( self.train_set.shape )
        self.score = self.generate_score()
        self.cost = self.generateCost()
    def create_dataset( self ):
        train_set = []
        for x in self.history_list:
            feat_vecs = []
            for y in self.tag_set:
                feat_vecs.append( self.get_feat_vec( x, y ) )
            train_set.append( feat_vecs )
        return np.asarray(train_set)

    def get_feat_vec( self, x, y ):
        feat_vec = []
        for f in self.feat_functs:
            feat_vec.append( f( x, y ) )
        return feat_vec

    def generate_score( self ):
        score = []
        for v,f in zip( self.train_set, self.model ):
            l = []
            for x,y in zip( v, f ):
                l.append( np.dot( x, y.transpose() ) )
            score.append( l )
        return np.asarray( score )

    def generateCost( self ):
        for i in range( self.score.shape[0] ):
            for j in range( self.score.shape[1] ):
                pass
                #cost.append( )

if __name__ == '__main__':
    feat_functs = [ ff.feat_func1, ff.feat_func2, ff.feat_func3, ff.feat_func4, ff.feat_func5, ff.feat_func6, ff.feat_func7, ff.feat_func8, ff.feat_func9, ff.feat_func10 ]
    me = MaxEntClassifier( [ ( "ORGANIZATION", "OTHER", ["Microsoft","released","Windows", "10"],2 ),( "*", "*", ["Microsoft","released","Windows", "10"],1 )], [ "ORGANIZATION", "PERSON", "GPE" ], feat_functs )
    #print me.train_set.shape
    #print me.model
    print me.score.shape
