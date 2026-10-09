import pandas as pd
import requests

class InventoryAgent:
    def __init__(self, file_path):
        # Load and clean dataset
        self.df = pd.read_excel(file_path, skiprows=5)
        self.df.columns = [col.strip().replace("\n", " ").replace("  ", " ") for col in self.df.columns]
        self.df = self.df.drop(columns=["Unnamed: 0"])

        # Dictionary of business definitions
        self.definitions = {
            "cost price": "Cost price is the amount paid to acquire or produce a product, including raw materials, labor, and overheads.",
            "stock value": "Stock value is the total worth of inventory on hand, calculated as quantity multiplied by cost price per unit.",
            "units sold": "Units sold refers to the total number of items sold from inventory over a given period."
        }

    def lookup_definition(self, term):
        term = term.lower().strip()
        if term in self.definitions:
            return self.definitions[term]
        else:
            # fallback to DuckDuckGo if not in dictionary
            url = f"https://api.duckduckgo.com/?q={term}&format=json"
            response = requests.get(url).json()
            if response.get("AbstractText"):
                return response["AbstractText"]
            else:
                return f"Sorry, I couldn’t find a definition for {term}."

    def answer(self, query):
        query = query.lower()

        if "total stock value" in query:
            self.df["StockValue"] = self.df["Hand-In- Stock"] * self.df["Cost Price Per Unit (USD)"]
            total_value = self.df["StockValue"].sum()
            return f"The total stock value is ${total_value:,}."

        elif "highest cost product" in query:
            max_row = self.df.loc[self.df["Cost Price Per Unit (USD)"].idxmax()]
            return f"The highest cost product is {max_row['Product Name']} at ${max_row['Cost Price Per Unit (USD)']} per unit."

        elif "units sold" in query:
            total_sold = self.df["Number of Units Sold"].sum()
            return f"A total of {total_sold} units have been sold across all products."

        elif "what is" in query or "define" in query:
            term = query.replace("what is", "").replace("define", "").strip()
            definition = self.lookup_definition(term)

            # Combine definition with dataset insight
            if "cost price" in term:
                avg_cost = self.df["Cost Price Per Unit (USD)"].mean()
                return f"{definition} In your dataset, the average cost price per unit is ${avg_cost:.2f}."
            elif "stock value" in term:
                total_value = (self.df["Hand-In- Stock"] * self.df["Cost Price Per Unit (USD)"]).sum()
                return f"{definition} In your dataset, the total stock value is ${total_value:,}."
            elif "units sold" in term:
                total_sold = self.df["Number of Units Sold"].sum()
                return f"{definition} In your dataset, {total_sold} units have been sold."
            else:
                return definition

        else:
            return "Sorry, I don’t understand that query yet."
