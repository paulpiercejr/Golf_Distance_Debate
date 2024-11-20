#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 13:15:25 2023

@author: paulpiercejr
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime as dt
import html5lib
import json
import csv
from datetime import datetime

from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

url = 'https://www.pgatour.com/players'
# url_start = 'https://www.pgatour.com'
link_list = []
link_list_names = []
link_list_countries = []
#player_list = []
career_stat_dict = {}
player_count = 1


# extract urls of all player pages to gather data from players page
def extract_link_list(url):
    driver.get(url)
    # select players button
    get_to_players = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div/main/div[5]/div[2]/div/div/button')
    get_to_players.click()
    # select all players button from pop-out menu
    all_players_btn = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div/main/div[5]/div[2]/div/div/div[2]/div/button[2]')
    all_players_btn.click()
    # pull all player links from list
    player_listing = driver.find_elements(By.XPATH, '//*[@id="__next"]/div[2]/div/div/main/div/div[2]/div/div[2]/span/p/a')
    for player in player_listing:
        # add each link to the link_list
        link_list.append(player.get_attribute('href'))
        link_list_names.append(player.text)
    player_country = driver.find_elements(By.XPATH, '//*[@id="__next"]/div[2]/div/div/main/div/div[2]/div/div[2]/span[2]/p')
    for country in player_country:
        link_list_countries.append(country.text)
    
    return link_list, link_list_names, link_list_countries

