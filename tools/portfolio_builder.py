from pathlib import Path
import argparse,sys
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from tools.portfolio_logic import recommend_for_role,score_project

def main():
 p=argparse.ArgumentParser(description='AI Portfolio Builder CLI'); sub=p.add_subparsers(dest='command',required=True)
 r=sub.add_parser('recommend'); r.add_argument('--role',required=True)
 s=sub.add_parser('score'); s.add_argument('--title',required=True)
 for name in ['business-value','technical-depth','demo-quality','differentiation','production-readiness']:
  s.add_argument('--'+name,type=int,required=True)
 for name in ['documentation','learning-value','interview-value']:
  s.add_argument('--'+name,type=int,default=3)
 a=p.parse_args()
 if a.command=='recommend':
  print(f'Recommended portfolio for {a.role}:')
  for i,item in enumerate(recommend_for_role(a.role),1): print(f'{i}. {item}')
 else:
  res=score_project(a.business_value,a.technical_depth,a.demo_quality,a.differentiation,a.production_readiness,a.documentation,a.learning_value,a.interview_value)
  print(f'Project: {a.title}'); print(f"Score: {res['total']} / {res['max']}"); print(f"Verdict: {res['verdict']}")
if __name__=='__main__': main()
