# Date in fisierul de intrare input.txt:
# pe prima linie (n) gradul suprafetei
# pe urmatoarele (n+1)(n+2)/2 linii cate un punct, in ordinea
#            (b(i,j,k) iterat cu i=0..n, j=0..(n-i), k=n-i-j):
# b_(0,0,n)
# b_(0,1,n-1)
# ...
# b_(0, n, 0)
# b_(1, 0, n-1)
# ....
# b_(n,0,0)
# pe urmatoarele linii, oricate tupluri (u,v,w)
# pentru care se va calcula r(u,v,w)

# 2
# 0 0 0
# 1 0 0
# 0 1 0
# 1 1 0
# 0 0 1
# 1 1 1
# 0.3 0.3 0.4

def iterate_idices(n):
    for i in range(n+1):
        for j in range(n+1-i):
            k = n-i-j
            yield (i, j, k)

def ix_add(i, e):
    i0, i1, i2 = i
    e0, e1, e2 = e
    return (i0+e0, i1+e1, i2+e2)

e1 = (1, 0, 0)
e2 = (0, 1, 0)
e3 = (0, 0, 1)

def pt_scale(u, p):
    x, y, z = p
    return (u*x, u*y, u*z)

def pt_add(*args):
    rx, ry, rz = 0, 0, 0
    for (x, y, z) in args:
        rx += x
        ry += y
        rz += z
    return (rx,ry,rz)


def load_input(fname):
    with open(fname, 'r') as f:
        lines = f.read().splitlines()
    n = int(lines[0])

    points = {}
    lcnt = 1
    for ix in iterate_idices(n):
            points[ix] = tuple(map(float, lines[lcnt].split()[:3]))
            lcnt += 1
    coords = []
    for line in lines[lcnt:]:
        coords.append(tuple(map(float, line.split())))
    #u0, v0, w0 = tuple(map(float, lines[-1].split()))
    return n, points, coords

def deCasteljau(n, pts, u,v,w, save_intermediates = False):
    b = pts.copy()

    points = {}

    for r in range(1, n+1):
        new_b = {}
        for ix in iterate_idices(n-r):
            new_b[ix]=pt_add(
                pt_scale(u, b[ix_add(ix, e1)]),
                pt_scale(v, b[ix_add(ix, e2)]),
                pt_scale(w, b[ix_add(ix, e3)]),
            )
        if(save_intermediates): points = {**points, **b}
        b = new_b
    if(save_intermediates): points = {**points, **b}
    return b[(0, 0, 0)], points

if __name__ == '__main__':
    n, pts, coords = load_input("input.txt")
    print(f"n = {n}")
    for k in pts.keys(): print(f"b_{k} = {pts[k]}")
    for u0, v0, w0 in coords:
        print(f"u0,v0,w0 = {u0}, {v0}, {w0}")
        result, _ = deCasteljau(n, pts, u0, v0, w0)
        print(f"r{u0, v0, w0} = {result}")

exit(0)