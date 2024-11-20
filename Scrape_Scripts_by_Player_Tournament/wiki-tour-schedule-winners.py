import requests
import bs4 as bs
import pandas as pd

#change these per page
#title = 'PGA TOUR - '
table_name = 'wikitable'
docTitle = 'wiki-pga-tour-schedule3'
url = 'https://en.wikipedia.org/wiki/'

#year info
year_id_start = 2016
end_id = 2023
year_id = 0
#1987,2013
#2010-2012,2014-2022
#hold info about each stat
stat_data = []


while(year_id_start < end_id):
    if year_id < 1987:
        year_id = year_id_start
        print(year_id)
        sauce = requests.get(url + str(year_id) + '_PGA_Tour')
        type(sauce)
        sauce.text
        #create beautifulSoup object
        soup = bs.BeautifulSoup(sauce.text, 'lxml')
        #print(soup)
        
        # if title is not the title of the page then don't traverse the page
        #if title in soup.title.text:
        #	print(soup.title.text)
            # save stat info to list for savingto specific csv
        body = soup.body
        statTable = body.find('table', {"class": table_name})
        if statTable:
            count_tr = 0
            for tr in statTable.find_all('tr'):
                #print(tr.text)
                if count_tr > 0:
                    count_td = 0
                    stat_record = []
                    for td in tr.find_all('td'):
                        #if count_td == 0:
                         #   stat_record.append(year_id)
                        stat_record.append(td.text)
                        count_td += 1
                    dates = stat_record[0] + ", " + str(year_id)
                    print(dates)
                    tournament_name = stat_record[1]
                    print(tournament_name)
                    location = stat_record[2]
                    print(location)
                    purse = stat_record[3]
                    print(purse)
                    winner = stat_record[4]
                    print(winner)
                    owgr = 'NULL'
                    print(owgr)
                    other_tour = 'NULL'
                    print(other_tour)
                    notes = stat_record[5]
                    print(notes)
                    stat_data.append([year_id,dates,tournament_name,location,purse,winner,owgr,other_tour,notes])
                    #print('STAT DATA for ' + str(year_id) + ': ' + stat_data[count_tr])
                count_tr += 1
                
        year_id_start += 1
    if year_id >= 1987 and year_id <= 2009:
        year_id = year_id_start
        print(year_id)
        sauce = requests.get(url + str(year_id) + '_PGA_Tour')
        type(sauce)
        sauce.text
        #create beautifulSoup object
        soup = bs.BeautifulSoup(sauce.text, 'lxml')
        #print(soup)
        
        # if title is not the title of the page then don't traverse the page
        #if title in soup.title.text:
        #	print(soup.title.text)
            # save stat info to list for savingto specific csv
        body = soup.body
        statTable = body.find('table', {"class": table_name})
        if statTable:
            count_tr = 0
            for tr in statTable.find_all('tr'):
                #print(tr.text)
                if count_tr > 0:
                    count_td = 0
                    stat_record = []
                    for td in tr.find_all('td'):
                        #if count_td == 0:
                         #   stat_record.append(year_id)
                        stat_record.append(td.text)
                        count_td += 1
                    dates = stat_record[0] + ", " + str(year_id)
                    print(dates)
                    tournament_name = stat_record[1]
                    print(tournament_name)
                    location = stat_record[2]
                    print(location)
                    purse = stat_record[3]
                    print(purse)
                    winner = stat_record[4]
                    print(winner)
                    owgr = stat_record[5]
                    print(owgr)
                    other_tour = 'NULL'
                    print(other_tour)
                    notes = stat_record[6]
                    print(notes)
                    stat_data.append([year_id,dates,tournament_name,location,purse,winner,owgr,other_tour,notes])
                    #print('STAT DATA for ' + str(year_id) + ': ' + stat_data[count_tr])
                count_tr += 1
                
        year_id_start += 1
        
    if year_id in [2010,2011,2012]:
        year_id = year_id_start
        print(year_id)
        sauce = requests.get(url + str(year_id) + '_PGA_Tour')
        type(sauce)
        sauce.text
        #create beautifulSoup object
        soup = bs.BeautifulSoup(sauce.text, 'lxml')
        #print(soup)
        
        # if title is not the title of the page then don't traverse the page
        #if title in soup.title.text:
        #	print(soup.title.text)
            # save stat info to list for savingto specific csv
        body = soup.body
        statTable = body.find('table', {"class": table_name})
        if statTable:
            count_tr = 0
            for tr in statTable.find_all('tr'):
                #print(tr.text)
                if count_tr > 0:
                    count_td = 0
                    stat_record = []
                    for td in tr.find_all('td'):
                        #if count_td == 0:
                         #   stat_record.append(year_id)
                        stat_record.append(td.text)
                        count_td += 1
                    dates = stat_record[0] + ", " + str(year_id)
                    print(str(0) + " dates " + dates)
                    tournament_name = stat_record[1]
                    print(str(1) + " tournament " + tournament_name)
                    location = stat_record[2]
                    print(str(2) + " location " + location)
                    purse = stat_record[3]
                    print(str(3) + " purse " + purse)
                    winner = stat_record[4]
                    print(str(4) + " winner " + winner)
                    owgr = stat_record[5]
                    print(str(5) + " owgr " + owgr)
                    other_tour = stat_record[6]
                    print(str(6) + " other_tour " + other_tour)
                    notes = stat_record[7]
                    print(str(7) + " notes " + notes)
                    stat_data.append([year_id,dates,tournament_name,location,purse,winner,owgr,other_tour,notes])
                    #print('STAT DATA for ' + str(year_id) + ': ' + stat_data[count_tr])
                count_tr += 1
                
        year_id_start += 1
        
    if year_id == 2013:
        year_id = year_id_start
        print(year_id)
        sauce = requests.get(url + str(year_id) + '_PGA_Tour')
        type(sauce)
        sauce.text
        #create beautifulSoup object
        soup = bs.BeautifulSoup(sauce.text, 'lxml')
        #print(soup)
        
        # if title is not the title of the page then don't traverse the page
        #if title in soup.title.text:
        #	print(soup.title.text)
            # save stat info to list for savingto specific csv
        body = soup.body
        statTable = body.find('table', {"class": table_name})
        if statTable:
            count_tr = 0
            for tr in statTable.find_all('tr'):
                #print(tr.text)
                if count_tr > 0:
                    count_td = 0
                    stat_record = []
                    for td in tr.find_all('td'):
                        #if count_td == 0:
                         #   stat_record.append(year_id)
                        stat_record.append(td.text)
                        count_td += 1
                    dates = stat_record[0] + ", " + str(year_id)
                    print(dates)
                    tournament_name = stat_record[1]
                    print(tournament_name)
                    location = stat_record[2]
                    print(location)
                    purse = stat_record[3]
                    print(purse)
                    winner = stat_record[4]
                    print(winner)
                    owgr = stat_record[5]
                    print(owgr)
                    other_tour = 'NULL'
                    print(other_tour)
                    notes = stat_record[6]
                    print(notes)
                    stat_data.append([year_id,dates,tournament_name,location,purse,winner,owgr,other_tour,notes])
                    #print('STAT DATA for ' + str(year_id) + ': ' + stat_data[count_tr])
                count_tr += 1
                
        year_id_start += 1
    
    if year_id >= 2014 and year_id <= 2022:
        year_id = year_id_start
        print(year_id)
        sauce = requests.get(url + str(year_id) + '_PGA_Tour')
        type(sauce)
        sauce.text
        #create beautifulSoup object
        soup = bs.BeautifulSoup(sauce.text, 'lxml')
        #print(soup)
        
        # if title is not the title of the page then don't traverse the page
        #if title in soup.title.text:
        #	print(soup.title.text)
            # save stat info to list for savingto specific csv
        body = soup.body
        statTable = body.find('table', {"class": table_name})
        if statTable:
            count_tr = 0
            for tr in statTable.find_all('tr'):
                #print(tr.text)
                if count_tr > 0:
                    count_td = 0
                    stat_record = []
                    for td in tr.find_all('td'):
                        #if count_td == 0:
                         #   stat_record.append(year_id)
                        stat_record.append(td.text)
                        count_td += 1
                    dates = stat_record[0] + ", " + str(year_id)
                    print(str(0) + " dates " + dates)
                    tournament_name = stat_record[1]
                    print(str(1) + " tournament " + tournament_name)
                    location = stat_record[2]
                    print(str(2) + " location " + location)
                    purse = stat_record[3]
                    print(str(3) + " purse " + purse)
                    winner = stat_record[4]
                    print(str(4) + " winner " + winner)
                    owgr = stat_record[5]
                    print(str(5) + " owgr " + owgr)
                    other_tour = stat_record[6]
                    print(str(6) + " other_tour " + other_tour)
                    notes = stat_record[7]
                    print(str(7) + " notes " + notes)
                    stat_data.append([year_id,dates,tournament_name,location,purse,winner,owgr,other_tour,notes])
                    #print('STAT DATA for ' + str(year_id) + ': ' + stat_data[count_tr])
                count_tr += 1
                
        year_id_start += 1
        
    
print(stat_data)

df_sd = pd.DataFrame(stat_data, columns = ['year','date','tournament','location','purse','winner','owgr','other_tour','notes'])

print(df_sd)
df_sd.to_csv(docTitle + '.csv')
print('DONE')
