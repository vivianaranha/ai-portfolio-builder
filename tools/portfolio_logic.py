ROLE_RECOMMENDATIONS={
'ai-engineer':['ML Classification Service','Enterprise RAG Assistant','Tool-Using AI Agent','AI Evaluation Workbench','AI Security Lab','Industry AI Capstone'],
'ai-architect':['Enterprise RAG Reference Architecture','Multi-Agent Orchestration Platform','Enterprise Model Gateway','AI Governance Control Plane','Hybrid AI Architecture','Agent Security Architecture'],
'forward-deployed-engineer':['Customer Discovery to Prototype Lab','Support Ticket Automation','Sales Intelligence Agent','Enterprise API Integration','AI ROI Calculator','Customer Handoff Capstone'],
'genai-engineer':['Structured LLM Application','Enterprise RAG Assistant','Advanced Retrieval Benchmark','Tool-Using AI Agent','LLM Evaluation Harness','Prompt Injection Defense Lab']}

def score_project(business_value,technical_depth,demo_quality,differentiation,production_readiness,documentation=3,learning_value=3,interview_value=3):
 scores={'business_value':business_value,'technical_depth':technical_depth,'demo_quality':demo_quality,'differentiation':differentiation,'production_readiness':production_readiness,'documentation':documentation,'learning_value':learning_value,'interview_value':interview_value}
 if any(v<1 or v>5 for v in scores.values()): raise ValueError('Every score must be between 1 and 5.')
 total=sum(scores.values())
 verdict='Flagship project candidate' if total>=34 else 'Strong portfolio project' if total>=28 else 'Useful, but strengthen weak areas' if total>=22 else 'Too weak or generic for a primary portfolio project'
 return {'scores':scores,'total':total,'max':40,'verdict':verdict}

def recommend_for_role(role):
 key=role.lower().strip()
 if key not in ROLE_RECOMMENDATIONS: raise ValueError(f'Unknown role: {role}')
 return ROLE_RECOMMENDATIONS[key]
