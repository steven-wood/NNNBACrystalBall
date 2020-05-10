from nba_api.stats.static import teams
from nba_api.stats.endpoints import teamdashboardbygeneralsplits

class TeamUtil:
	def __init__(self, team_id, date, statPrefixString, season):
		self.team_info = teamdashboardbygeneralsplits.TeamDashboardByGeneralSplits(team_id=team_id, season=season, season_type_all_star="Regular Season", per_mode_detailed= 'PerMinute', date_to_nullable=date).get_dict()
		self.team_id = team_id
		self.statPrefixString = statPrefixString
		self.statHeaderArray = self.team_info["resultSets"][0]["headers"]
		self.statNumberArray = self.team_info["resultSets"][0]["rowSet"][0]

		self.indexesToProduce = [27, 10, 13, 16, 17, 18, 20, 21, 22, 23, 28]

	def getStats(self):
		resultDict = dict()
		for i in self.indexesToProduce:
			resultDict[self.statPrefixString+self.statHeaderArray[i]] = self.statNumberArray[i]
		return resultDict

	def getTeamname(self):
		return teams.find_team_name_by_id(self.team_id)["nickname"]