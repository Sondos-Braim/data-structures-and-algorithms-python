from data_structures_and_algorithms.Data_Structures.stacks_and_queues.stacks_and_queues import Stack
from data_structures_and_algorithms.challenges.multi_bracket_validation.multi_bracket_validation import multi_bracket_validation

def test_multi_bracket_validation():
    assert multi_bracket_validation('[{(])}]')==False
    assert multi_bracket_validation('{ [ ] ( ) }')==True
    assert multi_bracket_validation('{ [ }')==False
    assert multi_bracket_validation('hi(hi)(hi(hi))(())(()hi(hi)')==False
    assert multi_bracket_validation('[{] [ }')==False

