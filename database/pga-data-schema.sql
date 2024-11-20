--


CREATE TABLE PLAYERS(
  player_id INT,
  first_name VARCHAR(30) NOT NULL,
  last_name VARCHAR(30) NOT NULL,
  full_name VARCHAR(60) NOT NULL,
  birth_country VARCHAR(30) DEFAULT NULL,
  birth_city VARCHAR(30) DEFAULT NULL,
  birth_state VARCHAR(30) DEFAULT NULL,
  birth_date DATE DEFAULT NULL,
  career_earnings INT DEFAULT NULL,
  height INT DEFAULT NULL,
  weight INT DEFAULT NULL,
  turned_pro YEAR DEFAULT NULL,
  college VARCHAR(65) DEFAULT NULL,
  plays_from_city VARCHAR(30) DEFAULT NULL,
  plays_from_state VARCHAR(30) DEFAULT NULL,
  plays_from_country VARCHAR(30) DEFAULT NULL,
  CONSTRAINT PK_Players PRIMARY KEY(player_id)
);

LOAD DATA INFILE 'database_files/player_list2.csv'
INTO TABLE PLAYERS
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

CREATE TABLE YEARS (
  year YEAR PRIMARY KEY
);


LOAD DATA INFILE 'database_files/years.csv'
INTO TABLE YEARS
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

CREATE TABLE DRIVING_DISTANCE_MAX_AVG(
  year YEAR PRIMARY KEY,
  avg_driving_distance DECIMAL(4,1) NOT NULL,
  max_avg_driving_distance DECIMAL(4,1) NOT NULL,
  avg_driving_distance_all DECIMAL(4,1) DEFAULT NULL,
  max_avg_driving_distance_all DECIMAL(4,1) DEFAULT NULL,
  clubhead_speed_avg DECIMAL(6,2) DEFAULT NULL,
  max_avg_clubhead_speed DECIMAL(5,2) DEFAULT NULL,
  max_speed_player VARCHAR(60) DEFAULT NULL,
  max_speed_player_id INT DEFAULT NULL,
  driving_distance_leader VARCHAR(60) DEFAULT NULL,
  driving_distance_leader_id INT DEFAULT NULL,
  CONSTRAINT FK_Driving_Distance_Max_Avg_Year FOREIGN KEY (year) REFERENCES YEARS (year),
  CONSTRAINT FK_Driving_Distance_Max_Avg_Player_Speed FOREIGN KEY (max_speed_player_id) REFERENCES PLAYERS (player_id),
  CONSTRAINT FK_Driving_Distance_Max_Avg_Player_Distance FOREIGN KEY (driving_distance_leader_id) REFERENCES PLAYERS (player_id)
);

LOAD DATA INFILE 'database_files/driving_distance-max_avg_by_year.csv'
INTO TABLE DRIVING_DISTANCE_MAX_AVG
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

