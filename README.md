
![Homepage](https://github.com/user-attachments/assets/3c994d46-d6b2-4cb5-9716-4b06e30ff832)

# Sahm - AI Equity Research Assistant and Portfolio Management Hub
Sahm is an AI-powered assistant for retail investors, providing stock analysis and portfolio management tools. It leverages GPT-4o mini to offer insights on financial data retrieved through yfinance. The project utilizes modern LLM features like function calling and structured JSON outputs for efficient data processing and presentation.
## Key Features
- comprehensive single stock analysis
- batch stock comparison for portfolio decisions 
- ai-generated insights on basic company financials
- real-time stock data integration using yfinance
- structured JSON outputs for easy integration with other tools
## How It Works 
the application uses GPT-4o mini to analyze stocks based on data retrieved from yfinance:
- function calling enables dynamic retrieval of financial data
- structured JSON outputs provide standardized, easily parseable results
- ai-generated insights offer analysis of company performance based on available metrics
- integration with yfinance provides up-to-date basic company information
## Project Structure
```

fastapi-openai-stock/
│ 
├── app/
│   ├── **init**.py
│   ├── main.py
│   ├── routers/
│   │   └── stock.py
│   ├── services/
│   │   └── openai_service.py  
│   └── models/
│       └── stock.py
│
├── .env
├── requirements.txt
└── readme.md
```
## Setup
1. clone the repository:
   ```
   git clone https://github.com/yourusername/fastapi-openai-stock.git
   cd fastapi-openai-stock
   ```
2. create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/scripts/activate  # on Windows
   # source venv/bin/activate  # on Unix or macOS 
   ```
3. install required packages:
   ```
   pip install -r requirements.txt
   ```
4. create a `.env` file and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```
## Running the Application
start the server:
```
uvicorn app.main:app --reload
```
the API will be available at `http://localhost:8000`. Documentation is at `http://localhost:8000/docs`.
## API Endpoints
- `POST /api/stock/analyze`: get comprehensive analysis of a single stock
- `GET /api/stock/info/{ticker}`: retrieve basic stock information 
- `POST /api/stock/batch-analyze`: analyze multiple stocks for portfolio decisions
- `POST /api/stock/compare`: compare stocks side-by-side with AI insights
## Usage Examples
### Analyze a Single Stock
```python
import requests
response = requests.post("http://localhost:8000/api/stock/analyze", json={"ticker": "AAPL"})
print(response.json())
```
### Get Stock Information
```python
import requests 
response = requests.get("http://localhost:8000/api/stock/info/AAPL")
print(response.json())
```
### Batch Analyze Stocks
```python
import requests
response = requests.post("http://localhost:8000/api/stock/batch-analyze", json=["AAPL", "GOOGL", "MSFT"])
print(response.json())
```  
### Compare Stocks
```python
import requests
response = requests.post("http://localhost:8000/api/stock/compare", json=["AAPL", "GOOGL"])
print(response.json())
```
## Future Plans  
- implement natural language querying of company regulatory filings (10-Ks, 10-Qs) for deeper insights
- develop an analytics dashboard for visualizing company metrics
- build a user-friendly frontend for easy interaction and data visualization  
- create ai-powered news analysis for market sentiment
- implement user authentication for personalized experiences
- set up a database for user portfolios and analysis history
- integrate advanced charting for technical analysis
- add more comprehensive fundamental analysis metrics and ratios
- implement alerts for significant stock movements or ai-detected opportunities
## Contributing
contributions are welcome. please feel free to submit a pull request.
## License
This project is licensed under the MIT License.
