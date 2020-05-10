import csv
from . import Game
from nba_api.stats.endpoints import leaguegamefinder

def traverseSchedule(season, startDate, endDate, fileName):
	schedule = getSchedule(startDate, endDate)
	count = 0
	for i in schedule:
		count = count + 1
		a_file = open(fileName, "a")
		writer = csv.writer(a_file)
		writer.writerow(Game(i, season).getGameRow())
		a_file.close()
		print(count)

def getSchedule(dateFrom, dateTo):
	lgf = leaguegamefinder.LeagueGameFinder(date_to_nullable=dateTo, date_from_nullable=dateFrom)
	gameDict = lgf.get_dict()["resultSets"][0]["rowSet"]
	gameList = []
	for i in gameDict:
		if isGameRegularSeason(i[4]):
			gameList.insert(0, i[4])
	gameList = sorted(list(set(gameList)))
	return gameList

def isGameRegularSeason(gid):
	return int(int(gid)/10000000)==2

#traverseSchedule("2014-15", "11/1/2014", "5/1/2015", "ResultsFIXED/2014-15Stats.csv")
traverseSchedule("2013-14", "11/1/2013", "5/1/2014", "Seasons/2013-14Stats.csv")
traverseSchedule("2012-13", "11/1/2012", "5/1/2013", "Seasons/2012-13Stats.csv")
# traverseSchedule("2011-12", "11/1/2011", "5/1/2012", "ResultsFIXED/2011-12Stats.csv")
traverseSchedule("2010-11", "11/1/2010", "5/1/2011", "Seasons/2010-11Stats.csv")