CREATE TABLE ALL_YEARLY_STATS(
  stat_id INT,
  player_id INT NOT NULL,
  year YEAR NOT NULL,
  season VARCHAR(10) NOT NULL,
  age_end_yr INT DEFAULT NULL,
  sg_total DECIMAL(5,3) DEFAULT NULL,
  sg_total_rank INT DEFAULT NULL,
  sg_total_total DECIMAL(7,3) DEFAULT NULL,
  sg_total_measured_rounds INT DEFAULT NULL,
  sg_tee_to_green DECIMAL(5,3) DEFAULT NULL,
  sg_tee_to_green_rank INT DEFAULT NULL,
  sg_off_tee DECIMAL(5,3) DEFAULT NULL,
  sg_off_tee_rank INT DEFAULT NULL,
  sg_off_tee_total DECIMAL(7,3) DEFAULT NULL,
  sg_app_green DECIMAL(5,3) DEFAULT NULL,
  sg_app_green_rank INT DEFAULT NULL,
  sg_app_green_total DECIMAL(7,3) DEFAULT NULL,
  sg_around_green DECIMAL(5,3) DEFAULT NULL,
  sg_around_green_rank INT DEFAULT NULL,
  sg_around_green_total DECIMAL(7,3) DEFAULT NULL,
  sg_putting DECIMAL(5,3) DEFAULT NULL,
  sg_putting_rank INT DEFAULT NULL,
  sg_putting_total DECIMAL(7,3) DEFAULT NULL,
  total_driving INT DEFAULT NULL,
  total_driving_rank INT DEFAULT NULL,
  longest_drive INT DEFAULT NULL,
  longest_drive_rank INT DEFAULT NULL,
  longest_drive_tourney VARCHAR(30) DEFAULT NULL,
  driving_distance DECIMAL(4,1) DEFAULT NULL,
  driving_distance_rank INT DEFAULT NULL,
  driving_distance_total INT DEFAULT NULL,
  driving_distance_total_drives INT DEFAULT NULL,
  driving_distance_all_drives DECIMAL(4,1) DEFAULT NULL,
  driving_distance_all_drives_rank INT DEFAULT NULL,
  driving_distance_all_drives_total INT DEFAULT NULL,
  driving_distance_all_drives_total_drives INT DEFAULT NULL,
  driving_accuracy DECIMAL(5,2) DEFAULT NULL,
  driving_accuracy_rank INT DEFAULT NULL,
  fairways_hit INT DEFAULT NULL,
  fairways_possible INT DEFAULT NULL,
  left_rough_tendency DECIMAL(5,2) DEFAULT NULL,
  left_rough_tendency_rank INT DEFAULT NULL,
  left_rough_total INT DEFAULT NULL,
  left_rough_possible_fairways INT DEFAULT NULL,
  right_rough_tendency DECIMAL(5,2) DEFAULT NULL,
  right_rough_tendency_rank INT DEFAULT NULL,
  right_rough_total INT DEFAULT NULL,
  right_rough_possible_fairways INT DEFAULT NULL,
  distance_from_edge_frwy_in INT DEFAULT NULL,
  distance_from_edge_frwy_rank INT DEFAULT NULL,
  distance_from_edge_frwy_total_ft DECIMAL(8,3) DEFAULT NULL,
  distance_from_edge_frwy_strokes INT DEFAULT NULL,
  club_head_speed DECIMAL(5,2) DEFAULT NULL,
  club_head_speed_rank INT DEFAULT NULL,
  club_head_speed_total DECIMAL(7,2) DEFAULT NULL,
  club_head_speed_attempts INT DEFAULT NULL,
  total_driving_efficiency INT DEFAULT NULL,
  total_driving_efficiency_rank INT DEFAULT NULL,
  carry_efficiency_rank INT DEFAULT NULL,
  greens_in_regulation_percent DECIMAL(5,2) DEFAULT NULL,
  greens_in_regulation_percent_rank INT DEFAULT NULL,
  greens_hit INT DEFAULT NULL,
  greens_possible INT DEFAULT NULL,
  proximity_to_hole_in INT DEFAULT NULL,
  proximity_to_hole_rank INT DEFAULT NULL,
  proximity_to_hole_total_ft DECIMAL(8,3) DEFAULT NULL,
  proximity_to_hole_total_att INT DEFAULT NULL,
  approach_more_275_in INT DEFAULT NULL,
  approach_more_275_rank INT DEFAULT NULL,
  approach_more_275_total_ft DECIMAL(8,3) DEFAULT NULL,
  approach_more_275_total_att INT DEFAULT NULL,
  approach_250_275_in INT DEFAULT NULL,
  approach_250_275_rank INT DEFAULT NULL,
  approach_250_275_total_ft DECIMAL(8,3) DEFAULT NULL,
  approach_250_275_total_att INT DEFAULT NULL,
  approach_225_250_in INT DEFAULT NULL,
  approach_225_250_rank INT DEFAULT NULL,
  approach_225_250_total_ft DECIMAL(8,3) DEFAULT NULL,
  approach_225_250_total_att INT DEFAULT NULL,
  approach_200_225_in INT DEFAULT NULL,
  approach_200_225_rank INT DEFAULT NULL,
  approach_200_225_total_ft DECIMAL(8,3) DEFAULT NULL,
  approach_200_225_total_att INT DEFAULT NULL,
  approach_more_200_in INT DEFAULT NULL,
  approach_more_200_rank INT DEFAULT NULL,
  approach_more_200_total_ft DECIMAL(8,3) DEFAULT NULL,
  approach_more_200_total_att INT DEFAULT NULL,
  approach_175_200_in INT DEFAULT NULL,
  approach_175_200_rank INT DEFAULT NULL,
  approach_175_200_total_ft DECIMAL(8,3) DEFAULT NULL,
  approach_175_200_total_att INT DEFAULT NULL,
  approach_150_175_in INT DEFAULT NULL,
  approach_150_175_rank INT DEFAULT NULL,
  approach_150_175_total_ft DECIMAL(8,3) DEFAULT NULL,
  approach_150_175_total_att INT DEFAULT NULL,
  approach_125_150_in INT DEFAULT NULL,
  approach_125_150_rank INT DEFAULT NULL,
  approach_125_150_total_ft DECIMAL(8,3) DEFAULT NULL,
  approach_125_150_total_att INT DEFAULT NULL,
  approach_50_125_in INT DEFAULT NULL,
  approach_50_125_rank INT DEFAULT NULL,
  approach_50_125_total_ft DECIMAL(8,3) DEFAULT NULL,
  approach_50_125_total_att INT DEFAULT NULL,
  approach_100_125_in INT DEFAULT NULL,
  approach_100_125_rank INT DEFAULT NULL,
  approach_100_125_total_ft DECIMAL(8,3) DEFAULT NULL,
  approach_100_125_total_att INT DEFAULT NULL,
  approach_75_100_in INT DEFAULT NULL,
  approach_75_100_rank INT DEFAULT NULL,
  approach_75_100_total_ft DECIMAL(8,3) DEFAULT NULL,
  approach_75_100_total_att INT DEFAULT NULL,
  approach_50_75_in INT DEFAULT NULL,
  approach_50_75_rank INT DEFAULT NULL,
  approach_50_75_total_ft DECIMAL(7,3) DEFAULt NULL,
  approach_50_75_total_att INT DEFAULT NULL,
  approach_less_100_in INT DEFAULT NULL,
  approach_less_100_rank INT DEFAULT NULL,
  approach_less_100_total_ft DECIMAL(8,3) DEFAULT NULL,
  approach_less_100_total_att INT DEFAULT NULL,
  approach_more_100_in INT DEFAULT NULL,
  approach_more_100_rank INT DEFAULT NULL,
  approach_more_100_total_ft DECIMAL(8,3) DEFAULT NULL,
  approach_more_100_total_att INT DEFAULT NULL,
  fairway_proximity INT DEFAULT NULL,
  fairway_proximity_rank INT DEFAULT NULL,
  fairway_proximity_att INT DEFAULT NULL,
  rough_proximity INT DEFAULT NULL,
  rough_proximity_rank INT DEFAULT NULL,
  rough_proximity_total_in INT DEFAULT NULL,
  rough_proximity_total_att INT DEFAULT NULL,
  left_rough_proximity INT DEFAULT NULL,
  left_rough_proximity_rank INT DEFAULT NULL,
  left_rough_proximity_att INT DEFAULT NULL,
  right_rough_proximity INT DEFAULT NULL,
  right_rough_proximity_rank INT DEFAULT NULL,
  right_rough_proximity_att INT DEFAULT NULL,
  approach_more_275_rough_in INT DEFAULT NULL,
  approach_more_275_rough_rank INT DEFAULT NULL,
  approach_more_275_rough_total_ft DECIMAL(8,3) DEFAULT NULL,
  approach_more_275_rough_total_att INT DEFAULT NULL,
  approach_250_275_rough_in INT DEFAULT NULL,
  approach_250_275_rough_rank INT DEFAULT NULL,
  approach_250_275_rough_total_ft DECIMAL(8,3) DEFAULT NULL,
  approach_250_275_rough_total_att INT DEFAULT NULL,
  approach_225_250_rough_in INT DEFAULT NULL,
  approach_225_250_rough_rank INT DEFAULT NULL,
  approach_225_250_rough_total_ft DECIMAL(8,3) DEFAULT NULL,
  approach_225_250_rough_total_att INT DEFAULT NULL,
  approach_200_225_rough_in INT DEFAULT NULL,
  approach_200_225_rough_rank INT DEFAULT NULL,
  approach_200_225_rough_total_ft DECIMAL(8,3) DEFAULT NULL,
  approach_200_225_rough_total_att INT DEFAULT NULL,
  approach_more_100_rough_in INT DEFAULT NULL,
  approach_more_100_rough_rank INT DEFAULT NULL,
  approach_more_100_rough_total_ft DECIMAL(8,3) DEFAULT NULL,
  approach_more_100_rough_total_att INT DEFAULT NULL,
  approach_less_100_rough_in INT DEFAULT NULL,
  approach_less_100_rough_rank INT DEFAULT NULL,
  approach_less_100_rough_total_ft DECIMAL(8,3) DEFAULT NULL,
  approach_less_100_rough_total_att INT DEFAULT NULL,
  approach_more_200_rough_in INT DEFAULT NULL,
  approach_more_200_rough_rank INT DEFAULT NULL,
  approach_more_200_rough_total_ft DECIMAL(8,3) DEFAULT NULL,
  approach_more_200_rough_total_att INT DEFAULT NULL,
  approach_175_200_rough_in INT DEFAULT NULL,
  approach_175_200_rough_rank INT DEFAULT NULL,
  approach_175_200_rough_total_ft DECIMAL(8,3) DEFAULT NULL,
  approach_175_200_rough_total_att INT DEFAULT NULL,
  approach_150_175_rough_in INT DEFAULT NULL,
  approach_150_175_rough_rank INT DEFAULT NULL,
  approach_150_175_rough_total_ft DECIMAL(8,3) DEFAULT NULL,
  approach_150_175_rough_total_att INT DEFAULT NULL,
  approach_125_150_rough_in INT DEFAULT NULL,
  approach_125_150_rough_rank INT DEFAULT NULL,
  approach_125_150_rough_total_ft DECIMAL(8,3) DEFAULT NULL,
  approach_125_150_rough_total_att INT DEFAULT NULL,
  approach_50_125_rough_in INT DEFAULT NULL,
  approach_50_125_rough_rank INT DEFAULT NULL,
  approach_50_125_rough_total_ft DECIMAL(8,3) DEFAULT NULL,
  approach_50_125_rough_total_att INT DEFAULT NULL,
  approach_100_125_rough_in INT DEFAULT NULL,
  approach_100_125_rough_rank INT DEFAULT NULL,
  approach_100_125_rough_total_ft DECIMAL(8,3) DEFAULT NULL,
  approach_100_125_rough_total_att INT DEFAULT NULL,
  approach_75_100_rough_in INT DEFAULT NULL,
  approach_75_100_rough_rank INT DEFAULT NULL,
  approach_75_100_rough_total_ft DECIMAL(8,3) DEFAULT NULL,
  approach_75_100_rough_total_att INT DEFAULT NULL,
  approach_50_75_rough_in INT DEFAULT NULL,
  approach_50_75_rough_rank INT DEFAULT NULL,
  approach_50_75_rough_total_ft DECIMAL(8,3) DEFAULT NULL,
  approach_50_75_rough_total_att INT DEFAULT NULL,
  going_for_green_percent DECIMAL(5,2) DEFAULT NULL,
  going_for_green_percent_rank INT DEFAULT NULL,
  going_for_green_percent_attempts INT DEFAULT NULL,
  going_for_green_percent_non_attemptes INT DEFAULT NULL,
  going_for_green_hit_percent DECIMAL(5,2) DEFAULT NULL,
  going_for_green_hit_rank INT DEFAULT NULL,
  going_for_green_hit INT DEFAULT NULL,
  going_for_green_attempts INT DEFAULT NULL,
  going_for_green_birdie_better_pct DECIMAL(5,2) DEFAULT NULL,
  going_for_green_birdie_better_pct_rank INT DEFAULT NULL,
  going_for_green_birdie_better_total INT DEFAULT NULL,
  total_hole_outs INT DEFAULT NULL,
  total_hole_outs_rank INT DEFAULT NULL,
  longest_hole_out_yrds INT DEFAULT NULL,
  longest_hole_out_rank INT DEFAULT NULL,
  longest_hole_out_tourney VARCHAR(30) DEFAULT NULL,
  longest_hole_out_rd INT DEFAULT NULL,
  scrambling_percent DECIMAL(5,2) DEFAULT NULL,
  scrambling_rank INT DEFAULT NULL,
  scrambling_par_or_better INT DEFAULT NULL,
  scrambling_missed_gir INT DEFAULT NULL,
  scrambling_from_rough_perecnt DECIMAL(5,2) DEFAULT NULL,
  scrambling_from_rough_rank INT DEFAULT NULL,
  scrambling_from_rough_success INT DEFAULT NULL,
  scrambling_from_rough_att INT DEFAULT NULL,
  scrambling_from_fringe_percent DECIMAL(5,2) DEFAULT NULL,
  scrambling_from_fringe_rank INT DEFAULT NULL,
  scrambling_from_fringe_success INT DEFAULT NULL,
  scrambling_from_fringe_att INT DEFAULT NULL,
  scrambling_more_30_percent DECIMAL(5,2) DEFAULT NULL,
  scrambling_more_30_rank INT DEFAULT NULL,
  scrambling_more_30_success INT DEFAULT NULL,
  scrambling_more_30_att INT DEFAULT NULL,
  scrambling_20_30_percent DECIMAL(5,2) DEFAULT NULL,
  scrambling_20_30_rank INT DEFAULT NULL,
  scrambling_20_30_success INT DEFAULT NULL,
  scrambling_20_30_att INT DEFAULT NULL,
  scrambling_10_20_percent DECIMAL(5,2) DEFAULT NULL,
  scrambling_10_20_rank INT DEFAULT NULL,
  scrambling_10_20_success INT DEFAULT NULL,
  scrambling_10_20_att INT DEFAULT NULL,
  scrambling_less_10_percent DECIMAL(5,2) DEFAULT NULL,
  scrambling_less_10_rank INT DEFAULT NULL,
  scrambling_less_10_success INT DEFAULT NULL,
  scrambling_less_10_att INT DEFAULT NULL,
  sand_save_percent DECIMAL(5,2) DEFAULT NULL,
  sand_save_rank INT DEFAULT NULL,
  sand_save_saves INT DEFAULT NULL,
  sand_save_bunkers INT DEFAULT NULL,
  proximity_to_hole_sand INT DEFAULT NULL,
  proximity_to_hole_sand_rank INT DEFAULT NULL,
  proximity_to_hole_sand_total_ft DECIMAL(8,3) DEFAULT NULL,
  proximity_to_hole_sand_shots INT DEFAULT NULL,
  total_putting DECIMAL(5,1) DEFAULT NULL,
  total_putting_rank INT DEFAULT NULL,
  putting_avg DECIMAL(4,3) DEFAULT NULL,
  putting_avg_rank INT DEFAULT NULL,
  putting_avg_gir_putts INT DEFAULT NULL,
  putting_avg_greens_hit INT DEFAULT NULL,
  overall_putting_avg DECIMAL(4,3) DEFAULT NULL,
  overall_putting_avg_rank INT DEFAULT NULL,
  overall_putting_total_putts INT DEFAULT NULL,
  overall_putting_total_holes INT DEFAULT NULL,
  birdie_or_better_conversion_percent DECIMAL(5,2) DEFAULT NULL,
  birdie_or_better_conversion_rank INT DEFAULT NULL,
  birdie_or_better_conversion_birdies INT DEFAULT NULL,
  birdie_or_better_conversion_greens_hit INT DEFAULT NULL,
  putts_per_round DECIMAL(5,2) DEFAULT NULL,
  putts_per_round_rank INT DEFAULT NULL,
  total_putts INT DEFAULT NULL,
  total_rounds INT DEFAULT NULL,
  putts_per_round_rd1 INT DEFAULT NULL,
  putts_per_round_rd1_rank INT DEFAULT NULL,
  total_putts_rd1 INT DEFAULT NULL,
  total_rounds_rd1 INT DEFAULT NULL,
  putts_per_round_rd2 DECIMAL(5,2) DEFAULT NULL,
  putts_per_round_rd2_rank INT DEFAULT NULL,
  total_putts_rd2 INT DEFAULT NULL,
  total_rounds_rd2 INT DEFAULT NULL,
  putts_per_round_rd3 DECIMAL(5,2) DEFAULT NULL,
  putts_per_round_rd3_rank INT DEFAULT NULL,
  total_putts_rd3 INT DEFAULT NULL,
  total_rounds_rd3 INT DEFAULT NULL,
  putts_per_round_rd4 DECIMAL(5,2) DEFAULT NULL,
  putts_per_round_rd4_rank INT DEFAULT NULL,
  total_putts_rd4 INT DEFAULT NULL,
  total_rounds_rd4 INT DEFAULT NULL,
  one_putt_percentage DECIMAL(5,2) DEFAULT NULL,
  one_putt_rank INT DEFAULT NULL,
  one_putt_total INT DEFAULT NULL,
  one_putt_total_holes INT DEFAULT NULL,
  longest_putt INT DEFAULT NULL,
  longest_putt_break INT DEFAULT NULL,
  longest_putt_tourney VARCHAR(30) DEFAULT NULL,
  longest_putt_rd INT DEFAULT NULL,
  three_putt_avoidance DECIMAL(5,2) DEFAULT NULL,
  three_putt_avoidance_rank INT DEFAULT NULL,
  three_putt_total INT DEFAULT NULL,
  three_putt_total_holes INT DEFAULT NULL,
  putting_more_25_percent DECIMAL(5,2) DEFAULT NULL,
  putting_more_25_rank INT DEFAULT NULL,
  putting_more_25_att INT DEFAULT NULL,
  putting_more_25_made INT DEFAULT NULL,
  putting_20_25_percent DECIMAL(5,2) DEFAULT NULL,
  putting_20_25_rank INT DEFAULT NULL,
  putting_20_25_att INT DEFAULT NULL,
  putting_20_25_made INT DEFAULT NULL,
  putting_15_20_percent DECIMAL(5,2) DEFAULT NULL,
  putting_15_20_rank INT DEFAULT NULL,
  putting_15_20_att INT DEFAULT NULL,
  putting_15_20_made INT DEFAULT NULL,
  putting_10_15_percent DECIMAL(5,2) DEFAULT NULL,
  putting_10_15_rank INT DEFAULT NULL,
  putting_10_15_att INT DEFAULT NULL,
  putting_10_15_made INT DEFAULT NULL,
  putting_less_10_percent DECIMAL(5,2) DEFAULT NULL,
  putting_less_10_rank INT DEFAULT NULL,
  putting_less_10_att INT DEFAULT NULL,
  putting_less_10_made INT DEFAULT NULL,
  putting_from_10_percent DECIMAL(5,2) DEFAULT NULL,
  putting_from_10_rank INT DEFAULT NULL,
  putting_from_10_att INT DEFAULT NULL,
  putting_from_9_percent DECIMAL(5,2) DEFAULT NULL,
  putting_from_9_rank INT DEFAULT NULL,
  putting_from_9_att INT DEFAULT NULL,
  putting_from_8_percent DECIMAL(5,2) DEFAULT NULL,
  putting_from_8_rank INT DEFAULT NULL,
  putting_from_8_att INT DEFAULT NULL,
  putting_from_7_percent DECIMAL(5,2) DEFAULT NULL,
  putting_from_7_rank INT DEFAULT NULL,
  putting_from_7_att INT DEFAULT NULL,
  putting_from_6_percent DECIMAL(5,2) DEFAULT NULL,
  putting_from_6_rank INT DEFAULT NULL,
  putting_from_6_att INT DEFAULT NULL,
  putting_from_5_percent DECIMAL(5,2) DEFAULT NULL,
  putting_from_5_rank INT DEFAULT NULL,
  putting_from_5_att INT DEFAULT NULL,
  putting_from_4_8_percent DECIMAL(5,2) DEFAULT NULL,
  putting_from_4_8_rank INT DEFAULT NULL,
  putting_from_4_8_att INT DEFAULT NULL,
  putting_from_4_8_made INT DEFAULT NULL,
  putting_from_4_percent DECIMAL(5,2) DEFAULT NULL,
  putting_from_4_rank INT DEFAULT NULL,
  putting_from_4_att INT DEFAULT NULL,
  putting_from_3_percent DECIMAL(5,2) DEFAULT NULL,
  putting_from_3_rank INT DEFAULT NULL,
  putting_from_3_att INT DEFAULT NULL,
  avg_distance_putts_made INT DEFAULT NULL,
  avg_distance_putts_made_rank INT DEFAULT NULL,
  avg_distance_putts_made_in INT DEFAULT NULL,
  avg_distance_putts_made_rounds INT DEFAULT NULL,
  approach_putt_performance INT DEFAULT NULL,
  approach_putt_rank INT DEFAULT NULL,
  approach_putt_att INT DEFAULT NULL,
  scoring_avg_adj DECIMAL(6,3) DEFAULT NULL,
  scoring_avg_adj_rank INT DEFAULT NULL,
  scoring_avg_adj_total_strokes INT DEFAULT NULL,
  scoring_avg_adj_total_adjustment DECIMAL(6,3) DEFAULT NULL,
  scoring_avg_actual DECIMAL(5,2) DEFAULT NULL,
  scoring_avg_actual_rank INT DEFAULT NULL,
  scoring_avg_actual_total_strokes INT DEFAULT NULL,
  scoring_avg_actual_total_rounds INT DEFAULT NULL,
  lowest_round INT DEFAULT NULL,
  lowest_round_rank INT DEFAULT NULL,
  lowest_round_tourney VARCHAR(30) DEFAULT NULL,
  lowest_round_round INT DEFAULT NULL,
  birdie_avg DECIMAL(3,2) DEFAULT NULL,
  birdie_avg_rank INT DEFAULT NULL,
  birdie_avg_num_birdies INT DEFAULT NULL,
  birdie_avg_total_rounds INT DEFAULT NULL,
  total_birdies INT DEFAULT NULL,
  total_birdies_rank INT DEFAULT NULL,
  eagles_holes_per DECIMAL(5,1) DEFAULT NULL,
  eagles_holes_per_rank INT DEFAULT NULL,
  total_eagles INT DEFAULT NULL,
  total_eagles_rank INT DEFAULT NULL,
  par_breaker_percent DECIMAL(5,2) DEFAULT NULL,
  par_breaker_rank INT DEFAULT NULL,
  bounce_back_percent DECIMAL(5,2) DEFAULT NULL,
  bounce_back_rank INT DEFAULT NULL,
  par3_birdie_or_better DECIMAL(5,2) DEFAULT NULL,
  par3_birdie_or_better_rank INT DEFAULT NULL,
  par3_birdie_or_better_total INT DEFAULT NULL,
  par3_holes INT DEFAULT NULL,
  par4_birdie_or_better DECIMAL(5,2) DEFAULT NULL,
  par4_birdie_or_better_rank INT DEFAULT NULL,
  par4_birdie_or_better_total INT DEFAULT NULL,
  par4_holes INT DEFAULT NULL,
  par5_birdie_or_better DECIMAL(5,2) DEFAULT NULL,
  par5_birdie_or_better_rank INT DEFAULT NULL,
  par5_birdie_or_better_total INT DEFAULT NULL,
  par5_holes INT DEFAULT NULL,
  birdie_or_better_percent DECIMAL(5,2) DEFAULT NULL,
  birdie_or_better_rank INT DEFAULT NULL,
  bogey_avoidance_percent DECIMAL(5,2) DEFAULT NULL,
  bogey_avoidance_rank INT DEFAULT NULL,
  bogey_total INT DEFAULT NULL,
  final_round_scoring_avg DECIMAL(4,2) DEFAULT NULL,
  final_round_scoring_avg_rank INT DEFAULT NULL,
  final_round_scoring_total_strokes INT DEFAULT NULL,
  final_round_scoring_total_rds INT DEFAULT NULL,
  final_round_performance DECIMAL(5,2) DEFAULT NULL,
  final_round_performance_rank INT DEFAULT NULL,
  rd1_scoring_avg DECIMAL(5,2) DEFAULT NULL,
  rd1_scoring_avg_rank INT DEFAULT NULL,
  rd1_scoring_total_strokes INT DEFAULT NULL,
  rd1_scoring_total_rds INT DEFAULT NULL,
  rd2_scoring_avg DECIMAL(5,2) DEFAULT NULL,
  rd2_scoring_avg_rank INT DEFAULT NULL,
  rd2_scoring_total_strokes INT DEFAULT NULL,
  rd2_scoring_total_rds INT DEFAULT NULL,
  rd3_scoring_avg DECIMAL(5,2) DEFAULT NULL,
  rd3_scoring_avg_rank INT DEFAULT NULL,
  rd3_scoring_total_strokes INT DEFAULT NULL,
  rd3_scoring_total_rds INT DEFAULT NULL,
  rd4_scoring_avg DECIMAL(5,2) DEFAULT NULL,
  rd4_scoring_avg_rank INT DEFAULT NULL,
  rd4_scoring_total_strokes INT DEFAULT NULL,
  rd4_scoring_total_rds INT DEFAULT NULL,
  par3_scoring_avg DECIMAL(3,2) DEFAULT NULL,
  par3_scoring_avg_rank INT DEFAULT NULL,
  par3_scoring_avg_strokes INT DEFAULT NULL,
  par3_scoring_avg_holes INT DEFAULT NULL,
  par4_scoring_avg DECIMAL(3,2) DEFAULT NULL,
  par4_scoring_avg_rank INT DEFAULT NULL,
  par4_scoring_avg_strokes INT DEFAULT NULL,
  par4_scoring_avg_holes INT DEFAULT NULL,
  par5_scoring_avg DECIMAL(3,2) DEFAULT NULL,
  par5_scoring_avg_rank INT DEFAULT NULL,
  par5_scoring_avg_strokes INT DEFAULT NULL,
  par5_scoring_avg_holes INT DEFAULT NULL,
  front9_scoring_avg DECIMAL(4,2) DEFAULT NULL,
  front9_scoring_avg_rank INT DEFAULT NULL,
  front9_scoring_avg_strokes INT DEFAULT NULL,
  front9_scoring_avg_holes INT DEFAULT NULL,
  back9_scoring_avg DECIMAL(4,2) DEFAULT NULL,
  back9_scoring_avg_rank INT DEFAULT NULL,
  back9_scoring_avg_strokes INT DEFAULT NULL,
  back9_scoring_avg_holes INT DEFAULT NULL,
  early_scoring_avg DECIMAL(5,2) DEFAULT NULL,
  early_scoring_avg_rank INT DEFAULT NULL,
  early_scoring_total_strokes INT DEFAULT NULL,
  early_scoring_total_rounds INT DEFAULT NULL,
  late_scoring_avg DECIMAL(5,2) DEFAULT NULL,
  late_scoring_avg_rank INT DEFAULT NULL,
  late_scoring_total_strokes INT DEFAULT NULL,
  late_scoring_total_rounds INT DEFAULT NULL,
  consecutive_cuts INT DEFAULT NULL,
  consecutive_cuts_rank INT DEFAULT NULL,
  consecutive_fairways_hit INT DEFAULT NULL,
  consecutive_fairways_hit_rank INT DEFAULT NULL,
  consecutive_gir INT DEFAULT NULL,
  consecutive_gir_rank INT DEFAULT NULL,
  consecutive_sand_saves INT DEFAULT NULL,
  consecutive_sand_saves_rank INT DEFAULT NULL,
  best_ytd_1_putt_or_better_streak INT DEFAULT NULL,
  best_ytd_1_putt_or_better_streak_rank INT DEFAULT NULL,
  best_ytd_streak_wo_3_putt INT DEFAULT NULL,
  best_ytd_streak_wo_3_putt_rank INT DEFAULT NULL,
  ytd_par_or_better_streak INT DEFAULT NULL,
  ytd_par_or_better_streak_rank INT DEFAULT NULL,
  consecutive_par_3_birdies INT DEFAULT NULL,
  consecutive_par_3_birdies_rank INT DEFAULT NULL,
  consecutive_holes_below_par INT DEFAULT NULL,
  consecutive_holes_below_par_rank INT DEFAULT NULL,
  consecutive_birdies_streak INT DEFAULT NULL,
  consecutive_birdies_streak_rank INT DEFAULT NULL,
  consecutive_birdies_eagles_streak INT DEFAULT NULL,
  consecutive_birdies_eagles_streak_rank INT DEFAULT NULL,
  official_money INT DEFAULT NULL,
  official_money_rank INT DEFAULT NULL,
  fedexcup_regular_season_points INT DEFAULT NULL,
  fedexcup_rank INT DEFAULT NULL,
  wins INT DEFAULT NULL,
  top_10s INT DEFAULT NULL,
  CONSTRAINT PK_All_Yearly_Stats PRIMARY KEY(stat_id),
  CONSTRAINT FK_All_Yearly_Stats_Players FOREIGN KEY (player_id) REFERENCES PLAYERS(player_id),
  CONSTRAINT FK_All_Yearly_Stats_Years FOREIGN KEY (year) REFERENCES YEARS(year)
);


