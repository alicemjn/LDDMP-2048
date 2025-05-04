import json

def save_game(filename,board,score,player_name="Player"):
    game_state={"player":player_name,"score":score,"board":board}

    with open(filename,"w")   as f:
     json.dump(game_state,f,indent=4)
    print(f"game saved to {filename}") 

   


    with open(filename,"r") as f:
     saved_data=json.load(f)
    
    print(f"player:{saved_data[player_name]})
    print(f"score:{saved_data[score]})  
    print("board:") 
    for row in saved_data['board']:
    print(row)