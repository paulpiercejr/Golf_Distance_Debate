SELECT p.full_name, ays.player_id, ays.age_end_yr, ays.year, ays.driving_distance, 
ROUND( PERCENT_RANK() OVER(
    PARTITION BY ays.year
    ORDER BY ays.driving_distance
  ),3) as percentile_rank_distance,
  ays.driving_distance_all_drives, 
ROUND( PERCENT_RANK() OVER(
    PARTITION BY ays.year
    ORDER BY ays.driving_distance_all_drives
  ),3) as percentile_rank_distance_all,
IFNULL(ays.driving_distance_rank,0) as driving_distance_rank,
ays.scoring_avg_actual,
ays.scoring_avg_adj, ays.sg_total, ays.sg_off_tee, ays.sg_app_green, ays.sg_around_green,
ays.sg_putting, ays.sg_tee_to_green, 
ays.driving_accuracy, 
ROUND( PERCENT_RANK() OVER(
    PARTITION BY ays.year
    ORDER BY ays.driving_accuracy
  ),3) as percentile_rank_driving_accuracy,
cs.events, cs.wins, cs.seconds, cs.thirds, cs.top_10, cs.top_25, cs.cuts_made, cs.earnings,
cs.earnings/cs.events as money_per_event, 
ROUND( PERCENT_RANK() OVER(
    PARTITION BY ays.year
    ORDER BY cs.earnings/cs.events
  ),3) as percentile_rank_money_per_event,
ays.club_head_speed, ays.greens_in_regulation_percent,
ROUND( PERCENT_RANK() OVER(
    PARTITION BY ays.year
    ORDER BY ays.greens_in_regulation_percent
  ),3) as percentile_rank_GIR_percent,
ays.proximity_to_hole_in/12 as proximity_to_hole_ft,
dts.distance_after_tee_shot_avg_yrds, dts.total_drives
FROM PLAYERS p
JOIN ALL_YEARLY_STATS ays ON (p.player_id = ays.player_id)
JOIN CAREER_STATS cs ON (ays.player_id = cs.player_id AND ays.year = cs.year)
JOIN DISTANCE_TO_HOLE_AFTER_TEE_SHOT dts ON (ays.player_id = dts.player_id AND ays.year = dts.year)
WHERE ays.driving_distance_rank is not null
AND ays.year < 2023
ORDER BY ays.year desc, ays.driving_distance desc;








-- 
select p.full_name as "Name", ays.player_id as "Player ID", ays.age_end_yr "Age", ays.year "Year", ays.season as "Season", ays.driving_distance as "Driving Distance",
ays.scoring_avg_actual as "Scoring Avg", ays.scoring_avg_adj as "Scoring Avg - Adj", 
ays.sg_total as "SG - Total", ays.sg_off_tee as "SG - Off Tee", ays.sg_app_green as "SG - App Green", ays.sg_around_green as "SG - Around Green",
ays.sg_putting as "SG - Putting", ays.sg_tee_to_green as "SG-Tee to Green", 
ays.sg_total_measured_rounds as "SG - Measured Rds",
ays.sg_total_total as "SG - Total Total",
ays.sg_off_tee_total "SG - Off Tee Total",
ays.sg_app_green_total "SG - App Green Total",
ays.sg_around_green_total "SG - Around Green Total",
ays.sg_putting_total "SG - Putting Total",
ays.driving_distance_total "Driving Distance Total",
ays.driving_distance_total_drives "Driving Distance Total Drives",
ays.driving_distance_all_drives_total "Driving Distance All Total",
ays.driving_distance_all_drives_total_drives "Driving Distance All Total Drives",
ays.driving_accuracy as "Driving Accuracy", 
ays.fairways_possible "Driving Acc - Frwy Possible",
ays.fairways_hit "Driving Acc - Frwy Hit",
cs.events "Events", cs.wins "Wins", cs.seconds "2nd", cs.thirds "3rd", cs.top_10 "Top 10s", cs.top_25 "Top 25s", cs.cuts_made "Cuts Made", cs.earnings "Earnings",
cs.earnings/cs.events as "Money per Event", 
ays.club_head_speed "Clubhead Speed", 
ays.club_head_speed_attempts "Clubhead Speed Att",
ays.club_head_speed_total "Clubhead Speed Total",
ays.greens_in_regulation_percent "GIR %",
ays.greens_possible "GIR - Possible",
ays.greens_hit "GIR - Hit",
ays.proximity_to_hole_in/12 as "Proximity to hole ft",
ays.approach_50_75_in/12 as "Proximity (50-75)", ays.approach_50_75_total_att as "Proximity (50-75) Total Att", ays.approach_50_75_total_ft as "Proximity (50-75) Total ft",
ays.approach_75_100_in/12 as "Proximity (75-100)", ays.approach_75_100_total_att as "Proximity (75-100) Total Att", ays.approach_75_100_total_ft as "Proximity (75-100) Total ft",
ays.approach_100_125_in/12 as "Proximity (100-125)", ays.approach_100_125_total_att as "Proximity (100-125) Total Att", ays.approach_100_125_total_ft as "Proximity (100-125) Total ft",
ays.approach_125_150_in/12 as "Proximity (125-150)", ays.approach_125_150_total_att as "Proximity (125-150) Total Att", ays.approach_125_150_total_ft as "Proximity (125-150) Total ft",
ays.approach_150_175_in/12 as "Proximity (150-175)", ays.approach_150_175_total_att as "Proximity (150-175) Total Att", ays.approach_150_175_total_ft as "Proximity (150-175) Total ft",
ays.approach_175_200_in/12 as "Proximity (175-200)", ays.approach_175_200_total_att as "Proximity (175-200) Total Att", ays.approach_175_200_total_ft as "Proximity (175-200) Total ft",
ays.approach_200_225_in/12 as "Proximity (200-225)", ays.approach_200_225_total_att as "Proximity (200-225) Total Att", ays.approach_200_225_total_ft as "Proximity (200-225) Total ft",
ays.approach_225_250_in/12 as "Proximity (225-250)", ays.approach_225_250_total_att as "Proximity (225-250) Total Att", ays.approach_225_250_total_ft as "Proximity (225-250) Total ft",
ays.approach_250_275_in/12 as "Proximity (250-275)", ays.approach_250_275_total_att as "Proximity (250-275) Total Att", ays.approach_250_275_total_ft as "Proximity (250-275) Total ft",
ays.approach_more_275_in/12 as "Proximity (>275)", ays.approach_more_275_total_att as "Proximity (>275) Total Att", ays.approach_more_275_total_ft as "Proximity (>275) Total ft",
ays.going_for_green_percent "Going for Green %",
ays.going_for_green_attempts "Going for Green Att",
ays.going_for_green_hit "Going for Green Hit",
ays.going_for_green_percent_non_attemptes "Going for Green % Non-Att",
ays.going_for_green_percent_attempts "Going for Green % Att",
ays.going_for_green_hit_percent "Going for Green Hit %",
ays.going_for_green_birdie_better_pct "Going for Green Birdie+ %",
ays.going_for_green_birdie_better_total "Going for Green Birdie + Total",
ays.birdie_avg "Birdie Avg",
ays.birdie_avg_num_birdies "Birdie Avg Birdies",
ays.birdie_avg_total_rounds "Birdie Avg Total Rds",
ays.birdie_or_better_conversion_birdies "Birdie or Better Conversion Birdies",
ays.birdie_or_better_conversion_percent "Birdie or Better Conversion %",
ays.birdie_or_better_percent "Birdie or Better %"
FROM PLAYERS p
JOIN ALL_YEARLY_STATS ays ON (p.player_id = ays.player_id)
LEFT OUTER JOIN CAREER_STATS cs ON (ays.player_id = cs.player_id AND ays.year = cs.year)
WHERE ays.year < 2023
AND ays.year > 1979
ORDER BY ays.year desc, ays.driving_distance desc;









SELECT p.full_name as "Name", ays.player_id as "Player ID", ays.age_end_yr "Age", ays.year "Year", ays.season as "Season", ays.driving_distance as "Driving Distance", 
ROUND( PERCENT_RANK() OVER(
    PARTITION BY ays.year
    ORDER BY ays.driving_distance
  ),3) as "Driving Distance Percentile Rank",
ays.driving_distance_all_drives as "Driving Distance All", 
ROUND( PERCENT_RANK() OVER(
    PARTITION BY ays.year
    ORDER BY ays.driving_distance_all_drives
  ),3) as "Driving Distance All Percentile Rank",
ays.driving_distance_rank as "Driving Distance Rank",
ays.scoring_avg_actual as "Scoring Avg",
ROUND( PERCENT_RANK() OVER(
    PARTITION BY ays.year
    ORDER BY ays.scoring_avg_actual
  ),3) as "Scoring Avg Percentile",
ays.scoring_avg_adj as "Scoring Avg - Adj", 
ROUND( PERCENT_RANK() OVER(
    PARTITION BY ays.year
    ORDER BY ays.scoring_avg_adj
  ),3) as "Scoring Avg Adj Percentile",