LOAD DATA INFILE 'database_files/all_yearly_stats2.csv'
INTO TABLE ALL_YEARLY_STATS
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

CREATE TABLE WINNERS_PER_YEAR(
  winner_id INT PRIMARY KEY AUTO_INCREMENT,
  year YEAR NOT NULL,
  player_id INT,
  winner VARCHAR(60) NOT NULL,
  wins INT NOT NULL,
  CONSTRAINT FK_Winners_Per_Year_Year FOREIGN KEY (year) REFERENCES YEARS(year),
  CONSTRAINT FK_Winners_Per_Year_Players FOREIGN KEY (player_id) REFERENCES PLAYERS(player_id),
  CONSTRAINT UQ_Winners_Per_Year UNIQUE (year, player_id)
);

LOAD DATA INFILE 'database_files/winners-per-year.csv'
INTO TABLE WINNERS_PER_YEAR
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

CREATE TABLE WINNERS_PER_YEAR_BY_PLAYER(
  win_id INT PRIMARY KEY AUTO_INCREMENT,
  year YEAR NOT NULL,
  player_id INT,
  winner VARCHAR(60) NOT NULL,
  wins INT DEFAULT NULL,
  team_wins INT DEFAULT NULL,
  CONSTRAINT FK_Winners_Per_Year_By_Players_Year FOREIGN KEY (year) REFERENCES YEARS(year),
  CONSTRAINT FK_Winners_Per_Year__By_Players_Players FOREIGN KEY (player_id) REFERENCES PLAYERS(player_id),
  CONSTRAINT UQ_Winners_Per_Year_By_Players_ UNIQUE (year, player_id)
);

