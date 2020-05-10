import csv
from os import getcwd

dictTranslate = {
	"OklahomaCity":"Thunder",
	"Charlotte":"Hornets",
	"LAClippers":"Clippers",
	"Philadelphia":"76ers",
	"Denver":"Nuggets",
	"Cleveland":"Cavaliers",
	"Sacramento":"Kings",
	"Milwaukee":"Bucks",
	"NewOrleans":"Pelicans",
	"Portland":"Trail Blazers",
	"Orlando":"Magic",
	"Minnesota":"Timberwolves",
	"Detroit":"Pistons",
	"Miami":"Heat",
	"Chicago":"Bulls",
	"Toronto":"Raptors",
	"Utah":"Jazz",
	"NewYork":"Knicks",
	"Houston":"Rockets",
	"LALakers":"Lakers",
	"Washington":"Wizards",
	"Memphis":"Grizzlies",
	"Indiana":"Pacers",
	"Dallas":"Mavericks",
	"Phoenix":"Suns",
	"Atlanta":"Hawks",
	"SanAntonio":"Spurs",
	"GoldenState":"Warriors",
	"Brooklyn":"Nets",
	"Boston":"Celtics",
	"NewJersey":"Nets",
	"Oklahoma City":"Thunder",
	"LA Clippers":"Clippers"
}

def formatDate(date):
	d = int(date)%100
	m = int(int(date)/100)
	return str(m)+"/"+str(d)

def FormattOdds(season):
	with open(getcwd()+"/PastLines/Odds"+season+".csv", 'r') as read_obj:
		csv_reader = csv.reader(read_obj)
		pastRow = 0
		doRecord = False
		for row in csv_reader:
			if doRecord and int(int(row[0])/100) != 10:
				a_file = open("PastLines/OddsRefined"+season+".csv", "a")
				writer = csv.writer(a_file)
				row = [formatDate(row[0]), dictTranslate[pastRow[3]], dictTranslate[row[3]], pastRow[11], row[11]]
				writer.writerow(row)
				a_file.close()
			doRecord = not doRecord
			pastRow = row