from stockwhisper.actor import Actor
from stockwhisper.db_lib import FUTURES_TABLE
from stockwhisper.prompts import PROMPT_FOR_VALIDATING_QUERY_FOR_YFINANCE

stock_actor = Actor(FUTURES_TABLE, PROMPT_FOR_VALIDATING_QUERY_FOR_YFINANCE)
