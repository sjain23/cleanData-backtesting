import yfinance as yf
import back_testing
import pandas as pd
import requests as rq
from config import get_access_token, get_consumer_key, get_db_name, get_password, get_refresh_token, get_username
import asyncio
from pymongo import MongoClient

class BackTesting():
    def main(self):
        return "nothing yet"
    def load_data():
        df = pd.read_csv("tickersS&P.csv")
        db = create_connection()
        for i in df['Symbol']:
            response = rq.get("https://api.tdameritrade.com/v1/marketdata/" +i+"/pricehistory",{
                "apikey":get_consumer_key()
            });
            response_data = response.json()
            db.replace_one({
                "ticker":i
            },
            {
                "ticker":i,
                "candlesticks": response_data
                })
        return "success"


    def parse_tickers():
        payload=pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
        df = payload[0]
        df.to_csv('tickersS&P.csv',columns=['Symbol'])

    def cleanse_data(self):
        print("cleansing data")

def create_connection():
    cluster = MongoClient('mongodb+srv://'+get_username()+':'+get_password()+'@cluster0.mfsww.mongodb.net/'+get_db_name()+'?retryWrites=true&w=majority')
    db = cluster.CleanData
    col = db.tradeCandlesticks
    return col

BackTesting.load_data()