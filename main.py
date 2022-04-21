import entrezpy.esearch.esearcher
import entrezpy.esummary.esummarizer
import json
import entrezpy.log.logger

entrezpy.log.logger.set_level('DEBUG')


def write_json(data, filename="European Urology Focus_2011.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


date_count = 1
# 4 dates to count to
journal_count = 1
# 17 journals to count up to
e = entrezpy.esearch.esearcher.Esearcher("entrezpy",
                                         "rohanshah2067@gmail.com",
                                         apikey=None,
                                         apikey_var=None,
                                         threads=None,
                                         qid=None)

analyzer = e.inquire({'db': 'pubmed',
                      'term': "Cancer",
                      'datetype': 'pdat',
                      'mindate': '2011/1/1',
                      'maxdate': '2011/12/31',
                      'rettype': 'uilist', })

e2 = entrezpy.esummary.esummarizer.Esummarizer("entrezpy",
                                               "rohanshah2067@gmail.com",
                                               apikey=None,
                                               apikey_var=None,
                                               threads=None,
                                               qid=None)
analyzer2 = e2.inquire({'db': "pubmed",
                        'retmode': "json",
                        'id': analyzer.result.uids})

write_json(analyzer2.get_result().summaries)
