"""Regenerate every active figure and table from audited archived-API results."""
from pathlib import Path
import sys
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import patches
ROOT=Path(__file__).resolve().parents[1]
F=ROOT/'results/figures';T=ROOT/'results/tables'
F.mkdir(parents=True,exist_ok=True);T.mkdir(parents=True,exist_ok=True)
df=pd.read_csv(ROOT/'results/processed/benchmark_results.csv').fillna('')
pos=df[df.gold_label=='RETRACTED']
metrics=pd.read_csv(ROOT/'results/processed/metrics_summary.csv')
plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False,'pdf.fonttype':42,'savefig.dpi':230})
COL={'blue':'#1e497b','cyan':'#168ba0','orange':'#c66b30','green':'#2c7961','gray':'#758392','light':'#e8eef3','red':'#b54047'}

def save(fig,name):
    fig.savefig(F/f'{name}.png',dpi=230,bbox_inches='tight',facecolor='white')
    fig.savefig(F/f'{name}.pdf',bbox_inches='tight',facecolor='white')
    fig.savefig(ROOT/'paper/figures'/f'{name}.pdf',bbox_inches='tight',facecolor='white')
    plt.close(fig)

def diagram():
    fig,ax=plt.subplots(figsize=(10.5,3.5));ax.set_xlim(0,10.5);ax.set_ylim(0,3.5);ax.axis('off')
    def box(x,y,w,h,label,detail,color):
        ax.add_patch(patches.FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.11',facecolor='#f7f9fb',edgecolor=color,linewidth=1.7))
        ax.text(x+w/2,y+h*.70,label,ha='center',va='center',size=10.5,weight='bold',color=color)
        ax.text(x+w/2,y+h*.37,detail,ha='center',va='center',size=8.5,color='#222b38',linespacing=1.35)
    def arrow(x,y,x2,y2):ax.annotate('',xy=(x2,y2),xytext=(x,y),arrowprops={'arrowstyle':'-|>','lw':1.6,'color':'#52667a'})
    box(.08,1.30,1.55,.88,'Input DOI','Normalize and\ncheck syntax',COL['gray'])
    box(2.20,2.16,2.42,.94,'OpenAlex B0','is_retracted status\n(no notice DOI)',COL['blue'])
    box(2.20,.26,2.42,.94,'Crossref B1*','typed retraction status\n+ distinct notice DOI',COL['cyan'])
    box(5.39,1.31,2.32,.98,'Reconcile','RETRACTED if either positive\nUNKNOWN on missing data',COL['green'])
    box(8.38,1.31,1.96,.98,'Outputs','Status + signal sources\n+ optional notice link',COL['orange'])
    arrow(1.67,1.74,2.12,2.55);arrow(1.67,1.74,2.12,.69)
    arrow(4.67,2.55,5.31,1.90);arrow(4.67,.73,5.31,1.71);arrow(7.77,1.78,8.31,1.78)
    ax.text(5.4,3.33,'Notice-link evidence is optional; it is not a prerequisite for a positive status signal',ha='left',size=9,color=COL['red'])
    save(fig,'system_architecture')

def performance():
    fig,ax=plt.subplots(figsize=(7.6,3.2))
    names=['OpenAlex B0','Crossref B1*','Combined M*']
    xs=np.arange(3)
    ax.bar(xs-.17,[1,1,1],width=.32,color=COL['blue'],label='Positive-label recall')
    ax.bar(xs+.17,[.95,.95,.95],width=.32,color=COL['cyan'],label='Decision coverage')
    for x in xs:
        ax.text(x-.17,1.018,'40/40',ha='center',va='bottom',fontsize=9)
        ax.text(x+.17,.965,'76/80',ha='center',va='bottom',fontsize=9)
    ax.set_ylim(0,1.13)
    ax.set_xticks(xs,names)
    ax.set_ylabel('Share of cases')
    ax.set_yticks([0,.25,.5,.75,1],["0%","25%","50%","75%","100%"])
    ax.legend(ncol=2,loc='lower center',bbox_to_anchor=(.5,1.12),frameon=False)
    ax.set_title('Archived benchmark decisions',weight='bold',pad=37)
    fig.subplots_adjust(left=.11,right=.98,bottom=.19,top=.72)
    save(fig,'metric_comparison')

def confusions():
    fig,axes=plt.subplots(1,3,figsize=(10.3,3.0))
    names=['B0 OpenAlex','B1* Crossref','M* Combined']
    for ax,name in zip(axes,names):
        matrix=np.array([[40,0,0],[0,36,4]])
        ax.imshow(matrix,cmap='Blues',vmin=0,vmax=40,aspect='auto')
        ax.set_title(name,size=10,weight='bold')
        ax.set_xticks([0,1,2],['RET','NOT RET','UNK'],fontsize=8)
        ax.set_yticks([0,1],['RW retraction (40)','Presumed control (40)'],fontsize=8)
        for (i,j),v in np.ndenumerate(matrix):ax.text(j,i,str(v),ha='center',va='center',color='white' if v>24 else 'black',size=13,weight='bold')
        ax.set_xlabel('Predicted status',size=9)
    fig.tight_layout();save(fig,'confusion_matrices')

def coverage():
    grouped=pd.read_csv(ROOT/'results/processed/publisher_breakdown.csv')
    grouped['rate']=100*grouped.distinct_notice_doi/grouped.positive_cases
    grouped=grouped.sort_values('positive_cases',ascending=True)
    fig,ax=plt.subplots(figsize=(8.0,4.2))
    y=np.arange(len(grouped))
    ax.barh(y+.19,[100]*len(grouped),.34,color=COL['blue'],label='Typed status signal')
    ax.barh(y-.19,grouped.rate,.34,color=COL['orange'],label='Distinct notice DOI')
    ax.set_yticks(y,[f'{a} (n={b})' for a,b in zip(grouped.publisher_group,grouped.positive_cases)],fontsize=9)
    for i,row in enumerate(grouped.itertuples()):
        ax.text(row.rate+2.2,i-.19,f'{row.distinct_notice_doi}/{row.positive_cases}',va='center',fontsize=9)
    ax.set_xlim(0,121)
    ax.set_xticks([0,25,50,75,100],["0%","25%","50%","75%","100%"])
    ax.set_xlabel('Share of source-labeled positives')
    ax.legend(ncol=2,loc='lower center',bbox_to_anchor=(.5,1.07),frameon=False)
    ax.set_title('Status signal vs. separate notice DOI',size=11,weight='bold',pad=37)
    fig.subplots_adjust(left=.33,right=.96,bottom=.13,top=.76)
    save(fig,'publisher_coverage')

def provenance():
    a=int(pos.status_sources.str.contains('publisher').sum())
    b=int(pos.status_sources.str.contains('retraction-watch').sum())
    both=int((pos.status_sources.str.contains('publisher')&pos.status_sources.str.contains('retraction-watch')).sum())
    values=[a-both,b-both,both]
    fig,ax=plt.subplots(figsize=(7.5,2.6))
    labels=['Publisher signal only','Retraction Watch signal only','Both sources']
    colors=[COL['blue'],COL['orange'],COL['green']]
    ax.barh(['40 RW-listed papers'],[values[0]],color=colors[0],label=f'{labels[0]} ({values[0]})')
    ax.barh(['40 RW-listed papers'],[values[1]],left=[values[0]],color=colors[1],label=f'{labels[1]} ({values[1]})')
    ax.barh(['40 RW-listed papers'],[values[2]],left=[values[0]+values[1]],color=colors[2],label=f'{labels[2]} ({values[2]})')
    for size,start in zip(values,[0,values[0],values[0]+values[1]]):ax.text(start+size/2,0,str(size),ha='center',va='center',color='white',weight='bold')
    ax.set_xlim(0,40);ax.set_xlabel('Number of papers');ax.legend(ncol=1,loc='upper center',bbox_to_anchor=(.53,-.34),frameon=False)
    ax.set_title('Crossref source attribution for typed retraction signals',weight='bold',size=11)
    save(fig,'provenance_sources')

def latex(x):
    return str(x).replace('\\','\\textbackslash{}').replace('_','\\_').replace('&','\\&').replace('%','\\%').replace('#','\\#')

def write_table(s,name):
    if name == 'publisher_compliance_table':
        s = s.replace(r'\begin{tabular}{lrrrr}', r'\resizebox{\columnwidth}{!}{\begin{tabular}{lrrrr}').replace(r'\end{tabular}', r'\end{tabular}}')
    if name == 'comparative_metrics_table':
        s = s.replace(r'\begin{tabular}{lrrrrrrrr}', r'\resizebox{\textwidth}{!}{\begin{tabular}{lrrrrrrrr}').replace(r'\end{tabular}', r'\end{tabular}}')
    (T/f'{name}.tex').write_text(s,encoding='utf-8')
    (ROOT/'paper/tables'/f'{name}.tex').write_text(s,encoding='utf-8')

def tables():
    table=r'''\begin{table*}[t]
\centering\small
\caption{Archived benchmark-label agreement. $U_+$ and $U_-$ are positive- and control-class abstentions. FP = FN = 0 in every row. ``F1 det.'' excludes abstentions; ``F1 e2e'' penalizes positive abstentions. None is an independently established detection-accuracy estimate.}
\label{tab:comparison}
\begin{tabular}{lrrrrrrrr}
\toprule
Method & TP & TN & $U_+$ & $U_-$ & Recall$^+$ & F1 det. & F1 e2e & Coverage \\
\midrule
OpenAlex $B_0$ & 40 & 36 & 0 & 4 & 1.00 & 1.00 & 1.00 & 76/80 \\
Corrected Crossref $B_1^*$ & 40 & 36 & 0 & 4 & 1.00 & 1.00 & 1.00 & 76/80 \\
Combined $M^*$ & 40 & 36 & 0 & 4 & 1.00 & 1.00 & 1.00 & 76/80 \\
\midrule
Legacy $B_1$ (diagnostic) & 24 & 36 & 16 & 4 & 0.60 & 1.00 & 0.75 & 60/80 \\
\bottomrule
\end{tabular}
\end{table*}'''
    write_table(table,'comparative_metrics_table')
    grouped=pd.read_csv(ROOT/'results/processed/publisher_breakdown.csv').sort_values('publisher_group')
    table=r'''\begin{table}[t]
\centering\footnotesize
\caption{Publisher groups reflect the labels in the frozen split. A distinct notice link must differ from the article DOI; it is not proof of independent publisher verification.}
\label{tab:publisher}
\begin{tabular}{lrrrr}
\toprule
Group & $N$ & Typed & Notice & Self-only \\
\midrule
'''
    for row in grouped.itertuples():
        table += f'{latex(row.publisher_group)} & {row.positive_cases} & {row.crossref_typed} & {row.distinct_notice_doi} & {row.self_only} ' + r'\\' + '\n'
    table+=r'''\midrule
Total & 40 & 40 & 32 & 8 \\
\bottomrule
\end{tabular}
\end{table}'''
    write_table(table,'publisher_compliance_table')
    table=r'''\begin{table}[t]
\centering\footnotesize
\caption{What the archived records actually establish.}
\label{tab:signals}
\begin{tabular}{lr}
\toprule
Observed condition & Papers \\
\midrule
Crossref typed retraction signal & 40/40 \\
Distinct retraction notice DOI & 32/40 \\
Self-only typed retraction & 8/40 \\
Publisher-attributed typed signal & 29/40 \\
Retraction Watch-attributed typed signal & 37/40 \\
Publisher-attributed distinct notice & 20/40 \\
Both APIs return 404 on controls & 4/40 \\
\bottomrule
\end{tabular}
\end{table}'''
    write_table(table,'signal_evidence_table')
    table=r'''\begin{table*}[t]
\centering\small
\caption{Representative cached Crossref cases; a same-DOI entry is a status signal, not a separately linkable notice.}
\label{tab:cases}
\begin{tabular}{lp{6.3cm}p{4.0cm}}
\toprule
Article DOI & Archived retraction relations & Correct interpretation \\
\midrule
\texttt{10.1007/s13204-021-01976-4} & Typed retraction with target DOI as update DOI & RETRACTED; no distinct notice DOI \\
\texttt{10.15252/embr.202153509} & Both self-DOI and distinct notice DOI & RETRACTED; notice DOI available \\
\texttt{10.1016/j.arabjc.2021.102998} & Retraction update(s), plus erratum & RETRACTED; correction does not cancel retraction \\
\texttt{10.1109/cctae.2010.5544611} & Self-DOI typed retraction entry & RETRACTED; no distinct notice DOI \\
\bottomrule
\end{tabular}
\end{table*}'''
    # The case-study table is generated from underlying cached retraction relations.
    cases=['10.1007/s13204-021-01976-4','10.15252/embr.202153509',
           '10.1016/j.arabjc.2021.102998','10.1109/cctae.2010.5544611']
    table=r'''\begin{table*}[t]
\centering\small
\caption{Four representative legacy failure traces from the archived Crossref responses. ``Self'' counts retraction updates whose DOI equals the article DOI; ``Distinct'' counts retraction updates with a different DOI. No case is independently adjudicated by this table.}
\label{tab:cases}
\begin{tabular}{lrrrrl}
\toprule
Article DOI & Self & Distinct & Other update(s) & Legacy $B_1$ & Corrected $B_1^*$ \\
\midrule
'''
    import json,hashlib
    for identifier in cases:
        row=df[df.doi==identifier].iloc[0]
        p=ROOT/'data/processed/api_cache/crossref'/(hashlib.sha256(identifier.encode()).hexdigest()+'.json')
        rec=json.loads(p.read_text()).get('record') or {}
        others=[x for x in (rec.get('updated-by') or []) if isinstance(x,dict) and str(x.get('type')).lower() != 'retraction']
        table+=f'\\texttt{{{latex(identifier)}}} & {int(row.self_relation_count)} & {int(row.distinct_relation_count)} & {len(others)} & UNKNOWN & RETRACTED ' + r'\\' + '\n'
    table+=r'''\bottomrule
\end{tabular}
\end{table*}'''
    write_table(table,'case_studies_table')
    title_summary=pd.crosstab(df.gold_label,df.title_audit_flag).reindex(
        index=['RETRACTED','NOT_RETRACTED'],
        columns=['MATCH_OR_SIMILAR','TITLE_MISMATCH_REVIEW','MISSING_PROVIDER_RECORD'],fill_value=0)
    title_summary.loc['TOTAL']=title_summary.sum()
    table=r'''\begin{table}[t]
\centering\footnotesize
\caption{Crossref-title audit by benchmark class. Mismatches use a normalized-string similarity threshold below 0.55; this is a screening flag, not independent adjudication.}
\label{tab:titleaudit}
\begin{tabular}{lrrr}
\toprule
Class & Similar & Flagged & No record \\
\midrule
'''
    for name in ['RETRACTED','NOT_RETRACTED','TOTAL']:
        row=title_summary.loc[name]
        table+=f'{latex(name)} & {int(row.MATCH_OR_SIMILAR)} & {int(row.TITLE_MISMATCH_REVIEW)} & {int(row.MISSING_PROVIDER_RECORD)} ' + r'\\' + '\n'
    table+=r'''\bottomrule
\end{tabular}
\end{table}'''
    write_table(table,'title_integrity_table')

def main():
    assert len(df)==80 and len(pos)==40 and int(pos.has_notice_evidence.sum())==32
    assert int(pos.status_self_only.sum())==8
    diagram();performance();confusions();coverage();provenance();tables()
    print('Created 5 paired PDF/PNG figures and 5 LaTeX tables directly from corrected 80-row results')

if __name__=='__main__':main()