ays.sg_total as "SG - Total", ays.sg_off_tee as "SG - Off Tee", ays.sg_app_green as "SG - App Green", ays.sg_around_green as "SG - Around Green",
ays.sg_putting as "SG - Putting", ays.sg_tee_to_green as "SG-Tee to Green", 
ays.sg_total_measured_rounds as "SG - Measured Rds",
ays.sg_total_total as "SG - Total Total",
ays.sg_off_tee_total "SG - Off Tee Total",
ays.sg_app_green_total "SG - App Green Total",
ays.sg_around_green_total "SG - Around Green Total",
ays.sg_putting_total "SG - Putting Total",
ays.driving_distance_total "Driving Distance Total",
ays.driving_distance_total_drives "Driving Distance Total Drives",
ays.driving_distance_all_drives_total "Driving Distance All Total",
ays.driving_distance_all_drives_total_drives "Driving Distance All Total Drives",
ays.driving_accuracy as "Driving Accuracy", 
ROUND( PERCENT_RANK() OVER(
    PARTITION BY ays.year
    ORDER BY ays.driving_accuracy
  ),3) as "Driving Accuracy Percentile",
ays.fairways_possible "Driving Acc - Frwy Possible",
ays.fairways_hit "Driving Acc - Frwy Hit",
cs.events "Events", cs.wins "Wins", cs.seconds "2nd", cs.thirds "3rd", cs.top_10 "Top 10s", cs.top_25 "Top 25s", cs.cuts_made "Cuts Made", cs.earnings "Earnings",
cs.earnings/cs.events as "Money per Event", 
ROUND( PERCENT_RANK() OVER(
    PARTITION BY ays.year
    ORDER BY cs.earnings/cs.events
  ),3) as "Money per Event Percentile ",
ays.club_head_speed "Clubhead Speed", 
ays.club_head_speed_attempts "Clubhead Speed Att",
ays.club_head_speed_total "Clubhead Speed Total",
dts.distance_after_tee_shot_avg_yrds "Distance after tee shot", dts.total_drives "Distance after tee shot total drives",
ays.greens_in_regulation_percent "GIR %",
ays.greens_possible "GIR - Possible",
ays.greens_hit "GIR - Hit",
ROUND( PERCENT_RANK() OVER(
    PARTITION BY ays.year
    ORDER BY ays.greens_in_regulation_percent
  ),3) as "GIR % Percentile",
ays.proximity_to_hole_in/12 as "Proximity to hole ft",
ays.approach_50_75_in/12 as "Proximity (50-75)", ays.approach_50_75_total_att as "Proximity (50-75) Total Att", ays.approach_50_75_total_ft as "Proximity (50-75) Total ft",
ays.approach_75_100_in/12 as "Proximity (75-100)", ays.approach_75_100_total_att as "Proximity (75-100) Total Att", ays.approach_75_100_total_ft as "Proximity (75-100) Total ft",
ays.approach_100_125_in/12 as "Proximity (100-125)", ays.approach_100_125_total_att as "Proximity (100-125) Total Att", ays.approach_100_125_total_ft as "Proximity (100-125) Total ft",
ays.approach_125_150_in/12 as "Proximity (125-150)", ays.approach_125_150_total_att as "Proximity (125-150) Total Att", ays.approach_125_150_total_ft as "Proximity (125-150) Total ft",
ays.approach_150_175_in/12 as "Proximity (150-175)", ays.approach_150_175_total_att as "Proximity (150-175) Total Att", ays.approach_150_175_total_ft as "Proximity (150-175) Total ft",
ays.approach_175_200_in/12 as "Proximity (175-200)", ays.approach_175_200_total_att as "Proximity (175-200) Total Att", ays.approach_175_200_total_ft as "Proximity (175-200) Total ft",
ays.approach_200_225_in/12 as "Proximity (200-225)", ays.approach_200_225_total_att as "Proximity (200-225) Total Att", ays.approach_200_225_total_ft as "Proximity (200-225) Total ft",
ays.approach_225_250_in/12 as "Proximity (225-250)", ays.approach_225_250_total_att as "Proximity (225-250) Total Att", ays.approach_225_250_total_ft as "Proximity (225-250) Total ft",
ays.approach_250_275_in/12 as "Proximity (250-275)", ays.approach_250_275_total_att as "Proximity (250-275) Total Att", ays.approach_250_275_total_ft as "Proximity (250-275) Total ft",
ays.approach_more_275_in/12 as "Proximity (>275)", ays.approach_more_275_total_att as "Proximity (>275) Total Att", ays.approach_more_275_total_ft as "Proximity (>275) Total ft",
ays.going_for_green_percent "Going for Green %",
ROUND( PERCENT_RANK() OVER(
    PARTITION BY ays.year
    ORDER BY ays.going_for_green_percent
  ),3) as "Going for Green % Percentile",
ays.going_for_green_attempts "Going for Green Att",
ays.going_for_green_hit "Going for Green Hit",
ays.going_for_green_percent_non_attemptes "Going for Green % Non-Att",
ays.going_for_green_percent_attempts "Going for Green % Att",
ays.going_for_green_hit_percent "Going for Green Hit %",
ROUND( PERCENT_RANK() OVER(
    PARTITION BY ays.year
    ORDER BY ays.going_for_green_hit_percent
  ),3) as "Going for Green Hit % Percentile",
ays.going_for_green_birdie_better_pct "Going for Green Birdie+ %",
ays.going_for_green_birdie_better_total "Going for Green Birdie + Total",
ays.birdie_avg "Birdie Avg",
ROUND( PERCENT_RANK() OVER(
    PARTITION BY ays.year
    ORDER BY ays.birdie_avg
  ),3) as "Birdie Avg Percentile",
ays.birdie_avg_num_birdies "Birdie Avg Birdies",
ays.birdie_avg_total_rounds "Birdie Avg Total Rds",
ays.birdie_or_better_conversion_birdies "Birdie or Better Conversion Birdies",
ays.birdie_or_better_conversion_percent "Birdie or Better Conversion %",
ays.birdie_or_better_percent "Birdie or Better %",
ROUND( PERCENT_RANK() OVER(
    PARTITION BY ays.year
    ORDER BY ays.birdie_or_better_percent
  ),3) as "Birdie or Better % Percentile",
ays.scoring_avg_actual_total_strokes "Scoring Avg - Actual Total Strokes",
ays.scoring_avg_actual_total_rounds "Scoring Avg - Actual Total Rds",
ays.lowest_round "Lowest Rd",
ays.birdie_avg "Birdie Avg",
ROUND( PERCENT_RANK() OVER(
    PARTITION BY ays.year
    ORDER BY ays.birdie_avg
  ),3) as "Birdie Avg Percentile",
ays.eagles_holes_per "Holes per Eagle",
ays.par_breaker_percent "Par Breaker %",
ays.birdie_or_better_percent "Birdie+ %",
ays.bogey_avoidance_percent "Bogey Avoidance %",
ROUND( PERCENT_RANK() OVER(
    PARTITION BY ays.year
    ORDER BY ays.bogey_avoidance_percent
  ),3) as "Bogey Avoidance % Percentile",
ays.par3_scoring_avg "Par 3 Avg",
ays.par3_birdie_or_better "Par 3 Birdie+",
ROUND( PERCENT_RANK() OVER(
    PARTITION BY ays.year
    ORDER BY ays.par3_scoring_avg
  ),3) as "Par 3 Avg Percentile",
ays.par4_scoring_avg "Par 4 Avg",
ays.par4_birdie_or_better "Par 4 Birdie+",
ROUND( PERCENT_RANK() OVER(
    PARTITION BY ays.year
    ORDER BY ays.par4_scoring_avg
  ),3) as "Par 4 Avg Percentile",
ays.par5_scoring_avg "Par 5 Avg",
ays.par5_birdie_or_better "Par 5 Birdie+",
ROUND( PERCENT_RANK() OVER(
    PARTITION BY ays.year
    ORDER BY ays.par5_scoring_avg
  ),3) as "Par 5 Avg Percentile",
ays.early_scoring_avg "Early Scoring Avg",
ays.early_scoring_total_rounds "Early Scoring Total Rds",
ays.early_scoring_total_strokes "Early Scoring Total Strokes",
ays.late_scoring_avg "Late Scoring Avg",
ays.late_scoring_total_rounds "Late Scoring Total Rds",
ays.late_scoring_total_strokes "Late Scoring Total Strokes"
FROM PLAYERS p
JOIN ALL_YEARLY_STATS ays ON (p.player_id = ays.player_id)
LEFT OUTER JOIN CAREER_STATS cs ON (ays.player_id = cs.player_id AND ays.year = cs.year)
LEFT OUTER JOIN DISTANCE_TO_HOLE_AFTER_TEE_SHOT dts ON (ays.player_id = dts.player_id AND ays.year = dts.year)
-- WHERE ays.driving_distance_rank is not null
WHERE ays.year < 2023
-- AND ays.year = 1980
ORDER BY ays.year desc, ays.driving_distance desc;

select ays.player_id, p.full_name, ays.year
from all_yearly_stats ays
join players p ON (ays.player_id = p.player_id)
where ays.year = 1980
order by p.full_name;

select full_name from players
where last_name = 'Pohl';


SELECT
    full_name,
    `year`,
    events,
    distance_measured_avg,
    IFNULL(finish_top_10,0) AS finish_top_10,
    IFNULL(finish_1st,0) AS finish_1st,
    ROUND(
        PERCENT_RANK() OVER (
            PARTITION BY `year`
            ORDER BY distance_measured_avg
        ) 
    ,3) percentile_rank,
    avg_score_stroke_differential,
    sg_putting_avg_m,
    sg_tee2green_avg_m,
    sg_total_avg_m,
    sg_off_tee_avg_m,
    sg_approach_avg_m,
    sg_around_green_avg_m,
    distance_all_avg,
    fairway_accuracy_percent,
    fairways_missed_other_percent,
    total_putting,
    distance_measured_total,
    distance_measured_num_drives,
    distance_all_rank_total,
    distance_all_total,
    distance_all_num_drives,
    fairways_hit,
    fairways_possible,
    finish_2nd,
    finish_3rd,
    avg_score_player,
    avg_score_field,
    app_attempts,
    app_total_distance,
    app_avg_proximity,
    ROUND(
        PERCENT_RANK() OVER (
            PARTITION BY `year`
            ORDER BY distance_all_avg
        ) 
    ,3) percentile_rank_all
