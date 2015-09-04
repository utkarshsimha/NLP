''' To implement tf-idf and score computation '''
import math
len_corpus = 0
def term_frequency( corpus ):
	global len_corpus
	tf = { }
	len_corpus = len( corpus )
	for it in range( len_corpus ):
		doc = corpus[it]
		for word in doc:
			if( word not in tf.keys() ):
				tf[word] = [0]*len_corpus
			tf[word][it] = doc.count( word )
	return tf

def inverse_document_frequency( tf ):
	idf = { }
	for word in tf:
		try:
			idf[word] = math.log( len_corpus / float( len_corpus - tf[word].count(0) ), math.e )
		except Exception as e:
			pass
	return idf

def print_documents( query_string, corpus, tf, idf, all_words=False ):	
	print query_string
	print "All words : ",all_words
	documents = { }
	for doc_idx in range( len_corpus ):
		score = 0
		word_found = False
		for term in query_string:
			if( term not in tf.keys() and all_words is True ):
				word_found = False
				break
			elif( term not in tf.keys() and all_words is False ):
				continue
			elif( tf[term][doc_idx] is 0 and all_words is True ):
				word_found = False
				break
			try:
				word_found = True
				score += tf[term][doc_idx] * idf[term]
			except:
				pass
		if(  word_found ):
			documents[doc_idx] = score
	sorted_doc = sorted( documents, key=documents.get, reverse=True )[:10]
	count = 0
	for doc_idx in sorted_doc:
		count +=1
		#print ' '.join( corpus[doc_idx] )
		print count,".",corpus[doc_idx]
		print "\n"
	if( count == 0 ):
		print "No documents found! :( "
	print "-"*40

