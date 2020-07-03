import logging

def logger():
    logging.basicConfig(filename="log1.txt",filemode='a',format='%(asctime)s-%(message)s',level=logging.INFO)
    return logging