FROM
    FULL_STATS
    join players on full_stats.`player_id` = players.`player_id`
    where distance_measured_avg is not NULL
    OR finish_1st > 0
    -- AND year = 2021
    order by year desc;
    
    
    

-- UNION tables together to get all golfers with ranked distance and golfers with a win
SELECT
    fs1.player_id as player_id, 
    p1.full_name as full_name,
    p1.height as height,
    fs1.year as year,
    fs1.distance_measured_avg as driving_distance, 
    ROUND(
        PERCENT_RANK() OVER (
            PARTITION BY fs1.year
            ORDER BY fs1.distance_measured_avg
        ) 
    ,3) percentile_rank,
    IFNULL(fs1.finish_1st,0) AS wins,
    IFNULL(fs1.finish_2nd,0) AS seconds,
    IFNULL(fs1.finish_3rd,0) AS thirds,
	IFNULL(fs1.finish_top_10,0) AS top_10,
    NULL AS top_25,
    fs1.events,
    NULL AS cuts_made,
    fs1.avg_score_stroke_differential as stroke_diff,
    fs1.avg_score_player as scoring_avg,
    fs1.avg_score_field as field_avg
FROM
    FULL_STATS fs1
    join players p1 on fs1.player_id = p1.player_id
    where distance_measured_avg is not NULL
    OR finish_1st > 0
UNION
select 
    ays.player_id as player_id, 
    p.full_name as full_name, 
    p.height as height,
    ays.year as year,
	max(ays.driving_distance) as driving_distance, 
    max(d10.distance_percentile_rank) as percentile_rank,  -- max(ays.driving_distance_rank), 
    sum(cs.wins) as wins, 
    sum(cs.seconds) as seconds, 
    sum(cs.thirds) as thirds, 
    sum(cs.top_10) as top_10,
    sum(cs.top_25) as top_25, 
    sum(cs.events) as events, 
    sum(cs.cuts_made) as cuts_made,
    NULL as stroke_diff,
    avg(scoring_avg_actual) as scoring_avg,
    NULL as field_avg
	#ROUND( PERCENT_RANK() OVER(
	#	PARTITION BY ays.year
	#	ORDER BY max(ays.driving_distance)
	#  ),3) as percentile_rank_distance, 
from all_yearly_stats ays
CROSS JOIN FULL_STATS fs ON fs.player_id = ays.player_id AND fs.year = ays.year
CROSS JOIN CAREER_STATS cs ON ays.player_id = cs.player_id AND ays.year = cs.year
CROSS JOIN players p ON p.player_id = ays.player_id
LEFT JOIN DISTANCE_PERCENTILE_VS_TOP10 d10 ON d10.player_id = ays.player_id AND d10.year = ays.year
LEFT JOIN DRIVING_DISTANCE_MAX_AVG dma ON cs.year = dma.year
-- where p.player_id = 8793 -- 20396 -- 
where ays.year > 1979
group by ays.player_id, p.full_name, ays.year, cs.season
having max(ays.driving_distance_rank) is not null
OR sum(cs.wins) > 0
order by year, driving_distance desc;
-- order by year desc;















SELECT p.full_name as "Name", ays.player_id as "Player ID", ays.age_end_yr "Age", ays.year "Year", ays.season as "Season", ays.driving_distance as "Driving Distance", 
ays.driving_distance_all_drives as "Driving Distance All", ays.driving_distance_rank as "Driving Distance Rank",
ays.scoring_avg_actual as "Scoring Avg",
ays.scoring_avg_adj as "Scoring Avg - Adj", ays.sg_total as "SG - Total", ays.sg_off_tee as "SG - Off Tee", ays.sg_app_green as "SG - App Green", ays.sg_around_green as "SG - Around Green",
ays.sg_putting as "SG - Putting", ays.sg_tee_to_green as "SG-Tee to Green", 
ays.driving_accuracy as "Driving Accuracy", 
cs.events "Events", cs.wins "Wins", cs.seconds "2nd", cs.thirds "3rd", cs.top_10 "Top 10s", cs.top_25 "Top 25s", cs.cuts_made "Cuts Made", cs.earnings "Earnings",
cs.earnings/cs.events as "Money per Event", 
ays.club_head_speed "Clubhead Speed", 
dts.distance_after_tee_shot_avg_yrds "Distance after tee shot", dts.total_drives "DATS total drives",
ays.greens_in_regulation_percent "GIR %",
ays.proximity_to_hole_in/12 as "Proximity to hole ft",
ays.approach_50_75_in/12 as "Proximity (50-75)", ays.approach_50_75_total_att as "Proximity (50-75) Total Att", ays.approach_50_75_total_ft as "Proximity (50-75) Total ft",
ays.approach_75_100_in/12 as "Proximity (75-100)", ays.approach_75_100_total_att as "Proximity (75-100) Total Att", ays.approach_75_100_total_ft as "Proximity (75-100) Total ft",
ays.approach_100_125_in/12 as "Proximity (100-125)", ays.approach_100_125_total_att as "Proximity (100-125) Total Att", ays.approach_100_125_total_ft as "Proximity (100-125) Total ft",
ays.approach_125_150_in/12 as "Proximity (125-150)", ays.approach_125_150_total_att as "Proximity (125-150) Total Att", ays.approach_125_150_total_ft as "Proximity (125-150) Total ft",
ays.approach_150_175_in/12 as "Proximity (150-175)", ays.approach_150_175_total_att as "Proximity (150-175) Total Att", ays.approach_150_175_total_ft as "Proximity (150-175) Total ft",
ays.approach_175_200_in/12 as "Proximity (175-200)", ays.approach_175_200_total_att as "Proximity (175-200) Total Att", ays.approach_175_200_total_ft as "Proximity (175-200) Total ft",
ays.approach_200_225_in/12 as "Proximity (200-225)", ays.approach_200_225_total_att as "Proximity (200-225) Total Att", ays.approach_200_225_total_ft as "Proximity (200-225) Total ft",
ays.approach_225_250_in/12 as "Proximity (225-250)", ays.approach_225_250_total_att as "Proximity (225-250) Total Att", ays.approach_225_250_total_ft as "Proximity (225-250) Total ft",
ays.approach_250_275_in/12 as "Proximity (250-275)", ays.approach_250_275_total_att as "Proximity (250-275) Total Att", ays.approach_250_275_total_ft as "Proximity (250-275) Total ft",
ays.approach_more_275_in/12 as "Proximity (>275)", ays.approach_more_275_total_att as "Proximity (>275) Total Att", ays.approach_more_275_total_ft as "Proximity (>275) Total ft",
ays.going_for_green_percent "Going for Green %",
ays.going_for_green_attempts "Going for Green Att",
ays.going_for_green_hit "Going for Green Hit",
ays.going_for_green_percent_non_attemptes "Going for Green % Non-Att",
ays.going_for_green_percent_attempts "Going for Green % Att",
ays.going_for_green_hit_percent "Going for Green Hit %",
ays.going_for_green_birdie_better_pct "Going for Green Birdie+ %",
ays.going_for_green_birdie_better_total "Going for Green Birdie + Total",
ays.birdie_avg "Birdie Avg",
ays.birdie_avg_num_birdies "Birdie Avg Birdies",
ays.birdie_avg_total_rounds "Birdie Avg Total Rds",
ays.birdie_or_better_conversion_birdies "Birdie or Better Conversion Birdies",
ays.birdie_or_better_conversion_percent "Birdie or Better Conversion %",
ays.birdie_or_better_percent "Birdie or Better %",
ays.scoring_avg_actual_total_strokes "Scoring Avg - Actual Total Strokes",
ays.scoring_avg_actual_total_rounds "Scoring Avg - Actual Total Rds",
ays.lowest_round "Lowest Rd",
ays.birdie_avg "Birdie Avg",
ays.eagles_holes_per "Holes per Eagle",
ays.par_breaker_percent "Par Breaker %",
ays.birdie_or_better_percent "Birdie+ %",
ays.bogey_avoidance_percent "Bogey Avoidance %",
ays.par3_scoring_avg "Par 3 Avg",
ays.par3_birdie_or_better "Par 3 Birdie+",
ays.par4_scoring_avg "Par 4 Avg",
ays.par4_birdie_or_better "Par 4 Birdie+",
ays.par5_scoring_avg "Par 5 Avg",
ays.par5_birdie_or_better "Par 5 Birdie+",
ays.early_scoring_avg "Early Scoring Avg",
ays.early_scoring_total_rounds "Early Scoring Total Rds",
ays.early_scoring_total_strokes "Early Scoring Total Strokes",
ays.late_scoring_avg "Late Scoring Avg",
ays.late_scoring_total_rounds "Late Scoring Total Rds",
ays.late_scoring_total_strokes "Late Scoring Total Strokes"
FROM PLAYERS p
JOIN ALL_YEARLY_STATS ays ON (p.player_id = ays.player_id)
LEFT OUTER JOIN CAREER_STATS cs ON (ays.player_id = cs.player_id AND ays.year = cs.year)
LEFT OUTER JOIN DISTANCE_TO_HOLE_AFTER_TEE_SHOT dts ON (ays.player_id = dts.player_id AND ays.year = dts.year)
-- WHERE ays.driving_distance_rank is not null
WHERE ays.year < 2023
ORDER BY ays.year desc, ays.driving_distance desc;
-- INTO OUTFILE '\\Users\\paulpiercejr\\pga_stats-2022.csv';

