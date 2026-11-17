import tempfile
import unittest
from pathlib import Path
import pandas as pd
from src.validate_rw import validate_csv

class CSVValidationTests(unittest.TestCase):
    def write_csv(self, folder, rows):
        path = Path(folder) / 'fixture_SYNTHETIC.csv'
        pd.DataFrame(rows).to_csv(path, index=False)
        return path

    def test_valid_fixture_counts_and_no_ground_truth_claim(self):
        with tempfile.TemporaryDirectory() as d:
            p = self.write_csv(d, [
                {'Record ID': '1', 'OriginalPaperDOI': 'https://doi.org/10.1234/ABC', 'RetractionDOI': '10.1234/notice', 'RetractionNature': 'Retraction'},
                {'Record ID': '2', 'OriginalPaperDOI': '10.1234/abc', 'RetractionDOI': '', 'RetractionNature': 'Correction'},
                {'Record ID': '3', 'OriginalPaperDOI': '', 'RetractionDOI': '', 'RetractionNature': 'Correction'},
                {'Record ID': '4', 'OriginalPaperDOI': '10.1234/one;10.1234/two', 'RetractionDOI': '', 'RetractionNature': 'Retraction'},
            ])
            r = validate_csv(p)
            self.assertEqual(r['rows'], 4)
            self.assertEqual(r['unique_eligible_original_dois'], 1)
            self.assertEqual(r['rows_with_multi_doi_field_excluded'], 1)
            self.assertEqual(r['rows_with_missing_or_invalid_original_doi'], 1)
            self.assertFalse(r['labels_verified'])
            self.assertFalse(r['heldout_split_frozen'])

    def test_missing_columns_fails(self):
        with tempfile.TemporaryDirectory() as d:
            p = self.write_csv(d, [{'OriginalPaperDOI': '10.1234/a'}])
            with self.assertRaisesRegex(ValueError, 'Missing required CSV columns'):
                validate_csv(p)

    def test_missing_file_fails(self):
        with self.assertRaises(FileNotFoundError):
            validate_csv('this_file_is_not_real.csv')

if __name__ == '__main__':
    unittest.main()
