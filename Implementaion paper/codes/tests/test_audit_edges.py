import unittest, tempfile
from pathlib import Path
import pandas as pd
from src.core import doi, openalex, crossref, combine
from src.data import load_candidates
from src.metrics import evaluate
from src.validate_rw import validate_csv

class AuditEdges(unittest.TestCase):
    def test_reinstatement_requires_review(self):
        r={'DOI':'10.1234/a', 'updated-by':[{'type':'retraction','DOI':'10.1234/b'}, {'type':'reinstatement','DOI':'10.1234/c'}]}
        self.assertEqual(crossref(r,'10.1234/a')['prediction'],'UNKNOWN')
    def test_missing_source_unknown(self):
        self.assertEqual(openalex(None)['prediction'],'UNKNOWN')
        self.assertEqual(crossref(None,'10.1234/a')['prediction'],'UNKNOWN')
    def test_multi_doi_not_selected_even_when_regex_matches(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/'rw.csv'
            pd.DataFrame([{'Record ID':'1','OriginalPaperDOI':'10.1234/a;10.1234/b','RetractionDOI':'10.1234/n','RetractionNature':'Retraction'},
                          {'Record ID':'2','OriginalPaperDOI':'10.1234/c','RetractionDOI':'10.1234/n','RetractionNature':'Retraction'}]).to_csv(p,index=False)
            report=validate_csv(p)
            self.assertEqual(report['rows_with_multi_doi_field_excluded'],1)
            frame, manifest=load_candidates(p,positive_limit=10,correction_limit=0)
            self.assertEqual(frame['doi'].tolist(),['10.1234/c'])
    def test_abstention_cannot_inflate_f1_end_to_end(self):
        rows=[{'gold_label':'RETRACTED','gold_evidence_url':'https://publisher.example/a','openalex_prediction':'UNKNOWN','crossref_prediction':'UNKNOWN','combined_prediction':'UNKNOWN'},
              {'gold_label':'NOT_RETRACTED','gold_evidence_url':'https://publisher.example/b','openalex_prediction':'NOT_RETRACTED','crossref_prediction':'NOT_RETRACTED','combined_prediction':'NOT_RETRACTED'}]
        summary=evaluate(rows)
        self.assertEqual(summary.iloc[0]['end_to_end_recall'],0)
        self.assertEqual(summary.iloc[0]['positive_unknown'],1)
        self.assertEqual(summary.iloc[0]['F1_end_to_end'],0)
    def test_unverified_scoring_refused(self):
        with self.assertRaises(ValueError):
            evaluate([{'gold_label':'UNVERIFIED','gold_evidence_url':''}])
