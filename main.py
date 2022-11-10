import entrezpy.efetch.efetcher
import json
import entrezpy.log.logger

entrezpy.log.logger.set_level('DEBUG')

e = entrezpy.efetch.efetcher.Efetcher("entrezpy",
                                      "rohanshah2067@gmail.com",
                                      apikey=None,
                                      apikey_var=None,
                                      threads=None,
                                      qid=None)

analyzer = e.inquire({'db': 'pubmed',
                      'id': [17284678, 9997],
                      'retmod': 'xml',
                      'rettype': 'abstract'})


print(analyzer.)