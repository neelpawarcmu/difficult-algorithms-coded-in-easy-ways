if not rodLength or not lengths:
            return 0
        n = len(lengths) - 1
        if lengths[n] <= rodLength:
            maxPrice = max(self.cutRod(rodLength-lengths[n], lengths, prices), self.cutRod(rodLength, lengths[:n], prices[:n])
        else:
            maxPrice = self.cutRod(rodLength, lengths[:n], prices[:n])
        return price