# get the html soup for each player link
def extract_player_soup(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}
    r = requests.get(url,headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

# extract player data based on the link list (should be run in a loop so that index is valid)
# def extract_player_data(link_list_index):
#     headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}
#     r = requests.get(link_list_index,headers)
#     return r

# 
# def extract_player_info(link):
#     driver.get(link)
#     # select Bio link
#     select_bio = driver.get_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div/main/div[4]/div/div/button[4]')
#     select_bio.click()
#     # read all fields of bio data
#     select_field_names = driver.get_elements(By.XPATH, '//*[@id="__next"]/div[2]/div/div/main/div[4]/div[2]/div[4]/div/div/div[2]/div[2]/div/div/div[2]/div/p[1]')
#     select_field_values = driver.get_elements(By.XPATH, '//*[@id="__next"]/div[2]/div/div/main/div[4]/div[2]/div[4]/div/div/div[2]/div[2]/div/div/div[2]/div/p[1]')
#     # if filed name = website disregaurd
    
# get JSON text from player website, gather all Bio information
def get_player_info(soup):
    #bio_stats = soup.find('div', class_ = 'css-1u0ht80')
    script = soup.find('script', id = '__NEXT_DATA__')
    json_text = script.get_text()
    json_data = json.loads(json_text)

    # keylist = list(json_data.keys())

    player_info = json_data['props']

    #player_key_list = list(player_info.keys())

    p_info = player_info['pageProps']
    #page_key_list = list(p_info.keys())

    # #try:
    #     #p_info2 = p_info['player']
    #     #print('p_info2: ', p_info2)
    #     # p_info2_key = list(p_info2.keys())
    #     #print(p_info2_key)
    # except:
    #     pass

    
    try:
        player_id = p_info['playerId']
    except:
        player_id = 'NULL'
    try:
        fname = p_info['player']['firstName']
    except:
        fname = 'NULL'
    try:
        lname = p_info['player']['lastName']
    except:
        lname = 'NULL'
    try:
        birth_country = p_info['player']['playerBio']['birthplace']['country']
    except:
        birth_country = 'NULL'
    try:
        birth_country_code = p_info['player']['playerBio']['birthplace']['countryCode']
    except:
        birth_country_code = 'NULL'
    try:
        birth_city = p_info['player']['playerBio']['birthplace']['city']
    except:
        birth_city = 'NULL'
    try:
        birth_state = p_info['player']['playerBio']['birthplace']['state']
    except:
        birth_state = 'NULL'
    try:
        birthdate = p_info['player']['playerBio']['bornAccessibilityText']
    except:
        birthdate = 'NULL'
    try:
        career_earnings = p_info['player']['playerBio']['careerEarnings']
    except:
        career_earnings = 'NULL'
    try:
        height = p_info['player']['playerBio']['heightImperial']
    except:
        height = 'NULL'
    try:
        weight = p_info['player']['playerBio']['weightImperial']
    except:
        weight = 'NULL'
    try:
        turned_pro = p_info['player']['playerBio']['turnedPro']
    except:
        turned_pro = 'NULL'
    try:
        college = p_info['player']['playerBio']['school']
    except:
        college = 'NULL'
    try:
        plays_from_city = p_info['player']['playerBio']['playsFrom']['city']
    except:
        plays_from_city = 'NULL'
    try:
        plays_from_state = p_info['player']['playerBio']['playsFrom']['state']
    except:
        plays_from_state = 'NULL'
    try:
        plays_from_country = p_info['player']['playerBio']['playsFrom']['country']
    except:
        plays_from_country = 'NULL'
    try:
        plays_from_country_code = p_info['player']['playerBio']['playsFrom']['countryCode']
    except:
        plays_from_country_code = 'NULL'
        
    player_data = {'player_id': player_id,
                   'first_name': str_to_str_or_null(fname),
                   'last_name': str_to_str_or_null(lname),
                   'birth_country': str_to_str_or_null(birth_country),
                   'birth_country_code': str_to_str_or_null(birth_country_code),
                   'birth_city': str_to_str_or_null(birth_city),
                   'birth_state': str_to_str_or_null(birth_state),
                   'birthdate': str_to_date_or_null(birthdate, '%B %d, %Y'),
                   'career_earnings': str_money_to_int_or_zero(career_earnings),
                   'height': height, #_to_inches(height),
                   'weight': str_to_int_or_null(weight),
                   'turned_pro': str_to_int_or_null(turned_pro),
                   'college': str_to_str_or_null(college),
                   'plays_from_city': str_to_str_or_null(plays_from_city),
                   'plays_from_state': str_to_str_or_null(plays_from_state),
                   'plays_from_country': str_to_str_or_null(plays_from_country),
                   'plays_from_country_code': str_to_str_or_null(plays_from_country_code)
                  }
    success = True
    if player_data['player_id'] == 'NULL':
       success = False
    
    return player_data, success, player_id


def str_to_date_or_null(date, dformat):
    try:
        new_date = datetime.strptime(date, dformat)
    except:
        new_date = 'NULL'
    return new_date



def get_player_stats(soup):
    # bio_stats = soup.find('div', class_ = 'css-1u0ht80')
    script = soup.find('script', id = '__NEXT_DATA__')
    json_text = script.get_text()
    json_data = json.loads(json_text)
    # keylist = list(json_data.keys())
    #print(keylist)
    player_info = json_data['props']
    #print("Type: ", type(player_info))
    # player_key_list = list(player_info.keys())
    #print(player_key_list)
    p_info = player_info['pageProps']
    # page_key_list = list(p_info.keys())
    #print(page_key_list)
    player_id = p_info['playerId']
    year = ''
    season = ''
    wins = ''
    seconds = ''
    thirds = ''
    top_10 = ''
    top_25 = ''
    events = ''
    cuts_made = ''
    earnings = ''
    profileOverview = False
    career_results = []
    try:
        profileOverview = p_info['profileOverview']['performance']
        #i = 0
        for season in profileOverview:
            #print(type(season))
            if season['tour'] == 'R':
                #print(player_id)
                tour = season['tour']
                #print(tour)
                year = season_to_year_status(season['season'])
                #print(year)
                seasons = season['displaySeason']
                #print(seasons)
                season_values = season['stats']
                for vals in season_values:
                    if vals['title'] == 'Wins':
                        wins = vals['value']   
                    if vals['title'] == 'Seconds':
                        seconds = vals['value']
                    if vals['title'] == 'Thirds':
                        thirds = vals['value']
                    if vals['title'] == 'Top 10':
                        top_10 = vals['value']
                    if vals['title'] == 'Top 25':
                        top_25 = vals['value']
                    if vals['title'] == 'Events':
                        events = vals['value']
                    if vals['title'] == 'Cuts Made':
                        cuts_made = vals['value']
                    if vals['title'] == 'Earnings':
                        earnings = vals['value']
                    career_data = {'player_id': player_id,
                                   'tour': tour,
                                   'year': year,
                                   'season': seasons,
                                   'events': str_to_int_or_zero(events),
                                   'wins': str_to_int_or_zero(wins),
                                   'seconds': str_to_int_or_zero(seconds),
                                   'thirds': str_to_int_or_zero(thirds),
                                   'top_10': str_to_int_or_zero(top_10),
                                   'top_25': str_to_int_or_zero(top_25),
                                   'cuts_made': str_to_int_or_zero(cuts_made),
                                   'earnings': str_money_to_int_or_zero(earnings)
                                   }
                #print('career data: ', career_data)
                career_results.append(career_data)        
    except:
        pass
    return career_results


# add /stats to player url
# select Tour as PGA Tour - if PGA Tour doesn't exist put one blank entry in the list with player_id
# select each season from list by for loop and pull stats for each year from each category
# TR in stats page
# //*[@id="tabs-:ra:--tabpanel-2"]/div/div/div[2]/div[2]/div[6]/div/div[2]/div/table/tbody/tr






def season_to_year_status(season):
    year = ''
    if season.lower().__contains__('2013-14') or season.lower().__contains__('2013-2014'):
        year = 2014
    elif season.lower().__contains__('2014-15') or season.lower().__contains__('2014-2015'):
        year = 2015
    elif season.lower().__contains__('2015-16') or season.lower().__contains__('2015-2016'):
        year = 2016
    elif season.lower().__contains__('2016-17') or season.lower().__contains__('2016-2017'):
        year = 2017
    elif season.lower().__contains__('2017-18') or season.lower().__contains__('2017-2018'):
        year = 2018
    elif season.lower().__contains__('2018-19') or season.lower().__contains__('2018-2019'):
        year = 2019
    elif season.lower().__contains__('2019-20') or season.lower().__contains__('2019-2020'):
        year = 2020
    elif season.lower().__contains__('2020-21') or season.lower().__contains__('2020-2021'):
        year = 2021
    elif season.lower().__contains__('2021-22') or season.lower().__contains__('2021-2022'):
        year = 2022
    elif season.lower().__contains__('2022-23') or season.lower().__contains__('2022-2023'):
        year = 2023
    else:
        try:
            year = int(season.lower().strip())
        except (TypeError, ValueError) as e:
            try: 
                year_1 = season.split('-',1) 
                year = int(year_1[0])# + my_int
            except:
                year = 9999
    return year




def get_season_stats(url, player_id):
    # add /stats to player url
    stat_url = url + '/stats'
    stats = []
    driver.get(stat_url)
    driver.implicitly_wait(20)
    # select Tour as PGA Tour - if PGA Tour doesn't exist then go to next year
    # select year and loop through them checking to see if PGA Tour is in each year
    
    # set season button
    season = '/html/body/div/div[2]/div/div/main/div[4]/div[2]/div[3]/div/div/div/div/div/button[1]'
    season = '/html/body/div/div[2]/div/div/main/div[5]/div[2]/div[5]/div/div/div/div/div/button[1]'
    
    year_path = '/html/body/div/div[2]/div/div/main/div[4]/div[2]/div[3]/div/div/div/div/div[1]/div[1]/div[1]/button'
    year_path = '/html/body/div/div[2]/div/div/main/div[5]/div[2]/div[5]/div/div/div/div/div/div/div/button'
    years = driver.find_elements(By.XPATH, year_path)
    
    pga_tour_path = '/html/body/div/div[2]/div/div/main/div[4]/div[2]/div[3]/div/div/div/div/div/button[2]'
    pga_tour_path = '/html/body/div/div[2]/div/div/main/div[5]/div[2]/div[5]/div/div/div/div/div/button[2]'
    pga_tour_tours = '/html/body/div/div[2]/div/div/main/div[4]/div[2]/div[3]/div/div/div/div/div/div[2]/div/button'
    pga_tour_tours = '/html/body/div/div[2]/div/div/main/div[5]/div[2]/div[5]/div/div/div/div/div/div[2]/div/button'
    
    performance_path = '/html/body/div/div[2]/div/div/main/div[5]/div[2]/div[5]/div/div/div[2]/div[1]/div[3]/div[1]/div[1]/button[1]'
    performance_path = '/html/body/div/div[3]/div/div/main/div[4]/div[2]/div[6]/div/div/div[3]/div/div[3]/div/div/button[1]'

    
    
    j = 0
    while j < len(years):
        print('year: ', j)
        # click season button
        season_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, season)))
        season_button.click()
        years = driver.find_elements(By.XPATH, year_path)
        this_year = years[j].text
        year_click = driver.execute_script("arguments[0].click();", years[j])
        year_click
        # click PGA Tour button if it exists else pass
        pga_tour_click = driver.find_element(By.XPATH, pga_tour_path)
        pga_tour_click.click()
        pga_tour_select_tour = driver.find_elements(By.XPATH, pga_tour_tours)
        #print('tours: ', len(pga_tour_select_tour))
        # loop through each season
        sg_total = ''
        sg_total_rank = ''
        sg_total_total = ''
        sg_total_m_rounds = ''
        sg_tee_2_gr = ''
        sg_tee_2_gr_rank = ''
        sg_off_tee = ''
        sg_off_tee_rank = ''
        sg_off_tee_total = ''
        sg_app_gr = ''
        sg_app_gr_rank = ''
        sg_app_gr_total = ''
        sg_around_gr = ''
        sg_around_gr_rank = ''
        sg_around_gr_total = ''
        sg_putting = ''
        sg_putting_rank = ''
        sg_putting_total = ''
        total_driving = ''
        total_driving_rank = ''
        longest_drive = ''
        longest_drive_rank = ''
        longest_drive_tourney = ''
        longest_drive_round = ''
        driving_distance = ''
        driving_distance_rank = ''
        driving_distance_total = ''
        driving_distance_total_drives = ''
        driving_distance_all_drives = ''
        driving_distance_all_drives_rank = ''
        driving_distance_all_drives_total = ''
        driving_distance_all_drives_total_drives = ''
        driving_accuracy = ''
        driving_accuracy_rank = ''
        fairways_hit = ''
        fairways_possible = ''
        left_rough_tendency = ''
        left_rough_tendency_rank = ''
        left_rough_total = ''
        left_rough_possible_fairways = ''
        right_rough_tendency = ''
        right_rough_tendency_rank = ''
        right_rough_total = ''
        right_rough_possible_fairways = ''
        distance_from_edge_frwy = ''
        distance_from_edge_frwy_rank = ''
        distance_from_edge_frwy_total = ''
        distance_from_edge_frwy_strokes = ''
        club_head_speed = ''
        club_head_speed_rank = ''
        club_head_speed_total = ''
        club_head_speed_attempts = ''
        total_driving_efficiency = ''
        total_driving_efficiency_rank = ''
        carry_efficiency_rank = ''
        greens_in_regulation_percent = ''
        greens_in_regulation_percent_rank = ''
        greens_hit = ''
        greens_possible = ''
        proximity_to_hole = ''
        proximity_to_hole_rank = ''
        proximity_to_hole_total_ft = ''
        proximity_to_hole_total_att = ''
        
        approach_more_275_in = ''
        approach_more_275_rank = ''
        approach_more_275_total_ft = ''
        approach_more_275_total_att = ''
        
        approach_250_275_in = ''
        approach_250_275_rank = ''
        approach_250_275_total_ft = ''
        approach_250_275_total_att = ''
        
        approach_225_250_in = ''
        approach_225_250_rank = ''
        approach_225_250_total_ft = ''
        approach_225_250_total_att = ''
        
        approach_200_225_in = ''
        approach_200_225_rank = ''
        approach_200_225_total_ft = ''
        approach_200_225_total_att = ''
        
        approach_more_200_in = ''
        approach_more_200_rank = ''
        approach_more_200_total_ft = ''
        approach_more_200_total_att = ''
        
        approach_175_200_in = ''
        approach_175_200_rank = ''
        approach_175_200_total_ft = ''
        approach_175_200_total_att = ''
        
        approach_150_175_in = ''
        approach_150_175_rank = ''
        approach_150_175_total_ft = ''
        approach_150_175_total_att = ''
        
        approach_125_150_in = ''
        approach_125_150_rank = ''
        approach_125_150_total_ft = ''
        approach_125_150_total_att = ''
        
        approach_50_125_in = ''
        approach_50_125_rank = ''
        approach_50_125_total_ft = ''
        approach_50_125_total_att = ''
        
        approach_100_125_in = ''
        approach_100_125_rank = ''
        approach_100_125_total_ft = ''
        approach_100_125_total_att = ''
        
        approach_75_100_in = ''
        approach_75_100_rank = ''
        approach_75_100_total_ft = ''
        approach_75_100_total_att = ''
        
        approach_50_75_in = ''
        approach_50_75_rank = ''
        approach_50_75_total_ft = ''
        approach_50_75_total_att = ''
        
        approach_less_100_in = ''
        approach_less_100_rank = ''
        approach_less_100_total_ft = ''
        approach_less_100_total_att = ''
        
        approach_more_100_in = ''
        approach_more_100_rank = ''
        approach_more_100_total_ft = ''
        approach_more_100_total_att = ''
        
        
        
        
        fairway_proximity = ''
        fairway_proximity_rank = ''
        fairway_proximity_att = ''
        
        rough_proximity = ''
        rough_proximity_rank = ''
        rough_proximity_total_in = ''
        rough_proximity_total_att = ''
        
        left_rough_proximity = ''
        left_rough_proximity_rank = ''
        left_rough_proximity_att = ''
        
        right_rough_proximity = ''
        right_rough_proximity_rank = ''
        right_rough_proximity_att = ''
        
        
        
        
        
        approach_more_275_rough_in = ''
        approach_more_275_rough_rank = ''
        approach_more_275_rough_total_ft = ''
        approach_more_275_rough_total_att = ''
        
        approach_250_275_rough_in = ''
        approach_250_275_rough_rank = ''
        approach_250_275_rough_total_ft = ''
        approach_250_275_rough_total_att = ''
        
        approach_225_250_rough_in = ''
        approach_225_250_rough_rank = ''
        approach_225_250_rough_total_ft = ''
        approach_225_250_rough_total_att = ''
        
        approach_200_225_rough_in = ''
        approach_200_225_rough_rank = ''
        approach_200_225_rough_total_ft = ''
        approach_200_225_rough_total_att = ''
        
        approach_more_100_rough_in = ''
        approach_more_100_rough_rank = ''
        approach_more_100_rough_total_ft = ''
        approach_more_100_rough_total_att = ''
        
        approach_less_100_rough_in = ''
        approach_less_100_rough_rank = ''
        approach_less_100_rough_total_ft = ''
        approach_less_100_rough_total_att = ''
        
        approach_more_200_rough_in = ''
        approach_more_200_rough_rank = ''
        approach_more_200_rough_total_ft = ''
        approach_more_200_rough_total_att = ''
        
        approach_175_200_rough_in = ''
        approach_175_200_rough_rank = ''
        approach_175_200_rough_total_ft = ''
        approach_175_200_rough_total_att = ''
        
        approach_150_175_rough_in = ''
        approach_150_175_rough_rank = ''
        approach_150_175_rough_total_ft = ''
        approach_150_175_rough_total_att = ''
        
        approach_125_150_rough_in = ''
        approach_125_150_rough_rank = ''
        approach_125_150_rough_total_ft = ''
        approach_125_150_rough_total_att = ''
        
        approach_50_125_rough_in = ''
        approach_50_125_rough_rank = ''
        approach_50_125_rough_total_ft = ''
        approach_50_125_rough_total_att = ''
        
        approach_100_125_rough_in = ''
        approach_100_125_rough_rank = ''
        approach_100_125_rough_total_ft = ''
        approach_100_125_rough_total_att = ''
        
        approach_75_100_rough_in = ''
        approach_75_100_rough_rank = ''
        approach_75_100_rough_total_ft = ''
        approach_75_100_rough_total_att = ''
        
        approach_50_75_rough_in = ''
        approach_50_75_rough_rank = ''
        approach_50_75_rough_total_ft = ''
        approach_50_75_rough_total_att = ''
        
        going_for_green_percent = ''
        going_for_green_percent_rank = ''
        going_for_green_percent_attempts = ''
        going_for_green_percent_non_attemptes = ''
        
        going_for_green_hit_percent = ''
        going_for_green_hit_rank = ''
        going_for_green_hit = ''
        going_for_green_attempts = ''
        
        going_for_green_birdie_better_pct = ''
        going_for_green_birdie_better_pct_rank = ''
        going_for_green_birdie_better_total =''
        
        total_hole_outs = ''
        total_hole_outs_rank = ''
        
        
        longest_hole_out_yrds = ''
        longest_hole_out_rank = ''
        longest_hole_out_tourney = ''
        longest_hole_out_rd = ''
        
        scrambling_percent = ''
        scrambling_rank = ''
        scrambling_par_or_better = ''
        scrambling_missed_gir = ''
        
        scrambling_from_rough_perecnt = ''
        scrambling_from_rough_rank = ''
        scrambling_from_rough_success = ''
        scrambling_from_rough_att = ''
        
        scrambling_from_fringe_percent = ''
        scrambling_from_fringe_rank = ''
        scrambling_from_fringe_success = ''
        scrambling_from_fringe_att = ''
        
        scrambling_more_30_percent = ''
        scrambling_more_30_rank = ''
        scrambling_more_30_success = ''
        scrambling_more_30_att = ''
        
        scrambling_20_30_percent = ''
        scrambling_20_30_rank = ''
        scrambling_20_30_success = ''
        scrambling_20_30_att = ''
        
        scrambling_10_20_percent = ''
        scrambling_10_20_rank = ''
        scrambling_10_20_success = ''
        scrambling_10_20_att = ''
        
        scrambling_less_10_percent = ''
        scrambling_less_10_rank = ''
        scrambling_less_10_success = ''
        scrambling_less_10_att = ''
        
        sand_save_percent = ''
        sand_save_rank = ''
        sand_save_saves = ''
        sand_save_bunkers = ''
        
        proximity_to_hole_sand = ''
        proximity_to_hole_sand_rank = ''
        proximity_to_hole_sand_total_ft = ''
        proximity_to_hole_sand_shots = ''
        
        total_putting = ''
        total_putting_rank = ''
        
        putting_avg = ''
        putting_avg_rank = ''
        putting_avg_gir_putts = ''
        putting_avg_greens_hit = ''
        
        overall_putting_avg = ''
        overall_putting_avg_rank = ''
        overall_putting_total_putts = ''
        overall_putting_total_holes = ''
        
        
        birdie_or_better_conversion_percent = ''
        birdie_or_better_conversion_rank = ''
        birdie_or_better_conversion_birdies = ''
        birdie_or_better_conversion_greens_hit = ''
        
        putts_per_round = ''
        putts_per_round_rank = ''
        total_putts = ''
        total_rounds = ''
        
        putts_per_round_rd1 = ''
        putts_per_round_rd1_rank = ''
        total_putts_rd1 = ''
        total_rounds_rd1 = ''
        
        putts_per_round_rd2 = ''
        putts_per_round_rd2_rank = ''
        total_putts_rd2 = ''
        total_rounds_rd2 = ''
        
        putts_per_round_rd3 = ''
        putts_per_round_rd3_rank = ''
        total_putts_rd3 = ''
        total_rounds_rd3 = ''
        
        putts_per_round_rd4 = ''
        putts_per_round_rd4_rank = ''
        total_putts_rd4 = ''
        total_rounds_rd4 = ''
        
        one_putt_percentage = ''
        one_putt_rank = ''
        one_putt_total = ''
        one_putt_total_holes = ''
        
        longest_putt = ''
        longest_putt_break = ''
        longest_putt_tourney = ''
        longest_putt_rd = ''
        
        three_putt_avoidance = ''
        three_putt_avoidance_rank = ''
        three_putt_total = ''
        three_putt_total_holes = ''
        
        putting_more_25_percent = ''
        putting_more_25_rank = ''
        putting_more_25_att = ''
        putting_more_25_made = ''
        
        putting_20_25_percent = ''
        putting_20_25_rank = ''
        putting_20_25_att = ''
        putting_20_25_made = ''
        
        putting_15_20_percent = ''
        putting_15_20_rank = ''
        putting_15_20_att = ''
        putting_15_20_made = ''
        
        putting_10_15_percent = ''
        putting_10_15_rank = ''
        putting_10_15_att = ''
        putting_10_15_made = ''
        
        putting_less_10_percent = ''
        putting_less_10_rank = ''
        putting_less_10_att = ''
        putting_less_10_made = ''
        
        putting_from_10_percent = ''
        putting_from_10_rank = ''
        putting_from_10_att = ''
        
        putting_from_9_percent = ''
        putting_from_9_rank = ''
        putting_from_9_att = ''
        
        putting_from_8_percent = ''
        putting_from_8_rank = ''
        putting_from_8_att = ''
        
        putting_from_7_percent = ''
        putting_from_7_rank = ''
        putting_from_7_att = ''
        
        putting_from_6_percent = ''
        putting_from_6_rank = ''
        putting_from_6_att = ''
        
        putting_from_5_percent = ''
        putting_from_5_rank = ''
        putting_from_5_att = ''
        
        putting_from_4_8_percent = ''
        putting_from_4_8_rank = ''
        putting_from_4_8_att = ''
        putting_from_4_8_made = ''
        
        putting_from_4_percent = ''
        putting_from_4_rank = ''
        putting_from_4_att = ''
        
        putting_from_3_percent = ''
        putting_from_3_rank = ''
        putting_from_3_att = ''
        
        avg_distance_putts_made = ''
        avg_distance_putts_made_rank = ''
        avg_distance_putts_made_in = ''
        avg_distance_putts_made_rounds = ''
        
        approach_putt_performance = ''
        approach_putt_rank = ''
        approach_putt_att = ''
        
        scoring_avg_adj = ''
        scoring_avg_adj_rank = ''
        scoring_avg_adj_total_strokes = ''
        scoring_avg_adj_total_adjustment = ''
        
        scoring_avg_actual = ''
        scoring_avg_actual_rank = ''
        scoring_avg_actual_total_strokes = ''
        scoring_avg_actual_total_rounds = ''
        
        lowest_round = ''
        lowest_round_rank = ''
        lowest_round_tourney = ''
        lowest_round_round = ''
        
        birdie_avg = ''
        birdie_avg_rank = ''
        birdie_avg_num_birdies = ''
        birdie_avg_total_rounds = ''
        
        total_birdies = ''
        total_birdies_rank = ''
        
        eagles_holes_per = ''
        eagles_holes_per_rank = ''
        
        total_eagles = ''
        total_eagles_rank = ''
        
        par_breaker_percent = ''
        par_breaker_rank = ''
        
        bounce_back_percent = ''
        bounce_back_rank = ''
        
        par3_birdie_or_better = ''
        par3_birdie_or_better_rank = ''
        par3_birdie_or_better_total = ''
        par3_holes = ''
        
        par4_birdie_or_better = ''
        par4_birdie_or_better_rank = ''
        par4_birdie_or_better_total = ''
        par4_holes = ''
        
        par5_birdie_or_better = ''
        par5_birdie_or_better_rank = ''
        par5_birdie_or_better_total = ''
        par5_holes = ''
        
        birdie_or_better_percent = ''
        birdie_or_better_rank = ''
        
        bogey_avoidance_percent = ''
        bogey_avoidance_rank = ''
        bogey_total = ''
        
        final_round_scoring_avg = ''
        final_round_scoring_avg_rank = ''
        final_round_scoring_total_strokes = ''
        final_round_scoring_total_rds = ''
        
        final_round_performance = ''
        final_round_performance_rank = ''
        
        rd1_scoring_avg = ''
        rd1_scoring_avg_rank = ''
        rd1_scoring_total_strokes = ''
        rd1_scoring_total_rds = ''
        
        rd2_scoring_avg = ''
        rd2_scoring_avg_rank = ''
        rd2_scoring_total_strokes = ''
        rd2_scoring_total_rds = ''
        
        rd3_scoring_avg = ''
        rd3_scoring_avg_rank = ''
        rd3_scoring_total_strokes = ''
        rd3_scoring_total_rds = ''
        
        rd4_scoring_avg = ''
        rd4_scoring_avg_rank = ''
        rd4_scoring_total_strokes = ''
        rd4_scoring_total_rds = ''
        
        par3_scoring_avg = ''
        par3_scoring_avg_rank = ''
        par3_scoring_avg_strokes = ''
        par3_scoring_avg_holes = ''
        
        par4_scoring_avg = ''
        par4_scoring_avg_rank = ''
        par4_scoring_avg_strokes = ''
        par4_scoring_avg_holes = ''
        
        par5_scoring_avg = ''
        par5_scoring_avg_rank = ''
        par5_scoring_avg_strokes = ''
        par5_scoring_avg_holes = ''
        
        front9_scoring_avg = ''
        front9_scoring_avg_rank = ''
        front9_scoring_avg_strokes = ''
        front9_scoring_avg_holes = ''
        
        back9_scoring_avg = ''
        back9_scoring_avg_rank = ''
        back9_scoring_avg_strokes = ''
        back9_scoring_avg_holes = ''
        
        early_scoring_avg = ''
        early_scoring_avg_rank = ''
        early_scoring_total_strokes = ''
        early_scoring_total_rounds = ''
        
        late_scoring_avg = ''
        late_scoring_avg_rank = ''
        late_scoring_total_strokes = ''
        late_scoring_total_rounds = ''
        
        consecutive_cuts = ''
        consecutive_cuts_rank = ''
        
        #skip current_streak without 3 putt
        
        consecutive_fairways_hit = ''
        consecutive_fairways_hit_rank = ''
        
        consecutive_gir = ''
        consecutive_gir_rank = ''
        
        consecutive_sand_saves = ''
        consecutive_sand_saves_rank = ''
        
        best_ytd_1_putt_or_better_streak = ''
        best_ytd_1_putt_or_better_streak_rank = ''
        
        best_ytd_streak_wo_3_putt = ''
        best_ytd_streak_wo_3_putt_rank = ''
        
        ytd_par_or_better_streak = ''
        ytd_par_or_better_streak_rank = ''
        
        consecutive_par_3_birdies = ''
        consecutive_par_3_birdies_rank = ''
        
        consecutive_holes_below_par = ''
        consecutive_holes_below_par_rank = ''
        
        consecutive_birdies_streak = ''
        consecutive_birdies_streak_rank = ''
        
        consecutive_birdies_eagles_streak = ''
        consecutive_birdies_eagles_streak_rank = ''
        
        official_money = ''
        official_money_rank = ''
        
        fedexcup_regular_season_points = ''
        fedexcup_rank = ''
        wins = ''
        top_10s = ''
    
        
        
        
        
        
        
        
        for tour in pga_tour_select_tour:
            if tour.text.lower() == 'pga tour':
                print(this_year)
                print(tour.text)
                tour.click()
                try: 
                    performance = driver.find_element(By.XPATH, performance_path)
                except:
                    performance_path2 = '/html/body/div/div[2]/div/div/main/div[5]/div[2]/div[5]/div/div/div[3]/div[2]/div[3]/div/div[1]/button[1]'
                    performance = driver.find_element(By.XPATH, performance_path2)
                # performance_text = driver.find_elements(By.XPATH, performance_path + '/div/span')
                if performance.text.lower() != 'all':
                    pass
                else:
                    performance.click()
                    
                    # gather stats
                    
                    # SG Total
                    tr_num = 0
                    # sg_total_xpat2 = '/html/body/div/div[2]/div/div/main/div[4]/div[2]/div[3]/div/div/div[2]/div/div[6]/div/div[2]/div/table/tbody/tr['
                    sg_total_xpat2 = '/html/body/div/div[2]/div/div/main/div[4]/div[2]/div[3]/div/div/div[2]/div/div[6]/div/div[2]/div/div/table/tbody/tr['
                    sg_total_xpath = "/html/body/div/div[2]/div/div/main/div[4]/div[2]/div[3]/div/div/div[2]/div[2]/div[6]/div/div[2]/div/table/tbody/tr["
                    sg_total_xpat2 = '/html/body/div/div[2]/div/div/main/div[5]/div[2]/div[5]/div/div/div[2]/div[2]/div[6]/div/div[2]/div/table/tbody/tr['
                    sg_total_xpath = '/html/body/div/div[2]/div/div/main/div[5]/div[2]/div[5]/div/div/div[2]/div/div[6]/div/div[2]/div/div/table/tbody/tr['
                    sg_total_xpat2 = '/html/body/div/div[2]/div/div/main/div[5]/div[2]/div[5]/div/div/div[3]/div[2]/div[6]/div/div[2]/div/div/table/tbody/tr['
                    sg_total_xpath = '/html/body/div/div[2]/div/div/main/div[5]/div[2]/div[5]/div/div/div[2]/div/div[4]/div/div[2]/div/div/table/tbody/tr['
                    add_to_path_stat_val = '/td/span' # col 1
                    add_to_path_sup = '/td/div/span' # col 2
                    # gather stats
                    try:
                        sg_total = get_stats(f"{sg_total_xpath}1]", add_to_path_stat_val)[0]
                        sg_total_rank = get_stats(f"{sg_total_xpath}1]", add_to_path_stat_val)[1]
                        sg_total_total = get_sup_stats(f"{sg_total_xpath}1]", add_to_path_sup)[0]
                        sg_total_m_rounds = get_sup_stats(f"{sg_total_xpath}1]", add_to_path_sup)[1]
                        sg_tee_2_gr = get_stats(f"{sg_total_xpath}2]", add_to_path_stat_val)[0]
                        sg_tee_2_gr_rank = get_stats(f"{sg_total_xpath}2]", add_to_path_stat_val)[1]
                        sg_off_tee = get_stats(f"{sg_total_xpath}3]", add_to_path_stat_val)[0]
                        sg_off_tee_rank = get_stats(f"{sg_total_xpath}3]", add_to_path_stat_val)[1]
                        sg_off_tee_total = get_sup_stats(f"{sg_total_xpath}3]", add_to_path_sup)[0]
                        sg_app_gr = get_stats(f"{sg_total_xpath}4]", add_to_path_stat_val)[0]
                        sg_app_gr_rank = get_stats(f"{sg_total_xpath}4]", add_to_path_stat_val)[1]
                        sg_app_gr_total = get_sup_stats(f"{sg_total_xpath}4]", add_to_path_sup)[0]
                        sg_around_gr = get_stats(f"{sg_total_xpath}5]", add_to_path_stat_val)[0]
                        sg_around_gr_rank = get_stats(f"{sg_total_xpath}5]", add_to_path_stat_val)[1]
                        sg_around_gr_total = get_sup_stats(f"{sg_total_xpath}5]", add_to_path_sup)[0]
                        sg_putting = get_stats(f"{sg_total_xpath}6]", add_to_path_stat_val)[0]
                        sg_putting_rank = get_stats(f"{sg_total_xpath}6]", add_to_path_stat_val)[1]
                        sg_putting_total = get_sup_stats(f"{sg_total_xpath}6]", add_to_path_sup)[0]
                        total_driving = get_stats(f"{sg_total_xpath}7]", add_to_path_stat_val)[0]
                        total_driving_rank = get_stats(f"{sg_total_xpath}7]", add_to_path_stat_val)[1]
                        longest_drive = get_stats(f"{sg_total_xpath}8]", add_to_path_stat_val)[0]
                        longest_drive_rank = get_stats(f"{sg_total_xpath}8]", add_to_path_stat_val)[1]
                        longest_drive_tourney = get_sup_stats(f"{sg_total_xpath}8]", add_to_path_sup)[0]
                        longest_drive_round = get_sup_stats(f"{sg_total_xpath}8]", add_to_path_sup)[1]
                        driving_distance = get_stats(f"{sg_total_xpath}9]", add_to_path_stat_val)[0]
                        driving_distance_rank = get_stats(f"{sg_total_xpath}9]", add_to_path_stat_val)[1]
                        driving_distance_total = get_sup_stats(f"{sg_total_xpath}9]", add_to_path_sup)[0]
                        driving_distance_total_drives = get_sup_stats(f"{sg_total_xpath}9]", add_to_path_sup)[1]
                        driving_distance_all_drives = get_stats(f"{sg_total_xpath}10]", add_to_path_stat_val)[0]
                        driving_distance_all_drives_rank = get_stats(f"{sg_total_xpath}10]", add_to_path_stat_val)[1]
                        driving_distance_all_drives_total = get_sup_stats(f"{sg_total_xpath}10]", add_to_path_sup)[0]
                        driving_distance_all_drives_total_drives = get_sup_stats(f"{sg_total_xpath}10]", add_to_path_sup)[1]
                        driving_accuracy = get_stats(f"{sg_total_xpath}11]", add_to_path_stat_val)[0]
                        driving_accuracy_rank = get_stats(f"{sg_total_xpath}11]", add_to_path_stat_val)[1]
                        fairways_hit = get_sup_stats(f"{sg_total_xpath}11]", add_to_path_sup)[0]
                        fairways_possible = get_sup_stats(f"{sg_total_xpath}11]", add_to_path_sup)[1]
                        left_rough_tendency = get_stats(f"{sg_total_xpath}12]", add_to_path_stat_val)[0]
                        left_rough_tendency_rank = get_stats(f"{sg_total_xpath}12]", add_to_path_stat_val)[1]
                        left_rough_total = get_sup_stats(f"{sg_total_xpath}12]", add_to_path_sup)[0]
                        left_rough_possible_fairways = get_sup_stats(f"{sg_total_xpath}12]", add_to_path_sup)[1]
                        right_rough_tendency = get_stats(f"{sg_total_xpath}13]", add_to_path_stat_val)[0]
                        right_rough_tendency_rank = get_stats(f"{sg_total_xpath}13]", add_to_path_stat_val)[1]
                        right_rough_total = get_sup_stats(f"{sg_total_xpath}13]", add_to_path_sup)[0]
                        right_rough_possible_fairways = get_sup_stats(f"{sg_total_xpath}13]", add_to_path_sup)[1]
                        distance_from_edge_frwy = get_stats(f"{sg_total_xpath}14]", add_to_path_stat_val)[0]
                        distance_from_edge_frwy_rank = get_stats(f"{sg_total_xpath}14]", add_to_path_stat_val)[1]
                        distance_from_edge_frwy_total = get_sup_stats(f"{sg_total_xpath}14]", add_to_path_sup)[0]
                        distance_from_edge_frwy_strokes = get_sup_stats(f"{sg_total_xpath}14]", add_to_path_sup)[1]
                        club_head_speed = get_stats(f"{sg_total_xpath}15]", add_to_path_stat_val)[0]
                        club_head_speed_rank = get_stats(f"{sg_total_xpath}15]", add_to_path_stat_val)[1]
                        club_head_speed_total = get_sup_stats(f"{sg_total_xpath}15]", add_to_path_sup)[0]
                        club_head_speed_attempts = get_sup_stats(f"{sg_total_xpath}15]", add_to_path_sup)[1]
                        total_driving_efficiency = get_stats(f"{sg_total_xpath}16]", add_to_path_stat_val)[0]
                        total_driving_efficiency_rank = get_stats(f"{sg_total_xpath}16]", add_to_path_stat_val)[1]
                        carry_efficiency_rank = get_sup_stats(f"{sg_total_xpath}16]", add_to_path_sup)[1]
                        greens_in_regulation_percent = get_stats(f"{sg_total_xpath}17]", add_to_path_stat_val)[0]
                        greens_in_regulation_percent_rank = get_stats(f"{sg_total_xpath}17]", add_to_path_stat_val)[1]
                        greens_hit = get_sup_stats(f"{sg_total_xpath}17]", add_to_path_sup)[0]
                        greens_possible = get_sup_stats(f"{sg_total_xpath}17]", add_to_path_sup)[1]
                        proximity_to_hole = get_stats(f"{sg_total_xpath}18]", add_to_path_stat_val)[0]
                        proximity_to_hole_rank = get_stats(f"{sg_total_xpath}18]", add_to_path_stat_val)[1]
                        proximity_to_hole_total_ft = get_sup_stats(f"{sg_total_xpath}18]", add_to_path_sup)[0]
                        proximity_to_hole_total_att = get_sup_stats(f"{sg_total_xpath}18]", add_to_path_sup)[1]
                        
                        approach_more_275_in = get_stats(f"{sg_total_xpath}19]", add_to_path_stat_val)[0]
                        approach_more_275_rank = get_stats(f"{sg_total_xpath}19]", add_to_path_stat_val)[1]
                        approach_more_275_total_ft = get_sup_stats(f"{sg_total_xpath}19]", add_to_path_sup)[0]
                        approach_more_275_total_att = get_sup_stats(f"{sg_total_xpath}19]", add_to_path_sup)[1]
                        
                        approach_250_275_in = get_stats(f"{sg_total_xpath}20]", add_to_path_stat_val)[0]
                        approach_250_275_rank = get_stats(f"{sg_total_xpath}20]", add_to_path_stat_val)[1]
                        approach_250_275_total_ft = get_sup_stats(f"{sg_total_xpath}20]", add_to_path_sup)[0]
                        approach_250_275_total_att = get_sup_stats(f"{sg_total_xpath}20]", add_to_path_sup)[1]
                        
                        approach_225_250_in = get_stats(f"{sg_total_xpath}21]", add_to_path_stat_val)[0]
                        approach_225_250_rank = get_stats(f"{sg_total_xpath}21]", add_to_path_stat_val)[1]
                        approach_225_250_total_ft = get_sup_stats(f"{sg_total_xpath}21]", add_to_path_sup)[0]
                        approach_225_250_total_att = get_sup_stats(f"{sg_total_xpath}21]", add_to_path_sup)[1]
                        
                        approach_200_225_in = get_stats(f"{sg_total_xpath}22]", add_to_path_stat_val)[0]
                        approach_200_225_rank = get_stats(f"{sg_total_xpath}22]", add_to_path_stat_val)[1]
                        approach_200_225_total_ft = get_sup_stats(f"{sg_total_xpath}22]", add_to_path_sup)[0]
                        approach_200_225_total_att = get_sup_stats(f"{sg_total_xpath}22]", add_to_path_sup)[1]
                        
                        approach_more_200_in = get_stats(f"{sg_total_xpath}23]", add_to_path_stat_val)[0]
                        approach_more_200_rank = get_stats(f"{sg_total_xpath}23]", add_to_path_stat_val)[1]
                        approach_more_200_total_ft = get_sup_stats(f"{sg_total_xpath}23]", add_to_path_sup)[0]
                        approach_more_200_total_att = get_sup_stats(f"{sg_total_xpath}23]", add_to_path_sup)[1]
                        
                        approach_175_200_in = get_stats(f"{sg_total_xpath}24]", add_to_path_stat_val)[0]
                        approach_175_200_rank = get_stats(f"{sg_total_xpath}24]", add_to_path_stat_val)[1]
                        approach_175_200_total_ft = get_sup_stats(f"{sg_total_xpath}24]", add_to_path_sup)[0]
                        approach_175_200_total_att = get_sup_stats(f"{sg_total_xpath}24]", add_to_path_sup)[1]
                        
                        approach_150_175_in = get_stats(f"{sg_total_xpath}25]", add_to_path_stat_val)[0]
                        approach_150_175_rank = get_stats(f"{sg_total_xpath}25]", add_to_path_stat_val)[1]
                        approach_150_175_total_ft = get_sup_stats(f"{sg_total_xpath}25]", add_to_path_sup)[0]
                        approach_150_175_total_att = get_sup_stats(f"{sg_total_xpath}25]", add_to_path_sup)[1]
                        
                        approach_125_150_in = get_stats(f"{sg_total_xpath}26]", add_to_path_stat_val)[0]
                        approach_125_150_rank = get_stats(f"{sg_total_xpath}26]", add_to_path_stat_val)[1]
                        approach_125_150_total_ft = get_sup_stats(f"{sg_total_xpath}26]", add_to_path_sup)[0]
                        approach_125_150_total_att = get_sup_stats(f"{sg_total_xpath}26]", add_to_path_sup)[1]
                        
                        approach_50_125_in = get_stats(f"{sg_total_xpath}27]", add_to_path_stat_val)[0]
                        approach_50_125_rank = get_stats(f"{sg_total_xpath}27]", add_to_path_stat_val)[1]
                        approach_50_125_total_ft = get_sup_stats(f"{sg_total_xpath}27]", add_to_path_sup)[0]
                        approach_50_125_total_att = get_sup_stats(f"{sg_total_xpath}27]", add_to_path_sup)[1]
                        
                        approach_100_125_in = get_stats(f"{sg_total_xpath}28]", add_to_path_stat_val)[0]
                        approach_100_125_rank = get_stats(f"{sg_total_xpath}28]", add_to_path_stat_val)[1]
                        approach_100_125_total_ft = get_sup_stats(f"{sg_total_xpath}28]", add_to_path_sup)[0]
                        approach_100_125_total_att = get_sup_stats(f"{sg_total_xpath}28]", add_to_path_sup)[1]
                        
                        approach_75_100_in = get_stats(f"{sg_total_xpath}29]", add_to_path_stat_val)[0]
                        approach_75_100_rank = get_stats(f"{sg_total_xpath}29]", add_to_path_stat_val)[1]
                        approach_75_100_total_ft = get_sup_stats(f"{sg_total_xpath}29]", add_to_path_sup)[0]
                        approach_75_100_total_att = get_sup_stats(f"{sg_total_xpath}29]", add_to_path_sup)[1]
                        
                        approach_50_75_in = get_stats(f"{sg_total_xpath}30]", add_to_path_stat_val)[0]
                        approach_50_75_rank = get_stats(f"{sg_total_xpath}30]", add_to_path_stat_val)[1]
                        approach_50_75_total_ft = get_sup_stats(f"{sg_total_xpath}30]", add_to_path_sup)[0]
                        approach_50_75_total_att = get_sup_stats(f"{sg_total_xpath}30]", add_to_path_sup)[1]
                        
                        approach_less_100_in = get_stats(f"{sg_total_xpath}31]", add_to_path_stat_val)[0]
                        approach_less_100_rank = get_stats(f"{sg_total_xpath}31]", add_to_path_stat_val)[1]
                        approach_less_100_total_ft = get_sup_stats(f"{sg_total_xpath}31]", add_to_path_sup)[0]
                        approach_less_100_total_att = get_sup_stats(f"{sg_total_xpath}31]", add_to_path_sup)[1]
                        
                        approach_more_100_in = get_stats(f"{sg_total_xpath}32]", add_to_path_stat_val)[0]
                        approach_more_100_rank = get_stats(f"{sg_total_xpath}32]", add_to_path_stat_val)[1]
                        approach_more_100_total_ft = get_sup_stats(f"{sg_total_xpath}32]", add_to_path_sup)[0]
                        approach_more_100_total_att = get_sup_stats(f"{sg_total_xpath}32]", add_to_path_sup)[1]
        
                        fairway_proximity = get_stats(f"{sg_total_xpath}33]", add_to_path_stat_val)[0]
                        fairway_proximity_rank = get_stats(f"{sg_total_xpath}33]", add_to_path_stat_val)[1]
                        fairway_proximity_att = get_sup_stats(f"{sg_total_xpath}33]", add_to_path_sup)[1]
                        
                        rough_proximity = get_stats(f"{sg_total_xpath}34]", add_to_path_stat_val)[0]
                        rough_proximity_rank = get_stats(f"{sg_total_xpath}34]", add_to_path_stat_val)[1]
                        rough_proximity_total_in = get_sup_stats(f"{sg_total_xpath}34]", add_to_path_sup)[0]
                        rough_proximity_total_att = get_sup_stats(f"{sg_total_xpath}34]", add_to_path_sup)[1]
                        
                        left_rough_proximity = get_stats(f"{sg_total_xpath}35]", add_to_path_stat_val)[0]
                        left_rough_proximity_rank = get_stats(f"{sg_total_xpath}35]", add_to_path_stat_val)[1]
                        left_rough_proximity_att = get_sup_stats(f"{sg_total_xpath}35]", add_to_path_sup)[1]
                        
                        right_rough_proximity = get_stats(f"{sg_total_xpath}36]", add_to_path_stat_val)[0]
                        right_rough_proximity_rank = get_stats(f"{sg_total_xpath}36]", add_to_path_stat_val)[1]
                        right_rough_proximity_att = get_sup_stats(f"{sg_total_xpath}36]", add_to_path_sup)[1]
        
                        approach_more_275_rough_in = get_stats(f"{sg_total_xpath}37]", add_to_path_stat_val)[0]
                        approach_more_275_rough_rank = get_stats(f"{sg_total_xpath}37]", add_to_path_stat_val)[1]
                        approach_more_275_rough_total_ft = get_sup_stats(f"{sg_total_xpath}37]", add_to_path_sup)[0]
                        approach_more_275_rough_total_att = get_sup_stats(f"{sg_total_xpath}37]", add_to_path_sup)[1]
                        
                        approach_250_275_rough_in = get_stats(f"{sg_total_xpath}38]", add_to_path_stat_val)[0]
                        approach_250_275_rough_rank = get_stats(f"{sg_total_xpath}38]", add_to_path_stat_val)[1]
                        approach_250_275_rough_total_ft = get_sup_stats(f"{sg_total_xpath}38]", add_to_path_sup)[0]
                        approach_250_275_rough_total_att = get_sup_stats(f"{sg_total_xpath}38]", add_to_path_sup)[1]
                        
                        approach_225_250_rough_in = get_stats(f"{sg_total_xpath}39]", add_to_path_stat_val)[0]
                        approach_225_250_rough_rank = get_stats(f"{sg_total_xpath}39]", add_to_path_stat_val)[1]
                        approach_225_250_rough_total_ft = get_sup_stats(f"{sg_total_xpath}39]", add_to_path_sup)[0]
                        approach_225_250_rough_total_att = get_sup_stats(f"{sg_total_xpath}39]", add_to_path_sup)[1]
                        
                        approach_200_225_rough_in = get_stats(f"{sg_total_xpath}40]", add_to_path_stat_val)[0]
                        approach_200_225_rough_rank = get_stats(f"{sg_total_xpath}40]", add_to_path_stat_val)[1]
                        approach_200_225_rough_total_ft = get_sup_stats(f"{sg_total_xpath}40]", add_to_path_sup)[0]
                        approach_200_225_rough_total_att = get_sup_stats(f"{sg_total_xpath}40]", add_to_path_sup)[1]
                        
                        approach_more_100_rough_in = get_stats(f"{sg_total_xpath}41]", add_to_path_stat_val)[0]
                        approach_more_100_rough_rank = get_stats(f"{sg_total_xpath}41]", add_to_path_stat_val)[1]
                        approach_more_100_rough_total_ft = get_sup_stats(f"{sg_total_xpath}41]", add_to_path_sup)[0]
                        approach_more_100_rough_total_att = get_sup_stats(f"{sg_total_xpath}41]", add_to_path_sup)[1]
                        
                        approach_less_100_rough_in = get_stats(f"{sg_total_xpath}42]", add_to_path_stat_val)[0]
                        approach_less_100_rough_rank = get_stats(f"{sg_total_xpath}42]", add_to_path_stat_val)[1]
                        approach_less_100_rough_total_ft = get_sup_stats(f"{sg_total_xpath}42]", add_to_path_sup)[0]
                        approach_less_100_rough_total_att = get_sup_stats(f"{sg_total_xpath}42]", add_to_path_sup)[1]
                        
                        approach_more_200_rough_in = get_stats(f"{sg_total_xpath}43]", add_to_path_stat_val)[0]
                        approach_more_200_rough_rank = get_stats(f"{sg_total_xpath}43]", add_to_path_stat_val)[1]
                        approach_more_200_rough_total_ft = get_sup_stats(f"{sg_total_xpath}43]", add_to_path_sup)[0]
                        approach_more_200_rough_total_att = get_sup_stats(f"{sg_total_xpath}43]", add_to_path_sup)[1]
                        
                        approach_175_200_rough_in = get_stats(f"{sg_total_xpath}44]", add_to_path_stat_val)[0]
                        approach_175_200_rough_rank = get_stats(f"{sg_total_xpath}44]", add_to_path_stat_val)[1]
                        approach_175_200_rough_total_ft = get_sup_stats(f"{sg_total_xpath}44]", add_to_path_sup)[0]
                        approach_175_200_rough_total_att = get_sup_stats(f"{sg_total_xpath}44]", add_to_path_sup)[1]
                        
                        approach_150_175_rough_in = get_stats(f"{sg_total_xpath}45]", add_to_path_stat_val)[0]
                        approach_150_175_rough_rank = get_stats(f"{sg_total_xpath}45]", add_to_path_stat_val)[1]
                        approach_150_175_rough_total_ft = get_sup_stats(f"{sg_total_xpath}45]", add_to_path_sup)[0]
                        approach_150_175_rough_total_att = get_sup_stats(f"{sg_total_xpath}45]", add_to_path_sup)[1]
                        
                        approach_125_150_rough_in = get_stats(f"{sg_total_xpath}46]", add_to_path_stat_val)[0]
                        approach_125_150_rough_rank = get_stats(f"{sg_total_xpath}46]", add_to_path_stat_val)[1]
                        approach_125_150_rough_total_ft = get_sup_stats(f"{sg_total_xpath}46]", add_to_path_sup)[0]
                        approach_125_150_rough_total_att = get_sup_stats(f"{sg_total_xpath}46]", add_to_path_sup)[1]
                        
                        approach_50_125_rough_in = get_stats(f"{sg_total_xpath}47]", add_to_path_stat_val)[0]
                        approach_50_125_rough_rank = get_stats(f"{sg_total_xpath}47]", add_to_path_stat_val)[1]
                        approach_50_125_rough_total_ft = get_sup_stats(f"{sg_total_xpath}47]", add_to_path_sup)[0]
                        approach_50_125_rough_total_att = get_sup_stats(f"{sg_total_xpath}47]", add_to_path_sup)[1]
                        
                        approach_100_125_rough_in = get_stats(f"{sg_total_xpath}48]", add_to_path_stat_val)[0]
                        approach_100_125_rough_rank = get_stats(f"{sg_total_xpath}48]", add_to_path_stat_val)[1]
                        approach_100_125_rough_total_ft = get_sup_stats(f"{sg_total_xpath}48]", add_to_path_sup)[0]
                        approach_100_125_rough_total_att = get_sup_stats(f"{sg_total_xpath}48]", add_to_path_sup)[1]
                        
                        approach_75_100_rough_in = get_stats(f"{sg_total_xpath}49]", add_to_path_stat_val)[0]
                        approach_75_100_rough_rank = get_stats(f"{sg_total_xpath}49]", add_to_path_stat_val)[1]
                        approach_75_100_rough_total_ft = get_sup_stats(f"{sg_total_xpath}49]", add_to_path_sup)[0]
                        approach_75_100_rough_total_att = get_sup_stats(f"{sg_total_xpath}49]", add_to_path_sup)[1]
                        
                        approach_50_75_rough_in = get_stats(f"{sg_total_xpath}50]", add_to_path_stat_val)[0]
                        approach_50_75_rough_rank = get_stats(f"{sg_total_xpath}50]", add_to_path_stat_val)[1]
                        approach_50_75_rough_total_ft = get_sup_stats(f"{sg_total_xpath}50]", add_to_path_sup)[0]
                        approach_50_75_rough_total_att = get_sup_stats(f"{sg_total_xpath}50]", add_to_path_sup)[1]
                        
                        going_for_green_percent = get_stats(f"{sg_total_xpath}51]", add_to_path_stat_val)[0]
                        going_for_green_percent_rank = get_stats(f"{sg_total_xpath}51]", add_to_path_stat_val)[1]
                        going_for_green_percent_attempts = get_sup_stats(f"{sg_total_xpath}51]", add_to_path_sup)[0]
                        going_for_green_percent_non_attemptes = get_sup_stats(f"{sg_total_xpath}51]", add_to_path_sup)[1]
                        
                        going_for_green_hit_percent = get_stats(f"{sg_total_xpath}52]", add_to_path_stat_val)[0]
                        going_for_green_hit_rank = get_stats(f"{sg_total_xpath}52]", add_to_path_stat_val)[1]
                        going_for_green_hit = get_sup_stats(f"{sg_total_xpath}52]", add_to_path_sup)[0]
                        going_for_green_attempts = get_sup_stats(f"{sg_total_xpath}52]", add_to_path_sup)[1]
                        
                        going_for_green_birdie_better_pct = get_stats(f"{sg_total_xpath}53]", add_to_path_stat_val)[0]
                        going_for_green_birdie_better_pct_rank = get_stats(f"{sg_total_xpath}53]", add_to_path_stat_val)[1]
                        going_for_green_birdie_better_total = get_sup_stats(f"{sg_total_xpath}53]", add_to_path_sup)[0]
                        
                        total_hole_outs = get_stats(f"{sg_total_xpath}54]", add_to_path_stat_val)[0]
                        total_hole_outs_rank = get_stats(f"{sg_total_xpath}54]", add_to_path_stat_val)[1]
                        
                        
                        
                        
                        longest_hole_out_yrds = get_stats(f"{sg_total_xpath}55]", add_to_path_stat_val)[0]
                        longest_hole_out_rank = get_stats(f"{sg_total_xpath}55]", add_to_path_stat_val)[1]
                        longest_hole_out_tourney = get_sup_stats(f"{sg_total_xpath}55]", add_to_path_sup)[0]
                        longest_hole_out_rd = get_sup_stats(f"{sg_total_xpath}55]", add_to_path_sup)[1]
                        
                        scrambling_percent = get_stats(f"{sg_total_xpath}56]", add_to_path_stat_val)[0]
                        scrambling_rank = get_stats(f"{sg_total_xpath}56]", add_to_path_stat_val)[1]
                        scrambling_par_or_better = get_sup_stats(f"{sg_total_xpath}56]", add_to_path_sup)[0]
                        scrambling_missed_gir = get_sup_stats(f"{sg_total_xpath}56]", add_to_path_sup)[1]
                        
                        scrambling_from_rough_perecnt = get_stats(f"{sg_total_xpath}57]", add_to_path_stat_val)[0]
                        scrambling_from_rough_rank = get_stats(f"{sg_total_xpath}57]", add_to_path_stat_val)[1]
                        scrambling_from_rough_success = get_sup_stats(f"{sg_total_xpath}57]", add_to_path_sup)[0]
                        scrambling_from_rough_att = get_sup_stats(f"{sg_total_xpath}57]", add_to_path_sup)[1]
                        
                        scrambling_from_fringe_percent = get_stats(f"{sg_total_xpath}58]", add_to_path_stat_val)[0]
                        scrambling_from_fringe_rank = get_stats(f"{sg_total_xpath}58]", add_to_path_stat_val)[1]
                        scrambling_from_fringe_success = get_sup_stats(f"{sg_total_xpath}58]", add_to_path_sup)[0]
                        scrambling_from_fringe_att = get_sup_stats(f"{sg_total_xpath}58]", add_to_path_sup)[1]
                        
                        scrambling_more_30_percent = get_stats(f"{sg_total_xpath}59]", add_to_path_stat_val)[0]
                        scrambling_more_30_rank = get_stats(f"{sg_total_xpath}59]", add_to_path_stat_val)[1]
                        scrambling_more_30_success = get_sup_stats(f"{sg_total_xpath}59]", add_to_path_sup)[0]
                        scrambling_more_30_att = get_sup_stats(f"{sg_total_xpath}59]", add_to_path_sup)[1]
                        
                        scrambling_20_30_percent = get_stats(f"{sg_total_xpath}60]", add_to_path_stat_val)[0]
                        scrambling_20_30_rank = get_stats(f"{sg_total_xpath}60]", add_to_path_stat_val)[1]
                        scrambling_20_30_success = get_sup_stats(f"{sg_total_xpath}60]", add_to_path_sup)[0]
                        scrambling_20_30_att = get_sup_stats(f"{sg_total_xpath}60]", add_to_path_sup)[1]
                        
                        scrambling_10_20_percent = get_stats(f"{sg_total_xpath}61]", add_to_path_stat_val)[0]
                        scrambling_10_20_rank = get_stats(f"{sg_total_xpath}61]", add_to_path_stat_val)[1]
                        scrambling_10_20_success = get_sup_stats(f"{sg_total_xpath}61]", add_to_path_sup)[0]
                        scrambling_10_20_att = get_sup_stats(f"{sg_total_xpath}61]", add_to_path_sup)[1]
                        
                        scrambling_less_10_percent = get_stats(f"{sg_total_xpath}62]", add_to_path_stat_val)[0]
                        scrambling_less_10_rank = get_stats(f"{sg_total_xpath}62]", add_to_path_stat_val)[1]
                        scrambling_less_10_success = get_sup_stats(f"{sg_total_xpath}62]", add_to_path_sup)[0]
                        scrambling_less_10_att = get_sup_stats(f"{sg_total_xpath}62]", add_to_path_sup)[1]
                        
                        sand_save_percent = get_stats(f"{sg_total_xpath}63]", add_to_path_stat_val)[0]
                        sand_save_rank = get_stats(f"{sg_total_xpath}63]", add_to_path_stat_val)[1]
                        sand_save_saves = get_sup_stats(f"{sg_total_xpath}63]", add_to_path_sup)[0]
                        sand_save_bunkers = get_sup_stats(f"{sg_total_xpath}63]", add_to_path_sup)[1]
                        
                        proximity_to_hole_sand = get_stats(f"{sg_total_xpath}64]", add_to_path_stat_val)[0]
                        proximity_to_hole_sand_rank = get_stats(f"{sg_total_xpath}64]", add_to_path_stat_val)[1]
                        proximity_to_hole_sand_total_ft = get_sup_stats(f"{sg_total_xpath}64]", add_to_path_sup)[0]
                        proximity_to_hole_sand_shots = get_sup_stats(f"{sg_total_xpath}64]", add_to_path_sup)[1]
                        
                        total_putting = get_stats(f"{sg_total_xpath}65]", add_to_path_stat_val)[0]
                        total_putting_rank = get_stats(f"{sg_total_xpath}65]", add_to_path_stat_val)[1]
                        
                        putting_avg = get_stats(f"{sg_total_xpath}66]", add_to_path_stat_val)[0]
                        putting_avg_rank = get_stats(f"{sg_total_xpath}66]", add_to_path_stat_val)[1]
                        putting_avg_gir_putts = get_sup_stats(f"{sg_total_xpath}66]", add_to_path_sup)[0]
                        putting_avg_greens_hit = get_sup_stats(f"{sg_total_xpath}66]", add_to_path_sup)[1]
                        
                        overall_putting_avg = get_stats(f"{sg_total_xpath}67]", add_to_path_stat_val)[0]
                        overall_putting_avg_rank = get_stats(f"{sg_total_xpath}67]", add_to_path_stat_val)[1]
                        overall_putting_total_putts = get_sup_stats(f"{sg_total_xpath}67]", add_to_path_sup)[0]
                        overall_putting_total_holes = get_sup_stats(f"{sg_total_xpath}67]", add_to_path_sup)[1]
                        
                        birdie_or_better_conversion_percent = get_stats(f"{sg_total_xpath}68]", add_to_path_stat_val)[0]
                        birdie_or_better_conversion_rank = get_stats(f"{sg_total_xpath}68]", add_to_path_stat_val)[1]
                        birdie_or_better_conversion_birdies = get_sup_stats(f"{sg_total_xpath}68]", add_to_path_sup)[0]
                        birdie_or_better_conversion_greens_hit = get_sup_stats(f"{sg_total_xpath}68]", add_to_path_sup)[1]
                        
                        putts_per_round = get_stats(f"{sg_total_xpath}69]", add_to_path_stat_val)[0]
                        putts_per_round_rank = get_stats(f"{sg_total_xpath}69]", add_to_path_stat_val)[1]
                        total_putts = get_sup_stats(f"{sg_total_xpath}69]", add_to_path_sup)[0]
                        total_rounds = get_sup_stats(f"{sg_total_xpath}69]", add_to_path_sup)[1]
                        
                        putts_per_round_rd1 = get_stats(f"{sg_total_xpath}70]", add_to_path_stat_val)[0]
                        putts_per_round_rd1_rank = get_stats(f"{sg_total_xpath}70]", add_to_path_stat_val)[1]
                        total_putts_rd1 = get_sup_stats(f"{sg_total_xpath}70]", add_to_path_sup)[0]
                        total_rounds_rd1 = get_sup_stats(f"{sg_total_xpath}70]", add_to_path_sup)[1]
                        
                        putts_per_round_rd2 = get_stats(f"{sg_total_xpath}71]", add_to_path_stat_val)[0]
                        putts_per_round_rd2_rank = get_stats(f"{sg_total_xpath}71]", add_to_path_stat_val)[1]
                        total_putts_rd2 = get_sup_stats(f"{sg_total_xpath}71]", add_to_path_sup)[0]
                        total_rounds_rd2 = get_sup_stats(f"{sg_total_xpath}71]", add_to_path_sup)[1]
                        
                        putts_per_round_rd3 = get_stats(f"{sg_total_xpath}72]", add_to_path_stat_val)[0]
                        putts_per_round_rd3_rank = get_stats(f"{sg_total_xpath}72]", add_to_path_stat_val)[1]
                        total_putts_rd3 = get_sup_stats(f"{sg_total_xpath}72]", add_to_path_sup)[0]
                        total_rounds_rd3 = get_sup_stats(f"{sg_total_xpath}72]", add_to_path_sup)[1]
                        
                        putts_per_round_rd4 = get_stats(f"{sg_total_xpath}73]", add_to_path_stat_val)[0]
                        putts_per_round_rd4_rank = get_stats(f"{sg_total_xpath}73]", add_to_path_stat_val)[1]
                        total_putts_rd4 = get_sup_stats(f"{sg_total_xpath}73]", add_to_path_sup)[0]
                        total_rounds_rd4 = get_sup_stats(f"{sg_total_xpath}73]", add_to_path_sup)[1]
                        
                        one_putt_percentage = get_stats(f"{sg_total_xpath}74]", add_to_path_stat_val)[0]
                        one_putt_rank = get_stats(f"{sg_total_xpath}74]", add_to_path_stat_val)[1]
                        one_putt_total = get_sup_stats(f"{sg_total_xpath}74]", add_to_path_sup)[0]
                        one_putt_total_holes = get_sup_stats(f"{sg_total_xpath}74]", add_to_path_sup)[1]
                        
                        longest_putt = get_stats(f"{sg_total_xpath}75]", add_to_path_stat_val)[0]
                        longest_putt_break = get_stats(f"{sg_total_xpath}75]", add_to_path_stat_val)[1]
                        longest_putt_tourney = get_sup_stats(f"{sg_total_xpath}75]", add_to_path_sup)[0]
                        longest_putt_rd = get_sup_stats(f"{sg_total_xpath}75]", add_to_path_sup)[1]
                        
                        three_putt_avoidance = get_stats(f"{sg_total_xpath}76]", add_to_path_stat_val)[0]
                        three_putt_avoidance_rank = get_stats(f"{sg_total_xpath}76]", add_to_path_stat_val)[1]
                        three_putt_total = get_sup_stats(f"{sg_total_xpath}76]", add_to_path_sup)[0]
                        three_putt_total_holes = get_sup_stats(f"{sg_total_xpath}76]", add_to_path_sup)[1]
                        
                        putting_more_25_percent = get_stats(f"{sg_total_xpath}77]", add_to_path_stat_val)[0]
                        putting_more_25_rank = get_stats(f"{sg_total_xpath}77]", add_to_path_stat_val)[1]
                        putting_more_25_att = get_sup_stats(f"{sg_total_xpath}77]", add_to_path_sup)[0]
                        putting_more_25_made = get_sup_stats(f"{sg_total_xpath}77]", add_to_path_sup)[1]
                        
                        putting_20_25_percent = get_stats(f"{sg_total_xpath}78]", add_to_path_stat_val)[0]
                        putting_20_25_rank = get_stats(f"{sg_total_xpath}78]", add_to_path_stat_val)[1]
                        putting_20_25_att = get_sup_stats(f"{sg_total_xpath}78]", add_to_path_sup)[0]
                        putting_20_25_made = get_sup_stats(f"{sg_total_xpath}78]", add_to_path_sup)[1]
                        
                        putting_15_20_percent = get_stats(f"{sg_total_xpath}79]", add_to_path_stat_val)[0]
                        putting_15_20_rank = get_stats(f"{sg_total_xpath}79]", add_to_path_stat_val)[1]
                        putting_15_20_att = get_sup_stats(f"{sg_total_xpath}79]", add_to_path_sup)[0]
                        putting_15_20_made = get_sup_stats(f"{sg_total_xpath}79]", add_to_path_sup)[1]
                        
                        putting_10_15_percent = get_stats(f"{sg_total_xpath}80]", add_to_path_stat_val)[0]
                        putting_10_15_rank = get_stats(f"{sg_total_xpath}80]", add_to_path_stat_val)[1]
                        putting_10_15_att = get_sup_stats(f"{sg_total_xpath}80]", add_to_path_sup)[0]
                        putting_10_15_made = get_sup_stats(f"{sg_total_xpath}80]", add_to_path_sup)[1]
                        
                        putting_less_10_percent = get_stats(f"{sg_total_xpath}81]", add_to_path_stat_val)[0]
                        putting_less_10_rank = get_stats(f"{sg_total_xpath}81]", add_to_path_stat_val)[1]
                        putting_less_10_att = get_sup_stats(f"{sg_total_xpath}81]", add_to_path_sup)[0]
                        putting_less_10_made = get_sup_stats(f"{sg_total_xpath}81]", add_to_path_sup)[1]
                        
                        putting_from_10_percent = get_stats(f"{sg_total_xpath}82]", add_to_path_stat_val)[0]
                        putting_from_10_rank = get_stats(f"{sg_total_xpath}82]", add_to_path_stat_val)[1]
                        putting_from_10_att = get_sup_stats(f"{sg_total_xpath}82]", add_to_path_sup)[0]
                        
                        putting_from_9_percent = get_stats(f"{sg_total_xpath}83]", add_to_path_stat_val)[0]
                        putting_from_9_rank = get_stats(f"{sg_total_xpath}83]", add_to_path_stat_val)[1]
                        putting_from_9_att = get_sup_stats(f"{sg_total_xpath}83]", add_to_path_sup)[0]
                        
                        putting_from_8_percent = get_stats(f"{sg_total_xpath}84]", add_to_path_stat_val)[0]
                        putting_from_8_rank = get_stats(f"{sg_total_xpath}84]", add_to_path_stat_val)[1]
                        putting_from_8_att = get_sup_stats(f"{sg_total_xpath}84]", add_to_path_sup)[0]
                        
                        putting_from_7_percent = get_stats(f"{sg_total_xpath}85]", add_to_path_stat_val)[0]
                        putting_from_7_rank = get_stats(f"{sg_total_xpath}85]", add_to_path_stat_val)[1]
                        putting_from_7_att = get_sup_stats(f"{sg_total_xpath}85]", add_to_path_sup)[0]
                        
                        putting_from_6_percent = get_stats(f"{sg_total_xpath}86]", add_to_path_stat_val)[0]
                        putting_from_6_rank = get_stats(f"{sg_total_xpath}86]", add_to_path_stat_val)[1]
                        putting_from_6_att = get_sup_stats(f"{sg_total_xpath}86]", add_to_path_sup)[0]
                        
                        putting_from_5_percent = get_stats(f"{sg_total_xpath}87]", add_to_path_stat_val)[0]
                        putting_from_5_rank = get_stats(f"{sg_total_xpath}87]", add_to_path_stat_val)[1]
                        putting_from_5_att = get_sup_stats(f"{sg_total_xpath}87]", add_to_path_sup)[0]
                        
                        putting_from_4_8_percent = get_stats(f"{sg_total_xpath}88]", add_to_path_stat_val)[0]
                        putting_from_4_8_rank = get_stats(f"{sg_total_xpath}88]", add_to_path_stat_val)[1]
                        putting_from_4_8_att = get_sup_stats(f"{sg_total_xpath}88]", add_to_path_sup)[0]
                        putting_from_4_8_made = get_sup_stats(f"{sg_total_xpath}88]", add_to_path_sup)[1]
                        
                        putting_from_4_percent = get_stats(f"{sg_total_xpath}89]", add_to_path_stat_val)[0]
                        putting_from_4_rank = get_stats(f"{sg_total_xpath}89]", add_to_path_stat_val)[1]
                        putting_from_4_att = get_sup_stats(f"{sg_total_xpath}89]", add_to_path_sup)[0]
                        
                        putting_from_3_percent = get_stats(f"{sg_total_xpath}90]", add_to_path_stat_val)[0]
                        putting_from_3_rank = get_stats(f"{sg_total_xpath}90]", add_to_path_stat_val)[1]
                        putting_from_3_att = get_sup_stats(f"{sg_total_xpath}90]", add_to_path_sup)[0]
                        
                        avg_distance_putts_made = get_stats(f"{sg_total_xpath}91]", add_to_path_stat_val)[0]
                        avg_distance_putts_made_rank = get_stats(f"{sg_total_xpath}91]", add_to_path_stat_val)[1]
                        avg_distance_putts_made_in = get_sup_stats(f"{sg_total_xpath}91]", add_to_path_sup)[0]
                        avg_distance_putts_made_rounds = get_sup_stats(f"{sg_total_xpath}91]", add_to_path_sup)[1]
                        
                        approach_putt_performance = get_stats(f"{sg_total_xpath}92]", add_to_path_stat_val)[0]
                        approach_putt_rank = get_stats(f"{sg_total_xpath}92]", add_to_path_stat_val)[1]
                        approach_putt_att = get_sup_stats(f"{sg_total_xpath}92]", add_to_path_sup)[1]
                        
                        scoring_avg_adj = get_stats(f"{sg_total_xpath}93]", add_to_path_stat_val)[0]
                        scoring_avg_adj_rank = get_stats(f"{sg_total_xpath}93]", add_to_path_stat_val)[1]
                        scoring_avg_adj_total_strokes = get_sup_stats(f"{sg_total_xpath}93]", add_to_path_sup)[0]
                        scoring_avg_adj_total_adjustment = get_sup_stats(f"{sg_total_xpath}93]", add_to_path_sup)[1]
                        
                        scoring_avg_actual = get_stats(f"{sg_total_xpath}94]", add_to_path_stat_val)[0]
                        scoring_avg_actual_rank = get_stats(f"{sg_total_xpath}94]", add_to_path_stat_val)[1]
                        scoring_avg_actual_total_strokes = get_sup_stats(f"{sg_total_xpath}94]", add_to_path_sup)[0]
                        scoring_avg_actual_total_rounds = get_sup_stats(f"{sg_total_xpath}94]", add_to_path_sup)[1]
                        
                        lowest_round = get_stats(f"{sg_total_xpath}95]", add_to_path_stat_val)[0]
                        lowest_round_rank = get_stats(f"{sg_total_xpath}95]", add_to_path_stat_val)[1]
                        lowest_round_tourney = get_sup_stats(f"{sg_total_xpath}95]", add_to_path_sup)[0]
                        lowest_round_round = get_sup_stats(f"{sg_total_xpath}95]", add_to_path_sup)[1]
                        
                        birdie_avg = get_stats(f"{sg_total_xpath}96]", add_to_path_stat_val)[0]
                        birdie_avg_rank = get_stats(f"{sg_total_xpath}96]", add_to_path_stat_val)[1]
                        birdie_avg_num_birdies = get_sup_stats(f"{sg_total_xpath}96]", add_to_path_sup)[0]
                        birdie_avg_total_rounds = get_sup_stats(f"{sg_total_xpath}96]", add_to_path_sup)[1]
                        
                        total_birdies = get_stats(f"{sg_total_xpath}97]", add_to_path_stat_val)[0]
                        total_birdies_rank = get_stats(f"{sg_total_xpath}97]", add_to_path_stat_val)[1]
                        
                        eagles_holes_per = get_stats(f"{sg_total_xpath}98]", add_to_path_stat_val)[0]
                        eagles_holes_per_rank = get_stats(f"{sg_total_xpath}98]", add_to_path_stat_val)[1]
                        
                        total_eagles = get_stats(f"{sg_total_xpath}99]", add_to_path_stat_val)[0]
                        total_eagles_rank = get_stats(f"{sg_total_xpath}99]", add_to_path_stat_val)[1]
                        
                        par_breaker_percent = get_stats(f"{sg_total_xpath}100]", add_to_path_stat_val)[0]
                        par_breaker_rank = get_stats(f"{sg_total_xpath}100]", add_to_path_stat_val)[1]
                        
                        bounce_back_percent = get_stats(f"{sg_total_xpath}101]", add_to_path_stat_val)[0]
                        bounce_back_rank = get_stats(f"{sg_total_xpath}101]", add_to_path_stat_val)[1]
                        
                        par3_birdie_or_better = get_stats(f"{sg_total_xpath}102]", add_to_path_stat_val)[0]
                        par3_birdie_or_better_rank = get_stats(f"{sg_total_xpath}102]", add_to_path_stat_val)[1]
                        par3_birdie_or_better_total = get_sup_stats(f"{sg_total_xpath}102]", add_to_path_sup)[0]
                        par3_holes = get_sup_stats(f"{sg_total_xpath}102]", add_to_path_sup)[1]
                        
                        par4_birdie_or_better = get_stats(f"{sg_total_xpath}103]", add_to_path_stat_val)[0]
                        par4_birdie_or_better_rank = get_stats(f"{sg_total_xpath}103]", add_to_path_stat_val)[1]
                        par4_birdie_or_better_total = get_sup_stats(f"{sg_total_xpath}103]", add_to_path_sup)[0]
                        par4_holes = get_sup_stats(f"{sg_total_xpath}103]", add_to_path_sup)[1]
                        
                        par5_birdie_or_better = get_stats(f"{sg_total_xpath}104]", add_to_path_stat_val)[0]
                        par5_birdie_or_better_rank = get_stats(f"{sg_total_xpath}104]", add_to_path_stat_val)[1]
                        par5_birdie_or_better_total = get_sup_stats(f"{sg_total_xpath}104]", add_to_path_sup)[0]
                        par5_holes = get_sup_stats(f"{sg_total_xpath}104]", add_to_path_sup)[1]
                        
                        birdie_or_better_percent = get_stats(f"{sg_total_xpath}105]", add_to_path_stat_val)[0]
                        birdie_or_better_rank = get_stats(f"{sg_total_xpath}105]", add_to_path_stat_val)[1]
                        
                        bogey_avoidance_percent = get_stats(f"{sg_total_xpath}106]", add_to_path_stat_val)[0]
                        bogey_avoidance_rank = get_stats(f"{sg_total_xpath}106]", add_to_path_stat_val)[1]
                        bogey_total = get_sup_stats(f"{sg_total_xpath}106]", add_to_path_sup)[0]
                        
                        final_round_scoring_avg = get_stats(f"{sg_total_xpath}107]", add_to_path_stat_val)[0]
                        final_round_scoring_avg_rank = get_stats(f"{sg_total_xpath}107]", add_to_path_stat_val)[1]
                        final_round_scoring_total_strokes = get_sup_stats(f"{sg_total_xpath}107]", add_to_path_sup)[0]
                        final_round_scoring_total_rds = get_sup_stats(f"{sg_total_xpath}107]", add_to_path_sup)[1]
                        
                        final_round_performance = get_stats(f"{sg_total_xpath}108]", add_to_path_stat_val)[0]
                        final_round_performance_rank = get_stats(f"{sg_total_xpath}108]", add_to_path_stat_val)[1]
                        
                        rd1_scoring_avg = get_stats(f"{sg_total_xpath}109]", add_to_path_stat_val)[0]
                        rd1_scoring_avg_rank = get_stats(f"{sg_total_xpath}109]", add_to_path_stat_val)[1]
                        rd1_scoring_total_strokes = get_sup_stats(f"{sg_total_xpath}109]", add_to_path_sup)[0]
                        rd1_scoring_total_rds = get_sup_stats(f"{sg_total_xpath}109]", add_to_path_sup)[1]
                        
                        rd2_scoring_avg = get_stats(f"{sg_total_xpath}110]", add_to_path_stat_val)[0]
                        rd2_scoring_avg_rank = get_stats(f"{sg_total_xpath}110]", add_to_path_stat_val)[1]
                        rd2_scoring_total_strokes = get_sup_stats(f"{sg_total_xpath}110]", add_to_path_sup)[0]
                        rd2_scoring_total_rds = get_sup_stats(f"{sg_total_xpath}110]", add_to_path_sup)[1]
                        
                        rd3_scoring_avg = get_stats(f"{sg_total_xpath}111]", add_to_path_stat_val)[0]
                        rd3_scoring_avg_rank = get_stats(f"{sg_total_xpath}111]", add_to_path_stat_val)[1]
                        rd3_scoring_total_strokes = get_sup_stats(f"{sg_total_xpath}111]", add_to_path_sup)[0]
                        rd3_scoring_total_rds = get_sup_stats(f"{sg_total_xpath}111]", add_to_path_sup)[1]
                        
                        rd4_scoring_avg = get_stats(f"{sg_total_xpath}112]", add_to_path_stat_val)[0]
                        rd4_scoring_avg_rank = get_stats(f"{sg_total_xpath}112]", add_to_path_stat_val)[1]
                        rd4_scoring_total_strokes = get_sup_stats(f"{sg_total_xpath}112]", add_to_path_sup)[0]
                        rd4_scoring_total_rds = get_sup_stats(f"{sg_total_xpath}112]", add_to_path_sup)[1]
                        
                        par3_scoring_avg = get_stats(f"{sg_total_xpath}113]", add_to_path_stat_val)[0]
                        par3_scoring_avg_rank = get_stats(f"{sg_total_xpath}113]", add_to_path_stat_val)[1]
                        par3_scoring_avg_strokes = get_sup_stats(f"{sg_total_xpath}113]", add_to_path_sup)[0]
                        par3_scoring_avg_holes = get_sup_stats(f"{sg_total_xpath}113]", add_to_path_sup)[1]
                        
                        par4_scoring_avg = get_stats(f"{sg_total_xpath}114]", add_to_path_stat_val)[0]
                        par4_scoring_avg_rank = get_stats(f"{sg_total_xpath}114]", add_to_path_stat_val)[1]
                        par4_scoring_avg_strokes = get_sup_stats(f"{sg_total_xpath}114]", add_to_path_sup)[0]
                        par4_scoring_avg_holes = get_sup_stats(f"{sg_total_xpath}114]", add_to_path_sup)[1]
                        
                        par5_scoring_avg = get_stats(f"{sg_total_xpath}115]", add_to_path_stat_val)[0]
                        par5_scoring_avg_rank = get_stats(f"{sg_total_xpath}115]", add_to_path_stat_val)[1]
                        par5_scoring_avg_strokes = get_sup_stats(f"{sg_total_xpath}115]", add_to_path_sup)[0]
                        par5_scoring_avg_holes = get_sup_stats(f"{sg_total_xpath}115]", add_to_path_sup)[1]
                        
                        front9_scoring_avg = get_stats(f"{sg_total_xpath}116]", add_to_path_stat_val)[0]
                        front9_scoring_avg_rank = get_stats(f"{sg_total_xpath}116]", add_to_path_stat_val)[1]
                        front9_scoring_avg_strokes = get_sup_stats(f"{sg_total_xpath}116]", add_to_path_sup)[0]
                        front9_scoring_avg_holes = get_sup_stats(f"{sg_total_xpath}116]", add_to_path_sup)[1]
                        
                        back9_scoring_avg = get_stats(f"{sg_total_xpath}117]", add_to_path_stat_val)[0]
                        back9_scoring_avg_rank = get_stats(f"{sg_total_xpath}117]", add_to_path_stat_val)[1]
                        back9_scoring_avg_strokes = get_sup_stats(f"{sg_total_xpath}117]", add_to_path_sup)[0]
                        back9_scoring_avg_holes = get_sup_stats(f"{sg_total_xpath}117]", add_to_path_sup)[1]
                        
                        early_scoring_avg = get_stats(f"{sg_total_xpath}118]", add_to_path_stat_val)[0]
                        early_scoring_avg_rank = get_stats(f"{sg_total_xpath}118]", add_to_path_stat_val)[1]
                        early_scoring_total_strokes = get_sup_stats(f"{sg_total_xpath}118]", add_to_path_sup)[0]
                        early_scoring_total_rounds = get_sup_stats(f"{sg_total_xpath}118]", add_to_path_sup)[1]
                        
                        late_scoring_avg = get_stats(f"{sg_total_xpath}119]", add_to_path_stat_val)[0]
                        late_scoring_avg_rank = get_stats(f"{sg_total_xpath}119]", add_to_path_stat_val)[1]
                        late_scoring_total_strokes = get_sup_stats(f"{sg_total_xpath}119]", add_to_path_sup)[0]
                        late_scoring_total_rounds = get_sup_stats(f"{sg_total_xpath}119]", add_to_path_sup)[1]
                        
                        consecutive_cuts = get_stats(f"{sg_total_xpath}120]", add_to_path_stat_val)[0]
                        consecutive_cuts_rank = get_stats(f"{sg_total_xpath}120]", add_to_path_stat_val)[1]
                        
                        #skip current_streak without 3 putt 121
                        
                        consecutive_fairways_hit = get_stats(f"{sg_total_xpath}122]", add_to_path_stat_val)[0]
                        consecutive_fairways_hit_rank = get_stats(f"{sg_total_xpath}122]", add_to_path_stat_val)[1]
                        
                        consecutive_gir = get_stats(f"{sg_total_xpath}123]", add_to_path_stat_val)[0]
                        consecutive_gir_rank = get_stats(f"{sg_total_xpath}123]", add_to_path_stat_val)[1]
                        
                        consecutive_sand_saves = get_stats(f"{sg_total_xpath}124]", add_to_path_stat_val)[0]
                        consecutive_sand_saves_rank = get_stats(f"{sg_total_xpath}124]", add_to_path_stat_val)[1]
                        
                        best_ytd_1_putt_or_better_streak = get_stats(f"{sg_total_xpath}125]", add_to_path_stat_val)[0]
                        best_ytd_1_putt_or_better_streak_rank = get_stats(f"{sg_total_xpath}125]", add_to_path_stat_val)[1]
                        
                        best_ytd_streak_wo_3_putt = get_stats(f"{sg_total_xpath}126]", add_to_path_stat_val)[0]
                        best_ytd_streak_wo_3_putt_rank = get_stats(f"{sg_total_xpath}126]", add_to_path_stat_val)[1]
                        
                        ytd_par_or_better_streak = get_stats(f"{sg_total_xpath}127]", add_to_path_stat_val)[0]
                        ytd_par_or_better_streak_rank = get_stats(f"{sg_total_xpath}127]", add_to_path_stat_val)[1]
                        
                        consecutive_par_3_birdies = get_stats(f"{sg_total_xpath}128]", add_to_path_stat_val)[0]
                        consecutive_par_3_birdies_rank = get_stats(f"{sg_total_xpath}128]", add_to_path_stat_val)[1]
                        
                        consecutive_holes_below_par = get_stats(f"{sg_total_xpath}129]", add_to_path_stat_val)[0]
                        consecutive_holes_below_par_rank = get_stats(f"{sg_total_xpath}129]", add_to_path_stat_val)[1]
                        
                        consecutive_birdies_streak = get_stats(f"{sg_total_xpath}130]", add_to_path_stat_val)[0]
                        consecutive_birdies_streak_rank = get_stats(f"{sg_total_xpath}130]", add_to_path_stat_val)[1]
                        
                        consecutive_birdies_eagles_streak = get_stats(f"{sg_total_xpath}131]", add_to_path_stat_val)[0]
                        consecutive_birdies_eagles_streak_rank = get_stats(f"{sg_total_xpath}131]", add_to_path_stat_val)[1]
                        
                        official_money = get_stats(f"{sg_total_xpath}132]", add_to_path_stat_val)[0]
                        official_money_rank = get_stats(f"{sg_total_xpath}132]", add_to_path_stat_val)[1]
                        
                        fedexcup_regular_season_points = get_stats(f"{sg_total_xpath}133]", add_to_path_stat_val)[0]
                        fedexcup_rank = get_stats(f"{sg_total_xpath}133]", add_to_path_stat_val)[1]
                        wins = get_sup_stats(f"{sg_total_xpath}133]", add_to_path_sup)[0]
                        top_10s = get_sup_stats(f"{sg_total_xpath}133]", add_to_path_sup)[1]
                    except:
                        sg_total = get_stats(f"{sg_total_xpat2}1]", add_to_path_stat_val)[0]
                        sg_total_rank = get_stats(f"{sg_total_xpat2}1]", add_to_path_stat_val)[1]
                        sg_total_total = get_sup_stats(f"{sg_total_xpat2}1]", add_to_path_sup)[0]
                        sg_total_m_rounds = get_sup_stats(f"{sg_total_xpat2}1]", add_to_path_sup)[1]
                        sg_tee_2_gr = get_stats(f"{sg_total_xpat2}2]", add_to_path_stat_val)[0]
                        sg_tee_2_gr_rank = get_stats(f"{sg_total_xpat2}2]", add_to_path_stat_val)[1]
                        sg_off_tee = get_stats(f"{sg_total_xpat2}3]", add_to_path_stat_val)[0]
                        sg_off_tee_rank = get_stats(f"{sg_total_xpat2}3]", add_to_path_stat_val)[1]
                        sg_off_tee_total = get_sup_stats(f"{sg_total_xpat2}3]", add_to_path_sup)[0]
                        sg_app_gr = get_stats(f"{sg_total_xpat2}4]", add_to_path_stat_val)[0]
                        sg_app_gr_rank = get_stats(f"{sg_total_xpat2}4]", add_to_path_stat_val)[1]
                        sg_app_gr_total = get_sup_stats(f"{sg_total_xpat2}4]", add_to_path_sup)[0]
                        sg_around_gr = get_stats(f"{sg_total_xpat2}5]", add_to_path_stat_val)[0]
                        sg_around_gr_rank = get_stats(f"{sg_total_xpat2}5]", add_to_path_stat_val)[1]
                        sg_around_gr_total = get_sup_stats(f"{sg_total_xpat2}5]", add_to_path_sup)[0]
                        sg_putting = get_stats(f"{sg_total_xpat2}6]", add_to_path_stat_val)[0]
                        sg_putting_rank = get_stats(f"{sg_total_xpat2}6]", add_to_path_stat_val)[1]
                        sg_putting_total = get_sup_stats(f"{sg_total_xpat2}6]", add_to_path_sup)[0]
                        total_driving = get_stats(f"{sg_total_xpat2}7]", add_to_path_stat_val)[0]
                        total_driving_rank = get_stats(f"{sg_total_xpat2}7]", add_to_path_stat_val)[1]
                        longest_drive = get_stats(f"{sg_total_xpat2}8]", add_to_path_stat_val)[0]
                        longest_drive_rank = get_stats(f"{sg_total_xpat2}8]", add_to_path_stat_val)[1]
                        longest_drive_tourney = get_sup_stats(f"{sg_total_xpat2}8]", add_to_path_sup)[0]
                        longest_drive_round = get_sup_stats(f"{sg_total_xpat2}8]", add_to_path_sup)[1]
                        driving_distance = get_stats(f"{sg_total_xpat2}9]", add_to_path_stat_val)[0]
                        driving_distance_rank = get_stats(f"{sg_total_xpat2}9]", add_to_path_stat_val)[1]
                        driving_distance_total = get_sup_stats(f"{sg_total_xpat2}9]", add_to_path_sup)[0]
                        driving_distance_total_drives = get_sup_stats(f"{sg_total_xpat2}9]", add_to_path_sup)[1]
                        driving_distance_all_drives = get_stats(f"{sg_total_xpat2}10]", add_to_path_stat_val)[0]
                        driving_distance_all_drives_rank = get_stats(f"{sg_total_xpat2}10]", add_to_path_stat_val)[1]
                        driving_distance_all_drives_total = get_sup_stats(f"{sg_total_xpat2}10]", add_to_path_sup)[0]
                        driving_distance_all_drives_total_drives = get_sup_stats(f"{sg_total_xpat2}10]", add_to_path_sup)[1]
                        driving_accuracy = get_stats(f"{sg_total_xpat2}11]", add_to_path_stat_val)[0]
                        driving_accuracy_rank = get_stats(f"{sg_total_xpat2}11]", add_to_path_stat_val)[1]
                        fairways_hit = get_sup_stats(f"{sg_total_xpat2}11]", add_to_path_sup)[0]
                        fairways_possible = get_sup_stats(f"{sg_total_xpat2}11]", add_to_path_sup)[1]
                        left_rough_tendency = get_stats(f"{sg_total_xpat2}12]", add_to_path_stat_val)[0]
                        left_rough_tendency_rank = get_stats(f"{sg_total_xpat2}12]", add_to_path_stat_val)[1]
                        left_rough_total = get_sup_stats(f"{sg_total_xpat2}12]", add_to_path_sup)[0]
                        left_rough_possible_fairways = get_sup_stats(f"{sg_total_xpat2}12]", add_to_path_sup)[1]
                        right_rough_tendency = get_stats(f"{sg_total_xpat2}13]", add_to_path_stat_val)[0]
                        right_rough_tendency_rank = get_stats(f"{sg_total_xpat2}13]", add_to_path_stat_val)[1]
                        right_rough_total = get_sup_stats(f"{sg_total_xpat2}13]", add_to_path_sup)[0]
                        right_rough_possible_fairways = get_sup_stats(f"{sg_total_xpat2}13]", add_to_path_sup)[1]
                        distance_from_edge_frwy = get_stats(f"{sg_total_xpat2}14]", add_to_path_stat_val)[0]
                        distance_from_edge_frwy_rank = get_stats(f"{sg_total_xpat2}14]", add_to_path_stat_val)[1]
                        distance_from_edge_frwy_total = get_sup_stats(f"{sg_total_xpat2}14]", add_to_path_sup)[0]
                        distance_from_edge_frwy_strokes = get_sup_stats(f"{sg_total_xpat2}14]", add_to_path_sup)[1]
                        club_head_speed = get_stats(f"{sg_total_xpat2}15]", add_to_path_stat_val)[0]
                        club_head_speed_rank = get_stats(f"{sg_total_xpat2}15]", add_to_path_stat_val)[1]
                        club_head_speed_total = get_sup_stats(f"{sg_total_xpat2}15]", add_to_path_sup)[0]
                        club_head_speed_attempts = get_sup_stats(f"{sg_total_xpat2}15]", add_to_path_sup)[1]
                        total_driving_efficiency = get_stats(f"{sg_total_xpat2}16]", add_to_path_stat_val)[0]
                        total_driving_efficiency_rank = get_stats(f"{sg_total_xpat2}16]", add_to_path_stat_val)[1]
                        carry_efficiency_rank = get_sup_stats(f"{sg_total_xpat2}16]", add_to_path_sup)[1]
                        greens_in_regulation_percent = get_stats(f"{sg_total_xpat2}17]", add_to_path_stat_val)[0]
                        greens_in_regulation_percent_rank = get_stats(f"{sg_total_xpat2}17]", add_to_path_stat_val)[1]
                        greens_hit = get_sup_stats(f"{sg_total_xpat2}17]", add_to_path_sup)[0]
                        greens_possible = get_sup_stats(f"{sg_total_xpat2}17]", add_to_path_sup)[1]
                        proximity_to_hole = get_stats(f"{sg_total_xpat2}18]", add_to_path_stat_val)[0]
                        proximity_to_hole_rank = get_stats(f"{sg_total_xpat2}18]", add_to_path_stat_val)[1]
                        proximity_to_hole_total_ft = get_sup_stats(f"{sg_total_xpat2}18]", add_to_path_sup)[0]
                        proximity_to_hole_total_att = get_sup_stats(f"{sg_total_xpat2}18]", add_to_path_sup)[1]
                        
                        approach_more_275_in = get_stats(f"{sg_total_xpat2}19]", add_to_path_stat_val)[0]
                        approach_more_275_rank = get_stats(f"{sg_total_xpat2}19]", add_to_path_stat_val)[1]
                        approach_more_275_total_ft = get_sup_stats(f"{sg_total_xpat2}19]", add_to_path_sup)[0]
                        approach_more_275_total_att = get_sup_stats(f"{sg_total_xpat2}19]", add_to_path_sup)[1]
                        
                        approach_250_275_in = get_stats(f"{sg_total_xpat2}20]", add_to_path_stat_val)[0]
                        approach_250_275_rank = get_stats(f"{sg_total_xpat2}20]", add_to_path_stat_val)[1]
                        approach_250_275_total_ft = get_sup_stats(f"{sg_total_xpat2}20]", add_to_path_sup)[0]
                        approach_250_275_total_att = get_sup_stats(f"{sg_total_xpat2}20]", add_to_path_sup)[1]
                        
                        approach_225_250_in = get_stats(f"{sg_total_xpat2}21]", add_to_path_stat_val)[0]
                        approach_225_250_rank = get_stats(f"{sg_total_xpat2}21]", add_to_path_stat_val)[1]
                        approach_225_250_total_ft = get_sup_stats(f"{sg_total_xpat2}21]", add_to_path_sup)[0]
                        approach_225_250_total_att = get_sup_stats(f"{sg_total_xpat2}21]", add_to_path_sup)[1]
                        
                        approach_200_225_in = get_stats(f"{sg_total_xpat2}22]", add_to_path_stat_val)[0]
                        approach_200_225_rank = get_stats(f"{sg_total_xpat2}22]", add_to_path_stat_val)[1]
                        approach_200_225_total_ft = get_sup_stats(f"{sg_total_xpat2}22]", add_to_path_sup)[0]
                        approach_200_225_total_att = get_sup_stats(f"{sg_total_xpat2}22]", add_to_path_sup)[1]
                        
                        approach_more_200_in = get_stats(f"{sg_total_xpat2}23]", add_to_path_stat_val)[0]
                        approach_more_200_rank = get_stats(f"{sg_total_xpat2}23]", add_to_path_stat_val)[1]
                        approach_more_200_total_ft = get_sup_stats(f"{sg_total_xpat2}23]", add_to_path_sup)[0]
                        approach_more_200_total_att = get_sup_stats(f"{sg_total_xpat2}23]", add_to_path_sup)[1]
                        
                        approach_175_200_in = get_stats(f"{sg_total_xpat2}24]", add_to_path_stat_val)[0]
                        approach_175_200_rank = get_stats(f"{sg_total_xpat2}24]", add_to_path_stat_val)[1]
                        approach_175_200_total_ft = get_sup_stats(f"{sg_total_xpat2}24]", add_to_path_sup)[0]
                        approach_175_200_total_att = get_sup_stats(f"{sg_total_xpat2}24]", add_to_path_sup)[1]
                        
                        approach_150_175_in = get_stats(f"{sg_total_xpat2}25]", add_to_path_stat_val)[0]
                        approach_150_175_rank = get_stats(f"{sg_total_xpat2}25]", add_to_path_stat_val)[1]
                        approach_150_175_total_ft = get_sup_stats(f"{sg_total_xpat2}25]", add_to_path_sup)[0]
                        approach_150_175_total_att = get_sup_stats(f"{sg_total_xpat2}25]", add_to_path_sup)[1]
                        
                        approach_125_150_in = get_stats(f"{sg_total_xpat2}26]", add_to_path_stat_val)[0]
                        approach_125_150_rank = get_stats(f"{sg_total_xpat2}26]", add_to_path_stat_val)[1]
                        approach_125_150_total_ft = get_sup_stats(f"{sg_total_xpat2}26]", add_to_path_sup)[0]
                        approach_125_150_total_att = get_sup_stats(f"{sg_total_xpat2}26]", add_to_path_sup)[1]
                        
                        approach_50_125_in = get_stats(f"{sg_total_xpat2}27]", add_to_path_stat_val)[0]
                        approach_50_125_rank = get_stats(f"{sg_total_xpat2}27]", add_to_path_stat_val)[1]
                        approach_50_125_total_ft = get_sup_stats(f"{sg_total_xpat2}27]", add_to_path_sup)[0]
                        approach_50_125_total_att = get_sup_stats(f"{sg_total_xpat2}27]", add_to_path_sup)[1]
                        
                        approach_100_125_in = get_stats(f"{sg_total_xpat2}28]", add_to_path_stat_val)[0]
                        approach_100_125_rank = get_stats(f"{sg_total_xpat2}28]", add_to_path_stat_val)[1]
                        approach_100_125_total_ft = get_sup_stats(f"{sg_total_xpat2}28]", add_to_path_sup)[0]
                        approach_100_125_total_att = get_sup_stats(f"{sg_total_xpat2}28]", add_to_path_sup)[1]
                        
                        approach_75_100_in = get_stats(f"{sg_total_xpat2}29]", add_to_path_stat_val)[0]
                        approach_75_100_rank = get_stats(f"{sg_total_xpat2}29]", add_to_path_stat_val)[1]
                        approach_75_100_total_ft = get_sup_stats(f"{sg_total_xpat2}29]", add_to_path_sup)[0]
                        approach_75_100_total_att = get_sup_stats(f"{sg_total_xpat2}29]", add_to_path_sup)[1]
                        
                        approach_50_75_in = get_stats(f"{sg_total_xpat2}30]", add_to_path_stat_val)[0]
                        approach_50_75_rank = get_stats(f"{sg_total_xpat2}30]", add_to_path_stat_val)[1]
                        approach_50_75_total_ft = get_sup_stats(f"{sg_total_xpat2}30]", add_to_path_sup)[0]
                        approach_50_75_total_att = get_sup_stats(f"{sg_total_xpat2}30]", add_to_path_sup)[1]
                        
                        approach_less_100_in = get_stats(f"{sg_total_xpat2}31]", add_to_path_stat_val)[0]
                        approach_less_100_rank = get_stats(f"{sg_total_xpat2}31]", add_to_path_stat_val)[1]
                        approach_less_100_total_ft = get_sup_stats(f"{sg_total_xpat2}31]", add_to_path_sup)[0]
                        approach_less_100_total_att = get_sup_stats(f"{sg_total_xpat2}31]", add_to_path_sup)[1]
                        
                        approach_more_100_in = get_stats(f"{sg_total_xpat2}32]", add_to_path_stat_val)[0]
                        approach_more_100_rank = get_stats(f"{sg_total_xpat2}32]", add_to_path_stat_val)[1]
                        approach_more_100_total_ft = get_sup_stats(f"{sg_total_xpat2}32]", add_to_path_sup)[0]
                        approach_more_100_total_att = get_sup_stats(f"{sg_total_xpat2}32]", add_to_path_sup)[1]
    
                        fairway_proximity = get_stats(f"{sg_total_xpat2}33]", add_to_path_stat_val)[0]
                        fairway_proximity_rank = get_stats(f"{sg_total_xpat2}33]", add_to_path_stat_val)[1]
                        fairway_proximity_att = get_sup_stats(f"{sg_total_xpat2}33]", add_to_path_sup)[1]
                        
                        rough_proximity = get_stats(f"{sg_total_xpat2}34]", add_to_path_stat_val)[0]
                        rough_proximity_rank = get_stats(f"{sg_total_xpat2}34]", add_to_path_stat_val)[1]
                        rough_proximity_total_in = get_sup_stats(f"{sg_total_xpat2}34]", add_to_path_sup)[0]
                        rough_proximity_total_att = get_sup_stats(f"{sg_total_xpat2}34]", add_to_path_sup)[1]
                        
                        left_rough_proximity = get_stats(f"{sg_total_xpat2}35]", add_to_path_stat_val)[0]
                        left_rough_proximity_rank = get_stats(f"{sg_total_xpat2}35]", add_to_path_stat_val)[1]
                        left_rough_proximity_att = get_sup_stats(f"{sg_total_xpat2}35]", add_to_path_sup)[1]
                        
                        right_rough_proximity = get_stats(f"{sg_total_xpat2}36]", add_to_path_stat_val)[0]
                        right_rough_proximity_rank = get_stats(f"{sg_total_xpat2}36]", add_to_path_stat_val)[1]
                        right_rough_proximity_att = get_sup_stats(f"{sg_total_xpat2}36]", add_to_path_sup)[1]
    
                        approach_more_275_rough_in = get_stats(f"{sg_total_xpat2}37]", add_to_path_stat_val)[0]
                        approach_more_275_rough_rank = get_stats(f"{sg_total_xpat2}37]", add_to_path_stat_val)[1]
                        approach_more_275_rough_total_ft = get_sup_stats(f"{sg_total_xpat2}37]", add_to_path_sup)[0]
                        approach_more_275_rough_total_att = get_sup_stats(f"{sg_total_xpat2}37]", add_to_path_sup)[1]
                        
                        approach_250_275_rough_in = get_stats(f"{sg_total_xpat2}38]", add_to_path_stat_val)[0]
                        approach_250_275_rough_rank = get_stats(f"{sg_total_xpat2}38]", add_to_path_stat_val)[1]
                        approach_250_275_rough_total_ft = get_sup_stats(f"{sg_total_xpat2}38]", add_to_path_sup)[0]
                        approach_250_275_rough_total_att = get_sup_stats(f"{sg_total_xpat2}38]", add_to_path_sup)[1]
                        
                        approach_225_250_rough_in = get_stats(f"{sg_total_xpat2}39]", add_to_path_stat_val)[0]
                        approach_225_250_rough_rank = get_stats(f"{sg_total_xpat2}39]", add_to_path_stat_val)[1]
                        approach_225_250_rough_total_ft = get_sup_stats(f"{sg_total_xpat2}39]", add_to_path_sup)[0]
                        approach_225_250_rough_total_att = get_sup_stats(f"{sg_total_xpat2}39]", add_to_path_sup)[1]
                        
                        approach_200_225_rough_in = get_stats(f"{sg_total_xpat2}40]", add_to_path_stat_val)[0]
                        approach_200_225_rough_rank = get_stats(f"{sg_total_xpat2}40]", add_to_path_stat_val)[1]
                        approach_200_225_rough_total_ft = get_sup_stats(f"{sg_total_xpat2}40]", add_to_path_sup)[0]
                        approach_200_225_rough_total_att = get_sup_stats(f"{sg_total_xpat2}40]", add_to_path_sup)[1]
                        
                        approach_more_100_rough_in = get_stats(f"{sg_total_xpat2}41]", add_to_path_stat_val)[0]
                        approach_more_100_rough_rank = get_stats(f"{sg_total_xpat2}41]", add_to_path_stat_val)[1]
                        approach_more_100_rough_total_ft = get_sup_stats(f"{sg_total_xpat2}41]", add_to_path_sup)[0]
                        approach_more_100_rough_total_att = get_sup_stats(f"{sg_total_xpat2}41]", add_to_path_sup)[1]
                        
                        approach_less_100_rough_in = get_stats(f"{sg_total_xpat2}42]", add_to_path_stat_val)[0]
                        approach_less_100_rough_rank = get_stats(f"{sg_total_xpat2}42]", add_to_path_stat_val)[1]
                        approach_less_100_rough_total_ft = get_sup_stats(f"{sg_total_xpat2}42]", add_to_path_sup)[0]
                        approach_less_100_rough_total_att = get_sup_stats(f"{sg_total_xpat2}42]", add_to_path_sup)[1]
                        
                        approach_more_200_rough_in = get_stats(f"{sg_total_xpat2}43]", add_to_path_stat_val)[0]
                        approach_more_200_rough_rank = get_stats(f"{sg_total_xpat2}43]", add_to_path_stat_val)[1]
                        approach_more_200_rough_total_ft = get_sup_stats(f"{sg_total_xpat2}43]", add_to_path_sup)[0]
                        approach_more_200_rough_total_att = get_sup_stats(f"{sg_total_xpat2}43]", add_to_path_sup)[1]
                        
                        approach_175_200_rough_in = get_stats(f"{sg_total_xpat2}44]", add_to_path_stat_val)[0]
                        approach_175_200_rough_rank = get_stats(f"{sg_total_xpat2}44]", add_to_path_stat_val)[1]
                        approach_175_200_rough_total_ft = get_sup_stats(f"{sg_total_xpat2}44]", add_to_path_sup)[0]
                        approach_175_200_rough_total_att = get_sup_stats(f"{sg_total_xpat2}44]", add_to_path_sup)[1]
                        
                        approach_150_175_rough_in = get_stats(f"{sg_total_xpat2}45]", add_to_path_stat_val)[0]
                        approach_150_175_rough_rank = get_stats(f"{sg_total_xpat2}45]", add_to_path_stat_val)[1]
                        approach_150_175_rough_total_ft = get_sup_stats(f"{sg_total_xpat2}45]", add_to_path_sup)[0]
                        approach_150_175_rough_total_att = get_sup_stats(f"{sg_total_xpat2}45]", add_to_path_sup)[1]
                        
                        approach_125_150_rough_in = get_stats(f"{sg_total_xpat2}46]", add_to_path_stat_val)[0]
                        approach_125_150_rough_rank = get_stats(f"{sg_total_xpat2}46]", add_to_path_stat_val)[1]
                        approach_125_150_rough_total_ft = get_sup_stats(f"{sg_total_xpat2}46]", add_to_path_sup)[0]
                        approach_125_150_rough_total_att = get_sup_stats(f"{sg_total_xpat2}46]", add_to_path_sup)[1]
                        
                        approach_50_125_rough_in = get_stats(f"{sg_total_xpat2}47]", add_to_path_stat_val)[0]
                        approach_50_125_rough_rank = get_stats(f"{sg_total_xpat2}47]", add_to_path_stat_val)[1]
                        approach_50_125_rough_total_ft = get_sup_stats(f"{sg_total_xpat2}47]", add_to_path_sup)[0]
                        approach_50_125_rough_total_att = get_sup_stats(f"{sg_total_xpat2}47]", add_to_path_sup)[1]
                        
                        approach_100_125_rough_in = get_stats(f"{sg_total_xpat2}48]", add_to_path_stat_val)[0]
                        approach_100_125_rough_rank = get_stats(f"{sg_total_xpat2}48]", add_to_path_stat_val)[1]
                        approach_100_125_rough_total_ft = get_sup_stats(f"{sg_total_xpat2}48]", add_to_path_sup)[0]
                        approach_100_125_rough_total_att = get_sup_stats(f"{sg_total_xpat2}48]", add_to_path_sup)[1]
                        
                        approach_75_100_rough_in = get_stats(f"{sg_total_xpat2}49]", add_to_path_stat_val)[0]
                        approach_75_100_rough_rank = get_stats(f"{sg_total_xpat2}49]", add_to_path_stat_val)[1]
                        approach_75_100_rough_total_ft = get_sup_stats(f"{sg_total_xpat2}49]", add_to_path_sup)[0]
                        approach_75_100_rough_total_att = get_sup_stats(f"{sg_total_xpat2}49]", add_to_path_sup)[1]
                        
                        approach_50_75_rough_in = get_stats(f"{sg_total_xpat2}50]", add_to_path_stat_val)[0]
                        approach_50_75_rough_rank = get_stats(f"{sg_total_xpat2}50]", add_to_path_stat_val)[1]
                        approach_50_75_rough_total_ft = get_sup_stats(f"{sg_total_xpat2}50]", add_to_path_sup)[0]
                        approach_50_75_rough_total_att = get_sup_stats(f"{sg_total_xpat2}50]", add_to_path_sup)[1]
                        
                        going_for_green_percent = get_stats(f"{sg_total_xpat2}51]", add_to_path_stat_val)[0]
                        going_for_green_percent_rank = get_stats(f"{sg_total_xpat2}51]", add_to_path_stat_val)[1]
                        going_for_green_percent_attempts = get_sup_stats(f"{sg_total_xpat2}51]", add_to_path_sup)[0]
                        going_for_green_percent_non_attemptes = get_sup_stats(f"{sg_total_xpat2}51]", add_to_path_sup)[1]
                        
                        going_for_green_hit_percent = get_stats(f"{sg_total_xpat2}52]", add_to_path_stat_val)[0]
                        going_for_green_hit_rank = get_stats(f"{sg_total_xpat2}52]", add_to_path_stat_val)[1]
                        going_for_green_hit = get_sup_stats(f"{sg_total_xpat2}52]", add_to_path_sup)[0]
                        going_for_green_attempts = get_sup_stats(f"{sg_total_xpat2}52]", add_to_path_sup)[1]
                        
                        going_for_green_birdie_better_pct = get_stats(f"{sg_total_xpat2}53]", add_to_path_stat_val)[0]
                        going_for_green_birdie_better_pct_rank = get_stats(f"{sg_total_xpat2}53]", add_to_path_stat_val)[1]
                        going_for_green_birdie_better_total = get_sup_stats(f"{sg_total_xpat2}53]", add_to_path_sup)[0]
                        
                        total_hole_outs = get_stats(f"{sg_total_xpat2}54]", add_to_path_stat_val)[0]
                        total_hole_outs_rank = get_stats(f"{sg_total_xpat2}54]", add_to_path_stat_val)[1]
                        
                        
                        
                        
                        longest_hole_out_yrds = get_stats(f"{sg_total_xpat2}55]", add_to_path_stat_val)[0]
                        longest_hole_out_rank = get_stats(f"{sg_total_xpat2}55]", add_to_path_stat_val)[1]
                        longest_hole_out_tourney = get_sup_stats(f"{sg_total_xpat2}55]", add_to_path_sup)[0]
                        longest_hole_out_rd = get_sup_stats(f"{sg_total_xpat2}55]", add_to_path_sup)[1]
                        
                        scrambling_percent = get_stats(f"{sg_total_xpat2}56]", add_to_path_stat_val)[0]
                        scrambling_rank = get_stats(f"{sg_total_xpat2}56]", add_to_path_stat_val)[1]
                        scrambling_par_or_better = get_sup_stats(f"{sg_total_xpat2}56]", add_to_path_sup)[0]
                        scrambling_missed_gir = get_sup_stats(f"{sg_total_xpat2}56]", add_to_path_sup)[1]
                        
                        scrambling_from_rough_perecnt = get_stats(f"{sg_total_xpat2}57]", add_to_path_stat_val)[0]
                        scrambling_from_rough_rank = get_stats(f"{sg_total_xpat2}57]", add_to_path_stat_val)[1]
                        scrambling_from_rough_success = get_sup_stats(f"{sg_total_xpat2}57]", add_to_path_sup)[0]
                        scrambling_from_rough_att = get_sup_stats(f"{sg_total_xpat2}57]", add_to_path_sup)[1]
                        
                        scrambling_from_fringe_percent = get_stats(f"{sg_total_xpat2}58]", add_to_path_stat_val)[0]
                        scrambling_from_fringe_rank = get_stats(f"{sg_total_xpat2}58]", add_to_path_stat_val)[1]
                        scrambling_from_fringe_success = get_sup_stats(f"{sg_total_xpat2}58]", add_to_path_sup)[0]
                        scrambling_from_fringe_att = get_sup_stats(f"{sg_total_xpat2}58]", add_to_path_sup)[1]
                        
                        scrambling_more_30_percent = get_stats(f"{sg_total_xpat2}59]", add_to_path_stat_val)[0]
                        scrambling_more_30_rank = get_stats(f"{sg_total_xpat2}59]", add_to_path_stat_val)[1]
                        scrambling_more_30_success = get_sup_stats(f"{sg_total_xpat2}59]", add_to_path_sup)[0]
                        scrambling_more_30_att = get_sup_stats(f"{sg_total_xpat2}59]", add_to_path_sup)[1]
                        
                        scrambling_20_30_percent = get_stats(f"{sg_total_xpat2}60]", add_to_path_stat_val)[0]
                        scrambling_20_30_rank = get_stats(f"{sg_total_xpat2}60]", add_to_path_stat_val)[1]
                        scrambling_20_30_success = get_sup_stats(f"{sg_total_xpat2}60]", add_to_path_sup)[0]
                        scrambling_20_30_att = get_sup_stats(f"{sg_total_xpat2}60]", add_to_path_sup)[1]
                        
                        scrambling_10_20_percent = get_stats(f"{sg_total_xpat2}61]", add_to_path_stat_val)[0]
                        scrambling_10_20_rank = get_stats(f"{sg_total_xpat2}61]", add_to_path_stat_val)[1]
                        scrambling_10_20_success = get_sup_stats(f"{sg_total_xpat2}61]", add_to_path_sup)[0]
                        scrambling_10_20_att = get_sup_stats(f"{sg_total_xpat2}61]", add_to_path_sup)[1]
                        
                        scrambling_less_10_percent = get_stats(f"{sg_total_xpat2}62]", add_to_path_stat_val)[0]
                        scrambling_less_10_rank = get_stats(f"{sg_total_xpat2}62]", add_to_path_stat_val)[1]
                        scrambling_less_10_success = get_sup_stats(f"{sg_total_xpat2}62]", add_to_path_sup)[0]
                        scrambling_less_10_att = get_sup_stats(f"{sg_total_xpat2}62]", add_to_path_sup)[1]
                        
                        sand_save_percent = get_stats(f"{sg_total_xpat2}63]", add_to_path_stat_val)[0]
                        sand_save_rank = get_stats(f"{sg_total_xpat2}63]", add_to_path_stat_val)[1]
                        sand_save_saves = get_sup_stats(f"{sg_total_xpat2}63]", add_to_path_sup)[0]
                        sand_save_bunkers = get_sup_stats(f"{sg_total_xpat2}63]", add_to_path_sup)[1]
                        
                        proximity_to_hole_sand = get_stats(f"{sg_total_xpat2}64]", add_to_path_stat_val)[0]
                        proximity_to_hole_sand_rank = get_stats(f"{sg_total_xpat2}64]", add_to_path_stat_val)[1]
                        proximity_to_hole_sand_total_ft = get_sup_stats(f"{sg_total_xpat2}64]", add_to_path_sup)[0]
                        proximity_to_hole_sand_shots = get_sup_stats(f"{sg_total_xpat2}64]", add_to_path_sup)[1]
                        
                        total_putting = get_stats(f"{sg_total_xpat2}65]", add_to_path_stat_val)[0]
                        total_putting_rank = get_stats(f"{sg_total_xpat2}65]", add_to_path_stat_val)[1]
                        
                        putting_avg = get_stats(f"{sg_total_xpat2}66]", add_to_path_stat_val)[0]
                        putting_avg_rank = get_stats(f"{sg_total_xpat2}66]", add_to_path_stat_val)[1]
                        putting_avg_gir_putts = get_sup_stats(f"{sg_total_xpat2}66]", add_to_path_sup)[0]
                        putting_avg_greens_hit = get_sup_stats(f"{sg_total_xpat2}66]", add_to_path_sup)[1]
                        
                        overall_putting_avg = get_stats(f"{sg_total_xpat2}67]", add_to_path_stat_val)[0]
                        overall_putting_avg_rank = get_stats(f"{sg_total_xpat2}67]", add_to_path_stat_val)[1]
                        overall_putting_total_putts = get_sup_stats(f"{sg_total_xpat2}67]", add_to_path_sup)[0]
                        overall_putting_total_holes = get_sup_stats(f"{sg_total_xpat2}67]", add_to_path_sup)[1]
                        
                        birdie_or_better_conversion_percent = get_stats(f"{sg_total_xpat2}68]", add_to_path_stat_val)[0]
                        birdie_or_better_conversion_rank = get_stats(f"{sg_total_xpat2}68]", add_to_path_stat_val)[1]
                        birdie_or_better_conversion_birdies = get_sup_stats(f"{sg_total_xpat2}68]", add_to_path_sup)[0]
                        birdie_or_better_conversion_greens_hit = get_sup_stats(f"{sg_total_xpat2}68]", add_to_path_sup)[1]
                        
                        putts_per_round = get_stats(f"{sg_total_xpat2}69]", add_to_path_stat_val)[0]
                        putts_per_round_rank = get_stats(f"{sg_total_xpat2}69]", add_to_path_stat_val)[1]
                        total_putts = get_sup_stats(f"{sg_total_xpat2}69]", add_to_path_sup)[0]
                        total_rounds = get_sup_stats(f"{sg_total_xpat2}69]", add_to_path_sup)[1]
                        
                        putts_per_round_rd1 = get_stats(f"{sg_total_xpat2}70]", add_to_path_stat_val)[0]
                        putts_per_round_rd1_rank = get_stats(f"{sg_total_xpat2}70]", add_to_path_stat_val)[1]
                        total_putts_rd1 = get_sup_stats(f"{sg_total_xpat2}70]", add_to_path_sup)[0]
                        total_rounds_rd1 = get_sup_stats(f"{sg_total_xpat2}70]", add_to_path_sup)[1]
                        
                        putts_per_round_rd2 = get_stats(f"{sg_total_xpat2}71]", add_to_path_stat_val)[0]
                        putts_per_round_rd2_rank = get_stats(f"{sg_total_xpat2}71]", add_to_path_stat_val)[1]
                        total_putts_rd2 = get_sup_stats(f"{sg_total_xpat2}71]", add_to_path_sup)[0]
                        total_rounds_rd2 = get_sup_stats(f"{sg_total_xpat2}71]", add_to_path_sup)[1]
                        
                        putts_per_round_rd3 = get_stats(f"{sg_total_xpat2}72]", add_to_path_stat_val)[0]
                        putts_per_round_rd3_rank = get_stats(f"{sg_total_xpat2}72]", add_to_path_stat_val)[1]
                        total_putts_rd3 = get_sup_stats(f"{sg_total_xpat2}72]", add_to_path_sup)[0]
                        total_rounds_rd3 = get_sup_stats(f"{sg_total_xpat2}72]", add_to_path_sup)[1]
                        
                        putts_per_round_rd4 = get_stats(f"{sg_total_xpat2}73]", add_to_path_stat_val)[0]
                        putts_per_round_rd4_rank = get_stats(f"{sg_total_xpat2}73]", add_to_path_stat_val)[1]
                        total_putts_rd4 = get_sup_stats(f"{sg_total_xpat2}73]", add_to_path_sup)[0]
                        total_rounds_rd4 = get_sup_stats(f"{sg_total_xpat2}73]", add_to_path_sup)[1]
                        
                        one_putt_percentage = get_stats(f"{sg_total_xpat2}74]", add_to_path_stat_val)[0]
                        one_putt_rank = get_stats(f"{sg_total_xpat2}74]", add_to_path_stat_val)[1]
                        one_putt_total = get_sup_stats(f"{sg_total_xpat2}74]", add_to_path_sup)[0]
                        one_putt_total_holes = get_sup_stats(f"{sg_total_xpat2}74]", add_to_path_sup)[1]
                        
                        longest_putt = get_stats(f"{sg_total_xpat2}75]", add_to_path_stat_val)[0]
                        longest_putt_break = get_stats(f"{sg_total_xpat2}75]", add_to_path_stat_val)[1]
                        longest_putt_tourney = get_sup_stats(f"{sg_total_xpat2}75]", add_to_path_sup)[0]
                        longest_putt_rd = get_sup_stats(f"{sg_total_xpat2}75]", add_to_path_sup)[1]
                        
                        three_putt_avoidance = get_stats(f"{sg_total_xpat2}76]", add_to_path_stat_val)[0]
                        three_putt_avoidance_rank = get_stats(f"{sg_total_xpat2}76]", add_to_path_stat_val)[1]
                        three_putt_total = get_sup_stats(f"{sg_total_xpat2}76]", add_to_path_sup)[0]
                        three_putt_total_holes = get_sup_stats(f"{sg_total_xpat2}76]", add_to_path_sup)[1]
                        
                        putting_more_25_percent = get_stats(f"{sg_total_xpat2}77]", add_to_path_stat_val)[0]
                        putting_more_25_rank = get_stats(f"{sg_total_xpat2}77]", add_to_path_stat_val)[1]
                        putting_more_25_att = get_sup_stats(f"{sg_total_xpat2}77]", add_to_path_sup)[0]
                        putting_more_25_made = get_sup_stats(f"{sg_total_xpat2}77]", add_to_path_sup)[1]
                        
                        putting_20_25_percent = get_stats(f"{sg_total_xpat2}78]", add_to_path_stat_val)[0]
                        putting_20_25_rank = get_stats(f"{sg_total_xpat2}78]", add_to_path_stat_val)[1]
                        putting_20_25_att = get_sup_stats(f"{sg_total_xpat2}78]", add_to_path_sup)[0]
                        putting_20_25_made = get_sup_stats(f"{sg_total_xpat2}78]", add_to_path_sup)[1]
                        
                        putting_15_20_percent = get_stats(f"{sg_total_xpat2}79]", add_to_path_stat_val)[0]
                        putting_15_20_rank = get_stats(f"{sg_total_xpat2}79]", add_to_path_stat_val)[1]
                        putting_15_20_att = get_sup_stats(f"{sg_total_xpat2}79]", add_to_path_sup)[0]
                        putting_15_20_made = get_sup_stats(f"{sg_total_xpat2}79]", add_to_path_sup)[1]
                        
                        putting_10_15_percent = get_stats(f"{sg_total_xpat2}80]", add_to_path_stat_val)[0]
                        putting_10_15_rank = get_stats(f"{sg_total_xpat2}80]", add_to_path_stat_val)[1]
                        putting_10_15_att = get_sup_stats(f"{sg_total_xpat2}80]", add_to_path_sup)[0]
                        putting_10_15_made = get_sup_stats(f"{sg_total_xpat2}80]", add_to_path_sup)[1]
                        
                        putting_less_10_percent = get_stats(f"{sg_total_xpat2}81]", add_to_path_stat_val)[0]
                        putting_less_10_rank = get_stats(f"{sg_total_xpat2}81]", add_to_path_stat_val)[1]
                        putting_less_10_att = get_sup_stats(f"{sg_total_xpat2}81]", add_to_path_sup)[0]
                        putting_less_10_made = get_sup_stats(f"{sg_total_xpat2}81]", add_to_path_sup)[1]
                        
                        putting_from_10_percent = get_stats(f"{sg_total_xpat2}82]", add_to_path_stat_val)[0]
                        putting_from_10_rank = get_stats(f"{sg_total_xpat2}82]", add_to_path_stat_val)[1]
                        putting_from_10_att = get_sup_stats(f"{sg_total_xpat2}82]", add_to_path_sup)[0]
                        
                        putting_from_9_percent = get_stats(f"{sg_total_xpat2}83]", add_to_path_stat_val)[0]
                        putting_from_9_rank = get_stats(f"{sg_total_xpat2}83]", add_to_path_stat_val)[1]
                        putting_from_9_att = get_sup_stats(f"{sg_total_xpat2}83]", add_to_path_sup)[0]
                        
                        putting_from_8_percent = get_stats(f"{sg_total_xpat2}84]", add_to_path_stat_val)[0]
                        putting_from_8_rank = get_stats(f"{sg_total_xpat2}84]", add_to_path_stat_val)[1]
                        putting_from_8_att = get_sup_stats(f"{sg_total_xpat2}84]", add_to_path_sup)[0]
                        
                        putting_from_7_percent = get_stats(f"{sg_total_xpat2}85]", add_to_path_stat_val)[0]
                        putting_from_7_rank = get_stats(f"{sg_total_xpat2}85]", add_to_path_stat_val)[1]
                        putting_from_7_att = get_sup_stats(f"{sg_total_xpat2}85]", add_to_path_sup)[0]
                        
                        putting_from_6_percent = get_stats(f"{sg_total_xpat2}86]", add_to_path_stat_val)[0]
                        putting_from_6_rank = get_stats(f"{sg_total_xpat2}86]", add_to_path_stat_val)[1]
                        putting_from_6_att = get_sup_stats(f"{sg_total_xpat2}86]", add_to_path_sup)[0]
                        
                        putting_from_5_percent = get_stats(f"{sg_total_xpat2}87]", add_to_path_stat_val)[0]
                        putting_from_5_rank = get_stats(f"{sg_total_xpat2}87]", add_to_path_stat_val)[1]
                        putting_from_5_att = get_sup_stats(f"{sg_total_xpat2}87]", add_to_path_sup)[0]
                        
                        putting_from_4_8_percent = get_stats(f"{sg_total_xpat2}88]", add_to_path_stat_val)[0]
                        putting_from_4_8_rank = get_stats(f"{sg_total_xpat2}88]", add_to_path_stat_val)[1]
                        putting_from_4_8_att = get_sup_stats(f"{sg_total_xpat2}88]", add_to_path_sup)[0]
                        putting_from_4_8_made = get_sup_stats(f"{sg_total_xpat2}88]", add_to_path_sup)[1]
                        
                        putting_from_4_percent = get_stats(f"{sg_total_xpat2}89]", add_to_path_stat_val)[0]
                        putting_from_4_rank = get_stats(f"{sg_total_xpat2}89]", add_to_path_stat_val)[1]
                        putting_from_4_att = get_sup_stats(f"{sg_total_xpat2}89]", add_to_path_sup)[0]
                        
                        putting_from_3_percent = get_stats(f"{sg_total_xpat2}90]", add_to_path_stat_val)[0]
                        putting_from_3_rank = get_stats(f"{sg_total_xpat2}90]", add_to_path_stat_val)[1]
                        putting_from_3_att = get_sup_stats(f"{sg_total_xpat2}90]", add_to_path_sup)[0]
                        
                        avg_distance_putts_made = get_stats(f"{sg_total_xpat2}91]", add_to_path_stat_val)[0]
                        avg_distance_putts_made_rank = get_stats(f"{sg_total_xpat2}91]", add_to_path_stat_val)[1]
                        avg_distance_putts_made_in = get_sup_stats(f"{sg_total_xpat2}91]", add_to_path_sup)[0]
                        avg_distance_putts_made_rounds = get_sup_stats(f"{sg_total_xpat2}91]", add_to_path_sup)[1]
                        
                        approach_putt_performance = get_stats(f"{sg_total_xpat2}92]", add_to_path_stat_val)[0]
                        approach_putt_rank = get_stats(f"{sg_total_xpat2}92]", add_to_path_stat_val)[1]
                        approach_putt_att = get_sup_stats(f"{sg_total_xpat2}92]", add_to_path_sup)[1]
                        
                        scoring_avg_adj = get_stats(f"{sg_total_xpat2}93]", add_to_path_stat_val)[0]
                        scoring_avg_adj_rank = get_stats(f"{sg_total_xpat2}93]", add_to_path_stat_val)[1]
                        scoring_avg_adj_total_strokes = get_sup_stats(f"{sg_total_xpat2}93]", add_to_path_sup)[0]
                        scoring_avg_adj_total_adjustment = get_sup_stats(f"{sg_total_xpat2}93]", add_to_path_sup)[1]
                        
                        scoring_avg_actual = get_stats(f"{sg_total_xpat2}94]", add_to_path_stat_val)[0]
                        scoring_avg_actual_rank = get_stats(f"{sg_total_xpat2}94]", add_to_path_stat_val)[1]
                        scoring_avg_actual_total_strokes = get_sup_stats(f"{sg_total_xpat2}94]", add_to_path_sup)[0]
                        scoring_avg_actual_total_rounds = get_sup_stats(f"{sg_total_xpat2}94]", add_to_path_sup)[1]
                        
                        lowest_round = get_stats(f"{sg_total_xpat2}95]", add_to_path_stat_val)[0]
                        lowest_round_rank = get_stats(f"{sg_total_xpat2}95]", add_to_path_stat_val)[1]
                        lowest_round_tourney = get_sup_stats(f"{sg_total_xpat2}95]", add_to_path_sup)[0]
                        lowest_round_round = get_sup_stats(f"{sg_total_xpat2}95]", add_to_path_sup)[1]
                        
                        birdie_avg = get_stats(f"{sg_total_xpat2}96]", add_to_path_stat_val)[0]
                        birdie_avg_rank = get_stats(f"{sg_total_xpat2}96]", add_to_path_stat_val)[1]
                        birdie_avg_num_birdies = get_sup_stats(f"{sg_total_xpat2}96]", add_to_path_sup)[0]
                        birdie_avg_total_rounds = get_sup_stats(f"{sg_total_xpat2}96]", add_to_path_sup)[1]
                        
                        total_birdies = get_stats(f"{sg_total_xpat2}97]", add_to_path_stat_val)[0]
                        total_birdies_rank = get_stats(f"{sg_total_xpat2}97]", add_to_path_stat_val)[1]
                        
                        eagles_holes_per = get_stats(f"{sg_total_xpat2}98]", add_to_path_stat_val)[0]
                        eagles_holes_per_rank = get_stats(f"{sg_total_xpat2}98]", add_to_path_stat_val)[1]
                        
                        total_eagles = get_stats(f"{sg_total_xpat2}99]", add_to_path_stat_val)[0]
                        total_eagles_rank = get_stats(f"{sg_total_xpat2}99]", add_to_path_stat_val)[1]
                        
                        par_breaker_percent = get_stats(f"{sg_total_xpat2}100]", add_to_path_stat_val)[0]
                        par_breaker_rank = get_stats(f"{sg_total_xpat2}100]", add_to_path_stat_val)[1]
                        
                        bounce_back_percent = get_stats(f"{sg_total_xpat2}101]", add_to_path_stat_val)[0]
                        bounce_back_rank = get_stats(f"{sg_total_xpat2}101]", add_to_path_stat_val)[1]
                        
                        par3_birdie_or_better = get_stats(f"{sg_total_xpat2}102]", add_to_path_stat_val)[0]
                        par3_birdie_or_better_rank = get_stats(f"{sg_total_xpat2}102]", add_to_path_stat_val)[1]
                        par3_birdie_or_better_total = get_sup_stats(f"{sg_total_xpat2}102]", add_to_path_sup)[0]
                        par3_holes = get_sup_stats(f"{sg_total_xpat2}102]", add_to_path_sup)[1]
                        
                        par4_birdie_or_better = get_stats(f"{sg_total_xpat2}103]", add_to_path_stat_val)[0]
                        par4_birdie_or_better_rank = get_stats(f"{sg_total_xpat2}103]", add_to_path_stat_val)[1]
                        par4_birdie_or_better_total = get_sup_stats(f"{sg_total_xpat2}103]", add_to_path_sup)[0]
                        par4_holes = get_sup_stats(f"{sg_total_xpat2}103]", add_to_path_sup)[1]
                        
                        par5_birdie_or_better = get_stats(f"{sg_total_xpat2}104]", add_to_path_stat_val)[0]
                        par5_birdie_or_better_rank = get_stats(f"{sg_total_xpat2}104]", add_to_path_stat_val)[1]
                        par5_birdie_or_better_total = get_sup_stats(f"{sg_total_xpat2}104]", add_to_path_sup)[0]
                        par5_holes = get_sup_stats(f"{sg_total_xpat2}104]", add_to_path_sup)[1]
                        
                        birdie_or_better_percent = get_stats(f"{sg_total_xpat2}105]", add_to_path_stat_val)[0]
                        birdie_or_better_rank = get_stats(f"{sg_total_xpat2}105]", add_to_path_stat_val)[1]
                        
                        bogey_avoidance_percent = get_stats(f"{sg_total_xpat2}106]", add_to_path_stat_val)[0]
                        bogey_avoidance_rank = get_stats(f"{sg_total_xpat2}106]", add_to_path_stat_val)[1]
                        bogey_total = get_sup_stats(f"{sg_total_xpat2}106]", add_to_path_sup)[0]
                        
                        final_round_scoring_avg = get_stats(f"{sg_total_xpat2}107]", add_to_path_stat_val)[0]
                        final_round_scoring_avg_rank = get_stats(f"{sg_total_xpat2}107]", add_to_path_stat_val)[1]
                        final_round_scoring_total_strokes = get_sup_stats(f"{sg_total_xpat2}107]", add_to_path_sup)[0]
                        final_round_scoring_total_rds = get_sup_stats(f"{sg_total_xpat2}107]", add_to_path_sup)[1]
                        
                        final_round_performance = get_stats(f"{sg_total_xpat2}108]", add_to_path_stat_val)[0]
                        final_round_performance_rank = get_stats(f"{sg_total_xpat2}108]", add_to_path_stat_val)[1]
                        
                        rd1_scoring_avg = get_stats(f"{sg_total_xpat2}109]", add_to_path_stat_val)[0]
                        rd1_scoring_avg_rank = get_stats(f"{sg_total_xpat2}109]", add_to_path_stat_val)[1]
                        rd1_scoring_total_strokes = get_sup_stats(f"{sg_total_xpat2}109]", add_to_path_sup)[0]
                        rd1_scoring_total_rds = get_sup_stats(f"{sg_total_xpat2}109]", add_to_path_sup)[1]
                        
                        rd2_scoring_avg = get_stats(f"{sg_total_xpat2}110]", add_to_path_stat_val)[0]
                        rd2_scoring_avg_rank = get_stats(f"{sg_total_xpat2}110]", add_to_path_stat_val)[1]
                        rd2_scoring_total_strokes = get_sup_stats(f"{sg_total_xpat2}110]", add_to_path_sup)[0]
                        rd2_scoring_total_rds = get_sup_stats(f"{sg_total_xpat2}110]", add_to_path_sup)[1]
                        
                        rd3_scoring_avg = get_stats(f"{sg_total_xpat2}111]", add_to_path_stat_val)[0]
                        rd3_scoring_avg_rank = get_stats(f"{sg_total_xpat2}111]", add_to_path_stat_val)[1]
                        rd3_scoring_total_strokes = get_sup_stats(f"{sg_total_xpat2}111]", add_to_path_sup)[0]
                        rd3_scoring_total_rds = get_sup_stats(f"{sg_total_xpat2}111]", add_to_path_sup)[1]
                        
                        rd4_scoring_avg = get_stats(f"{sg_total_xpat2}112]", add_to_path_stat_val)[0]
                        rd4_scoring_avg_rank = get_stats(f"{sg_total_xpat2}112]", add_to_path_stat_val)[1]
                        rd4_scoring_total_strokes = get_sup_stats(f"{sg_total_xpat2}112]", add_to_path_sup)[0]
                        rd4_scoring_total_rds = get_sup_stats(f"{sg_total_xpat2}112]", add_to_path_sup)[1]
                        
                        par3_scoring_avg = get_stats(f"{sg_total_xpat2}113]", add_to_path_stat_val)[0]
                        par3_scoring_avg_rank = get_stats(f"{sg_total_xpat2}113]", add_to_path_stat_val)[1]
                        par3_scoring_avg_strokes = get_sup_stats(f"{sg_total_xpat2}113]", add_to_path_sup)[0]
                        par3_scoring_avg_holes = get_sup_stats(f"{sg_total_xpat2}113]", add_to_path_sup)[1]
                        
                        par4_scoring_avg = get_stats(f"{sg_total_xpat2}114]", add_to_path_stat_val)[0]
                        par4_scoring_avg_rank = get_stats(f"{sg_total_xpat2}114]", add_to_path_stat_val)[1]
                        par4_scoring_avg_strokes = get_sup_stats(f"{sg_total_xpat2}114]", add_to_path_sup)[0]
                        par4_scoring_avg_holes = get_sup_stats(f"{sg_total_xpat2}114]", add_to_path_sup)[1]
                        
                        par5_scoring_avg = get_stats(f"{sg_total_xpat2}115]", add_to_path_stat_val)[0]
                        par5_scoring_avg_rank = get_stats(f"{sg_total_xpat2}115]", add_to_path_stat_val)[1]
                        par5_scoring_avg_strokes = get_sup_stats(f"{sg_total_xpat2}115]", add_to_path_sup)[0]
                        par5_scoring_avg_holes = get_sup_stats(f"{sg_total_xpat2}115]", add_to_path_sup)[1]
                        
                        front9_scoring_avg = get_stats(f"{sg_total_xpat2}116]", add_to_path_stat_val)[0]
                        front9_scoring_avg_rank = get_stats(f"{sg_total_xpat2}116]", add_to_path_stat_val)[1]
                        front9_scoring_avg_strokes = get_sup_stats(f"{sg_total_xpat2}116]", add_to_path_sup)[0]
                        front9_scoring_avg_holes = get_sup_stats(f"{sg_total_xpat2}116]", add_to_path_sup)[1]
                        
                        back9_scoring_avg = get_stats(f"{sg_total_xpat2}117]", add_to_path_stat_val)[0]
                        back9_scoring_avg_rank = get_stats(f"{sg_total_xpat2}117]", add_to_path_stat_val)[1]
                        back9_scoring_avg_strokes = get_sup_stats(f"{sg_total_xpat2}117]", add_to_path_sup)[0]
                        back9_scoring_avg_holes = get_sup_stats(f"{sg_total_xpat2}117]", add_to_path_sup)[1]
                        
                        early_scoring_avg = get_stats(f"{sg_total_xpat2}118]", add_to_path_stat_val)[0]
                        early_scoring_avg_rank = get_stats(f"{sg_total_xpat2}118]", add_to_path_stat_val)[1]
                        early_scoring_total_strokes = get_sup_stats(f"{sg_total_xpat2}118]", add_to_path_sup)[0]
                        early_scoring_total_rounds = get_sup_stats(f"{sg_total_xpat2}118]", add_to_path_sup)[1]
                        
                        late_scoring_avg = get_stats(f"{sg_total_xpat2}119]", add_to_path_stat_val)[0]
                        late_scoring_avg_rank = get_stats(f"{sg_total_xpat2}119]", add_to_path_stat_val)[1]
                        late_scoring_total_strokes = get_sup_stats(f"{sg_total_xpat2}119]", add_to_path_sup)[0]
                        late_scoring_total_rounds = get_sup_stats(f"{sg_total_xpat2}119]", add_to_path_sup)[1]
                        
                        consecutive_cuts = get_stats(f"{sg_total_xpat2}120]", add_to_path_stat_val)[0]
                        consecutive_cuts_rank = get_stats(f"{sg_total_xpat2}120]", add_to_path_stat_val)[1]
                        
                        #skip current_streak without 3 putt 121
                        
                        consecutive_fairways_hit = get_stats(f"{sg_total_xpat2}122]", add_to_path_stat_val)[0]
                        consecutive_fairways_hit_rank = get_stats(f"{sg_total_xpat2}122]", add_to_path_stat_val)[1]
                        
                        consecutive_gir = get_stats(f"{sg_total_xpat2}123]", add_to_path_stat_val)[0]
                        consecutive_gir_rank = get_stats(f"{sg_total_xpat2}123]", add_to_path_stat_val)[1]
                        
                        consecutive_sand_saves = get_stats(f"{sg_total_xpat2}124]", add_to_path_stat_val)[0]
                        consecutive_sand_saves_rank = get_stats(f"{sg_total_xpat2}124]", add_to_path_stat_val)[1]
                        
                        best_ytd_1_putt_or_better_streak = get_stats(f"{sg_total_xpat2}125]", add_to_path_stat_val)[0]
                        best_ytd_1_putt_or_better_streak_rank = get_stats(f"{sg_total_xpat2}125]", add_to_path_stat_val)[1]
                        
                        best_ytd_streak_wo_3_putt = get_stats(f"{sg_total_xpat2}126]", add_to_path_stat_val)[0]
                        best_ytd_streak_wo_3_putt_rank = get_stats(f"{sg_total_xpat2}126]", add_to_path_stat_val)[1]
                        
                        ytd_par_or_better_streak = get_stats(f"{sg_total_xpat2}127]", add_to_path_stat_val)[0]
                        ytd_par_or_better_streak_rank = get_stats(f"{sg_total_xpat2}127]", add_to_path_stat_val)[1]
                        
                        consecutive_par_3_birdies = get_stats(f"{sg_total_xpat2}128]", add_to_path_stat_val)[0]
                        consecutive_par_3_birdies_rank = get_stats(f"{sg_total_xpat2}128]", add_to_path_stat_val)[1]
                        
                        consecutive_holes_below_par = get_stats(f"{sg_total_xpat2}129]", add_to_path_stat_val)[0]
                        consecutive_holes_below_par_rank = get_stats(f"{sg_total_xpat2}129]", add_to_path_stat_val)[1]
                        
                        consecutive_birdies_streak = get_stats(f"{sg_total_xpat2}130]", add_to_path_stat_val)[0]
                        consecutive_birdies_streak_rank = get_stats(f"{sg_total_xpat2}130]", add_to_path_stat_val)[1]
                        
                        consecutive_birdies_eagles_streak = get_stats(f"{sg_total_xpat2}131]", add_to_path_stat_val)[0]
                        consecutive_birdies_eagles_streak_rank = get_stats(f"{sg_total_xpat2}131]", add_to_path_stat_val)[1]
                        
                        official_money = get_stats(f"{sg_total_xpat2}132]", add_to_path_stat_val)[0]
                        official_money_rank = get_stats(f"{sg_total_xpat2}132]", add_to_path_stat_val)[1]
                        
                        fedexcup_regular_season_points = get_stats(f"{sg_total_xpat2}133]", add_to_path_stat_val)[0]
                        fedexcup_rank = get_stats(f"{sg_total_xpat2}133]", add_to_path_stat_val)[1]
                        wins = get_sup_stats(f"{sg_total_xpat2}133]", add_to_path_sup)[0]
                        top_10s = get_sup_stats(f"{sg_total_xpat2}133]", add_to_path_sup)[1]
                        # end of else
   
                
                # print('SG Total: ', sg_total)
                # print('SG Total Rank: ', sg_total_rank)
  
                
                player_stats = {'player_id': player_id,
                                'year': season_to_year_status(this_year),
                                'season': this_year,
                                'sg_total': str_to_float_or_null(sg_total),
                                'sg_total_rank': str_to_int_or_null(sg_total_rank),
                                'sg_total_total': str_to_float_or_null(sg_total_total),
                                'sg_total_measured_rounds': str_to_int_or_null(sg_total_m_rounds),
                                'sg_tee_to_green': str_to_float_or_null(sg_tee_2_gr),
                                'sg_tee_to_green_rank': str_to_int_or_null(sg_tee_2_gr_rank),
                                'sg_off_tee': str_to_float_or_null(sg_off_tee),
                                'sg_off_tee_rank': str_to_int_or_null(sg_off_tee_rank),
                                'sg_off_tee_total': str_to_float_or_null(sg_off_tee_total),
                                'sg_app_green': str_to_float_or_null(sg_app_gr),
                                'sg_app_green_rank': str_to_int_or_null(sg_app_gr_rank),
                                'sg_app_green_total': str_to_float_or_null(sg_app_gr_total),
                                'sg_around_green': str_to_float_or_null(sg_around_gr),
                                'sg_around_green_rank': str_to_int_or_null(sg_around_gr_rank),
                                'sg_around_green_total': str_to_float_or_null(sg_around_gr_total),
                                'sg_putting': str_to_float_or_null(sg_putting),
                                'sg_putting_rank': str_to_int_or_null(sg_putting_rank),
                                'sg_putting_total': str_to_float_or_null(sg_putting_total),
                                'total_driving': str_to_int_or_null(total_driving),
                                'total_driving_rank': str_to_int_or_null(total_driving_rank),
                                'longest_drive': str_to_int_or_null(longest_drive),
                                'longest_drive_rank': str_to_int_or_null(longest_drive_rank),
                                'longest_drive_tourney': longest_drive_tourney,
                                'longest_drive_round': str_to_int_or_null(longest_drive_round),
                                'driving_distance': str_to_float_or_null(driving_distance),
                                'driving_distance_rank': str_to_int_or_null(driving_distance_rank),
                                'driving_distance_total': str_to_int_or_null(driving_distance_total),
                                'driving_distance_total_drives': str_to_int_or_null(driving_distance_total_drives),
                                'driving_distance_all_drives': str_to_float_or_null(driving_distance_all_drives),
                                'driving_distance_all_drives_rank': str_to_int_or_null(driving_distance_all_drives_rank),
                                'driving_distance_all_drives_total': str_to_int_or_null(driving_distance_all_drives_total),
                                'driving_distance_all_drives_total_drives': str_to_int_or_null(driving_distance_all_drives_total_drives),
                                'driving_accuracy': percent_str_to_float_or_null(driving_accuracy),
                                'driving_accuracy_rank': str_to_int_or_null(driving_accuracy_rank),
                                'fairways_hit': str_to_int_or_null(fairways_hit),
                                'fairways_possible': str_to_int_or_null(fairways_possible),
                                'left_rough_tendency': percent_str_to_float_or_null(left_rough_tendency),
                                'left_rough_tendency_rank': str_to_int_or_null(left_rough_tendency_rank),
                                'left_rough_total': str_to_int_or_null(left_rough_total),
                                'left_rough_possible_fairways': str_to_int_or_null(left_rough_possible_fairways),
                                'right_rough_tendency': percent_str_to_float_or_null(right_rough_tendency),
                                'right_rough_tendency_rank': str_to_int_or_null(right_rough_tendency_rank),
                                'right_rough_total': str_to_int_or_null(right_rough_total),
                                'right_rough_possible_fairways': str_to_int_or_null(right_rough_possible_fairways),
                                #'distance_from_edge_frwy': distance_from_edge_frwy,
                                'distance_from_edge_frwy_in': length_to_inches(distance_from_edge_frwy),
                                'distance_from_edge_frwy_rank': str_to_int_or_null(distance_from_edge_frwy_rank),
                                'distance_from_edge_frwy_total_ft': str_to_float_or_null(distance_from_edge_frwy_total),
                                'distance_from_edge_frwy_strokes': str_to_int_or_null(distance_from_edge_frwy_strokes),
                                'club_head_speed': str_to_float_or_null(club_head_speed),
                                'club_head_speed_rank': str_to_int_or_null(club_head_speed_rank),
                                'club_head_speed_total': str_to_float_or_null(club_head_speed_total),
                                'club_head_speed_attempts': str_to_int_or_null(club_head_speed_attempts),
                                'total_driving_efficiency': str_to_int_or_null(total_driving_efficiency),
                                'total_driving_efficiency_rank': str_to_int_or_null(total_driving_efficiency_rank),
                                'carry_efficiency_rank': str_to_int_or_null(carry_efficiency_rank),
                                'greens_in_regulation_percent': percent_str_to_float_or_null(greens_in_regulation_percent),
                                'greens_in_regulation_percent_rank': str_to_int_or_null(greens_in_regulation_percent_rank),
                                'greens_hit': str_to_int_or_null(greens_hit),
                                'greens_possible': str_to_int_or_null(greens_possible),
                                'proximity_to_hole_in': length_to_inches(proximity_to_hole),
                                'proximity_to_hole_rank': str_to_int_or_null(proximity_to_hole_rank),
                                'proximity_to_hole_total_ft': str_to_float_or_null(proximity_to_hole_total_ft),
                                'proximity_to_hole_total_att': str_to_int_or_null(proximity_to_hole_total_att),
                                
                                'approach_more_275_in': length_to_inches(approach_more_275_in),
                                'approach_more_275_rank': str_to_int_or_null(approach_more_275_rank),
                                'approach_more_275_total_ft': str_to_float_or_null(approach_more_275_total_ft),
                                'approach_more_275_total_att': str_to_int_or_null(approach_more_275_total_att),
                                
                                'approach_250_275_in': length_to_inches(approach_250_275_in),
                                'approach_250_275_rank': str_to_int_or_null(approach_250_275_rank),
                                'approach_250_275_total_ft': str_to_float_or_null(approach_250_275_total_ft),
                                'approach_250_275_total_att': str_to_int_or_null(approach_250_275_total_att),
                                
                                'approach_225_250_in': length_to_inches(approach_225_250_in),
                                'approach_225_250_rank': str_to_int_or_null(approach_225_250_rank),
                                'approach_225_250_total_ft': str_to_float_or_null(approach_225_250_total_ft),
                                'approach_225_250_total_att': str_to_int_or_null(approach_225_250_total_att),
                                
                                'approach_200_225_in': length_to_inches(approach_200_225_in),
                                'approach_200_225_rank': str_to_int_or_null(approach_200_225_rank),
                                'approach_200_225_total_ft': str_to_float_or_null(approach_200_225_total_ft),
                                'approach_200_225_total_att': str_to_int_or_null(approach_200_225_total_att),
                                
                                'approach_more_200_in': length_to_inches(approach_more_200_in),
                                'approach_more_200_rank': str_to_int_or_null(approach_more_200_rank),
                                'approach_more_200_total_ft': str_to_float_or_null(approach_more_200_total_ft),
                                'approach_more_200_total_att': str_to_int_or_null(approach_more_200_total_att),
                                
                                'approach_175_200_in': length_to_inches(approach_175_200_in),
                                'approach_175_200_rank': str_to_int_or_null(approach_175_200_rank),
                                'approach_175_200_total_ft': str_to_float_or_null(approach_175_200_total_ft),
                                'approach_175_200_total_att': str_to_int_or_null(approach_175_200_total_att),
                                
                                'approach_150_175_in': length_to_inches(approach_150_175_in),
                                'approach_150_175_rank': str_to_int_or_null(approach_150_175_rank),
                                'approach_150_175_total_ft': str_to_float_or_null(approach_150_175_total_ft),
                                'approach_150_175_total_att': str_to_int_or_null(approach_150_175_total_att),
                                
                                'approach_125_150_in': length_to_inches(approach_125_150_in),
                                'approach_125_150_rank': str_to_int_or_null(approach_125_150_rank),
                                'approach_125_150_total_ft': str_to_float_or_null(approach_125_150_total_ft),
                                'approach_125_150_total_att': str_to_int_or_null(approach_125_150_total_att),
                                
                                'approach_50_125_in': length_to_inches(approach_50_125_in),
                                'approach_50_125_rank': str_to_int_or_null(approach_50_125_rank),
                                'approach_50_125_total_ft': str_to_float_or_null(approach_50_125_total_ft),
                                'approach_50_125_total_att': str_to_int_or_null(approach_50_125_total_att),
                                
                                'approach_100_125_in': length_to_inches(approach_100_125_in),
                                'approach_100_125_rank': str_to_int_or_null(approach_100_125_rank),
                                'approach_100_125_total_ft': str_to_float_or_null(approach_100_125_total_ft),
                                'approach_100_125_total_att': str_to_int_or_null(approach_100_125_total_att),
                                
                                'approach_75_100_in': length_to_inches(approach_75_100_in),
                                'approach_75_100_rank': str_to_int_or_null(approach_75_100_rank),
                                'approach_75_100_total_ft': str_to_float_or_null(approach_75_100_total_ft),
                                'approach_75_100_total_att': str_to_int_or_null(approach_75_100_total_att),
                                
                                'approach_50_75_in': length_to_inches(approach_50_75_in),
                                'approach_50_75_rank': str_to_int_or_null(approach_50_75_rank),
                                'approach_50_75_total_ft': str_to_float_or_null(approach_50_75_total_ft),
                                'approach_50_75_total_att': str_to_int_or_null(approach_50_75_total_att),
                                
                                'approach_less_100_in': length_to_inches(approach_less_100_in),
                                'approach_less_100_rank': str_to_int_or_null(approach_less_100_rank),
                                'approach_less_100_total_ft': str_to_float_or_null(approach_less_100_total_ft),
                                'approach_less_100_total_att': str_to_int_or_null(approach_less_100_total_att),
                                
                                'approach_more_100_in': length_to_inches(approach_more_100_in),
                                'approach_more_100_rank': str_to_int_or_null(approach_more_100_rank),
                                'approach_more_100_total_ft': str_to_float_or_null(approach_more_100_total_ft),
                                'approach_more_100_total_att': str_to_int_or_null(approach_more_100_total_att),
  
                                'fairway_proximity': length_to_inches(fairway_proximity),
                                'fairway_proximity_rank': str_to_int_or_null(fairway_proximity_rank),
                                'fairway_proximity_att': str_to_int_or_null(fairway_proximity_att),
                                
                                'rough_proximity': length_to_inches(rough_proximity),
                                'rough_proximity_rank': str_to_int_or_null(rough_proximity_rank),
                                'rough_proximity_total_in': str_to_int_or_null(rough_proximity_total_in),
                                'rough_proximity_total_att': str_to_int_or_null(rough_proximity_total_att),
                                
                                'left_rough_proximity': length_to_inches(left_rough_proximity),
                                'left_rough_proximity_rank': str_to_int_or_null(left_rough_proximity_rank),
                                'left_rough_proximity_att': str_to_int_or_null(left_rough_proximity_att),
                                
                                'right_rough_proximity': length_to_inches(right_rough_proximity),
                                'right_rough_proximity_rank': str_to_int_or_null(right_rough_proximity_rank),
                                'right_rough_proximity_att': str_to_int_or_null(right_rough_proximity_att),

                                'approach_more_275_rough_in': length_to_inches(approach_more_275_rough_in),
                                'approach_more_275_rough_rank': str_to_int_or_null(approach_more_275_rough_rank),
                                'approach_more_275_rough_total_ft': str_to_float_or_null(approach_more_275_rough_total_ft),
                                'approach_more_275_rough_total_att': str_to_int_or_null(approach_more_275_rough_total_att),
                                
                                'approach_250_275_rough_in': length_to_inches(approach_250_275_rough_in),
                                'approach_250_275_rough_rank': str_to_int_or_null(approach_250_275_rough_rank),
                                'approach_250_275_rough_total_ft': str_to_float_or_null(approach_250_275_rough_total_ft),
                                'approach_250_275_rough_total_att': str_to_int_or_null(approach_250_275_rough_total_att),
                                
                                'approach_225_250_rough_in': length_to_inches(approach_225_250_rough_in),
                                'approach_225_250_rough_rank': str_to_int_or_null(approach_225_250_rough_rank),
                                'approach_225_250_rough_total': str_to_float_or_null(approach_225_250_rough_total_ft),
                                'approach_225_250_rough_total_att': str_to_int_or_null(approach_225_250_rough_total_att),
                                
                                'approach_200_225_rough_in': length_to_inches(approach_200_225_rough_in),
                                'approach_200_225_rough_rank': str_to_int_or_null(approach_200_225_rough_rank),
                                'approach_200_225_rough_total_ft': str_to_float_or_null(approach_200_225_rough_total_ft),
                                'approach_200_225_rough_total_att': str_to_int_or_null(approach_200_225_rough_total_att),
                                
                                'approach_more_100_rough_in': length_to_inches(approach_more_100_rough_in),
                                'approach_more_100_rough_rank': str_to_int_or_null(approach_more_100_rough_rank),
                                'approach_more_100_rough_total_ft': str_to_float_or_null(approach_more_100_rough_total_ft),
                                'approach_more_100_rough_total_att': str_to_int_or_null(approach_more_100_rough_total_att),
                                
                                'approach_less_100_rough_in': length_to_inches(approach_less_100_rough_in),
                                'approach_less_100_rough_rank': str_to_int_or_null(approach_less_100_rough_rank),
                                'approach_less_100_rough_total_ft': str_to_float_or_null(approach_less_100_rough_total_ft),
                                'approach_less_100_rough_total_att': str_to_int_or_null(approach_less_100_rough_total_att),
                                
                                'approach_more_200_rough_in': length_to_inches(approach_more_200_rough_in),
                                'approach_more_200_rough_rank': str_to_int_or_null(approach_more_200_rough_rank),
                                'approach_more_200_rough_total_ft': str_to_float_or_null(approach_more_200_rough_total_ft),
                                'approach_more_200_rough_total_att': str_to_int_or_null(approach_more_200_rough_total_att),
                                
                                'approach_175_200_rough_in': length_to_inches(approach_175_200_rough_in),
                                'approach_175_200_rough_rank': str_to_int_or_null(approach_175_200_rough_rank),
                                'approach_175_200_rough_total_ft': str_to_float_or_null(approach_175_200_rough_total_ft),
                                'approach_175_200_rough_total_att': str_to_int_or_null(approach_175_200_rough_total_att),
                                
                                'approach_150_175_rough_in': length_to_inches(approach_150_175_rough_in),
                                'approach_150_175_rough_rank': str_to_int_or_null(approach_150_175_rough_rank),
                                'approach_150_175_rough_total_ft': str_to_float_or_null(approach_150_175_rough_total_ft),
                                'approach_150_175_rough_total_att': str_to_int_or_null(approach_150_175_rough_total_att),
                                
                                'approach_125_150_rough_in': length_to_inches(approach_125_150_rough_in),
                                'approach_125_150_rough_rank': str_to_int_or_null(approach_125_150_rough_rank),
                                'approach_125_150_rough_total_ft': str_to_float_or_null(approach_125_150_rough_total_ft),
                                'approach_125_150_rough_total_att': str_to_int_or_null(approach_125_150_rough_total_att),
                                
                                'approach_50_125_rough_in': length_to_inches(approach_50_125_rough_in),
                                'approach_50_125_rough_rank': str_to_int_or_null(approach_50_125_rough_rank),
                                'approach_50_125_rough_total_ft': str_to_float_or_null(approach_50_125_rough_total_ft),
                                'approach_50_125_rough_total_att': str_to_int_or_null(approach_50_125_rough_total_att),
                                
                                'approach_100_125_rough_in': length_to_inches(approach_100_125_rough_in),
                                'approach_100_125_rough_rank': str_to_int_or_null(approach_100_125_rough_rank),
                                'approach_100_125_rough_total_ft': str_to_float_or_null(approach_100_125_rough_total_ft),
                                'approach_100_125_rough_total_att': str_to_int_or_null(approach_100_125_rough_total_att),
                                
                                'approach_75_100_rough_in': length_to_inches(approach_75_100_rough_in),
                                'approach_75_100_rough_rank': str_to_int_or_null(approach_75_100_rough_rank),
                                'approach_75_100_rough_total_ft': str_to_float_or_null(approach_75_100_rough_total_ft),
                                'approach_75_100_rough_total_att': str_to_int_or_null(approach_75_100_rough_total_att),
                                
                                'approach_50_75_rough_in': length_to_inches(approach_50_75_rough_in),
                                'approach_50_75_rough_rank': str_to_int_or_null(approach_50_75_rough_rank),
                                'approach_50_75_rough_total_ft': str_to_float_or_null(approach_50_75_rough_total_ft),
                                'approach_50_75_rough_total_att': str_to_int_or_null(approach_50_75_rough_total_att),
                                
                                'going_for_green_percent': percent_str_to_float_or_null(going_for_green_percent),
                                'going_for_green_percent_rank': str_to_int_or_null(going_for_green_percent_rank),
                                'going_for_green_percent_attempts': str_to_int_or_null(going_for_green_percent_attempts),
                                'going_for_green_percent_non_attemptes': str_to_int_or_null(going_for_green_percent_non_attemptes),
                                
                                'going_for_green_hit_percent': percent_str_to_float_or_null(going_for_green_hit_percent),
                                'going_for_green_hit_rank': str_to_int_or_null(going_for_green_hit_rank),
                                'going_for_green_hit': str_to_int_or_null(going_for_green_hit),
                                'going_for_green_attempts': str_to_int_or_null(going_for_green_attempts),
                                
                                'going_for_green_birdie_better_pct': percent_str_to_float_or_null(going_for_green_birdie_better_pct),
                                'going_for_green_birdie_better_pct_rank': str_to_int_or_null(going_for_green_birdie_better_pct_rank),
                                'going_for_green_birdie_better_total': str_to_int_or_null(going_for_green_birdie_better_total),
                                
                                'total_hole_outs': str_to_int_or_null(total_hole_outs),
                                'total_hole_outs_rank': str_to_int_or_null(total_hole_outs_rank),
                                
                                
                                
                                
                                
                                
                                'longest_hole_out_yrds': str_to_int_or_null(longest_hole_out_yrds),
                                'longest_hole_out_rank': str_to_int_or_null(longest_hole_out_rank),
                                'longest_hole_out_tourney': longest_hole_out_tourney,
                                'longest_hole_out_rd': str_to_int_or_null(longest_hole_out_rd),
                                
                                'scrambling_percent': percent_str_to_float_or_null(scrambling_percent),
                                'scrambling_rank': str_to_int_or_null(scrambling_rank),
                                'scrambling_par_or_better': str_to_int_or_null(scrambling_par_or_better),
                                'scrambling_missed_gir': str_to_int_or_null(scrambling_missed_gir),
                                
                                'scrambling_from_rough_perecnt': percent_str_to_float_or_null(scrambling_from_rough_perecnt),
                                'scrambling_from_rough_rank': str_to_int_or_null(scrambling_from_rough_rank),
                                'scrambling_from_rough_success': str_to_int_or_null(scrambling_from_rough_success),
                                'scrambling_from_rough_att': str_to_int_or_null(scrambling_from_rough_att),
                                
                                'scrambling_from_fringe_percent': percent_str_to_float_or_null(scrambling_from_fringe_percent),
                                'scrambling_from_fringe_rank': str_to_int_or_null(scrambling_from_fringe_rank),
                                'scrambling_from_fringe_success': str_to_int_or_null(scrambling_from_fringe_success),
                                'scrambling_from_fringe_att': str_to_int_or_null(scrambling_from_fringe_att),
                                
                                'scrambling_more_30_percent': percent_str_to_float_or_null(scrambling_more_30_percent),
                                'scrambling_more_30_rank': str_to_int_or_null(scrambling_more_30_rank),
                                'scrambling_more_30_success': str_to_int_or_null(scrambling_more_30_success),
                                'scrambling_more_30_att': str_to_int_or_null(scrambling_more_30_att),
                                
                                'scrambling_20_30_percent': percent_str_to_float_or_null(scrambling_20_30_percent),
                                'scrambling_20_30_rank': str_to_int_or_null(scrambling_20_30_rank),
                                'scrambling_20_30_success': str_to_int_or_null(scrambling_20_30_success),
                                'scrambling_20_30_att': str_to_int_or_null(scrambling_20_30_att),
                                
                                'scrambling_10_20_percent': percent_str_to_float_or_null(scrambling_10_20_percent),
                                'scrambling_10_20_rank': str_to_int_or_null(scrambling_10_20_rank),
                                'scrambling_10_20_success': str_to_int_or_null(scrambling_10_20_success),
                                'scrambling_10_20_att': str_to_int_or_null(scrambling_10_20_att),
                                
                                'scrambling_less_10_percent': percent_str_to_float_or_null(scrambling_less_10_percent),
                                'scrambling_less_10_rank': str_to_int_or_null(scrambling_less_10_rank),
                                'scrambling_less_10_success': str_to_int_or_null(scrambling_less_10_success),
                                'scrambling_less_10_att': str_to_int_or_null(scrambling_less_10_att),
                                
                                'sand_save_percent': percent_str_to_float_or_null(sand_save_percent),
                                'sand_save_rank': str_to_int_or_null(sand_save_rank),
                                'sand_save_saves': str_to_int_or_null(sand_save_saves),
                                'sand_save_bunkers': str_to_int_or_null(sand_save_bunkers),
                                
                                'proximity_to_hole_sand ': length_to_inches(proximity_to_hole_sand),    # length
                                'proximity_to_hole_sand_rank': str_to_int_or_null(proximity_to_hole_sand_rank),
                                'proximity_to_hole_sand_total_ft': str_to_float_or_null(proximity_to_hole_sand_total_ft),      #float
                                'proximity_to_hole_sand_shots': str_to_int_or_null(proximity_to_hole_sand_shots),
                                
                                'total_putting': str_to_float_or_null(total_putting),      #float
                                'total_putting_rank': str_to_int_or_null(total_putting_rank),
                                
                                'putting_avg': str_to_float_or_null(putting_avg),      #float
                                'putting_avg_rank': str_to_int_or_null(putting_avg_rank),
                                'putting_avg_gir_putts': str_to_int_or_null(putting_avg_gir_putts),
                                'putting_avg_greens_hit': str_to_int_or_null(putting_avg_greens_hit),
                                
                                'overall_putting_avg': str_to_float_or_null(overall_putting_avg),     #float
                                'overall_putting_avg_rank': str_to_int_or_null(overall_putting_avg_rank),
                                'overall_putting_total_putts': str_to_int_or_null(overall_putting_total_putts),
                                'overall_putting_total_holes': str_to_int_or_null(overall_putting_total_holes),
                                
                                
                                'birdie_or_better_conversion_percent': percent_str_to_float_or_null(birdie_or_better_conversion_percent),
                                'birdie_or_better_conversion_rank': str_to_int_or_null(birdie_or_better_conversion_rank),
                                'birdie_or_better_conversion_birdies': str_to_int_or_null(birdie_or_better_conversion_birdies),
                                'birdie_or_better_conversion_greens_hit': str_to_int_or_null(birdie_or_better_conversion_greens_hit),
                                
                                'putts_per_round': str_to_float_or_null(putts_per_round),    #float
                                'putts_per_round_rank': str_to_int_or_null(putts_per_round_rank),
                                'total_putts': str_to_int_or_null(total_putts),
                                'total_rounds': str_to_int_or_null(total_rounds),
                                
                                'putts_per_round_rd1': str_to_float_or_null(putts_per_round_rd1),    #float
                                'putts_per_round_rd1_rank': str_to_int_or_null(putts_per_round_rd1_rank),
                                'total_putts_rd1': str_to_int_or_null(total_putts_rd1),
                                'total_rounds_rd1': str_to_int_or_null(total_rounds_rd1),
                                
                                'putts_per_round_rd2': str_to_float_or_null(putts_per_round_rd2),    #float
                                'putts_per_round_rd2_rank': str_to_int_or_null(putts_per_round_rd2_rank),
                                'total_putts_rd2': str_to_int_or_null(total_putts_rd2),
                                'total_rounds_rd2': str_to_int_or_null(total_rounds_rd2),
                                
                                'putts_per_round_rd3': str_to_float_or_null(putts_per_round_rd3),    #float
                                'putts_per_round_rd3_rank': str_to_int_or_null(putts_per_round_rd3_rank),
                                'total_putts_rd3': str_to_int_or_null(total_putts_rd3),
                                'total_rounds_rd3': str_to_int_or_null(total_rounds_rd3),
                                
                                'putts_per_round_rd4': str_to_float_or_null(putts_per_round_rd4),    #float
                                'putts_per_round_rd4_rank': str_to_int_or_null(putts_per_round_rd4_rank),
                                'total_putts_rd4': str_to_int_or_null(total_putts_rd4),
                                'total_rounds_rd4': str_to_int_or_null(total_rounds_rd4),
                                
                                'one_putt_percentage': percent_str_to_float_or_null(one_putt_percentage),
                                'one_putt_rank': str_to_int_or_null(one_putt_rank),
                                'one_putt_total': str_to_int_or_null(one_putt_total),
                                'one_putt_total_holes': str_to_int_or_null(one_putt_total_holes),
                                
                                'longest_putt': length_to_inches(longest_putt),      # length
                                'longest_putt_break': str_to_int_or_null(longest_putt_break),
                                'longest_putt_tourney': longest_putt_tourney,   #str
                                'longest_putt_rd': str_to_int_or_null(longest_putt_rd),
                                
                                'three_putt_avoidance': percent_str_to_float_or_null(three_putt_avoidance),     #percent
                                'three_putt_avoidance_rank': str_to_int_or_null(three_putt_avoidance_rank),
                                'three_putt_total': str_to_int_or_null(three_putt_total),
                                'three_putt_total_holes': str_to_int_or_null(three_putt_total_holes),
                                
                                'putting_more_25_percent': percent_str_to_float_or_null(putting_more_25_percent),
                                'putting_more_25_rank': str_to_int_or_null(putting_more_25_rank),
                                'putting_more_25_att': str_to_int_or_null(putting_more_25_att),
                                'putting_more_25_made': str_to_int_or_null(putting_more_25_made),
                                
                                'putting_20_25_percent': percent_str_to_float_or_null(putting_20_25_percent),
                                'putting_20_25_rank': str_to_int_or_null(putting_20_25_rank),
                                'putting_20_25_att': str_to_int_or_null(putting_20_25_att),
                                'putting_20_25_made': str_to_int_or_null(putting_20_25_made),
                                
                                'putting_15_20_percent': percent_str_to_float_or_null(putting_15_20_percent),
                                'putting_15_20_rank': str_to_int_or_null(putting_15_20_rank),
                                'putting_15_20_att': str_to_int_or_null(putting_15_20_att),
                                'putting_15_20_made': str_to_int_or_null(putting_15_20_made),
                                
                                'putting_10_15_percent': percent_str_to_float_or_null(putting_10_15_percent),
                                'putting_10_15_rank': str_to_int_or_null(putting_10_15_rank),
                                'putting_10_15_att': str_to_int_or_null(putting_10_15_att),
                                'putting_10_15_made': str_to_int_or_null(putting_10_15_made),
                                
                                'putting_less_10_percent': percent_str_to_float_or_null(putting_less_10_percent),
                                'putting_less_10_rank': str_to_int_or_null(putting_less_10_rank),
                                'putting_less_10_att': str_to_int_or_null(putting_less_10_att),
                                'putting_less_10_made': str_to_int_or_null(putting_less_10_made),
                                
                                'putting_from_10_percent': percent_str_to_float_or_null(putting_from_10_percent),
                                'putting_from_10_rank': str_to_int_or_null(putting_from_10_rank),
                                'putting_from_10_att': str_to_int_or_null(putting_from_10_att),
                                
                                'putting_from_9_percent': percent_str_to_float_or_null(putting_from_9_percent),
                                'putting_from_9_rank': str_to_int_or_null(putting_from_9_rank),
                                'putting_from_9_att': str_to_int_or_null(putting_from_9_att),
                                
                                'putting_from_8_percent': percent_str_to_float_or_null(putting_from_8_percent),
                                'putting_from_8_rank': str_to_int_or_null(putting_from_8_rank),
                                'putting_from_8_att': str_to_int_or_null(putting_from_8_att),
                                
                                'putting_from_7_percent': percent_str_to_float_or_null(putting_from_7_percent),
                                'putting_from_7_rank': str_to_int_or_null(putting_from_7_rank),
                                'putting_from_7_att': str_to_int_or_null(putting_from_7_att),
                                
                                'putting_from_6_percent': percent_str_to_float_or_null(putting_from_6_percent),
                                'putting_from_6_rank': str_to_int_or_null(putting_from_6_rank),
                                'putting_from_6_att': str_to_int_or_null(putting_from_6_att),
                                
                                'putting_from_5_percent': percent_str_to_float_or_null(putting_from_5_percent),
                                'putting_from_5_rank': str_to_int_or_null(putting_from_5_rank),
                                'putting_from_5_att': str_to_int_or_null(putting_from_5_att),
                                
                                'putting_from_4_8_percent': percent_str_to_float_or_null(putting_from_4_8_percent),
                                'putting_from_4_8_rank': str_to_int_or_null(putting_from_4_8_rank),
                                'putting_from_4_8_att': str_to_int_or_null(putting_from_4_8_att),
                                'putting_from_4_8_made': str_to_int_or_null(putting_from_4_8_made),
                                
                                'putting_from_4_percent': percent_str_to_float_or_null(putting_from_4_percent),
                                'putting_from_4_rank': str_to_int_or_null(putting_from_4_rank),
                                'putting_from_4_att': str_to_int_or_null(putting_from_4_att),
                                
                                'putting_from_3_percent': percent_str_to_float_or_null(putting_from_3_percent),
                                'putting_from_3_rank': str_to_int_or_null(putting_from_3_rank),
                                'putting_from_3_att': str_to_int_or_null(putting_from_3_att),
                                
                                'avg_distance_putts_made': length_to_inches(avg_distance_putts_made),       #length
                                'avg_distance_putts_made_rank': str_to_int_or_null(avg_distance_putts_made_rank),
                                'avg_distance_putts_made_in': str_to_int_or_null(avg_distance_putts_made_in),
                                'avg_distance_putts_made_rounds': str_to_int_or_null(avg_distance_putts_made_rounds),
                                
                                'approach_putt_performance': length_to_inches(approach_putt_performance),      #length
                                'approach_putt_rank': str_to_int_or_null(approach_putt_rank),
                                'approach_putt_att': str_to_int_or_null(approach_putt_att),
                                
                                'scoring_avg_adj': str_to_float_or_null(scoring_avg_adj),    #float
                                'scoring_avg_adj_rank': str_to_int_or_null(scoring_avg_adj_rank),              #------------------------------
                                'scoring_avg_adj_total_strokes': str_to_int_or_null(scoring_avg_adj_total_strokes),
                                'scoring_avg_adj_total_adjustment': str_to_float_or_null(scoring_avg_adj_total_adjustment),
                                
                                'scoring_avg_actual': str_to_float_or_null(scoring_avg_actual),    #float
                                'scoring_avg_actual_rank': str_to_int_or_null(scoring_avg_actual_rank),
                                'scoring_avg_actual_total_strokes': str_to_int_or_null(scoring_avg_actual_total_strokes),
                                'scoring_avg_actual_total_rounds': str_to_int_or_null(scoring_avg_actual_total_rounds),
                                
                                'lowest_round': str_to_int_or_null(lowest_round),
                                'lowest_round_rank': str_to_int_or_null(lowest_round_rank),
                                'lowest_round_tourney': lowest_round_tourney,      #str
                                'lowest_round_round': str_to_int_or_null(lowest_round_round),
                                
                                'birdie_avg': str_to_float_or_null(birdie_avg),    #float
                                'birdie_avg_rank': str_to_int_or_null(birdie_avg_rank),
                                'birdie_avg_num_birdies': str_to_int_or_null(birdie_avg_num_birdies),
                                'birdie_avg_total_rounds': str_to_int_or_null(birdie_avg_total_rounds),
                                
                                'total_birdies': str_to_int_or_null(total_birdies),
                                'total_birdies_rank': str_to_int_or_null(total_birdies_rank),
                                
                                'eagles_holes_per': str_to_float_or_null(eagles_holes_per),    #float
                                'eagles_holes_per_rank': str_to_int_or_null(eagles_holes_per_rank),
                                
                                'total_eagles': str_to_int_or_null(total_eagles),
                                'total_eagles_rank': str_to_int_or_null(total_eagles_rank),
                                
                                'par_breaker_percent': percent_str_to_float_or_null(par_breaker_percent),
                                'par_breaker_rank': str_to_int_or_null(par_breaker_rank),
                                
                                'bounce_back_percent': percent_str_to_float_or_null(bounce_back_percent),
                                'bounce_back_rank': str_to_int_or_null(bounce_back_rank),
                                
                                'par3_birdie_or_better': percent_str_to_float_or_null(par3_birdie_or_better),        #percent
                                'par3_birdie_or_better_rank': str_to_int_or_null(par3_birdie_or_better_rank),
                                'par3_birdie_or_better_total': str_to_int_or_null(par3_birdie_or_better_total),
                                'par3_holes': str_to_int_or_null(par3_holes),
                                
                                'par4_birdie_or_better': percent_str_to_float_or_null(par4_birdie_or_better),        #percent
                                'par4_birdie_or_better_rank': str_to_int_or_null(par4_birdie_or_better_rank),
                                'par4_birdie_or_better_total': str_to_int_or_null(par4_birdie_or_better_total),
                                'par4_holes': str_to_int_or_null(par4_holes),
                                
                                'par5_birdie_or_better': percent_str_to_float_or_null(par5_birdie_or_better),        #percent
                                'par5_birdie_or_better_rank': str_to_int_or_null(par5_birdie_or_better_rank),
                                'par5_birdie_or_better_total': str_to_int_or_null(par5_birdie_or_better_total),
                                'par5_holes': str_to_int_or_null(par5_holes),
                                
                                'birdie_or_better_percent': str_to_int_or_null(birdie_or_better_percent),
                                'birdie_or_better_rank': str_to_int_or_null(birdie_or_better_rank),
                                
                                'bogey_avoidance_percent': percent_str_to_float_or_null(bogey_avoidance_percent),
                                'bogey_avoidance_rank': str_to_int_or_null(bogey_avoidance_rank),
                                'bogey_total': str_to_int_or_null(bogey_total),
                                
                                'final_round_scoring_avg': str_to_float_or_null(final_round_scoring_avg),      #float
                                'final_round_scoring_avg_rank': str_to_int_or_null(final_round_scoring_avg_rank),
                                'final_round_scoring_total_strokes': str_to_int_or_null(final_round_scoring_total_strokes),
                                'final_round_scoring_total_rds': str_to_int_or_null(final_round_scoring_total_rds),
                                
                                'final_round_performance': percent_str_to_float_or_null(final_round_performance),      #percent
                                'final_round_performance_rank': str_to_int_or_null(final_round_performance_rank),
                                
                                'rd1_scoring_avg': str_to_float_or_null(rd1_scoring_avg),      #float
                                'rd1_scoring_avg_rank': str_to_int_or_null(rd1_scoring_avg_rank),
                                'rd1_scoring_total_strokes': str_to_int_or_null(rd1_scoring_total_strokes),
                                'rd1_scoring_total_rds': str_to_int_or_null(rd1_scoring_total_rds),
                                
                                'rd2_scoring_avg': str_to_float_or_null(rd2_scoring_avg),      #float
                                'rd2_scoring_avg_rank': str_to_int_or_null(rd2_scoring_avg_rank),
                                'rd2_scoring_total_strokes': str_to_int_or_null(rd2_scoring_total_strokes),
                                'rd2_scoring_total_rds': str_to_int_or_null(rd2_scoring_total_rds),
                                
                                'rd3_scoring_avg': str_to_float_or_null(rd3_scoring_avg),      #float
                                'rd3_scoring_avg_rank': str_to_int_or_null(rd3_scoring_avg_rank),
                                'rd3_scoring_total_strokes': str_to_int_or_null(rd3_scoring_total_strokes),
                                'rd3_scoring_total_rds': str_to_int_or_null(rd3_scoring_total_rds),
                                
                                'rd4_scoring_avg': str_to_float_or_null(rd4_scoring_avg),      #float
                                'rd4_scoring_avg_rank': str_to_int_or_null(rd4_scoring_avg_rank),
                                'rd4_scoring_total_strokes': str_to_int_or_null(rd4_scoring_total_strokes),
                                'rd4_scoring_total_rds': str_to_int_or_null(rd4_scoring_total_rds),
                                
                                'par3_scoring_avg': str_to_float_or_null(par3_scoring_avg),      #float
                                'par3_scoring_avg_rank': str_to_int_or_null(par3_scoring_avg_rank),
                                'par3_scoring_avg_strokes': str_to_int_or_null(par3_scoring_avg_strokes),
                                'par3_scoring_avg_holes': str_to_int_or_null(par3_scoring_avg_holes),
                                
                                'par4_scoring_avg': str_to_float_or_null(par4_scoring_avg),      #float
                                'par4_scoring_avg_rank': str_to_int_or_null(par4_scoring_avg_rank),
                                'par4_scoring_avg_strokes': str_to_int_or_null(par4_scoring_avg_strokes),
                                'par4_scoring_avg_holes': str_to_int_or_null(par4_scoring_avg_holes),
                                
                                'par5_scoring_avg': str_to_float_or_null(par5_scoring_avg),      #float
                                'par5_scoring_avg_rank': str_to_int_or_null(par5_scoring_avg_rank),
                                'par5_scoring_avg_strokes': str_to_int_or_null(par5_scoring_avg_strokes),
                                'par5_scoring_avg_holes': str_to_int_or_null(par5_scoring_avg_holes),
                                
                                'front9_scoring_avg': str_to_float_or_null(front9_scoring_avg),      #float
                                'front9_scoring_avg_rank': str_to_int_or_null(front9_scoring_avg_rank),
                                'front9_scoring_avg_strokes': str_to_int_or_null(front9_scoring_avg_strokes),
                                'front9_scoring_avg_rounds': str_to_int_or_null(front9_scoring_avg_holes),
                                
                                'back9_scoring_avg': str_to_float_or_null(back9_scoring_avg),      #float
                                'back9_scoring_avg_rank': str_to_int_or_null(back9_scoring_avg_rank),
                                'back9_scoring_avg_strokes': str_to_int_or_null(back9_scoring_avg_strokes),
                                'back9_scoring_avg_rounds': str_to_int_or_null(back9_scoring_avg_holes),
                                
                                'early_scoring_avg': str_to_float_or_null(early_scoring_avg),      #float
                                'early_scoring_avg_rank': str_to_int_or_null(early_scoring_avg_rank),
                                'early_scoring_total_strokes': str_to_int_or_null(early_scoring_total_strokes),
                                'early_scoring_total_rounds': str_to_int_or_null(early_scoring_total_rounds),
                                
                                'late_scoring_avg': str_to_float_or_null(late_scoring_avg),      #float
                                'late_scoring_avg_rank': str_to_int_or_null(late_scoring_avg_rank),
                                'late_scoring_total_strokes': str_to_int_or_null(late_scoring_total_strokes),
                                'late_scoring_total_rounds': str_to_int_or_null(late_scoring_total_rounds),
                                
                                'consecutive_cuts': str_to_int_or_null(consecutive_cuts),
                                'consecutive_cuts_rank': str_to_int_or_null(consecutive_cuts_rank),
                                
                                #skip current_streak without 3 putt
                                
                                'consecutive_fairways_hit': str_to_int_or_null(consecutive_fairways_hit),
                                'consecutive_fairways_hit_rank': str_to_int_or_null(consecutive_fairways_hit_rank),
                                
                                'consecutive_gir': str_to_int_or_null(consecutive_gir),
                                'consecutive_gir_rank': str_to_int_or_null(consecutive_gir_rank),
                                
                                'consecutive_sand_saves': str_to_int_or_null(consecutive_sand_saves),
                                'consecutive_sand_saves_rank': str_to_int_or_null(consecutive_sand_saves_rank),
                                
                                'best_ytd_1_putt_or_better_streak': str_to_int_or_null(best_ytd_1_putt_or_better_streak),
                                'best_ytd_1_putt_or_better_streak_rank': str_to_int_or_null(best_ytd_1_putt_or_better_streak_rank),
                                
                                'best_ytd_streak_wo_3_putt': str_to_int_or_null(best_ytd_streak_wo_3_putt),
                                'best_ytd_streak_wo_3_putt_rank': str_to_int_or_null(best_ytd_streak_wo_3_putt_rank),
                                
                                'ytd_par_or_better_streak': str_to_int_or_null(ytd_par_or_better_streak),
                                'ytd_par_or_better_streak_rank': str_to_int_or_null(ytd_par_or_better_streak_rank),
                                
                                'consecutive_par_3_birdies': str_to_int_or_null(consecutive_par_3_birdies),
                                'consecutive_par_3_birdies_rank': str_to_int_or_null(consecutive_par_3_birdies_rank),
                                
                                'consecutive_holes_below_par': str_to_int_or_null(consecutive_holes_below_par),
                                'consecutive_holes_below_par_rank': str_to_int_or_null(consecutive_holes_below_par_rank),
                                
                                'consecutive_birdies_streak': str_to_int_or_null(consecutive_birdies_streak),
                                'consecutive_birdies_streak_rank': str_to_int_or_null(consecutive_birdies_streak_rank),
                                
                                'consecutive_birdies_eagles_streak': str_to_int_or_null(consecutive_birdies_eagles_streak),
                                'consecutive_birdies_eagles_streak_rank': str_to_int_or_null(consecutive_birdies_eagles_streak_rank),
                                
                                'official_money': str_to_int_or_null(official_money),
                                'official_money_rank': str_to_int_or_null(official_money_rank),
                                
                                'fedexcup_regular_season_points': str_to_int_or_null(fedexcup_regular_season_points),
                                'fedexcup_rank': str_to_int_or_null(fedexcup_rank),
                                'wins': str_to_int_or_null(wins),
                                'top_10s': str_to_int_or_null(top_10s)   
                    
                                }
                stats.append(player_stats)
        j += 1
    return stats
                                    
    
