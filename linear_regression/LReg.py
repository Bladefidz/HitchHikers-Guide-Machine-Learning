import math

class LReg(object):
	""" Linear Regression """
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.n = len(x)
		self.meanX = None
		self.meanY = None
		self.productDeviation = None
		self.variationX = None
		self.variationY = None
		self.standardDeviation = None
		self.correlation = None
		self.slope = None
		self.intercept = None

	def calculate(self):
		self.__setMeanX()
		self.__setMeanY()
		self.__setDeviation()
		self.__setCorrelation()
		self.__setSlope()
		self.__setIntercept()

	def __setMeanX(self):
		self.meanX = 0
		for i in self.x:
			self.meanX += i
		self.meanX /= self.n

	def __setMeanY(self):
		self.meanY = 0
		for i in self.y:
			self.meanY += i
		self.meanY /= self.n

	def __setDeviation(self):
		self.productDeviation = 0
		self.variationX = 0
		self.variationY = 0
		for i in range(0, self.n):
			self.productDeviation += ((self.x[i] - self.meanX) * (self.y[i] - self.meanY))
			self.variationX += math.pow((self.x[i] - self.meanX), 2)
			self.variationY += math.pow((self.y[i] - self.meanY), 2)
		self.standardDeviation = math.sqrt(self.variationX * self.variationY)

	def __setCorrelation(self):
		self.correlation = self.productDeviation / self.standardDeviation

	def __setSlope(self):
		self.slope = self.correlation * (self.variationY / self.variationX)

	def __setIntercept(self):
		self.intercept = self.meanY - (self.slope * self.meanX)