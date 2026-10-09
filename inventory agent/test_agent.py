from agent import InventoryAgent

agent = InventoryAgent("data/Inventory-Records-Sample-Data.xlsx")

print(agent.answer("What is the total stock value?"))
print(agent.answer("Which is the highest cost product?"))
print(agent.answer("How many units sold?"))