SHOW VARIABLES LIKE 'secure_file_priv';



use pga_data_analysis;

-- players
select player_id, full_name, birth_country, birth_city, birth_state, birth_date, height, weight, college, plays_from_country, career_earnings
from players;


-- tournament_yardage_breakdown_by_type_year
SELECT at58.year, es.event_status, count(twy.yardage) as num_of_courses, sum(twy.yardage)/sum(twy.par) AS yrds_per_par,
  (sum(twy.yardage)/sum(twy.par))*72 AS yrds_per_par72,
  avg(twy.yardage) as avg_yardage, sum(twy.yardage) as total_yardage,
  avg(twy.par) as avg_par, sum(twy.par) as total_par, max(twy.yardage) as longest_course,
  min(twy.yardage) as shortest_course,
  avg(twy.to_par) as avg_to_par, sum(twy.score) as total_score
FROM TOURNAMENT_WITH_YARDAGE twy
JOIN ALL_TOURNAMENT_AFTER_1958 at58 ON (twy.tournament_yr_id = at58.tournament_yr_id)
JOIN EVENT_STATUS es ON (es.tour_status_id = at58.tour_status_id)
-- WHERE es.tour_status_id = 2
WHERE twy.yardage is not null
GROUP BY at58.year, es.tour_status_id
ORDER BY at58.year DESC;

-- tournament_yardage_breakdown_by_year_official
SELECT at58.year, count(twy.yardage) as num_of_courses, sum(twy.yardage)/sum(twy.par) AS yrds_per_par,
  (sum(twy.yardage)/sum(twy.par))*72 AS yrds_per_par72,
  avg(twy.yardage) as avg_yardage, sum(twy.yardage) as total_yardage,
  avg(twy.par) as avg_par, sum(twy.par) as total_par, max(twy.yardage) as longest_course,
  min(twy.yardage) as shortest_course
FROM TOURNAMENT_WITH_YARDAGE twy
JOIN ALL_TOURNAMENT_AFTER_1958 at58 ON (twy.tournament_yr_id = at58.tournament_yr_id)
JOIN EVENT_STATUS es ON (es.tour_status_id = at58.tour_status_id)
-- WHERE es.tour_status_id = 2
WHERE twy.yardage is not null AND es.tour_status_id != 9  -- 9 is unofficial events
GROUP BY at58.year
ORDER BY at58.year DESC;

select * from tournament_with_yardage;
-- tournament_yardage_breakdown_by_year_official
SELECT at58.year, count(twy.yardage) as num_of_courses, sum(twy.yardage)/sum(twy.par) AS yrds_per_par,
  (sum(twy.yardage)/sum(twy.par))*72 AS yrds_per_par72,
  avg(twy.yardage) as avg_yardage, sum(twy.yardage) as total_yardage,
  avg(twy.par) as avg_par, sum(twy.par) as total_par, max(twy.yardage) as longest_course,
  min(twy.yardage) as shortest_course,
  avg(twy.to_par) as avg_to_par, sum(twy.score) as total_score
FROM TOURNAMENT_WITH_YARDAGE twy
JOIN ALL_TOURNAMENT_AFTER_1958 at58 ON (twy.tournament_yr_id = at58.tournament_yr_id)
JOIN EVENT_STATUS es ON (es.tour_status_id = at58.tour_status_id)
-- WHERE es.tour_status_id = 2
WHERE es.tour_status_id = 2 -- 9 is unofficial events
AND twy.yardage is not null 
GROUP BY at58.year
ORDER BY at58.year asc;

select * from event_status;


-- proximity_to_hole_by_year
SELECT year, count(proximity_to_hole_total_ft) as total_players, (sum(proximity_to_hole_total_ft)/sum(proximity_to_hole_total_att)) as "proximity to hole ft"
FROM ALL_YEARLY_STATS
WHERE proximity_to_hole_total_ft is not NULL
GROUP BY year;

-- birdie_avg_by_year
SELECT year, sum(birdie_avg_num_birdies) as 'total birdies', sum(birdie_avg_total_rounds) as 'total rounds', sum(birdie_avg_num_birdies)/sum(birdie_avg_total_rounds) as 'birdie avg'
FROM `ALL_YEARLY_STATS`
GROUP BY year
ORDER BY year desc;

-- going_for_green_by_year
SELECT year,  count(player_id) as num_players, sum(going_for_green_percent_attempts) as going_for_green_att,
  sum(going_for_green_percent_non_attemptes) as going_for_green_non_att,
  sum(going_for_green_percent_attempts)/(sum(going_for_green_percent_attempts)+sum(going_for_green_percent_non_attemptes)) as 'possible_gfg_%',
  sum(going_for_green_hit), sum(going_for_green_attempts),
  sum(going_for_green_birdie_better_total)
FROM `ALL_YEARLY_STATS`
GROUP BY year
ORDER BY year desc;

-- going_for_green_by_year_ranked
SELECT year,  count(player_id) as num_players, sum(going_for_green_percent_attempts) as going_for_green_att,
  sum(going_for_green_percent_non_attemptes) as going_for_green_non_att,
  sum(going_for_green_percent_attempts)/(sum(going_for_green_percent_attempts)+sum(going_for_green_percent_non_attemptes)) as 'possible_gfg_%',
  sum(going_for_green_hit), sum(going_for_green_attempts),
  sum(going_for_green_birdie_better_total)
FROM `ALL_YEARLY_STATS`
where driving_distance_rank is not null
GROUP BY year
ORDER BY year desc;

-- proximity_after_2001_by_year_by_distance
SELECT year, sum(approach_more_275_total_ft) as '>275 total ft',
sum(approach_more_275_total_att) as '>275 att',
sum(approach_more_275_total_ft)/sum(approach_more_275_total_att) as 'avg ft >275',
sum(approach_250_275_total_ft) as '250-275 total ft',
sum(approach_250_275_total_att) as '250-275 att',
sum(approach_250_275_total_ft)/sum(approach_250_275_total_att) as 'avg ft 250-275',
sum(approach_225_250_total_ft) as '225-250 total ft',
sum(approach_225_250_total_att) as '225-250 att',
sum(approach_225_250_total_ft)/sum(approach_225_250_total_att) as 'avg ft 225-250',
sum(approach_200_225_total_ft) as '200-225 total ft',
sum(approach_200_225_total_att) as '200-225 att',
sum(approach_200_225_total_ft)/sum(approach_200_225_total_att) as 'avg ft 200-225',
sum(approach_175_200_total_ft) as '175-200 total ft',
sum(approach_175_200_total_att) as '175-200 att',
sum(approach_175_200_total_ft)/sum(approach_175_200_total_att) as 'avg ft 175-200',
sum(approach_150_175_total_ft) as '150-175 total ft',
sum(approach_150_175_total_att) as '150-175 att',
sum(approach_150_175_total_ft)/sum(approach_150_175_total_att) as 'avg ft 150-175',
sum(approach_125_150_total_ft) as '125-150 total ft',
sum(approach_125_150_total_att) as '125-150 att',
sum(approach_125_150_total_ft)/sum(approach_125_150_total_att) as 'avg ft 125-150',
sum(approach_100_125_total_ft) as '100-125 total ft',
sum(approach_100_125_total_att) as '100-125 att',
sum(approach_100_125_total_ft)/sum(approach_100_125_total_att) as 'avg ft 100-125',
sum(approach_75_100_total_ft) as '75-100 total ft',
sum(approach_75_100_total_att) as '75-100 att',
sum(approach_75_100_total_ft)/sum(approach_75_100_total_att) as 'avg ft 75-100',
sum(approach_50_75_total_ft) as '50-75 total ft',
sum(approach_50_75_total_att) as '50-75 att',
sum(approach_50_75_total_ft)/sum(approach_50_75_total_att) as 'avg ft 50-75',
sum(approach_less_100_total_ft) as '<100 total ft',
sum(approach_less_100_total_att) as '<100 att',
sum(approach_less_100_total_ft)/sum(approach_less_100_total_att) as 'avg ft <100',
(sum(approach_more_275_total_ft) +
sum(approach_250_275_total_ft) +
sum(approach_225_250_total_ft) +
sum(approach_200_225_total_ft) +
sum(approach_175_200_total_ft) +
sum(approach_150_175_total_ft) +
sum(approach_125_150_total_ft) +
sum(approach_100_125_total_ft) +
sum(approach_75_100_total_ft) +
sum(approach_50_75_total_ft)) as total_feet,
(sum(approach_more_275_total_att) +
sum(approach_250_275_total_att) +
sum(approach_225_250_total_att) +
sum(approach_200_225_total_att) +
sum(approach_175_200_total_att) +
sum(approach_150_175_total_att) +
sum(approach_125_150_total_att) +
sum(approach_100_125_total_att) +
sum(approach_75_100_total_att) +
sum(approach_50_75_total_att)) as total_att,
(sum(approach_more_275_total_ft) +
sum(approach_250_275_total_ft) +
sum(approach_225_250_total_ft) +
sum(approach_200_225_total_ft) +
sum(approach_175_200_total_ft) +
sum(approach_150_175_total_ft) +
sum(approach_125_150_total_ft) +
sum(approach_100_125_total_ft) +
sum(approach_75_100_total_ft) +
sum(approach_50_75_total_ft))/
(sum(approach_more_275_total_att) +
sum(approach_250_275_total_att) +
sum(approach_225_250_total_att) +
sum(approach_200_225_total_att) +
sum(approach_175_200_total_att) +
sum(approach_150_175_total_att) +
sum(approach_125_150_total_att) +
sum(approach_100_125_total_att) +
sum(approach_75_100_total_att) +
sum(approach_50_75_total_att)) as proximity
FROM `ALL_YEARLY_STATS`
WHERE driving_distance_rank is not null
AND year > 2001
GROUP BY year
ORDER BY year desc;

