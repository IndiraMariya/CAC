#library imports
from bs4 import BeautifulSoup
import requests
import csv
from dotenv import load_dotenv
import os
from supabase import Client
import re

#file imports
import washpost