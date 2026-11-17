import pandas as pd

def evaluate(rows):
    # Benchmark-label agreement only. These input labels are NOT independently adjudicated.
    df = pd.DataFrame(rows)
    if df.empty or 'gold_label' not in df:
        raise ValueError('No labeled records')
    verified = df[df['gold_label'].isin(['RETRACTED', 'NOT_RETRACTED'])].copy()
    if len(verified) != len(df):
        raise ValueError('Refusing formal scoring: some gold labels UNVERIFIED/UNCERTAIN.')
    if verified['gold_evidence_url'].fillna('').str.strip().eq('').any():
        raise ValueError('Missing label-evidence URL: cannot score even provisional benchmark labels.')
    if verified['gold_label'].nunique() < 2:
        raise ValueError('Both verified positive and verified negative cases required for full metrics.')
    out = []
    for col in ['openalex_prediction', 'crossref_prediction', 'combined_prediction']:
        p = verified[col]; y = verified.gold_label
        tp = int(((y == 'RETRACTED') & (p == 'RETRACTED')).sum())
        fp = int(((y == 'NOT_RETRACTED') & (p == 'RETRACTED')).sum())
        tn = int(((y == 'NOT_RETRACTED') & (p == 'NOT_RETRACTED')).sum())
        fn = int(((y == 'RETRACTED') & (p == 'NOT_RETRACTED')).sum())
        unknown = int((p == 'UNKNOWN').sum())
        # End-to-end recall counts abstentions on positives as failures to detect.
        pos_unknown = int(((y == 'RETRACTED') & (p == 'UNKNOWN')).sum())
        neg_unknown = int(((y == 'NOT_RETRACTED') & (p == 'UNKNOWN')).sum())
        recall = tp / (y == 'RETRACTED').sum()
        out.append({'method': col, 'TP': tp, 'FP': fp, 'TN': tn, 'FN': fn, 'UNKNOWN': unknown,
                    'positive_unknown': pos_unknown, 'negative_unknown': neg_unknown, 'end_to_end_recall': recall, 'precision_determinate': tp/(tp+fp) if tp+fp else None,
                    'F1_determinate': 2*tp/(2*tp+fp+fn) if 2*tp+fp+fn else None,
                    'F1_end_to_end': 2*tp/(2*tp+fp+fn+pos_unknown) if 2*tp+fp+fn+pos_unknown else None,
                    'FPR_determinate': fp/(fp+tn) if fp+tn else None,
                    'coverage': 1-unknown/len(verified)})
    return pd.DataFrame(out)
