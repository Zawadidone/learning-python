
def ticker(filename):
    ticker_symbol = {}

    lines = open(filename, "r").read().splitlines()

    for l in lines:
        key = l.split(":")
        ticker_symbol[key[0]] = key[1]

    return ticker_symbol

ticker_symbol_dict = ticker("ticker.txt")

try:
    company_name = input("Enter company name: ")
    print(f"Ticker Symbol: {ticker_symbol_dict[company_name]}\n")
except KeyError:
    print("Company doesn't exist ...\n")

symbol = input("Enter ticker symbol: ")

result = "Ticker symbol doesn't exist"

for item in ticker_symbol_dict.items():
    if item[1] == symbol:
        result = item[0]
        break

print(result)
