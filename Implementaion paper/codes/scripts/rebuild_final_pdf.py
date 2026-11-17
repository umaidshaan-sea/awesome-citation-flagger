from pathlib import Path
import fitz, json, shutil, hashlib, re, collections
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/'inputs/final_paper_source_verbatim.pdf'
TARGET=ROOT/'paper/manuscript.pdf'
DF=pd.read_csv(ROOT/'results/processed/benchmark_results.csv')
POS=DF[DF.gold_label=='RETRACTED']; NEG=DF[DF.gold_label=='NOT_RETRACTED']
assert len(DF)==80 and len(POS)==len(NEG)==40 and DF.doi.is_unique
assert int((POS.crossref_prediction=='RETRACTED').sum())==40
assert int((POS.legacy_prediction=='RETRACTED').sum())==24
assert int((POS.legacy_prediction=='UNKNOWN').sum())==16
assert int(POS.has_notice_evidence.sum())==32
assert int((NEG.openalex_prediction=='UNKNOWN').sum())==4
assert int((NEG.legacy_prediction=='UNKNOWN').sum())==4
assert int((NEG.crossref_prediction=='UNKNOWN').sum())==4
# Source latency is archived instrumentation, not new network measurement.
legacy=pd.read_csv(ROOT/'audit/original_results/benchmark_results_legacy.csv')
sequential=legacy.openalex_latency_ms+legacy.crossref_latency_ms
assert round(sequential.mean(),1)==2128.2 and round(sequential.std(),1)==558.9

# Regenerate chart 5 from exactly the saved historical/legacy decisions; unknown/unknown
# controls are deliberately excluded, so the chart's actual sample is N=76, not N=80.
counts=[
 int(((DF.gold_label=='RETRACTED')&(DF.openalex_prediction=='RETRACTED')&(DF.legacy_prediction=='RETRACTED')).sum()),
 int(((DF.gold_label=='RETRACTED')&(DF.openalex_prediction=='RETRACTED')&(DF.legacy_prediction=='UNKNOWN')).sum()),
 int(((DF.gold_label=='RETRACTED')&(DF.openalex_prediction!='RETRACTED')&(DF.legacy_prediction=='RETRACTED')).sum()),
 int(((DF.gold_label=='NOT_RETRACTED')&(DF.openalex_prediction=='NOT_RETRACTED')&(DF.legacy_prediction=='NOT_RETRACTED')).sum()),
]
assert counts==[24,16,0,36] and sum(counts)==76
labels=['Both Agree\n(Retracted)','OpenAlex Only\n(CR Missing Notice)','Crossref Only\n(OA Lag)','Both Agree\n(Negative Control)']
plt.rcParams.update({'font.family':'DejaVu Sans','pdf.fonttype':42})
fig,ax=plt.subplots(figsize=(6.9,3.6),dpi=225)
cs=['#0f9b82','#f59e0b','#64748b','#d9308b']
xs=np.arange(4)
ax.bar(xs,counts,width=.65,color=cs,edgecolor='#333333',linewidth=.5)
for x,v in zip(xs,counts):ax.text(x,v+.6,str(v),ha='center',va='bottom',fontsize=9,weight='bold')
ax.set_xticks(xs,labels,fontsize=7.4)
ax.set_yticks(range(0,41,10))
ax.set_ylim(0,43)
ax.set_ylabel('Number of DOIs',fontsize=9)
ax.set_title('Provider Agreement and Disagreement Distribution (N=76)',fontsize=10,weight='bold',pad=6)
ax.grid(axis='y',alpha=.23)
ax.set_axisbelow(True)
for spine in ['top','right']:ax.spines[spine].set_visible(False)
fig.subplots_adjust(left=.12,right=.99,top=.87,bottom=.22)
asset_dir=ROOT/'paper/figures'
fig.savefig(asset_dir/'legacy_disagreement_breakdown.pdf')
fig.savefig(asset_dir/'legacy_disagreement_breakdown.png',dpi=225)
shutil.copy2(asset_dir/'legacy_disagreement_breakdown.pdf',ROOT/'results/figures/legacy_disagreement_breakdown.pdf')
shutil.copy2(asset_dir/'legacy_disagreement_breakdown.png',ROOT/'results/figures/legacy_disagreement_breakdown.png')
plt.close(fig)

