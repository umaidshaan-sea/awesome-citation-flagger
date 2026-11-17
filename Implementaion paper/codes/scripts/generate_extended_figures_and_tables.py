"""Compatibility entrypoint for regenerated accurate figures and tables.
No artificial latency samples are produced in the corrected implementation.
"""
import subprocess,sys
from pathlib import Path
root=Path(__file__).resolve().parents[1]
subprocess.run([sys.executable,str(root/'scripts/render_corrected_artifacts.py')],cwd=root,check=True)
