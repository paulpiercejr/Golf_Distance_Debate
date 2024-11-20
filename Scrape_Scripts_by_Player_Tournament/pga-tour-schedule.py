import requests
import bs4 as bs
import pandas as pd

#change these per page
#title = 'PGA TOUR - '
table_name = 'schedule-history-table'
docTitle = 'pga-tour-schedule'
url = 'https://www.pgatour.com/tournaments/schedule.history.'

#year info
year_id_start = 1980
end_id = 2023
year_id = 0

#hold info about each stat
stat_data = []

while(year_id_start < end_id):
    year_id = year_id_start
    print(year_id)
    sauce = requests.get(url + str(year_id) + '.html')
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
    statTable = body.find('table', id=table_name)
    if statTable:
        count_tr = 0
        for tr in statTable.find_all('tr'):
            print(tr.text)
            if count_tr > 0:
                count_td = 0
                stat_record = []
                for td in tr.find_all('td'):
                    #if count_td == 0:
                     #   stat_record.append(year_id)
                    stat_record.append(td.text)
                    count_td += 1
                dates = stat_record[0]
                #print(rank)
                tournament_name = stat_record[2]
                #print(player_name)
                champion = stat_record[3]
                #print(rounds)
                points = stat_record[4]
                #print(sg_app_green_avg)
                #d5 = stat_record[5]
                #print(total_sg_app_green)
                d6 = stat_record[6]
                ##print(measured_rounds)
                #d7 = stat_record[7]
                #d8 = stat_record[8]
                stat_data.append([year_id,dates,tournament_name,champion,points) #,d5,d6,d7,d8])#,d8])
                #print('STAT DATA for ' + str(year_id) + ': ' + stat_data[count_tr])
            count_tr += 1
            
    year_id_start += 1
print(stat_data)

df_sd = pd.DataFrame(stat_data, columns = ['year','dates','tournament_name','champion','points'])

print(df_sd)
df_sd.to_csv(docTitle + '.csv')
print('DONE')