LOAD DATA INFILE 'database_files/winners-per-year-by-player.csv'
INTO TABLE WINNERS_PER_YEAR_BY_PLAYER
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

CREATE TABLE SCORING_AVERAGE(
  avg_id INT PRIMARY KEY AUTO_INCREMENT,
  year YEAR NOT NULL,
  adj_scoring_avg DECIMAL(5,3) DEFAULT NULL,
  actual_scoring_avg DECIMAL(5,3) DEFAULT NULL,
  player_id_1st INT DEFAULT NULL,
  player_name_1st VARCHAR(60) DEFAULT NULL,
  rounds_1st INT DEFAULT NULL,
  actual_avg_1st DECIMAL(5,3) DEFAULT NULL,
  total_strokes_1st INT DEFAULT NULL,
  total_rounds_1st INT DEFAULT NULL,
  player_id_2nd INT DEFAULT NULL,
  player_name_2nd VARCHAR(60) DEFAULT NULL,
  rounds_2nd INT DEFAULT NULL,
  actual_avg_2nd DECIMAL(5,3) DEFAULT NULL,
  total_strokes_2nd INT DEFAULT NULL,
  total_rounds_2nd INT DEFAULT NULL,
  difference_1st_2nd DECIMAL(5,3) DEFAULT NULL,
  adj_player_id_1st INT DEFAULT NULL,
  adj_player_name_1st VARCHAR(60) DEFAULT NULL,
  adj_scoring_avg_1st DECIMAL(5,3) DEFAULT NULL,
  adj_total_strokes_1st INT DEFAULT NULL,
  adj_total_adjustment_1st DECIMAL(7,3) DEFAULT NULL,
  adj_total_rounds_1st INT DEFAULT NULL,
  CONSTRAINT FK_Scoring_Average_Years FOREIGN KEY(year) REFERENCES YEARS(year),
  CONSTRAINT FK_Scoring_Average_Players_1st FOREIGN KEY(player_id_1st) REFERENCES PLAYERS(player_id),
  CONSTRAINT FK_Scoring_Average_Players_2nd FOREIGN KEY(player_id_2nd) REFERENCES PLAYERS(player_id),
  CONSTRAINT FK_Scoring_Average_Players_Adj_1st FOREIGN KEY(adj_player_id_1st) REFERENCES PLAYERS(player_id)
);