def get_stats(path, path_ext):
    raw_stat = driver.find_elements(By.XPATH, path + path_ext)
    stat = []
    i = 0
    while i < len(raw_stat):
        stat_1 = raw_stat[i].text
        stat.append(stat_1)
        i += 1
    return stat[0], stat[1]

def get_sup_stats(path, path_ext):
    raw_stat = driver.find_elements(By.XPATH, path + path_ext)
    stat = []
    i = 1
    while i < len(raw_stat):
        stat_1 = raw_stat[i].text.replace('(', '').replace(')', '')
        stat.append(stat_1)
        i += 2
    return stat[0], stat[1]

def percent_str_to_float_or_null(percent_str):
    percent = percent_str.strip().replace("%", "")
    try:
        percent = float(percent)
    except:
        percent = 'NULL'
    return percent

def length_to_inches(length):
    length = length.strip()
    try:
        lengths = length.split("' ",1)
        length_ft1 = int(lengths[0])
        length_in1 = int(lengths[1])
        length_ft = (length_ft1 * 12) + length_in1
    except:
        length_ft = 'NULL'
        
    return length_ft

def str_to_float_or_null(result):
    result = result.strip().replace(',', '')
    try:
        if result == '-':
            result_float = 'NULL'
        else:
            result_float = float(result)
    except:
        result_float = 'NULL'
    return result_float
    
