from pydantic import BaseModel
from typing import List, Optional

class StockRequest(BaseModel):
    ticker: str
    # just the stock symbol, like "aapl" for apple

class StockInfo(BaseModel):
    ticker: str
    current_price: Optional[float]
    market_cap: Optional[int]
    pe_ratio: Optional[float]
    dividend_yield: Optional[float]
    fifty_two_week_high: Optional[float]
    fifty_two_week_low: Optional[float]
    # all the basic stuff you'd want to know about a stock
    # using optionals cause sometimes this data might be missing

class Analysis(BaseModel):
    summary: str
    pros: List[str]
    cons: List[str]
    recommendation: str
    # this is where the ai's thoughts on the stock go
    # summary for a quick overview, pros and cons for the details,
    # and a recommendation to buy, sell, or hold

class AnalysisResult(BaseModel):
    analysis: Analysis
    stock_info: StockInfo
    # combines the ai analysis with the raw stock data
    # gives you the full picture in one package

class FunctionParameter(BaseModel):
    type: str
    properties: dict
    required: List[str]
    # this is for defining what info the openai function needs
    # helps the ai know what to ask for

class FunctionDefinition(BaseModel):
    name: str
    description: str
    parameters: FunctionParameter
    # the full definition of a function for the ai to use
    # tells it what the function does and what it needs to work

class StockResponse(BaseModel):
    analysis: Analysis
    stock_info: StockInfo
    # what we send back when someone asks for a stock analysis
    # includes both the ai's thoughts and the raw data