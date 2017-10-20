import random
class ThrowCoins:

    def __init__(self,threshold):
        self.threshold = threshold
        self.maxPositiveCount = 0
        self._countAmount = 0
        self._record = []
        self.playCount = 0 
        self.statistics = []

    def getRecord(self):
        return self._record

    def play(self,time):
        self.unitTime = time
        self._scaleAdjustmentVector()
        self._playGame()
        self._calcPlotInfo()

    def getPositiveAmount(self):
        return self._countAmount

    def _playGame(self):
        self.currentPositiveCount = self._calcPositiveCount(self.unitTime)
        self._statisticsAdd(self.currentPositiveCount)

    def _calcPlotInfo(self):
        self._calcMaxPositive(self.currentPositiveCount)
        self._countAmount = self._countAmount + self.currentPositiveCount
        self._playCounterAdd()

    def _playCounterAdd(self):
        self.playCount = self.playCount + 1

    def _calcPositiveCount(self,time):
        count = 0
        for i in range(0,time):
            if self._isPositive() :
                count = count + 1
                self._record.append(1)
            else :
                self._record.append(0)

        return count

    def _scaleAdjustmentVector(self):
        if len(self.statistics) < self.unitTime :
            for i in range(-1,self.unitTime):
                self.statistics.append(0)

    def _statisticsAdd(self,index):
        self.statistics[index] = self.statistics[index] + 1

    def _calcMaxPositive(self,currentCount) :
        if self.maxPositiveCount < self.statistics[currentCount] :
            self.maxPositiveCount = self.statistics[currentCount]

    def _isPositive(self):
        val = random.random()
        return self.threshold > val
 
