class Project:
    def __init__(pqr, x, y):
        pqr.x = x
        pqr.y = y

def is_within_polygon(polygon, point):
    A = []
    B = []
    C = []  
    for i in range(len(polygon)):
        p1 = polygon[i]
        p2 = polygon[(i + 1) % len(polygon)]
        
        a = -(p2.y - p1.y)
        b = p2.x - p1.x
        c = -(a * p1.x + b * p1.y)

        A.append(a)
        B.append(b)
        C.append(c)

    D = []
    for i in range(len(A)):
        y = A[i] * point.x + B[i] * point.y + C[i]
        D.append(y)

    z1 = all(y >= 0 for y in D)
    z2 = all(y <= 0 for y in D)
    return z1 or z2

if __name__ == '__main__':
    polygon = [Project(-3,2), Project(-2,-0.8), Project(0,1.2), Project(2.2,0), Project(2.4,5)]
    p1 = Project(0, 0)
    f= is_within_polygon(polygon, p1)
    print(f)