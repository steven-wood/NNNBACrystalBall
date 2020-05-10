from nba_api.stats.endpoints import boxscoresummaryv2
from datetime import datetime
from . import TeamUtil
from os import getcwd
from csv import reader

class Game:
	def __init__(self, game_id, season):
		self.game_id = game_id
		self.season = season
		self.game_info = boxscoresummaryv2.BoxScoreSummaryV2(game_id=game_id).get_dict()
		self.teamDict = self.game_info["resultSets"][0]["rowSet"][0]
		self.d = datetime.strptime(self.teamDict[0].split("T")[0], "%Y-%m-%d")
		self.dateString = self.d.strftime("%m/%d/%Y")
		self.homeTeam = TeamUtil(self.getHomeTeamID(), self.d, "HOME", season)
		self.awayTeam = TeamUtil(self.getAwayTeamID(), self.d, "AWAY", season)

	def getGameDict(self):
		dest = {"DATE": self.dateString, "AWAYNN": self.awayTeam.getTeamname(), "HOMENN": self.homeTeam.getTeamname(), "AWAYID": self.getAwayTeamID(), "HOMEID": self.getHomeTeamID(), "ISHOME": self.didHomeWin()}
		dest.update(self.homeTeam.getStats())
		dest.update(self.awayTeam.getStats())
		dest.update(self.getOdds())
		return dest

	def getGameRow(self):
		dest = self.getGameDict()
		row = []
		for key, value in dest.items():
			row.append(value)
		return row

	def getHomeTeamID(self):
		return self.teamDict[6]

	def getAwayTeamID(self):
		return self.teamDict[7]
		
	def didHomeWin(self):
		var2 = 0
		if self.game_info["resultSets"][5]["rowSet"][1][22] > self.game_info["resultSets"][5]["rowSet"][0][22]:
			var2 = 1
		winningTeamID = self.game_info["resultSets"][5]["rowSet"][var2][3]
		isHome = 1
		if self.teamDict[7] == winningTeamID:
			isHome = 0
		return isHome

	def getAwayScore(self):
		print("AWAY "+str(self.game_info["resultSets"][5]["rowSet"][1][22]))
		print(self.awayTeam.getTeamname())
		return self.game_info["resultSets"][5]["rowSet"][1][22]

	def getHomeScore(self):
		print("HOME "+str(self.game_info["resultSets"][5]["rowSet"][0][22]))
		print(self.homeTeam.getTeamname())
		return self.game_info["resultSets"][5]["rowSet"][0][22]

	def getOdds(self):
		with open(getcwd()+"/PastLines/OddsRefined"+self.season+".csv", 'r') as read_obj:
			csv_reader = reader(read_obj)
			for row in csv_reader:
				month = row[0].split("/")[0]
				day = row[0].split("/")[1]
				if str(month) == str(self.d.month) and str(day) == str(self.d.day) and row[1] == self.awayTeam.getTeamname() and row[2] == self.homeTeam.getTeamname():
					return {"AWAYML": row[3], "HOMEML": row[4]}
	
