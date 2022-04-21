import entrezpy.esummary.esummarizer

e = entrezpy.esummary.esummarizer.Esummarizer("entrezpy",
                                              "rohanshah2067@gmail.com",
                                              apikey="None",
                                              apikey_var="None",
                                              threads="None",
                                              qid="None")
analyzer = e.inquire({'db': "pubmed",
                    'id' :[22230712, 22225830]})
print(analyzer.get_result().summaries)