-- TOURNAMENT_LIST
select * from tournament_list limit 20;

select * from tournament_with_yardage 
where year > 1979 AND course_id = 12
order by course_id, year desc
limit 100;

-- new spreadsheets BELOW

-- tournament list with adjust par 72
select twy.course_id, twy.tournament_id, twy.tournament_yr_id, twy.course_name_specific, twy.year, twy.tourn_date, tournament_name_iteration, twy.par, twy.yardage, twy.yardage/twy.par as "length per par", 
(twy.yardage/twy.par)*72 as "par 72 adjusted", twy.score, twy.to_par, twy.winner_name_specific, twy.player_id
from TOURNAMENT_WITH_YARDAGE twy
-- WHERE twy.year > 1979
ORDER BY twy.course_id, twy.tourn_date desc;

-- aggregate course info 1980-2022
select twy.course_id, cl.course_name, count(distinct(player_id)) as num_winners, count(player_id) as num_events,
max(twy.yardage), min(twy.yardage), avg(twy.yardage), min(twy.year), max(twy.year), max(twy.year)-min(twy.year) as "num years",
max(twy.yardage)-min(twy.yardage) as "yardage change", (max(twy.yardage)-min(twy.yardage))/(max(twy.year)-min(twy.year)) as "yardage change per year since 1980"
FROM TOURNAMENT_WITH_YARDAGE twy
JOIN COURSE_LIST cl ON (twy.course_id = cl.course_id)
WHERE twy.year > 1979 AND twy.year < 2023
GROUP BY twy.course_id
ORDER BY max(twy.yardage)-min(twy.yardage) desc;
-- ORDER BY max(twy.year) desc, twy.course_id;
-- ORDER BY num_winners desc;

-- aggregate course info yardage etc
select twy.course_id, twy.yardage
from tournament_with_yardage twy
where twy.yardage >= (select avg(twy1.yardage) from tournament_with_yardage twy1 
					where twy.course_id = twy1.course_id
                    group by twy1.course_id)
order by twy.course_id;


select twy2.course_id, twy2.yardage
	from tournament_with_yardage twy2
	where twy2.yardage >= (select avg(twy1.yardage) from tournament_with_yardage twy1 
						where twy2.course_id = twy1.course_id
						group by twy1.course_id);


select * from SCORING_AVERAGE;


select * from DISTANCE_PERCENTILE_VS_TOP10;

select -- dpv10.row_id, 
dpv10.player_id "Player ID",dpv10.player_name "Name",dpv10.age_end_yr "Age",dpv10.year "Year", cs.season "Season", dpv10.distance_measured_avg "Driving Distance",
ROUND( PERCENT_RANK() OVER(
    PARTITION BY dpv10.year
    ORDER BY dpv10.distance_measured_avg
  ),3) as "Driving Distance Percentile Rank",
dpv10.distance_all_avg "Driving Distance (All)",
ROUND( PERCENT_RANK() OVER(
    PARTITION BY dpv10.year
    ORDER BY dpv10.distance_all_avg
  ),3) as "Driving Distance (All) Percentile Rank",
ays.driving_distance_rank "Distance Rank", dpv10.distance_measured_total "Distance (Measured) Total",
dpv10.distance_measured_num_drives "Distance (Measured) Num Drives", dpv10.distance_all_avg "Distance (All) Avg", dpv10.distance_all_total "Distance (All) Total", 
dpv10.distance_all_num_drives "Distance (All) Num Drives", 
ROUND( PERCENT_RANK() OVER(
    PARTITION BY ays.year
    ORDER BY ays.scoring_avg_actual
  ),3) as "Scoring Avg Percentile",
dpv10.avg_score_player "Scoring Avg - Player", dpv10.avg_score_field "Scoring Avg - Field", dpv10.avg_score_stroke_differential "Score Stroke Differential Avg",
ROUND( PERCENT_RANK() OVER(
    PARTITION BY ays.year
    ORDER BY ays.scoring_avg_adj
  ),3) as "Scoring Avg Adj Percentile",
ays.scoring_avg_adj as "Scoring Avg - Adj",
dpv10.sg_total_avg "SG - Total", dpv10.sg_off_tee_avg "SG - Off Tee", dpv10.sg_approach_avg "SG - Approach", dpv10.sg_around_green_avg "SG - Around Green", dpv10.sg_putting_avg "SG - Putting", 
dpv10.sg_tee2green_avg "SG - Tee to Green", ays.sg_total_measured_rounds as "SG - Measured Rds",
ays.sg_total_total as "SG - Total Total",
ays.sg_off_tee_total "SG - Off Tee Total",
ays.sg_app_green_total "SG - App Green Total",
ays.sg_around_green_total "SG - Around Green Total",
ays.sg_putting_total "SG - Putting Total",
dpv10.total_putting "Total Putting",
dpv10.fairway_accuracy_percent "Fairway %", dpv10.fairways_hit "Fairwyas Hit", dpv10.fairways_possible "Fairways Possible",
ROUND( PERCENT_RANK() OVER(
    PARTITION BY dpv10.year
    ORDER BY dpv10.fairway_accuracy_percent
  ),3) as "Driving Accuracy Percentile",
dpv10.fairways_missed_other_percent "Fairways Missed - Other",
cs.events "Events", cs.wins as "Wins",
cs.seconds "2nd", cs.thirds "3rd", cs.top_10 "Top 10s", cs.top_25 "Top 25s", cs.cuts_made "Cuts Made", cs.earnings "Earnings",
cs.earnings/cs.events as "Money per Event", 
ROUND( PERCENT_RANK() OVER(
    PARTITION BY ays.year
    ORDER BY cs.earnings/cs.events
  ),3) as "Money per Event Percentile ",
dpv10.distance_percentile_rank_all "Distance (All) Percentile", ays.club_head_speed "Clubhead Speed", ays.club_head_speed_total "Clubhead Speed Total", ays.club_head_speed_attempts "Clubhead Speed Att", 
dts.distance_after_tee_shot_avg_yrds "Distance after tee shot", dts.total_drives "DATS total drives",
cs.top_25 "Top 25s", cs.cuts_made "Cuts Made", cs.earnings "Earnings",
cs.earnings/cs.events as "Money per Event", 
dts.distance_after_tee_shot_avg_yrds "Distance after tee shot", dts.total_drives "Distance after tee shot total drives", dts.distance_after_tee_shot_total_yrds "Distance after tee shot total yrds",
ays.greens_in_regulation_percent "GIR %",
ays.greens_possible "GIR - Possible",
ays.greens_hit "GIR - Hit",
ROUND( PERCENT_RANK() OVER(
    PARTITION BY ays.year
    ORDER BY ays.greens_in_regulation_percent
  ),3) as "GIR % Percentile",
