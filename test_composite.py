# test_composits.py
from expects import *

from composites import Composite

arr = Composite()

arr[0] = 1
arr[1] = 2
arr[2] = lambda x: x+2
arr[3] = 'a'
arr[4] = {}
arr[7] = Composite

expect(len(arr)).to(equal(8))

expect(lambda: iter(arr)).not_to(raise_error(TypeError))
expect(lambda: [i for i in arr]).not_to(raise_error(TypeError))
expect(lambda: next(arr)).to(raise_error(TypeError))

expect(lambda: len(arr)).not_to(raise_error(TypeError))
expect(lambda: arr[2]).not_to(raise_error(TypeError))
expect(lambda: arr[:]).not_to(raise_error(TypeError))
expect(lambda: arr.extend([1, 2])).to(raise_error(AttributeError))
expect(lambda: arr.__array).to(raise_error(AttributeError))