def str_to_int_or_null(result):
    try:
        result = result.strip().replace(',', '')
    except:
        result = 'NULL'
    try:
        if result == '-':
            result_int = 'NULL'
        else:
            result_int = int(result)
    except:
        result_int = 'NULL'
    return result_int

def str_to_int_or_zero(result):
    try:
        result = result.strip().replace(',', '')
    except:
        result = 0
    try:
        if result == '-':
            result_int = 0
        else:
            result_int = int(result)
    except:
        result_int = 0
    return result_int
    
def str_money_to_int_or_zero(result):
    try:
        result = result.strip().replace(',', '').replace('$', '')
    except:
        result = 0
    try:
        if result == '-':
            result_int = 0
        else:
            result_int = int(result)
    except:
        result_int = 0
    return result_int

def height_to_inches(length):
    try:
        length = length.strip().replace('"','')
    except:
        length = 'NULL'
    try:
        lengths = length.split("' ",1)
        length_ft1 = int(lengths[0])
        length_in1 = int(lengths[1])
        length_ft = (length_ft1 * 12) + length_in1
    except:
        length_ft = 'NULL'
        
    return length_ft

def str_to_str_or_null(result):
    try:
        result = result.strip()
    except:
        result = 'NULL'
    try:
        result.replace(',', '')
    except:
        result = 'NULL'
    try:
        if result == '-':
            result_str = 'NULL'
        else:
            result_str = result
    except:
        result_str = 'NULL'
    return result_str











