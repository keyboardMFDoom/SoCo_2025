#################                                   Week 2                                      ##########

def add(n1,n2):
    result = n1 + n2
    return result

def my_abs(n1):
    if n1 > 0:
        return n1
    if n1 < n1:
        return -n1
## the shorter the better (Empirical Software Engineering proves that exponential growth per line of code)

a = add(1,3)
print(a)

abs_result = add(1,2)
##Problem: print not optimal for checking the code

additional_result = add(1,2)
expected_result = 3
if additional_result != expected_result:
    print("conducter we have a problem, the result was")

abs_result = abs(0)
expected_result = 0
if additional_result != expected_result:
    print(f"conducter we have a problem, the result was {abs_result}")

#Introduction to running tests

def first():
    print("first")

def second():
    print("second")

def third():
    print("third")

everything = [first, second, third]
for each_func in everything:
    each_func()

def sign(value):
    if value < 0:
        return -1
    else:
        return 1
def test_sign_negative():
    expected = -1
    result = sign(-3)
    assert result == expected

def test_sign_positive():
    expected = 1
    result = sign(3)
    assert result == expected


#Problem: no oversight, assertion and error. We want to get more information and run all tests.

def run_tests(all_tests):
    test_results = {"pass":0, "fail":0, "error": 0}
    for test in all_tests:
        try: #if it worked
            test()
            test_results["pass"] += 1
        except AssertionError: #specify for AssertionError
            test_results["fail"] += 1
        except Exception: #catches everything else (also a parent of AssertionError)
            test_results["error"] += 1
    print("pass", test_results["pass"])
    print("error", test_results["error"])
    print("fail", test_results["fail"])

tests = [test_sign_negative,test_sign_positive]
run_tests(tests)
# Nice but we can't see which test did fail or succeed
# Solution: one test per function/task etc.
# pytest does introspection

import pprint

pprint.pprint(globals())

if __name__ =="__main__":
    print("this file is executed directly and not imported")

def substract(n1, n2):
    return n1-n2



def find_tests(prefix="test_"):
    for (name, func) in globals().items():
        if name.startswith(prefix):
            print(name)
find_tests()

##later more on locally and globally
