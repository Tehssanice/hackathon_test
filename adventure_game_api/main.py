from fastapi import FastAPI, Body, HTTPException, Query
from pydantic import BaseModel
from typing import Annotated
from fastapi.responses import JSONResponse

app = FastAPI()


player_inventory = []

game_locations = {
  
  "Kaduna": {"description": "north", "items_available":"available"},
  "Abuja": {"description": "central", "items_available":"available"},
  "Enugu": {"description": "east", "items_available":"not available"},
  
}

class Player(BaseModel):
    name: str
    description: str
    location: str

@app.post("/inventory/add")
async def add_to_inventory(player: Annotated[Player, Body(...)]):
    try:
        if player.name in [i['name'] for i in player_inventory]:
            raise HTTPException(status_code=400, detail="Item already exists in inventory")
          
        player_inventory.append(player.dict())
      
        return JSONResponse(status_code=200, content= {"data": player_inventory, "message": "Item added to inventory"})
    except Exception as e:
        return {"message": str(e)}


@app.post("/inventory/remove")
async def remove_from_inventory(player: Annotated[Player, Body(...)]):
  try:
    if player.name not in [i['name'] for i in player_inventory]:
      raise HTTPException(status_code=400, detail="Item does not exist in inventory")
      
    player_inventory.remove(player.dict())
  
    return JSONResponse(status_code=200, content= {"data": player_inventory, "message": "Item removed from inventory"})
  except Exception as e:
    return {"message": str(e)}


@app.get("/explore/{location_name}")
async def explore_location(location_name:str):
  
  try:
    for key, value in game_locations.items():
      print(key, "test")
      if key.lower() == location_name.lower():
        return {"message": f" {location_name.title()} is {value['items_available']}", "location": location_name.title()}
    else:
      raise HTTPException(status_code=404, detail= "Location does not exist yet")
    

  except Exception as e:
    return{"message": str(e)}
  