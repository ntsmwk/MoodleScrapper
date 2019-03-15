#!/bin/bash
now=$(date)
curl --cookie "MoodleSessionjku2015SessionCookie=ehr876dtbaeflp4qmdo623m5s1" https://moodle.jku.at/jku2015/mod/assign/view.php?id=2194989 > ~/git/MoodleScrapper/"UE1_$now.txt"

