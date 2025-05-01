import json

def save_game(filename,board,score,player_name="Player"):
    game_state={"player":player_name,"score":score,"board":board}

    with open(filename,"w")   as f:
     json.dump(game_state,f,indent=4)
    print(f"game saved to {filename}") 