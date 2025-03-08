from fastapi import FastAPI
import random

app = FastAPI()

# Side hustles and money quotes
side_hustles = [
    "Start a blog",
    "Start a YouTube channel",
    "Start a podcast",
    "Start a dropshipping business",
    "Start a print-on-demand business",
    "Start a freelance business",
    "Start a social media marketing agency",
    "Start a web development agency",
    "Start a graphic design agency",
    "Start a video editing agency",
]

money_quotes = [
    "Too many people spend money they earned... to buy things they don't want... to impress people they don't like.",
    "A wise person should have money in their head, but not in their heart.",
    "Money is only a tool. It will take you wherever you wish.",
    "A budget is telling your money where to go instead of wondering where it went.",
    "The best thing money can buy is financial freedom.",
]

@app.get("/side_hustles")
async def get_side_hustles(api_key: str):
    """Return a random side hustle."""
    if api_key != "12345678":
        return {"error": "Invalid API key."}
    return {"side_hustle": random.choice(side_hustles)}

@app.get("/money_quotes")
async def get_money_quotes(api_key: str):
    """Return a random money quote."""
    if api_key != "12345678":
        return{"error": "Invalid API key."}
    return {"money_quote": random.choice(money_quotes)}
