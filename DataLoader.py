import pandas as pd
import os

class DataLoader:

	def getStatsCountback(self, firstYear, dataSeasons):
		self.getStats(firstYear - dataSeasons, firstYear+1)

	def getStats(self, startYear, endYear):
		self.startYear = int(startYear)
		self.endYear = int(endYear)
		self.gameCounter = 0
		self.statsFrame = pd.DataFrame(columns=['aPTS', 'aFGP', 'a3PTP', 'aFTP', 'aOREB', 'aDREB', 'aAST', 'aTOV', 'aSTL', 'aBLK', 'aPM', 'hPTS', 'hFGP', 'h3PTP', 'hFTP', 'hOREB', 'hDREB', 'hAST', 'hTOV', 'hSTL', 'hBLK', 'hPM'])
		self.didHomeWinFrame = pd.DataFrame(columns=['didHomeWin'])
		self.oddsFrame = pd.DataFrame(columns=['awayOdds', 'homeOdds'])
		self.dateFrame = pd.DataFrame(columns=['date'])
		for x in range(startYear, endYear):
			self.getStatsForYear(x)
	
	def getStatsForYear(self, year):
		fileName = os.getcwd()+"/NBAScraper/Seasons/"+str(year)+"-"+str((year+1)%100)+"Stats.csv"
		print("Loading Data: "+str(year))
		year = int(year)
		addOne = 0
		if year <= 2014:
			addOne = 1
		data = [line.split(',') for line in open(fileName)]
		for x in range(len(data)):
			prob = int(data[x][29].rstrip("\n"))
			if prob < 0:
				prob = (-(prob))/((-(prob)) + 100)
			else:
				prob = 100 / (prob + 100)
			num = prob + int(data[x][5])
			self.didHomeWinFrame = self.didHomeWinFrame.append({"didHomeWin":data[x][5]}, ignore_index=True)
			self.statsFrame = self.statsFrame.append(pd.Series(data[x][6:28], index=self.statsFrame.columns), ignore_index=True)
			self.oddsFrame = self.oddsFrame.append({"awayOdds":data[x][28], "homeOdds":data[x][29].rstrip("\n")}, ignore_index=True)
			self.dateFrame = self.dateFrame.append({"date":data[x][0]}, ignore_index=True)