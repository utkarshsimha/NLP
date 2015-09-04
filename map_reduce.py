''' Implementing Map Reduce for generation of triples from the sentence tokens '''
import pickle
import multiprocessing as mp
import collections

class MapReduce:
	def __init__( self, input, chunksize, map_func, num_workers ):
		self.input = input
		self.map_func = map_func
		self.pool = []
		self.res_queue = mp.Queue()
		for i in range( num_workers ):
			self.pool.append( mp.Process( target=self.map_func, args=(input[chunksize*i:chunksize*(i+1)], self.res_queue ) ) )
		self.pool.append( mp.Process( target=self.map_func, args=(input[chunksize*i+1:], self.res_queue) ) )

	def __call__( self ):
		#Map
		for proc in self.pool:
			proc.start()
		for proc in self.pool:
			proc.join()
		result = []

		#Concat
		for i in range(len(self.pool)):
			result.append( self.res_queue.get() )
		self.data = collections.defaultdict( list )
		for res in result:
			for key, val in res:
				self.data[key].append( val )

		#Reduce
		for key in self.data.keys():
			val = self.data[key]
			self.data[key] = sum(val)

		return dict( self.data )

