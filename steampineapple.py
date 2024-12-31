#pip install requests
#pip install flask
#pip install flask-cors

import requests
from flask import Flask, jsonify
from flask_cors import CORS
import threading
import time

apikey= "chave api steam"
steamid="id steam"

gameid="1174180"
#1174180 - Red_Dead_Redemption_2

urlconq="http://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v0001/"
parametros={"key":apikey,"steamid":steamid,"appid":gameid}

def steam_req():
    while True:
        try:
            req=requests.get(urlconq,params=parametros)
            if req.status_code==200:
                dados=req.json()
                conqall=len(dados["playerstats"]["achievements"])

                # conqs=0
                # for i in range(len(dados["playerstats"]["achievements"])):
                # conqs+=dados["playerstats"]["achievements"][i]["achieved"]

                conqs=sum(achv["achieved"] for achv in dados["playerstats"]["achievements"])

                with open("goal.txt","w") as goal_file:
                    goal_file.write(str(conqall))
                
                with open("count.txt","w") as count_file:
                    count_file.write(str(conqs))
            else: print(f"erro no request")
        except Exception as e: print(f"Erro ao atualizar dados: {e}")
        time.sleep(60)
            
app=Flask(__name__)
CORS(app)
@app.route('/count',methods=['GET'])
def get_count():
    try:
        with open("count.txt","r") as file:
            count=file.read().strip()
        return jsonify({"count":int(count)})
    except Exception as e: return jsonify({"error":str(e)}),500

@app.route('/goal',methods=['GET'])
def get_goal():
    try:
        with open("goal.txt","r") as file:
            goal=file.read().strip()
        return jsonify({"goal":int(goal)})
    except Exception as e: return jsonify({"error":str(e)}),500

if __name__ == "__main__": 
    threading.Thread(target=steam_req,daemon=True).start()
    app.run(debug=True,port=5000)