stocks = {
    'AAPL': 121,
    'AMZN': 3380,
    'MSFT': 219,
    'BIIB': 80,
    'QDEL': 266,
    'LVGO': 144
}

# print(stocks)

selected_stocks = {s: p for (s, p) in stocks.items() if p < 200}
print(selected_stocks)