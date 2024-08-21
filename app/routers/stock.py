from fastapi import APIRouter, HTTPException, Depends
from app.models.stock import StockRequest, StockResponse, StockInfo, Analysis
from app.services.openai_service import analyze_stock, fetch_stock_info
from typing import List

router = APIRouter()

@router.post("/analyze", response_model=StockResponse)
async def analyze_stock_endpoint(request: StockRequest):
    """
    Analyze a stock using OpenAI function calling and yfinance data.
    """
    try:
        result = await analyze_stock(request.ticker)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/info/{ticker}", response_model=StockInfo)
async def get_stock_info(ticker: str):
    """
    Get basic stock information for a given ticker.
    """
    try:
        return fetch_stock_info(ticker)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/batch-analyze", response_model=List[StockResponse])
async def batch_analyze_stocks(tickers: List[str]):
    """
    Analyze multiple stocks in a single request.
    """
    try:
        results = []
        for ticker in tickers:
            result = await analyze_stock(ticker)
            results.append(result)
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/compare", response_model=List[StockResponse])
async def compare_stocks(tickers: List[str]):
    """
    Compare multiple stocks and provide a comparative analysis.
    """
    try:
        results = []
        for ticker in tickers:
            result = await analyze_stock(ticker)
            results.append(result)
        
        # Here you might want to add additional comparative analysis
        # using OpenAI to compare the stocks directly
        
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))