LOAD DATA INFILE 'database_files/scoring-average.csv'
INTO TABLE SCORING_AVERAGE
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;





CREATE TABLE COURSE_LIST(
  course_id INT PRIMARY KEY AUTO_INCREMENT,
  course_name VARCHAR(60) DEFAULT NULL,
  city VARCHAR(50) DEFAULT NULL,
  state VARCHAR(2) DEFAULT NULL,
  country VARCHAR(50) DEFAULT NULL
);

LOAD DATA INFILE 'database_files/course_list.csv'
INTO TABLE COURSE_LIST
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

CREATE TABLE TOURNAMENT_LIST(
  tournament_num INT PRIMARY KEY AUTO_INCREMENT,
  tournament_name VARCHAR(75) NOT NULL
);

LOAD DATA INFILE 'database_files/tournament_list.csv'
INTO TABLE TOURNAMENT_LIST
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

CREATE TABLE TOURNAMENT_WITH_YARDAGE(
  tournament_id INT PRIMARY KEY AUTO_INCREMENT,
  tournament_yr_id INT NOT NULL, -- keep track of tournaments with multiple courses played in a single year
  tournament_num INT NOT NULL, -- FK TOURNAMENT_LIST
  year YEAR NOT NULL,
  tourn_date DATE DEFAULT NULL,
  tournament_name_iteration VARCHAR(75) DEFAULT NULL,
  purse INT DEFAULT NULL,
  score INT DEFAULT NULL,
  to_par INT DEFAULT NULL,
  player_id INT DEFAULT NULL,-- FK PLAYERS
  winner_name_specific VARCHAR(100) DEFAULT NULL,
  playoff VARCHAR(4) DEFAULT NULL,
  winner_prize INT DEFAULT NULL,
  course_id INT DEFAULT NULL,-- FK COURSE_LIST
  course_name_specific VARCHAR(60) DEFAULT NULL,
  par INT DEFAULT NULL,
  yardage INT DEFAULT NULL,
  CONSTRAINT FK_Tourn_With_Yardage_Years FOREIGN KEY(year) REFERENCES YEARS(year),
  CONSTRAINT FK_Tourn_With_Yardage_Tourn_Num FOREIGN KEY(tournament_num) REFERENCES TOURNAMENT_LIST(tournament_num),
  CONSTRAINT FK_Tourn_With_Yardage_Player_Id FOREIGN KEY(player_id) REFERENCES PLAYERS(player_id),
  CONSTRAINT FK_Tourn_With_Yardage_Course_Id FOREIGN KEY(course_id) REFERENCES COURSE_LIST(course_id)
);

