class UF:
    def __init__(self, n: int):
        self.uf = [-1] * (n + 1)
        self.count = n

    def find(self, p):
        if self.uf[p] < 0: return p
        self.uf[p] = self.find(self.uf[p])
        return self.uf[p]

    def union(self, p, q):
        pr = self.find(p)
        qr = self.find(q)
        if pr == qr:
            return
        if self.uf[pr] > self.uf[qr]:
            self.uf[qr] += self.uf[pr]
            self.uf[pr] = qr
        else:
            self.uf[pr] += self.uf[qr]
            self.uf[qr] = pr
        self.count -= 1
