import pytest
from tools.portfolio_logic import score_project,recommend_for_role

def test_flagship_score():
 r=score_project(5,5,5,4,4,4,5,5); assert r['total']==37; assert r['verdict']=='Flagship project candidate'
def test_invalid_score():
 with pytest.raises(ValueError): score_project(6,5,5,5,5)
def test_ai_engineer_recommendations():
 items=recommend_for_role('ai-engineer'); assert len(items)>=5; assert 'Enterprise RAG Assistant' in items
def test_unknown_role():
 with pytest.raises(ValueError): recommend_for_role('unknown-role')
