#!/bin/bash
export SOURCE='/Users/indiram/Work/CAC/rss_feeds'
source $SOURCE/.env

python3 $SOURCE/article_update.py
python3 $SOURCE/clean_data.py