def convert_dict_to_df(list_of_dicts):
    df = pd.DataFrame(list_of_dicts)
    return df
    
    
bad_links = []
#lnc = extract_link_list(url)
#print(lnc)
# career_stats_df = pd.DataFrame()
# player_list_df = pd.DataFrame()
# all_yearly_stats_df = pd.DataFrame()

#links = lnc[0]
#names = lnc[1]
#countries = lnc[2]


# save links to csv
#links_df = pd.DataFrame(lnc)
#links_df.to_csv('player_links.csv', index=False)

# read csv
#links_read_df = pd.read_csv('player_links.csv')
#links_read_df = pd.read_csv('completed_players.csv')
links_read_df = pd.read_csv('new-player-links-EXTRA-1.csv')
links2 = links_read_df.values.tolist()
link = links2[0]
name = links2[1]
#countries = links2[2]

print(link)

i = 0
print(len(link))

print(len(name))
for i in range(len(link)):
    career_stats_df = pd.DataFrame()
    player_list_df = pd.DataFrame()
    all_yearly_stats_df = pd.DataFrame()
    player_list = []
    
    #print(names[i])
    print(name[i])
    soup = extract_player_soup(link[i])
    player_info = get_player_info(soup)
    player_list.append(player_info[0])
    player_id_num = player_info[2]
    
    if player_info[1] == False:
        bad_links.append(link[i])

    career_stats = get_player_stats(soup)
    career_df = convert_dict_to_df(career_stats)
    career_stats_df = pd.concat([career_stats_df, career_df], ignore_index=True)
    yearly_stats = get_season_stats(link[i], player_id_num)
    yearly_stats_df = convert_dict_to_df(yearly_stats)
    all_yearly_stats_df = pd.concat([all_yearly_stats_df, yearly_stats_df], ignore_index=True)
    player_list_df = convert_dict_to_df(player_list)
    #player_list_df = pd.concat([player_list_df, player_li_df], ignore_index=True)
    player_list_df.to_csv('player_list-EXTRA-4.csv', mode='a',index=True, header=False)
    career_stats_df.to_csv('career_stats-EXTRA-4.csv', mode='a',index=True, header=False)
    all_yearly_stats_df.to_csv('all_yearly_stats-EXTRA-4.csv', mode='a',index=True, header=False)
    print(player_list_df)
    print(career_stats_df)
    print(all_yearly_stats_df)
    player_count += 1
    if player_count == 500:
        break

#player_list_df = convert_dict_to_df(player_list)
print('bad links: ', bad_links)
# print(player_list_df)
# print(career_stats_df)
# print(all_yearly_stats_df)
# player_list_df.to_csv('player_list.csv', mode='a',index=True, header=False)
# career_stats_df.to_csv('career_stats.csv', mode='a',index=True, header=False)
# all_yearly_stats_df.to_csv('all_yearly_stats.csv', mode='a',index=True, header=False)