from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse
from typing import Optional
from services.steamapi import getPlayerSummaries, getOwnedGames
from utils.card import renderUserCard, renderOwnedGamesCard
import os
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/favicon.ico")
async def favicon():
    return {"message": "Hello World"}


@app.get("/api/getPlayerSummaries/{steamId}")
async def playerSummaries(steamId: str,
                          width: Optional[int] = 150,
                          height:Optional[int] = 160,
                          bgColor: Optional[str] = 'transparent',
                          textColor: Optional[str] = 'black',
                          boarderColor: Optional[str] = 'black',
                          boarderWidth: Optional[str] = '2'):
    #hex or transparent
    res = await getPlayerSummaries(steamId)
    card = renderUserCard(res['playerName'], res['playerProfileUrl'],
                          res['avatar'],width,height, bgColor, textColor,boarderColor,boarderWidth)
    contentControlHeader = "public, max-age={}".format(os.getenv('CACHE_AGE'))
    headers = dict({
        "Content-Type": "image/svg+xml",
        "Cache-Control": contentControlHeader,
    })
    return Response(content=card, headers=headers)


@app.get("/api/getOwnedGames/{steamId}")
async def playerSummaries(steamId: str,
                          limit: Optional[int] = 6,
                          row: Optional[int] = 1,
                          col: Optional[int] = 12,
                          width: Optional[int] = 120,
                          height:Optional[int] = 70,
                          bgColor: Optional[str] = 'transparent',
                          textColor: Optional[str] = 'black',
                          boarderColor: Optional[str] = 'black',
                          boarderWidth: Optional[str] = '2'):
    if (limit < col):
        col = limit
    res = await getOwnedGames(steamId, limit)
    card = renderOwnedGamesCard(res, row, col,width,height,bgColor,textColor,boarderColor,boarderWidth)
    contentControlHeader = "public, max-age={}".format(os.getenv('CACHE_AGE'))

    headers = dict({
        "Content-Type": "image/svg+xml",
        "Cache-Control": contentControlHeader,
    })
    return Response(content=card, headers=headers)
