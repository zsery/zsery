"""Restore the recorded working layout into a NEW directory; never run builders."""
import argparse, hashlib, shutil
from pathlib import Path

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--target',required=True,help='New, nonexistent local working directory; never VDI')
    ap.add_argument('--dry-run',action='store_true')
    args=ap.parse_args()
    bundle=Path(__file__).resolve().parents[1];repo=bundle.parent
    target=Path(args.target).expanduser().resolve()
    if target.exists():ap.error('Target already exists. Choose a NEW directory; no overwrite is performed.')
    if target==repo or repo in target.parents:ap.error('Target must be outside the source checkout.')
    pairs=[]
    for p in (bundle/'outputs').rglob('*'):
        if p.is_file() and not p.name.startswith('~$'):pairs.append((p,Path('outputs')/p.relative_to(bundle/'outputs')))
    for p in (bundle/'reproduction/book1-v03').iterdir():
        if p.is_file():pairs.append((p,Path('work/book1-consolidation')/p.name))
    pairs.extend([(repo/'Atlas.7z',Path('inputs/Atlas.7z')),(repo/'Book1.xlsx',Path('work/book1/Book1-original.xlsx')),
                  (bundle/'reproduction/ea-index.py',Path('work/ea/index.py')),
                  (bundle/'reproduction/review_primary_business.py',Path('work/ea/review_primary_business.py')),
                  (bundle/'reproduction/book1-original-data.json',Path('work/book1/data.json'))])
    for p in (bundle/'pending/book1-dxl-update').iterdir():
        if p.is_file():pairs.append((p,Path('pending/book1-dxl-update')/p.name))
    if any(not p.is_file() for p,_ in pairs):ap.error('Source package is incomplete.')
    print(f'{len(pairs)} files; target {target}; pending code remains separate; no builder will run.')
    if args.dry_run:return
    target.mkdir(parents=True,exist_ok=False)
    for src,rel in pairs:
        dst=target/rel;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst)
        if hashlib.sha256(src.read_bytes()).digest()!=hashlib.sha256(dst.read_bytes()).digest():
            raise RuntimeError(f'Copy verification failed: {rel}')
    print('Copied and hash-verified. Read instructions/reproduction.md before executing any builder.')

if __name__=='__main__':main()
