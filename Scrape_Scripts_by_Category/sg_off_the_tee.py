import requests
import bs4 as bs
import pandas as pd

#change these per page
#title = 'SG: Approach the Green | PGA Tour Stats'
table_name = 'statsTable'
docTitle = 'sg_off_tee'
url = 'https://www.pgatour.com/stats/stat.02567.y'

#year info
year_id_start = 2004
end_id = 2022
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
                rank = stat_record[0]
                #print(rank)
                player_name = stat_record[2]
                #print(player_name)
                rounds = stat_record[3]
                #print(rounds)
                sg_off_tee_avg = stat_record[4]
                #print(sg_app_green_avg)
                total_sg_off_tee = stat_record[5]
                #print(total_sg_app_green)
                measured_rounds = stat_record[6]
                #print(measured_rounds)
                #relative_to_par = stat_record[7]
                stat_data.append([year_id,rank,player_name,rounds,sg_off_tee_avg,total_sg_off_tee,measured_rounds])
                #print('STAT DATA for ' + str(year_id) + ': ' + stat_data[count_tr])
            count_tr += 1
            
    year_id_start += 1
print(stat_data)

df_sd = pd.DataFrame(stat_data, columns = ['year','rank','player_name','rounds','sg_off_tee_avg','total_sg_off_tee','measured_rounds'])

print(df_sd)
df_sd.to_csv(docTitle + '.csv')
print('DONE')

