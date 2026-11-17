import unittest
from src.core import crossref, combine, openalex, doi

class CorrectionAuditTests(unittest.TestCase):
    def test_self_referencing_typed_retraction_is_detected(self):
        rec = {'DOI':'10.5555/source', 'updated-by': [{'type':'retraction','DOI':'10.5555/source','source':'retraction-watch'}]}
        got = crossref(rec,'10.5555/source')
        self.assertEqual(got['prediction'],'RETRACTED')
        self.assertEqual(got['evidence'],[])
    def test_mixed_self_and_notice_retains_notice(self):
        rec = {'DOI':'10.5555/source','updated-by':[{'type':'retraction','DOI':'10.5555/source'},
             {'type':'retraction','DOI':'10.5555/notice','source':'publisher'}]}
        got = crossref(rec,'10.5555/source')
        self.assertEqual(got['prediction'],'RETRACTED')
        self.assertEqual(got['evidence'][0]['notice_doi'],'10.5555/notice')
    def test_distinct_notice_explanation(self):
        rec={'DOI':'10.5555/source','updated-by':[{'type':'retraction','DOI':'10.5555/notice'}]}
        merged=combine(openalex({'is_retracted':True}),crossref(rec,'10.5555/source'))
        self.assertEqual(merged['explanation_type'],'distinct_notice_doi_available')
    def test_invalid_compound_doi(self):
        self.assertEqual(doi('10.1234/first;10.1234/second'), '')
    def test_reinstatement_overrides_signal(self):
        rec={'DOI':'10.5555/source','updated-by':[{'type':'retraction','DOI':'10.5555/source'},
                {'type':'reinstatement','DOI':'10.5555/reinstate'}]}
        self.assertEqual(crossref(rec,'10.5555/source')['prediction'],'UNKNOWN')
