class Matrix(object):
          
    def __init__(self, list2D):
        self.list2D = list2D
        self.dim_R = len(self.list2D)
        self.dim_C = len(self.list2D[0])
    
          
                
    
    def __repr__(self):
        b=0
        for i in self.list2D:
            if len(self.list2D[b])==len(self.list2D):
                b=b+1
                x = True
            else:
                b=b+1
                x = False
                if x == False:
                    return 'ill-shape'        
        c = (''.join([str(i) for i in self.list2D]))
        c = c.replace('[', '')
        c = c.replace(',', '')
        c = c.replace(']', '')
        c = c.replace(' ', '')
        if c.isdigit()==True:
                res = ''
                for x in self.list2D:
                    s = '['
                    for y in x:
                        s +=str(y) + ',' + ' '
                    s = s[0:-1]
                    s = s[0:-1]
                    s = s + ']' + ','
                    res += s + '\n' + ' '
                res = res[0:-1]
                res = res[0:-1]
                res = '[' + res +']'
                res = res[0:-2] + ']'                
                return res
        else:
            return 'not digit'
   
    def __add__(self, other):
        if self.dim_R == other.dim_R and self.dim_C == other.dim_C:
            result = []
            res = []
            for x in range(self.dim_R):
                for y in range(self.dim_C):
                    sum = self.list2D[x][y] + other.list2D[x][y]
                    res.append(sum)
                result.append(res)
                res = []
            return matrix(result)
        else:
            return 'No match'
    def __sub__(self, other):
        if self.dim_R == other.dim_R and self.dim_C == other.dim_C:
            res = []
            result = []
            for x in range(self.dim_R):
                for y in range(self.dim_C):
                    sub = self.list2D[x][y] - other.list2D[x][y]
                    res.append(sub)
                result.append(res)
                res = []
            return matrix(result)
        else:
            return 'No match'
    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            result = [[other * x for x in y] for y in self.list2D]
            return matrix(result)
        elif self.dim_C != other.dim_R:
            return 'Can"t do it'
        else:
            a = range(self.dim_C)
            b = range(self.dim_R)
            c = range(other.dim_C)
            result = []
            for i in b:
                res = []
                for j in c:
                    el, m = 0, 0
                    for k in a:
                        m = self.list2D[i][k] * other.list2D[k][j]
                        el += m
                    res.append(el)
                result.append(res)
            return matrix(result)
    def __rmul__(self, other):
        return self.__mul__(other)
    
a = Matrix([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
print (a)
