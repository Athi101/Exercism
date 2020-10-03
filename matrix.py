class Matrix(object):
    matrix=[]
    def __init__(self, m_string):
        self.matrix = []
        for line in m_string.split('\n'):
            nums = [] 
            for i in line.split():
              nums.append(int(i))
            self.matrix.append(nums)
            
    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        l=[]
        for r in self.matrix:
            l.append(r[index-1])
        return l