# Preserve every word, grammar choice, and spelling in the uploaded PDF. Change ONLY
# three source numeric values and the numerical chart sample size.
doc=fitz.open(SOURCE)
body_regular='/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf'
body_bold='/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf'
operations=[
 (3,fitz.Rect(276.682,334.668,289.355,344.631),'36','DVReg',body_regular,9.9626,'all 40 negative controls => 36 determinate controls'),
 (4,fitz.Rect(349.09,579.039,377.63,589.002),'558.9','DVReg',body_regular,9.9626,'sequential latency sample SD = 558.9'),
 (5,fitz.Rect(490.9,289.573,528.16,298.17),'(80.0%)','DVBold',body_bold,8.59673,'32 distinct notices / 40 = 80.0%'),
]
for page_num,rect,new_name,font_name,font_file,size,comment in operations:
 pg=doc[page_num]
 pg.add_redact_annot(rect,fill=(1,1,1),cross_out=False)
# White-out chart canvas completely; it contains no document prose.
chart_rect=fitz.Rect(94,475.1,281,581.1)
doc[4].add_redact_annot(chart_rect,fill=(1,1,1),cross_out=False)
for pg in doc:
 pg.apply_redactions(images=0,graphics=0,text=0)
for page_num,rect,value,font_name,fontfile,size,comment in operations:
 pg=doc[page_num]
 pg.insert_font(fontname=font_name,fontfile=fontfile)
 width=fitz.Font(fontfile=fontfile).text_length(value,fontsize=size)
 scale=min(1.0,(rect.width-1)/max(width,1))
 # Maintain the original word baseline rather than y of bounding-box top.
 baseline = rect.y0 + (7.5716 if size>9.0 else 6.5335)
 pg.insert_text((rect.x0,baseline),value,fontname=font_name,fontsize=size,morph=(fitz.Point(rect.x0,baseline),fitz.Matrix(scale,0,0,1,0,0)),color=(0,0,0),overlay=True)
chart=fitz.open(asset_dir/'legacy_disagreement_breakdown.pdf')
doc[4].show_pdf_page(chart_rect,chart,0,keep_proportion=True,overlay=True)
doc.set_metadata({**doc.metadata,'title':'Retraction Status and Notice-Link Evidence: An Audit of Crossref and OpenAlex','author':'Md Umaid Shaan'})
doc.save(TARGET,garbage=4,deflate=True)
doc.close()
shutil.copy2(TARGET,ROOT/'paper/final_reconciled_paper.pdf')
# Update legacy source TABLE 3's arithmetic mistake; leave its legacy classifier
# values historical rather than pretending the original status code had been corrected.
tab=ROOT/'paper/tables/legacy_publisher_compliance_table.tex'
s=tab.read_text()
assert ('32 (60.0\\%)' in s) or ('32 (80.0\\%)' in s)
s=s.replace('32 (60.0\\%)','32 (80.0\\%)')
tab.write_text(s)
shutil.copy2(tab,ROOT/'audit/original_results/tables_legacy/publisher_compliance_table_numeric_reconciled.tex')
# Create a versioned, machine-readable ledger.
ledger={
 'source_file_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
 'output_file_sha256':hashlib.sha256(TARGET.read_bytes()).hexdigest(),
 'numeric_changes':[{'page':pn+1,'new':v,'explanation':why} for pn,r,v,_,_,sz,why in operations],
 'figure_5':{'historical_legacy_counts':dict(zip(['both_retracted','openalex_only','crossref_only','both_clean'],counts)),'shown_n':sum(counts),'omitted_unknown_controls':4,'old_plot_n_label':80,'new_plot_n_label':76},
 'table_3':{'distinct_notice_count':32,'positive_count':40,'corrected_notice_pct':80.0,'status_count_legacy':24,'status_count_corrected':40},
 'baseline_legacy':{'TP':24,'FP':0,'TN':36,'FN':0,'UNKNOWN':20,'F1_determinate':1.0,'F1_end_to_end':0.75},
 'baseline_corrected':{'TP':40,'FP':0,'TN':36,'FN':0,'UNKNOWN':4,'F1_determinate':1.0,'F1_end_to_end':1.0},
 'scope':'Only numeric glyphs patched in main PDF; no prose/spelling/grammar changes. Figures/tables retain historical classification modes where labeled as such.',
}
(ROOT/'audit/NUMERIC_CORRECTION_LEDGER.json').write_text(json.dumps(ledger,indent=2))
print(json.dumps(ledger,indent=2))
