
def test_are_equal(actual, expected):
    assert expected == actual, "Expected {0}, got {1}".format(expected, actual)


def test_not_equal(a, b):
    assert a != b, "Did not expect {0}, but got {1}".format(a, b)


def test_is_in(collection, item):
    assert item in collection, "{0} does not contain {1}".format(collection, item)

def test_equal(a, b):
    assert a == b, "Did not expect them to be equal"
    
def test_not_in(collection, item):
    assert item not in collection, "Was expecting {} in {}".format(item, collection)
    
def test_between(Range, a, b):
    localRange = range(Range[0], Range[1])
    assert a in localRange, "a {} is not within its range".format(a)
    assert b in localRange, "b {} is not within its range".format(b)


test_not_equal(3,4) # Challenge 1
test_is_in([1,2,3,4], 4)
test_between([0,5], 5,6)