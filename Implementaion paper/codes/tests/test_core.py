import unittest
from src.core import doi, openalex, crossref, combine
from src.metrics import evaluate

class Rules(unittest.TestCase):
    def test_doi(self):
        self.assertEqual(doi('https://doi.org/10.1021/AM300292V'), '10.1021/am300292v')
        self.assertEqual(doi('unavailable'), '')
    def test_oa(self):
        self.assertEqual(openalex({'is_retracted':True})['prediction'], 'RETRACTED')
        self.assertEqual(openalex(None)['prediction'], 'UNKNOWN')
    def test_crossref(self):
        original='10.1234/original'
        record={'DOI':original,'updated-by':[{'type':'retraction','DOI':'10.1234/notice'}]}
        self.assertEqual(crossref(record,original)['prediction'], 'RETRACTED')
        record['updated-by'][0]['type']='correction'
        self.assertEqual(crossref(record,original)['prediction'], 'NOT_RETRACTED')
        self.assertEqual(crossref({'DOI':'10.1234/another'},original)['prediction'], 'UNKNOWN')
    def test_union(self):
        p=combine(openalex({'is_retracted':True}),crossref({'DOI':'10.1234/a','updated-by':[]},'10.1234/a'))
        self.assertEqual(p['prediction'],'RETRACTED')
        self.assertEqual(p['explanation_type'],'indicator_only')
    def test_score_refusal(self):
        with self.assertRaises(ValueError):
            evaluate([{'gold_label':'UNVERIFIED'}])

if __name__=='__main__': unittest.main()
