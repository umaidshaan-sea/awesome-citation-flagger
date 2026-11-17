"""Regression checks for what the 2026-11-04 frozen responses establish."""
import hashlib
import json
from pathlib import Path
import unittest
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]

class ArchivedEvidenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.df=pd.read_csv(ROOT/'results/processed/benchmark_results.csv').fillna('')

    def test_exact_legacy_failure_subtypes(self):
        pos=self.df[self.df.gold_label=='RETRACTED']
        self.assertEqual(int(((pos.legacy_prediction=='UNKNOWN')&(pos.legacy_bug_category=='SELF_ONLY')).sum()),8)
        self.assertEqual(int(((pos.legacy_prediction=='UNKNOWN')&(pos.legacy_bug_category=='MIXED_SELF_AND_NOTICE')).sum()),8)
        self.assertEqual(int(((pos.legacy_prediction=='RETRACTED')&(pos.legacy_bug_category=='DISTINCT_ONLY')).sum()),24)
        self.assertEqual(len(pos),40)

    def test_title_flags_are_not_balanced_by_label(self):
        p=self.df[self.df.gold_label=='RETRACTED']
        c=self.df[self.df.gold_label=='NOT_RETRACTED']
        self.assertEqual(int((p.title_audit_flag=='TITLE_MISMATCH_REVIEW').sum()),1)
        self.assertEqual(int((c.title_audit_flag=='TITLE_MISMATCH_REVIEW').sum()),23)
        self.assertEqual(int((c.title_audit_flag=='MISSING_PROVIDER_RECORD').sum()),4)

    def test_cached_case_relation_counts(self):
        expected={'10.1007/s13204-021-01976-4':(2,0),
                  '10.15252/embr.202153509':(1,2),
                  '10.1016/j.arabjc.2021.102998':(1,1),
                  '10.1109/cctae.2010.5544611':(1,0)}
        for identifier,values in expected.items():
            with self.subTest(identifier=identifier):
                row=self.df[self.df.doi==identifier].iloc[0]
                self.assertEqual((int(row.self_relation_count),int(row.distinct_relation_count)),values)
                path=ROOT/'data/processed/api_cache/crossref'/(hashlib.sha256(identifier.encode()).hexdigest()+'.json')
                rec=json.loads(path.read_text())['record']
                self.assertEqual(rec['DOI'].lower(),identifier)