CREATE INDEX idx_tournament_yr_id
ON TOURNAMENT_WITH_YARDAGE (tournament_yr_id);

LOAD DATA INFILE 'database_files/tournament_with_yardage.csv'
INTO TABLE TOURNAMENT_WITH_YARDAGE
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

CREATE TABLE EVENT_STATUS(
  tour_status_id INT PRIMARY KEY AUTO_INCREMENT,
  event_status VARCHAR(50) NOT NULL
);

LOAD DATA INFILE 'database_files/event_status.csv'
INTO TABLE EVENT_STATUS
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

CREATE TABLE ALL_TOURNAMENT_AFTER_1958(
  event_id INT,
  year YEAR NOT NULL,
  date DATE NOT NULL,
  tournament_yr_id INT NOT NULL, -- FK TOURNAMENT_WITH_YARDAGE
  tournament_name VARCHAR(75) NOT NULL,
  country_specific VARCHAR(50) NOT NULL,
  location VARCHAR(50) DEFAULT NULL,
  tour_status_id INT NOT NULL, -- FK event_status
  player_id_1 INT NOT NULL, -- FK PLAYERS
  winner_1 VARCHAR(60) NOT NULL,
  win_num_1 INT DEFAULT NULL,
  owgr_pts_1 DECIMAL(5,2) DEFAULT NULL,
  player_id_2 INT DEFAULT NULL, -- FK Players
  winner_2 VARCHAR(60) DEFAULT NULL,
  win_num_2 INT DEFAULT NULL,
  CONSTRAINT FK_All_Tourn_After_1958_Years FOREIGN KEY(year) REFERENCES YEARS(year),
  CONSTRAINT FK_All_Tourn_After_1958_Yardage FOREIGN KEY(tournament_yr_id) REFERENCES TOURNAMENT_WITH_YARDAGE(tournament_yr_id),
  CONSTRAINT FK_All_Tourn_After_1958_Event_Status FOREIGN KEY(tour_status_id) REFERENCES EVENT_STATUS(tour_status_id),
  CONSTRAINT FK_All_Tourn_After_1958_Players1 FOREIGN KEY(player_id_1) REFERENCES PLAYERS(player_id),
  CONSTRAINT FK_All_Tourn_After_1958_Players2 FOREIGN KEY(player_id_2) REFERENCES PLAYERS(player_id)
);

