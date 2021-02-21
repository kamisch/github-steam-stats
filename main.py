from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse
from services.steamapi import getPlayerSummaries, getOwnedGames
from utils.card import renderUserCard, renderOwnedGamesCard
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/api/getPlayerSummaries/{steamId}")
async def playerSummaries(steamId:str):
    res = await getPlayerSummaries(steamId)
    card = renderUserCard(res['playerName'], res['playerProfileUrl'], res['avatar'])
    headers =  dict({
          "Content-Type": "image/svg+xml",
          "Cache-Control": "public, max-age=7200",
        })
    return Response(content=card, headers=headers)

@app.get("/api/getOwnedGames/{steamId}")
async def playerSummaries(steamId:str):
    res = await getOwnedGames(steamId,12)
    return res
