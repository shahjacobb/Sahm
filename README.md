# fastapi stock analysis with openai

this project is a fastapi application that provides stock analysis using openai's function calling feature and real-time stock data from yfinance.

## features

- single stock analysis
- batch stock analysis
- stock comparison
- real-time stock information retrieval
- integration with openai for intelligent analysis
- structured json outputs using pydantic models

## project structure

```
fastapi-openai-stock/
│
├── app/
│   ├── __init__.py
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

## setup

1. clone the repository:
   ```
   git clone https://github.com/yourusername/fastapi-openai-stock.git
   cd fastapi-openai-stock
   ```

2. create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/scripts/activate  # on windows
   # source venv/bin/activate  # on unix or macos
   ```

3. install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. create a `.env` file in the root directory and add your openai api key:
   ```
   openai_api_key=your_openai_api_key_here
   ```

## running the application

to run the fastapi application:

```
uvicorn app.main:app --reload
```

the api will be available at `http://localhost:8000`. you can access the interactive api documentation at `http://localhost:8000/docs`.

## api endpoints

- `post /api/stock/analyze`: analyze a single stock
- `get /api/stock/info/{ticker}`: get basic stock information
- `post /api/stock/batch-analyze`: analyze multiple stocks
- `post /api/stock/compare`: compare multiple stocks

## usage examples

### analyze a single stock

```python
import requests

response = requests.post("http://localhost:8000/api/stock/analyze", json={"ticker": "aapl"})
print(response.json())
```

### get stock information

```python
import requests

response = requests.get("http://localhost:8000/api/stock/info/aapl")
print(response.json())
```

### batch analyze stocks

```python
import requests

response = requests.post("http://localhost:8000/api/stock/batch-analyze", json=["aapl", "googl", "msft"])
print(response.json())
```

### compare stocks

```python
import requests

response = requests.post("http://localhost:8000/api/stock/compare", json=["aapl", "googl"])
print(response.json())
```

## to do

- develop an analytics dashboard using the structured json output from our api
- create an all-in-one investor hub with portfolio tracking and visualization features

## contributing

contributions are welcome! please feel free to submit a pull request.

## license

this project is licensed under the mit license.