"""Safe reproducible runner: archived-input replay and corrected outputs.

This *does not* refresh any APIs or alter frozen DOI selection; see audit/original_scripts
for the initial online collector and its historically inaccurate analysis.
"""
import subprocess,sys
from pathlib import Path
root=Path(__file__).resolve().parents[1]
for script in ('reanalyze_cached.py','render_corrected_artifacts.py'):
    subprocess.run([sys.executable,str(root/'scripts'/script)],cwd=root,check=True)
