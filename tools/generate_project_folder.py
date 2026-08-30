import argparse
from pathlib import Path
README='# {title}\n\n## Problem\n\n## Users\n\n## Architecture\n\n## Features\n\n## Tech Stack\n\n## Quick Start\n\n## Evaluation\n\n## Security\n\n## Failure Modes\n\n## Production Considerations\n\n## Business Value\n\n## What I Learned\n'
def main():
 p=argparse.ArgumentParser(); p.add_argument('name'); p.add_argument('--output',default='generated-projects'); a=p.parse_args()
 folder=Path(a.output)/a.name.lower().replace(' ','-'); folder.mkdir(parents=True,exist_ok=True)
 (folder/'README.md').write_text(README.format(title=a.name),encoding='utf-8')
 for d in ['src','tests','docs']: (folder/d).mkdir(exist_ok=True)
 print(f'Created: {folder}')
if __name__=='__main__': main()