LOAD DATA INFILE 'database_files/all_tournaments_after_1958.csv'
INTO TABLE ALL_TOURNAMENT_AFTER_1958
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

ALTER table ALL_TOURNAMENT_AFTER_1958
ADD PRIMARY KEY (event_id);

CREATE TABLE DISTANCE_TO_HOLE_AFTER_TEE_SHOT(
  id INT PRIMARY KEY,
  year YEAR NOT NULL,
  season VARCHAR(10) NOT NULL,
  distance_after_tee_rank INT DEFAULT NULL,
  player_id INT NOT NULL,
  player_name VARCHAR(60) NOT NULL,
  distance_after_tee_shot_avg_yrds DECIMAL(4,1) NOT NULL,
  distance_after_tee_shot_total_yrds INT NOT NULL,
  total_drives INT NOT NULL,
  CONSTRAINT FK_Distance_To_Hole_After_Tee_Years FOREIGN KEY(year) REFERENCES YEARS(year),
  CONSTRAINT FK_Distance_To_Hole_After_Tee_Players FOREIGN KEY(player_id) REFERENCES PLAYERS(player_id)
);

LOAD DATA INFILE 'database_files/distance_to_hole_after_tee_shot.csv'
INTO TABLE DISTANCE_TO_HOLE_AFTER_TEE_SHOT
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

CREATE TABLE DISTANCE_TO_HOLE_AFTER_TEE_SHOT_AVG(
  year YEAR PRIMARY KEY,
  season VARCHAR(10) NOT NULL,
  distance_after_tee_shot_avg_yrds_tour DECIMAL(4,1) NOT NULL,
  CONSTRAINT FK_Distance_To_Hole_After_Tee_Avg_Years FOREIGN KEY(year) REFERENCES YEARS(year)
);

LOAD DATA INFILE 'database_files/distance_to_hole_after_tee_shot_avg.csv'
INTO TABLE DISTANCE_TO_HOLE_AFTER_TEE_SHOT_AVG
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

