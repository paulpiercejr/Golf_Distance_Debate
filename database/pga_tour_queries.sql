-- select aggregate yardage and par for courses each year by type of event
SELECT at58.year, es.event_status, count(twy.yardage) as num_of_courses, sum(twy.yardage)/sum(twy.par) AS yrds_per_par,
  (sum(twy.yardage)/sum(twy.par))*72 AS yrds_per_par72,
  avg(twy.yardage) as avg_yardage, sum(twy.yardage) as total_yardage,
  avg(twy.par) as avg_par, sum(twy.par) as total_par, max(twy.yardage) as longest_course,
  min(twy.yardage) as shortest_course
FROM TOURNAMENT_WITH_YARDAGE twy
JOIN ALL_TOURNAMENT_AFTER_1958 at58 ON (twy.tournament_yr_id = at58.tournament_yr_id)
JOIN EVENT_STATUS es ON (es.tour_status_id = at58.tour_status_id)
-- WHERE es.tour_status_id = 2
WHERE twy.yardage is not null
GROUP BY at58.year, es.tour_status_id
ORDER BY at58.year DESC;

-- aggregate yardage of all courses played in official PGA Tour events
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

-- SELECT at58.year, twy.yardage, twy.par
-- FROM TOURNAMENT_WITH_YARDAGE twy
-- JOIN ALL_TOURNAMENT_AFTER_1958 at58 ON (twy.tournament_id = at58.tournament_id)
-- WHERE (SELECT twy.tournament_yr_id
--        FROMtwy.tournament_id


-- proximity to the hole in ft
SELECT year, count(proximity_to_hole_total_ft) as total_players, (sum(proximity_to_hole_total_ft)/sum(proximity_to_hole_total_att)) as "proximity to hole ft"
FROM ALL_YEARLY_STATS
WHERE proximity_to_hole_total_ft is not NULL
GROUP BY year;


-- total birdies and rounds
SELECT year, sum(birdie_avg_num_birdies) as 'total birdies', sum(birdie_avg_total_rounds) as 'total rounds', sum(birdie_avg_num_birdies)/sum(birdie_avg_total_rounds) as 'birdie avg'
FROM `ALL_YEARLY_STATS`
GROUP BY year
ORDER BY year desc;

-- going for green and hitting it
SELECT year, sum(going_for_green_percent_attempts) as going_for_green_att,
  sum(going_for_green_percent_non_attemptes) as going_for_green_non_att,
  sum(going_for_green_percent_attempts)/(sum(going_for_green_percent_attempts)+sum(going_for_green_percent_non_attemptes)) as 'possible_gfg_%',
  sum(going_for_green_hit), sum(going_for_green_attempts),
  sum(going_for_green_birdie_better_total)
FROM `ALL_YEARLY_STATS`
GROUP BY year
ORDER BY year desc;

--
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
GROUP BY year
ORDER BY year desc;



-- player stats query
select ays.stat_id, ays.player_id, p.full_name, ays.age_end_yr, ays.year, ays.season, ays.scoring_avg_actual, ays.scoring_avg_adj, ays.driving_distance,
  ays.driving_distance_all_drives, ays.club_head_speed, ays.birdie_avg, ays.driving_accuracy, ays.going_for_green_percent,
  ays.greens_in_regulation_percent, ays.par3_scoring_avg, ays.par4_scoring_avg, ays.par5_scoring_avg,
  ays.par_breaker_percent, ays.proximity_to_hole_in/12, ays.scrambling_percent, ays.sg_off_tee, ays.sg_app_green,
  ays.sg_around_green, ays.sg_putting, ays.sg_total, p.height, p.weight, wybp.wins, wybp.team_wins
FROM ALL_YEARLY_STATS ays
LEFT JOIN PLAYERS p USING (player_id)
LEFT OUTER JOIN WINNERS_PER_YEAR_BY_PLAYER wybp USING (player_id, year)
WHERE ays.driving_accuracy_rank is not null
AND ays.year < 2023
-- AND wybp.year = ays.year
ORDER BY ays.year desc, ays.driving_distance desc;

-- check which players have NULL ages
select ays.stat_id, ays.player_id, p.full_name, ays.age_end_yr, ays.season, ays.year
FROM ALL_YEARLY_STATS ays
LEFT JOIN PLAYERS p USING (player_id)
WHERE ays.age_end_yr is null
ORDER BY ays.player_id;

select *
from PLAYERS p
where p.player_id IN (select distinct ays.player_id
  FROM ALL_YEARLY_STATS ays
  WHERE ays.age_end_yr is null);


-- distance percentile of qualifying drivers
SELECT p.full_name, ays.player_id, ays.year, ays.driving_distance, ays.scoring_avg_actual,
ays.scoring_avg_adj, ays.sg_total, ays.sg_off_tee, ays.sg_app_green, ays.sg_around_green,
ays.sg_putting, ays.sg_tee_to_green, ays.driving_distance_all_drives, ays.driving_accuracy,
ROUND( PERCENT_RANK() OVER(
    PARTITION BY ays.year
    ORDER BY ays.driving_distance
  ),2) as percentile_rank
FROM PLAYERS p
JOIN ALL_YEARLY_STATS ays ON (p.player_id = ays.player_id)
WHERE ays.driving_distance_rank is not null
AND ays.year < 2023
ORDER BY ays.year desc, ays.driving_distance desc;


