# Double Scoop

Set up and automate RSS feed reader 

## Installation

### Install Packages

Run this code in your terminal to install all required packages.

```bash
pip install -r requirements.txt
```

## Usage

### Automate using a Cronjob
1. Create 'cron_update.sh' in project folder

```bash
#!/bin/bash
export SOURCE='project_path'
source $SOURCE/.env

echo -n "Updated on: "; date
python3 $SOURCE/article_update.py
python3 $SOURCE/clean_data.py

echo -e " "
```
2. Setup symbolic link
```bash
ln -s /full/path/to/project/main.py article_update
```
3. Create Cron Job
```
crontab -e
```
4. Edit Cronjob
```bash
0 7 * * * /Users/'user'/article_update >> /Users/'user'/log_folders/article_update_log.txt
```
This command runs article update every day at 7:00 AM. Time and frequency can be changed. For more information refer to:  [Crontab.guru](https://crontab.guru/#0_13_*_*_*)


## Configuration

### Set up .env
```python
SUPABASE_URL='your_url'
SUPABASE_KEY='public_api_key'
SOURCE_PATH='rss_feed_csv_file_path'
```

## Dependencies

## Dependencies

- [Beautiful Soup](https://pypi.org/project/beautifulsoup4/)
- [Requests](https://pypi.org/project/requests/)
- [CSV](https://docs.python.org/3/library/csv.html)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [Supabase](https://pypi.org/project/supabase-py/)
- [Regular Expressions (re)](https://docs.python.org/3/library/re.html)


## Folder Structure
```css
rss_feeds/
│
├── README.md
│
├── requirements.txt
│
├── rss_feeds.csv
│
├── .env
│
├── cron_update.sh
│
└── src/
    │
    ├── __init__.py
    │
    ├── main.py
    │
    ├── article_update.py
    │
    ├── clean_data.py
    │
    └── washpost.py

```

## License
This project is licensed under the MIT License - see the [LICENSE file](LICENSE) for details.

## Authors

- [Indira Mariya](link-to-author-profile)
- [Sabrina Yen-Ko](link-to-author-profile)

## Acknowledgments

Mention any resources or tools you used or were inspired by.

## Troubleshooting

Common issues and troubleshooting tips.

## Contact

How to reach out for questions or support.