CREATE TABLE pga_data_analysis.FULL_STATS (
  `stat_id` INT PRIMARY KEY,
  `year` year(4) DEFAULT NULL,
  `player_id` int(11) NOT NULL,
  `events` int(11) DEFAULT NULL,
  `rounds_total` int(11) DEFAULT NULL,
  `rounds_measured` int(11) DEFAULT NULL,
  `sg_total_avg_m` decimal(5,3) DEFAULT NULL,
  `sg_total` decimal(7,3) DEFAULT NULL,
  `sg_tee2green_avg_m` decimal(5,3) DEFAULT NULL,
  `sg_tee2green_total` decimal(7,3) DEFAULT NULL,
  `sg_putting_avg_m` decimal(5,3) DEFAULT NULL,
  `sg_putting_total` decimal(7,3) DEFAULT NULL,
  `sg_app_green_avg_m` decimal(5,3) DEFAULT NULL,
  `sg_app_green_total` decimal(7,3) DEFAULT NULL,
  `sg_off_tee_avg_m` decimal(5,3) DEFAULT NULL,
  `sg_off_tee_total` decimal(7,3) DEFAULT NULL,
  `sg_approach_avg_m` decimal(5,3) DEFAULT NULL,
  `sg_around_green_avg_m` decimal(5,3) DEFAULT NULL,
  `app_avg_proximity` varchar(7) DEFAULT NULL,
  `app_total_distance` decimal(10,3) DEFAULT NULL,
  `app_attempts` int(11) DEFAULT NULL,
  `avg_score_stroke_differential` decimal(4,2) DEFAULT NULL,
  `avg_score_player` decimal(4,2) DEFAULT NULL,
  `avg_score_field` decimal(4,2) DEFAULT NULL,
  `finish_top_10` int(11) DEFAULT NULL,
  `finish_1st` int(11) DEFAULT NULL,
  `finish_2nd` int(11) DEFAULT NULL,
  `finish_3rd` int(11) DEFAULT NULL,
  `distance_measured_avg` decimal(5,2) DEFAULT NULL,
  `distance_measured_total` int(11) DEFAULT NULL,
  `distance_measured_num_drives` int(11) DEFAULT NULL,
  `distance_all_rank_total` varchar(5) DEFAULT NULL,
  `distance_all_avg` decimal(5,2) DEFAULT NULL,
  `distance_all_total` int(11) DEFAULT NULL,
  `distance_all_num_drives` int(11) DEFAULT NULL,
  `fairway_accuracy_percent` decimal(5,2) DEFAULT NULL,
  `fairways_hit` int(11) DEFAULT NULL,
  `fairways_possible` int(11) DEFAULT NULL,
  `fairways_missed_other_percent` decimal(5,2) DEFAULT NULL,
  `fairways_missed_other_total` int(11) DEFAULT NULL,
  `fairways_missed_other_possible` int(11) DEFAULT NULL,
  `fairways_missed_other_relative_to_par` decimal(4,2) DEFAULT NULL,
  `total_putting` decimal(5,1) DEFAULT NULL,
  CONSTRAINT FK_Full_Stats_Years FOREIGN KEY(year) REFERENCES YEARS(year),
  CONSTRAINT FK_Full_Stats_Players FOREIGN KEY(player_id) REFERENCES PLAYERS(player_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOAD DATA INFILE 'database_files/FULL_STATS-1.csv'
INTO TABLE pga_data_analysis.FULL_STATS
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

-- ALTER TABLE pga_data_analysis.FULL_STATS
-- ADD PRIMARY KEY (stat_id);

-- ALTER TABLE pga_data_analysis.FULL_STATS
-- ADD CONSTRAINT FK_Full_Stats_Players FOREIGN KEY(player_id) REFERENCES PLAYERS(player_id);

CREATE TABLE CAREER_STATS(
  c_stats_id INT PRIMARY KEY AUTO_INCREMENT,
  player_id INT NOT NULL,
  tour CHAR(1) DEFAULT NULL,
  year YEAR NOT NULL,
  season VARCHAR(10) NOT NULL,
  events INT DEFAULT NULL,
  wins INT DEFAULT NULL,
  seconds INT DEFAULT NULL,
  thirds INT DEFAULT NULL,
  top_10 INT DEFAULT NULL,
  top_25 INT DEFAULT NULL,
  cuts_made INT DEFAULT NULL,
  earnings INT DEFAULT NULL,
  CONSTRAINT FK_Career_Stats_Years FOREIGN KEY(year) REFERENCES YEARS(year),
  CONSTRAINT FK_Career_Stats_Players FOREIGN KEY(player_id) REFERENCES PLAYERS(player_id)
);

LOAD DATA INFILE 'database_files/career_stats2.csv'
INTO TABLE CAREER_STATS
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

create table DISTANCE_PERCENTILE_VS_TOP10 (
	row_id INT PRIMARY KEY,
    player_id INT NOT NULL,
    player_name VARCHAR(60) NOT NULL,
    year YEAR NOT NULL,
    age_end_yr INT DEFAULT NULL,
    events INT DEFAULT NULL,
    distance_measured_avg DECIMAL(4,1) DEFAULT NULL,
    top10 INT,
    wins INT,
    distance_percentile_rank DECIMAL(4,3),
    avg_score_stroke_differential DECIMAL(4,2) DEFAULT NULL,
    sg_putting_avg DECIMAL(4,3) DEFAULT NULL,
    sg_tee2green_avg DECIMAL(4,3) DEFAULT NULL,
    sg_total_avg DECIMAL(4,3) DEFAULT NULL,
    sg_off_tee_avg DECIMAL(4,3) DEFAULT NULL,
    sg_approach_avg DECIMAL(4,3) DEFAULT NULL,
    sg_around_green_avg DECIMAL(4,3) DEFAULT NULL,
    distance_all_avg DECIMAL(4,1) DEFAULT NULL,
    fairway_accuracy_percent DECIMAL(5,2) DEFAULT NULL,
    fairways_missed_other_percent DECIMAL(5,2) DEFAULT NULL,
    total_putting DECIMAL(5,1) DEFAULT NULL,
    distance_measured_total INT DEFAULT NULL,
    distance_measured_num_drives  INT DEFAULT NULL,
    distance_all_rank_total VARCHAR(5) DEFAULT NULL,
    distance_all_total INT DEFAULT NULL,
    distance_all_num_drives INT DEFAULT NULL,
    fairways_hit INT DEFAULT NULL,
    fairways_possible INT DEFAULT NULL,
    finish_2nd INT DEFAULT NULL,
    finish_3rd INT DEFAULT NULL,
    avg_score_player DECIMAL(4,2) DEFAULT NULL,
    avg_score_field DECIMAL(4,2) DEFAULT NULL,
    approach_attempts INT DEFAULT NULL,
    approach_total_distance DECIMAL(8,3) DEFAULT NULL,
    app_avg_proximity DECIMAL(6,3) DEFAULT NULL,
    distance_percentile_rank_all DECIMAL(4,3) DEFAULT NULL,
    CONSTRAINT UNQ_Distance_Per_Top10 UNIQUE (player_id, year),
    CONSTRAINT FK_Distance_Per_Top10_Players FOREIGN KEY (player_id) REFERENCES PLAYERS(player_id)
);

LOAD DATA INFILE 'database_files/driving_distance_percentile_vs_top10_updated.csv'
INTO TABLE pga_data_analysis.DISTANCE_PERCENTILE_VS_TOP10
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;