dpv10.approach_attempts "Approach - Attempts", dpv10.approach_total_distance "Approach - Total Distance",
dpv10.app_avg_proximity "Approach - Avg Proximity", 
ays.proximity_to_hole_in/12 as "Proximity to hole ft",
ays.approach_50_75_in/12 as "Proximity (50-75)", ays.approach_50_75_total_att as "Proximity (50-75) Total Att", ays.approach_50_75_total_ft as "Proximity (50-75) Total ft",
ays.approach_75_100_in/12 as "Proximity (75-100)", ays.approach_75_100_total_att as "Proximity (75-100) Total Att", ays.approach_75_100_total_ft as "Proximity (75-100) Total ft",
ays.approach_100_125_in/12 as "Proximity (100-125)", ays.approach_100_125_total_att as "Proximity (100-125) Total Att", ays.approach_100_125_total_ft as "Proximity (100-125) Total ft",
ays.approach_125_150_in/12 as "Proximity (125-150)", ays.approach_125_150_total_att as "Proximity (125-150) Total Att", ays.approach_125_150_total_ft as "Proximity (125-150) Total ft",
ays.approach_150_175_in/12 as "Proximity (150-175)", ays.approach_150_175_total_att as "Proximity (150-175) Total Att", ays.approach_150_175_total_ft as "Proximity (150-175) Total ft",
ays.approach_175_200_in/12 as "Proximity (175-200)", ays.approach_175_200_total_att as "Proximity (175-200) Total Att", ays.approach_175_200_total_ft as "Proximity (175-200) Total ft",
ays.approach_200_225_in/12 as "Proximity (200-225)", ays.approach_200_225_total_att as "Proximity (200-225) Total Att", ays.approach_200_225_total_ft as "Proximity (200-225) Total ft",
ays.approach_225_250_in/12 as "Proximity (225-250)", ays.approach_225_250_total_att as "Proximity (225-250) Total Att", ays.approach_225_250_total_ft as "Proximity (225-250) Total ft",
ays.approach_250_275_in/12 as "Proximity (250-275)", ays.approach_250_275_total_att as "Proximity (250-275) Total Att", ays.approach_250_275_total_ft as "Proximity (250-275) Total ft",
ays.approach_more_275_in/12 as "Proximity (>275)", ays.approach_more_275_total_att as "Proximity (>275) Total Att", ays.approach_more_275_total_ft as "Proximity (>275) Total ft",
ays.going_for_green_percent "Going for Green %",
ays.going_for_green_attempts "Going for Green Att",
ays.going_for_green_hit "Going for Green Hit",
ays.going_for_green_percent_non_attemptes "Going for Green % Non-Att",
ays.going_for_green_percent_attempts "Going for Green % Att",
ays.going_for_green_hit_percent "Going for Green Hit %",
ays.going_for_green_birdie_better_pct "Going for Green Birdie+ %",
ays.going_for_green_birdie_better_total "Going for Green Birdie + Total",
ays.birdie_avg "Birdie Avg",
ays.birdie_avg_num_birdies "Birdie Avg Birdies",
ays.birdie_avg_total_rounds "Birdie Avg Total Rds",
ays.birdie_or_better_conversion_birdies "Birdie or Better Conversion Birdies",
ays.birdie_or_better_conversion_percent "Birdie or Better Conversion %",
ays.birdie_or_better_percent "Birdie or Better %",
ays.scoring_avg_actual_total_strokes "Scoring Avg - Actual Total Strokes",
ays.scoring_avg_actual_total_rounds "Scoring Avg - Actual Total Rds",
ays.lowest_round "Lowest Rd",
ays.birdie_avg "Birdie Avg",
ays.eagles_holes_per "Holes per Eagle",
ays.par_breaker_percent "Par Breaker %",
ays.birdie_or_better_percent "Birdie+ %",
ays.bogey_avoidance_percent "Bogey Avoidance %",
ays.par3_scoring_avg "Par 3 Avg",
ays.par3_birdie_or_better "Par 3 Birdie+",
ays.par4_scoring_avg "Par 4 Avg",
ays.par4_birdie_or_better "Par 4 Birdie+",
ays.par5_scoring_avg "Par 5 Avg",
ays.par5_birdie_or_better "Par 5 Birdie+",
ays.early_scoring_avg "Early Scoring Avg",
ays.early_scoring_total_rounds "Early Scoring Total Rds",
ays.early_scoring_total_strokes "Early Scoring Total Strokes",
ays.late_scoring_avg "Late Scoring Avg",
ays.late_scoring_total_rounds "Late Scoring Total Rds",
ays.late_scoring_total_strokes "Late Scoring Total Strokes"
from DISTANCE_PERCENTILE_VS_TOP10 dpv10
LEFT JOIN ALL_YEARLY_STATS ays ON (dpv10.player_id = ays.player_id AND dpv10.year = ays.year)
LEFT JOIN DISTANCE_TO_HOLE_AFTER_TEE_SHOT dts ON (dpv10.player_id = dts.player_id AND dpv10.year = dts.year)
LEFT JOIN CAREER_STATS cs ON (dpv10.player_id = cs.player_id AND dpv10.year = cs.year)
ORDER BY ays.year desc, ays.driving_distance desc;
-- ORDER BY wins_diff desc;

-- course_yardage_change_per_course_since_1980
select twy.course_id, cl.course_name, min(twy.yardage), max(twy.yardage), max(twy.yardage)-min(twy.yardage) as "yardage diff", (max(twy.yardage)-min(twy.yardage))/min(twy.yardage)*100 as percent_increase, 1980 as "start_year"
from TOURNAMENT_WITH_YARDAGE twy
left join course_list cl ON (twy.course_id = cl.course_id)
where tourn_date > '1979-12-31' AND year < 2023
group by twy.course_id
order by percent_increase desc;

-- course_yardage_every_year_by_course_1980
select twy.course_id, cl.course_name, twy.year, twy.tourn_date, twy.yardage, twy.par, twy.yardage/twy.par as yardage_per_par, (twy.yardage/twy.par)*72 as yardage_per_par_72, twy.score, twy.to_par
from TOURNAMENT_WITH_YARDAGE twy
left join course_list cl ON (twy.course_id = cl.course_id)
where tourn_date > '1979-12-31'
order by tourn_date desc;

-- course_yardage_by_major
select twy.tournament_num, tl.tournament_name, twy.course_id, cl.course_name, twy.year, twy.tourn_date, twy.yardage, twy.par, twy.yardage/twy.par as yardage_per_par, (twy.yardage/twy.par)*72 as yardage_per_par_72, twy.score, twy.to_par
from TOURNAMENT_WITH_YARDAGE twy
left join course_list cl ON (twy.course_id = cl.course_id)
left join tournament_list tl ON (twy.tournament_num = tl.tournament_num)
-- where tourn_date > '1979-12-31'
WHERE twy.tournament_num = 20 -- Masters
OR twy.tournament_num = 26 -- PGA Championship
OR twy.tournament_num = 30 -- US Open
OR twy.tournament_num = 36 -- Open Championship
OR twy.tournament_num = 15 -- Players
OR twy.tournament_num = 13 -- Arnold Palmer
OR twy.tournament_num = 28 -- Memorial
OR twy.tournament_num = 42 -- Tour Championship
order by twy.tourn_date desc;

select * from tournament_list;

select cl.course_name, min(twy.yardage) "Min. Yardage", max(twy.yardage) "Max Yardage", (max(twy.yardage)-min(twy.yardage))/min(twy.yardage) as "% Change", MIN(twy.year) "1st year", max(twy.year) "last_year"
from TOURNAMENT_WITH_YARDAGE twy
left join course_list cl ON (twy.course_id = cl.course_id)
where twy.year >= 1980 AND twy.year < 2023 AND cl.course_name != 'Las Vegas Hilton CC'
group by cl.course_name
order by "% Change" desc;



-- 
select dpv10.player_id "Player ID",dpv10.player_name "Name",dpv10.age_end_yr "Age",dpv10.year "Year", cs.season "Season", dpv10.distance_measured_avg "Driving Distance",
ays.par3_scoring_avg "Par 3 Avg",
ays.par3_birdie_or_better "Par 3 Birdie+",
ays.par4_scoring_avg "Par 4 Avg",
ays.par4_birdie_or_better "Par 4 Birdie+",
ays.par5_scoring_avg "Par 5 Avg",
ays.par5_birdie_or_better "Par 5 Birdie+"
from DISTANCE_PERCENTILE_VS_TOP10 dpv10
LEFT JOIN ALL_YEARLY_STATS ays ON (dpv10.player_id = ays.player_id AND dpv10.year = ays.year)
LEFT JOIN DISTANCE_TO_HOLE_AFTER_TEE_SHOT dts ON (dpv10.player_id = dts.player_id AND dpv10.year = dts.year)
LEFT JOIN CAREER_STATS cs ON (dpv10.player_id = cs.player_id AND dpv10.year = cs.year);

-- Top 50 all time distance with year
select dpv10.player_id "Player ID",dpv10.player_name "Name",dpv10.age_end_yr "Age",dpv10.year "Year", cs.season "Season", dpv10.distance_measured_avg "Driving Distance", 
dpv10.avg_score_player "Scoring Avg - Player", dpv10.avg_score_field "Scoring Avg - Field", dpv10.avg_score_stroke_differential "Score Stroke Differential Avg"
from DISTANCE_PERCENTILE_VS_TOP10 dpv10
LEFT JOIN ALL_YEARLY_STATS ays ON (dpv10.player_id = ays.player_id AND dpv10.year = ays.year)
LEFT JOIN CAREER_STATS cs ON (dpv10.player_id = cs.player_id AND dpv10.year = cs.year)
order by dpv10.distance_measured_avg desc
LIMIT 50;


-- % of shots taken from ecah distance
-- total shots -- shots from under 50 yards
select ays.year, sum(ays.proximity_to_hole_total_att), sum(approach_more_275_total_att) + sum(approach_250_275_total_att) + sum(approach_225_250_total_att) + sum(approach_200_225_total_att) +
	sum(approach_175_200_total_att) + sum(approach_150_175_total_att) + sum(approach_125_150_total_att) + sum(approach_100_125_total_att) + sum(approach_75_100_total_att) + sum(approach_50_75_total_att)
    as ">50",
    (sum(ays.proximity_to_hole_total_att)) - (sum(approach_more_275_total_att) + sum(approach_250_275_total_att) + sum(approach_225_250_total_att) + sum(approach_200_225_total_att) +
	sum(approach_175_200_total_att) + sum(approach_150_175_total_att) + sum(approach_125_150_total_att) + sum(approach_100_125_total_att) + sum(approach_75_100_total_att) + sum(approach_50_75_total_att)) 
    as "<50",
    sum(approach_less_100_total_att) - (sum(approach_75_100_total_att) + sum(approach_50_75_total_att)) as "<50 true",
	sum(approach_more_100_total_att),
    sum(approach_more_275_total_att) + sum(approach_250_275_total_att) + sum(approach_225_250_total_att) + sum(approach_200_225_total_att) +
	sum(approach_175_200_total_att) + sum(approach_150_175_total_att) + sum(approach_125_150_total_att) + sum(approach_100_125_total_att) + sum(approach_less_100_total_att)
    as "all"
