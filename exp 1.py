def threshold(val):
    return 1 if val>=0 else 0

def mcp(xval,wval,b):
    total = sum(x*v for x,v in zip(xval,wval))+b
    return threshold(total)

print("AND")
w=[1,1]
bias=-2

for a,b in [(0,0),(1,0),(0,1),(1,1)]:
    print(f"for value {a},{b}: {mcp([a,b],w,bias)}")

print("OR")
w=[1,1]
bias=-1

for a,b in [(0,0),(1,0),(0,1),(1,1)]:
    print(f"for value {a},{b}: {mcp([a,b],w,bias)}")

print("Not")
w=[-1]
bias=0

for a in [(0),(1)]:
    print(f"for value {a}: {mcp([a],w,bias)}")