from ShapeCube import Cube

inp = input().split()
inputs = (float(x) for x in inp)
c = Cube(*inputs)
c.printResults()