from ALL_YEARLY_STATS ays
where ays.year > 2000
group by ays.year;

select ays.year, sum(approach_more_275_total_att) + sum(approach_250_275_total_att) + sum(approach_225_250_total_att) + sum(approach_200_225_total_att) +
	sum(approach_175_200_total_att) + sum(approach_150_175_total_att) + sum(approach_125_150_total_att) + sum(approach_100_125_total_att) + sum(approach_75_100_total_att) + sum(approach_50_75_total_att)
    as ">50",
    sum(approach_more_275_total_att)/(sum(approach_more_275_total_att) + sum(approach_250_275_total_att) + sum(approach_225_250_total_att) + sum(approach_200_225_total_att) +
	sum(approach_175_200_total_att) + sum(approach_150_175_total_att) + sum(approach_125_150_total_att) + sum(approach_100_125_total_att) + sum(approach_75_100_total_att) + sum(approach_50_75_total_att))*100
    as "% >275",
    sum(approach_250_275_total_att)/(sum(approach_more_275_total_att) + sum(approach_250_275_total_att) + sum(approach_225_250_total_att) + sum(approach_200_225_total_att) +
	sum(approach_175_200_total_att) + sum(approach_150_175_total_att) + sum(approach_125_150_total_att) + sum(approach_100_125_total_att) + sum(approach_75_100_total_att) + sum(approach_50_75_total_att))*100
    as "% 250-275",
    sum(approach_225_250_total_att)/(sum(approach_more_275_total_att) + sum(approach_250_275_total_att) + sum(approach_225_250_total_att) + sum(approach_200_225_total_att) +
	sum(approach_175_200_total_att) + sum(approach_150_175_total_att) + sum(approach_125_150_total_att) + sum(approach_100_125_total_att) + sum(approach_75_100_total_att) + sum(approach_50_75_total_att))*100
    as "% 225-250",
    sum(approach_200_225_total_att)/(sum(approach_more_275_total_att) + sum(approach_250_275_total_att) + sum(approach_225_250_total_att) + sum(approach_200_225_total_att) +
	sum(approach_175_200_total_att) + sum(approach_150_175_total_att) + sum(approach_125_150_total_att) + sum(approach_100_125_total_att) + sum(approach_75_100_total_att) + sum(approach_50_75_total_att))*100
    as "% 200-225",
    sum(approach_175_200_total_att)/(sum(approach_more_275_total_att) + sum(approach_250_275_total_att) + sum(approach_225_250_total_att) + sum(approach_200_225_total_att) +
	sum(approach_175_200_total_att) + sum(approach_150_175_total_att) + sum(approach_125_150_total_att) + sum(approach_100_125_total_att) + sum(approach_75_100_total_att) + sum(approach_50_75_total_att))*100
    as "% 175-200",
    sum(approach_150_175_total_att)/(sum(approach_more_275_total_att) + sum(approach_250_275_total_att) + sum(approach_225_250_total_att) + sum(approach_200_225_total_att) +
	sum(approach_175_200_total_att) + sum(approach_150_175_total_att) + sum(approach_125_150_total_att) + sum(approach_100_125_total_att) + sum(approach_75_100_total_att) + sum(approach_50_75_total_att))*100
    as "% 150-175",
    sum(approach_125_150_total_att)/(sum(approach_more_275_total_att) + sum(approach_250_275_total_att) + sum(approach_225_250_total_att) + sum(approach_200_225_total_att) +
	sum(approach_175_200_total_att) + sum(approach_150_175_total_att) + sum(approach_125_150_total_att) + sum(approach_100_125_total_att) + sum(approach_75_100_total_att) + sum(approach_50_75_total_att))*100
    as "% 125-150",
    sum(approach_100_125_total_att)/(sum(approach_more_275_total_att) + sum(approach_250_275_total_att) + sum(approach_225_250_total_att) + sum(approach_200_225_total_att) +
	sum(approach_175_200_total_att) + sum(approach_150_175_total_att) + sum(approach_125_150_total_att) + sum(approach_100_125_total_att) + sum(approach_75_100_total_att) + sum(approach_50_75_total_att))*100
    as "% 100-125",
    sum(approach_75_100_total_att)/(sum(approach_more_275_total_att) + sum(approach_250_275_total_att) + sum(approach_225_250_total_att) + sum(approach_200_225_total_att) +
	sum(approach_175_200_total_att) + sum(approach_150_175_total_att) + sum(approach_125_150_total_att) + sum(approach_100_125_total_att) + sum(approach_75_100_total_att) + sum(approach_50_75_total_att))*100
    as "% 75-100",
    sum(approach_50_75_total_att)/(sum(approach_more_275_total_att) + sum(approach_250_275_total_att) + sum(approach_225_250_total_att) + sum(approach_200_225_total_att) +
	sum(approach_175_200_total_att) + sum(approach_150_175_total_att) + sum(approach_125_150_total_att) + sum(approach_100_125_total_att) + sum(approach_75_100_total_att) + sum(approach_50_75_total_att))*100
    as "% 50-75"
from ALL_YEARLY_STATS ays
where ays.year > 2000
group by ays.year;

use pga_data_analysis;

