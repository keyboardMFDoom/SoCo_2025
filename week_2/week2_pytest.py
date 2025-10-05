import pytest
import week2

def test_add():
    expected_result = 3
    addition_result = week2.add(1,2)
    assert addition_result == expected_result

##assert a function in pyhton if written returns a boolean 
#i.e
#(my_environment) C:\Users\arsen\Git_repositories\SoCo_2025>pytest.exe .\week2.py if this is ran
assert week2.additional_result == week2.expected_result, f"calling the problem"

print("end of this file")