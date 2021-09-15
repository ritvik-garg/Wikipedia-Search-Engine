import sys
import os
import Stemmer
import timeit
from math import log10


def loadDocToTitle(path_to_doc_to_title):
	with open(path_to_doc_to_title, "r") as f:
		for line in f:
			num_docs += 1
			id_title = line.split("#")
			docToTitle[id_title[0]] = id_title[1]
	

def loadStopwords(path_to_stopwords_file):
	try :
		file = open(path_to_stopwords_file, "r", encoding = "utf-8")
		for line in file:
			words = line.strip()
			stopwords.add(words)
	except:
		print("file containing stopwords not found.\n Exiting system")
		sys.exit(1)


def loadSecondaryIndexFile(path_to_sec_index_file):
	with open(path_to_sec_index_file, "r") as f:
		for line in f:
			sec_index.append(line.split()[0])


def search(query):
	




if __name__ == "__main__":

	path_to_query_file = "./queries.txt"
	path_to_doc_to_title = "./docToTitle.txt"
	path_to_stopwords_file = "./stopwords.txt"
	path_to_sec_index_file = "./secIndex.txt"

	stopwords = set()
	loadStopwords(path_to_stopwords_file)

	sec_index = []
	loadSecondaryIndexFile(path_to_sec_index_file)

	docToTitle = {}
	num_docs = 0
	loadDocToTitle(path_to_doc_to_title)

	


	with open(path_to_query_file, "r") as f:
		for query in f:
			search(query)