select ays.year, sum(proximity_to_hole_total_att), sum(approach_more_275_total_att) + sum(approach_more_275_rough_total_att) + sum(approach_250_275_total_att) + sum(approach_250_275_rough_total_att) + 
	sum(approach_225_250_total_att) + sum(approach_225_250_rough_total_att) + sum(approach_200_225_total_att) + sum(approach_200_225_rough_total_att) +
	sum(approach_175_200_total_att) + sum(approach_175_200_rough_total_att) + sum(approach_150_175_total_att) + sum(approach_150_175_rough_total_att) + 
    sum(approach_125_150_total_att) + sum(approach_125_150_rough_total_att) + sum(approach_100_125_total_att) + sum(approach_100_125_rough_total_att) + 
    sum(approach_75_100_total_att) + sum(approach_75_100_rough_total_att) + sum(approach_50_75_total_att) + sum(approach_50_75_rough_total_att)
    as ">50",
    (sum(approach_more_275_total_att) + sum(approach_more_275_rough_total_att))/(sum(approach_more_275_total_att) + sum(approach_more_275_rough_total_att) + sum(approach_250_275_total_att) + sum(approach_250_275_rough_total_att) + 
	sum(approach_225_250_total_att) + sum(approach_225_250_rough_total_att) + sum(approach_200_225_total_att) + sum(approach_200_225_rough_total_att) +
	sum(approach_175_200_total_att) + sum(approach_175_200_rough_total_att) + sum(approach_150_175_total_att) + sum(approach_150_175_rough_total_att) + 
    sum(approach_125_150_total_att) + sum(approach_125_150_rough_total_att) + sum(approach_100_125_total_att) + sum(approach_100_125_rough_total_att) + 
    sum(approach_75_100_total_att) + sum(approach_75_100_rough_total_att) + sum(approach_50_75_total_att) + sum(approach_50_75_rough_total_att))*100
    as "% >275",
    (sum(approach_more_275_total_att) + sum(approach_more_275_rough_total_att))/(sum(approach_more_275_total_att) + sum(approach_more_275_rough_total_att) + sum(approach_250_275_total_att) + sum(approach_250_275_rough_total_att) + 
	sum(approach_225_250_total_att) + sum(approach_225_250_rough_total_att) + sum(approach_200_225_total_att) + sum(approach_200_225_rough_total_att) +
	sum(approach_175_200_total_att) + sum(approach_175_200_rough_total_att) + sum(approach_150_175_total_att) + sum(approach_150_175_rough_total_att) + 
    sum(approach_125_150_total_att) + sum(approach_125_150_rough_total_att) + sum(approach_100_125_total_att) + sum(approach_100_125_rough_total_att) + 
    sum(approach_75_100_total_att) + sum(approach_75_100_rough_total_att) + sum(approach_50_75_total_att) + sum(approach_50_75_rough_total_att))*100
    as "% 250-275",
    (sum(approach_more_275_total_att) + sum(approach_more_275_rough_total_att))/(sum(approach_more_275_total_att) + sum(approach_more_275_rough_total_att) + sum(approach_250_275_total_att) + sum(approach_250_275_rough_total_att) + 
	sum(approach_225_250_total_att) + sum(approach_225_250_rough_total_att) + sum(approach_200_225_total_att) + sum(approach_200_225_rough_total_att) +
	sum(approach_175_200_total_att) + sum(approach_175_200_rough_total_att) + sum(approach_150_175_total_att) + sum(approach_150_175_rough_total_att) + 
    sum(approach_125_150_total_att) + sum(approach_125_150_rough_total_att) + sum(approach_100_125_total_att) + sum(approach_100_125_rough_total_att) + 
    sum(approach_75_100_total_att) + sum(approach_75_100_rough_total_att) + sum(approach_50_75_total_att) + sum(approach_50_75_rough_total_att))*100
    as "% 225-250",
    (sum(approach_more_275_total_att) + sum(approach_more_275_rough_total_att))/(sum(approach_more_275_total_att) + sum(approach_more_275_rough_total_att) + sum(approach_250_275_total_att) + sum(approach_250_275_rough_total_att) + 
	sum(approach_225_250_total_att) + sum(approach_225_250_rough_total_att) + sum(approach_200_225_total_att) + sum(approach_200_225_rough_total_att) +
	sum(approach_175_200_total_att) + sum(approach_175_200_rough_total_att) + sum(approach_150_175_total_att) + sum(approach_150_175_rough_total_att) + 
    sum(approach_125_150_total_att) + sum(approach_125_150_rough_total_att) + sum(approach_100_125_total_att) + sum(approach_100_125_rough_total_att) + 
    sum(approach_75_100_total_att) + sum(approach_75_100_rough_total_att) + sum(approach_50_75_total_att) + sum(approach_50_75_rough_total_att))*100
    as "% 200-225",
    (sum(approach_more_275_total_att) + sum(approach_more_275_rough_total_att))/(sum(approach_more_275_total_att) + sum(approach_more_275_rough_total_att) + sum(approach_250_275_total_att) + sum(approach_250_275_rough_total_att) + 
	sum(approach_225_250_total_att) + sum(approach_225_250_rough_total_att) + sum(approach_200_225_total_att) + sum(approach_200_225_rough_total_att) +
	sum(approach_175_200_total_att) + sum(approach_175_200_rough_total_att) + sum(approach_150_175_total_att) + sum(approach_150_175_rough_total_att) + 
    sum(approach_125_150_total_att) + sum(approach_125_150_rough_total_att) + sum(approach_100_125_total_att) + sum(approach_100_125_rough_total_att) + 
    sum(approach_75_100_total_att) + sum(approach_75_100_rough_total_att) + sum(approach_50_75_total_att) + sum(approach_50_75_rough_total_att))*100
    as "% 175-200",
    (sum(approach_more_275_total_att) + sum(approach_more_275_rough_total_att))/(sum(approach_more_275_total_att) + sum(approach_more_275_rough_total_att) + sum(approach_250_275_total_att) + sum(approach_250_275_rough_total_att) + 
	sum(approach_225_250_total_att) + sum(approach_225_250_rough_total_att) + sum(approach_200_225_total_att) + sum(approach_200_225_rough_total_att) +
	sum(approach_175_200_total_att) + sum(approach_175_200_rough_total_att) + sum(approach_150_175_total_att) + sum(approach_150_175_rough_total_att) + 
    sum(approach_125_150_total_att) + sum(approach_125_150_rough_total_att) + sum(approach_100_125_total_att) + sum(approach_100_125_rough_total_att) + 
    sum(approach_75_100_total_att) + sum(approach_75_100_rough_total_att) + sum(approach_50_75_total_att) + sum(approach_50_75_rough_total_att))*100
    as "% 150-175",
    (sum(approach_more_275_total_att) + sum(approach_more_275_rough_total_att))/(sum(approach_more_275_total_att) + sum(approach_more_275_rough_total_att) + sum(approach_250_275_total_att) + sum(approach_250_275_rough_total_att) + 
	sum(approach_225_250_total_att) + sum(approach_225_250_rough_total_att) + sum(approach_200_225_total_att) + sum(approach_200_225_rough_total_att) +
	sum(approach_175_200_total_att) + sum(approach_175_200_rough_total_att) + sum(approach_150_175_total_att) + sum(approach_150_175_rough_total_att) + 
    sum(approach_125_150_total_att) + sum(approach_125_150_rough_total_att) + sum(approach_100_125_total_att) + sum(approach_100_125_rough_total_att) + 
    sum(approach_75_100_total_att) + sum(approach_75_100_rough_total_att) + sum(approach_50_75_total_att) + sum(approach_50_75_rough_total_att))*100
    as "% 125-150",
    (sum(approach_more_275_total_att) + sum(approach_more_275_rough_total_att))/(sum(approach_more_275_total_att) + sum(approach_more_275_rough_total_att) + sum(approach_250_275_total_att) + sum(approach_250_275_rough_total_att) + 
	sum(approach_225_250_total_att) + sum(approach_225_250_rough_total_att) + sum(approach_200_225_total_att) + sum(approach_200_225_rough_total_att) +
	sum(approach_175_200_total_att) + sum(approach_175_200_rough_total_att) + sum(approach_150_175_total_att) + sum(approach_150_175_rough_total_att) + 
    sum(approach_125_150_total_att) + sum(approach_125_150_rough_total_att) + sum(approach_100_125_total_att) + sum(approach_100_125_rough_total_att) + 
    sum(approach_75_100_total_att) + sum(approach_75_100_rough_total_att) + sum(approach_50_75_total_att) + sum(approach_50_75_rough_total_att))*100
    as "% 100-125",
    (sum(approach_more_275_total_att) + sum(approach_more_275_rough_total_att))/(sum(approach_more_275_total_att) + sum(approach_more_275_rough_total_att) + sum(approach_250_275_total_att) + sum(approach_250_275_rough_total_att) + 
	sum(approach_225_250_total_att) + sum(approach_225_250_rough_total_att) + sum(approach_200_225_total_att) + sum(approach_200_225_rough_total_att) +
	sum(approach_175_200_total_att) + sum(approach_175_200_rough_total_att) + sum(approach_150_175_total_att) + sum(approach_150_175_rough_total_att) + 
    sum(approach_125_150_total_att) + sum(approach_125_150_rough_total_att) + sum(approach_100_125_total_att) + sum(approach_100_125_rough_total_att) + 
    sum(approach_75_100_total_att) + sum(approach_75_100_rough_total_att) + sum(approach_50_75_total_att) + sum(approach_50_75_rough_total_att))*100
    as "% 75-100",
    (sum(approach_more_275_total_att) + sum(approach_more_275_rough_total_att))/(sum(approach_more_275_total_att) + sum(approach_more_275_rough_total_att) + sum(approach_250_275_total_att) + sum(approach_250_275_rough_total_att) + 
	sum(approach_225_250_total_att) + sum(approach_225_250_rough_total_att) + sum(approach_200_225_total_att) + sum(approach_200_225_rough_total_att) +
	sum(approach_175_200_total_att) + sum(approach_175_200_rough_total_att) + sum(approach_150_175_total_att) + sum(approach_150_175_rough_total_att) + 
    sum(approach_125_150_total_att) + sum(approach_125_150_rough_total_att) + sum(approach_100_125_total_att) + sum(approach_100_125_rough_total_att) + 
    sum(approach_75_100_total_att) + sum(approach_75_100_rough_total_att) + sum(approach_50_75_total_att) + sum(approach_50_75_rough_total_att))*100
    as "% 50-75"
from ALL_YEARLY_STATS ays
where ays.year > 2000
group by ays.year;

select twy.year, AVG(twy.yardage), sum(twy.yardage), count(twy.tournament_id)
from TOURNAMENT_WITH_YARDAGE twy
WHERE twy.tournament_num = 20 -- Masters
OR twy.tournament_num = 26 -- PGA Championship
OR twy.tournament_num = 30 -- US Open
OR twy.tournament_num = 36 -- Open Championship
GROUP BY twy.year
HAVING twy.year BETWEEN 1980 AND  2022;

-- Average length of all majors or non-majors between 1980 and 2022
select avg(twy.yardage), count(twy.tournament_yr_id)
from TOURNAMENT_WITH_YARDAGE twy
left join ALL_TOURNAMENT_AFTER_1958 at58 USING (tournament_yr_id)
WHERE tour_status_id != 2
AND twy.year BETWEEN 1980 AND 2022;


select sum(approach_more_275_total_ft)/sum(approach_more_275_total_att) as ">275 fairway", sum(approach_more_275_rough_total_ft)/sum(approach_more_275_rough_total_att) ">275 rough",
sum(approach_250_275_total_ft)/sum(approach_250_275_total_att) "250_275 fairway", sum(approach_250_275_rough_total_ft)/sum(approach_250_275_rough_total_att) "250_275 rough",
sum(approach_225_250_total_ft)/sum(approach_225_250_total_att) "225_250 fairway", sum(approach_225_250_rough_total_ft)/sum(approach_225_250_rough_total_att) "225_250 rough",
sum(approach_200_225_total_ft)/sum(approach_200_225_total_att) "200-225 fairway", sum(approach_200_225_rough_total_ft)/sum(approach_200_225_rough_total_att) "200-225 rough",
sum(approach_175_200_total_ft)/sum(approach_175_200_total_att) "175_200 fairway", sum(approach_175_200_rough_total_ft)/sum(approach_175_200_rough_total_att) "175_200 rough",
sum(approach_150_175_total_ft)/sum(approach_150_175_total_att) "150_175 fairway", sum(approach_150_175_rough_total_ft)/sum(approach_150_175_rough_total_att) "150_175 rough",
sum(approach_125_150_total_ft)/sum(approach_125_150_total_att) "125_150 fairway", sum(approach_125_150_rough_total_ft)/sum(approach_125_150_rough_total_att) "125_150 rough",
sum(approach_100_125_total_ft)/sum(approach_100_125_total_att) "100_125 fairway", sum(approach_100_125_rough_total_ft)/sum(approach_100_125_rough_total_att) "100_125 rough",
sum(approach_75_100_total_ft)/sum(approach_75_100_total_att) "75_100 fairway", sum(approach_75_100_rough_total_ft)/sum(approach_75_100_rough_total_att) "75_100 rough",
sum(approach_50_75_total_ft)/sum(approach_50_75_total_att) "50_75 fairway", sum(approach_50_75_rough_total_ft)/sum(approach_50_75_rough_total_att) "50_75 rough"
from all_yearly_stats
where year between 2002 and 2022;

select sum(approach_200_225_total_ft)/sum(approach_200_225_total_att), sum(approach_200_225_rough_total_ft)/sum(approach_200_225_rough_total_att)
from all_yearly_stats;