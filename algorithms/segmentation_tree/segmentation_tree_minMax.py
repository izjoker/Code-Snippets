class SegTree(list):
    def __init__(self, series):
        self.source = [-1] + series
        self.tree = [[float('inf'), -float('inf')] for i in range(4*len(series))]   
        self.buildtree()

    def buildtree(self):
        def build(s, e, idx):
            if s == e:
                self.tree[idx] = [self.source[s], self.source[s]]
                return
            mid = (s+e)//2
            for i in range(s, e+1):
                self.tree[idx][0] = min(self.tree[idx][0], self.source[i])
                self.tree[idx][1] = max(self.tree[idx][1], self.source[i])
            build(s, mid, 2*idx)
            build(mid+1, e, 2*idx+1)
        build(1, len(self.source)-1, 1)

    def searchRange(self, ran):
        def search(s, e, idx, ran):
            if e < ran[0] or s > ran[1]:
                return [float('inf'), -float('inf')]
            if ran[0] <= s and e <= ran[1]:
                return self.tree[idx]
            mid = (s+e)//2
            left = search(s, mid, idx*2, ran)
            right = search(mid+1, e, idx*2+1, ran)
            return [min(left[0], right[0]), max(left[1], right[1])]
        return search(1, len(self.source)-1, 1, ran)

    def changeValue(self, v_i, v):
        self.source[v_i] = v
        def change(s, e, idx, v_i, v):
            if e < v_i or s > v_i or s == e:
                return
            if s <= v_i <= e:
                self.tree[idx] = [min(self.tree[idx][0], v), max(self.tree[idx][1], v)]
            mid = (s+e)//2
            left = change(s, mid, idx*2, v_i, v)
            right = change(mid+1, e, idx*2+1, v_i, v)
        change(1, len(self.source)-1, 1, v_i, v)
        
