import openai
import json
import yfinance as yf
from app.models.stock import StockInfo, Analysis, AnalysisResult, FunctionDefinition, FunctionParameter
from typing import List

def initialize_openai(api_key: str):
    openai.api_key = api_key

def get_stock_info_function():
    return FunctionDefinition(
        name="get_stock_info",
        description="Get the current stock information for a given ticker symbol",
        parameters=FunctionParameter(
            type="object",
            properties={
                "ticker": {
                    "type": "string",
                    "description": "The stock ticker symbol, e.g., AAPL for Apple Inc.",
                },
            },
            required=["ticker"]
        )
    )

def fetch_stock_info(ticker: str) -> StockInfo:
    stock = yf.Ticker(ticker)
    info = stock.info
    return StockInfo(
        ticker=ticker,
        current_price=info.get('currentPrice'),
        market_cap=info.get('marketCap'),
        pe_ratio=info.get('trailingPE'),
        dividend_yield=info.get('dividendYield'),
        fifty_two_week_high=info.get('fiftyTwoWeekHigh'),
        fifty_two_week_low=info.get('fiftyTwoWeekLow')
    )

async def analyze_stock(ticker: str) -> AnalysisResult:
    messages = [{"role": "user", "content": f"Analyze the stock {ticker} and provide insights."}]
    functions = [get_stock_info_function().dict()]

    while True:
        response = await openai.ChatCompletion.acreate(
            model="gpt-4o-mini",  # changed to 4o mini
            messages=messages,
            functions=functions,
            function_call="auto",
        )

        message = response["choices"][0]["message"]

        if message.get("function_call"):
            function_name = message["function_call"]["name"]
            function_args = json.loads(message["function_call"]["arguments"])
            
            if function_name == "get_stock_info":
                stock_info = fetch_stock_info(function_args["ticker"])
                messages.append({
                    "role": "function",
                    "name": function_name,
                    "content": json.dumps(stock_info.dict())
                })
            else:
                break
        else:
            break

    final_response = await openai.ChatCompletion.acreate(
        model="gpt-4o-mini",  # changed to 4o mini
        messages=messages,
        functions=[{
            "name": "provide_analysis",
            "description": "Provide a structured analysis of the stock",
            "parameters": {
                "type": "object",
                "properties": {
                    "summary": {"type": "string"},
                    "pros": {"type": "array", "items": {"type": "string"}},
                    "cons": {"type": "array", "items": {"type": "string"}},
                    "recommendation": {"type": "string"}
                },
                "required": ["summary", "pros", "cons", "recommendation"]
            }
        }],
        function_call={"name": "provide_analysis"}
    )

    analysis_data = json.loads(final_response["choices"][0]["message"]["function_call"]["arguments"])
    
    return AnalysisResult(
        analysis=Analysis(**analysis_data),
        stock_info=stock_info
    )

async def batch_analyze_stocks(tickers: List[str]) -> List[AnalysisResult]:
    results = []
    for ticker in tickers:
        result = await analyze_stock(ticker)
        results.append(result)
    return results

async def compare_stocks(tickers: List[str]) -> List[AnalysisResult]:
    results = await batch_analyze_stocks(tickers)
    return results