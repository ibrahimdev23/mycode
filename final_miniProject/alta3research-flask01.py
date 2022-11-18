#!/usr/bin/env python3
"""DEMO: receiving JSON"""

from flask import Flask
from flask import request
from flask import redirect
from flask import jsonify
from flask import render_template
from pprint import pprint

app= Flask(__name__)


playerData = [
        { "first_name":"LeBron",
      "last_name":"James",
      "full_name": "Lebron James",
      "position":"F",
      "height": "6'8",
      "weight_pounds": 250,
      "photo_url": "https://cdn.cnn.com/cnnnext/dam/assets/201012094850-lebron-james-nba-final-win-1011-restricted-super-tease.jpg",
      "team":{
        "abbreviation":"LAL",
        "city":"Los Angeles",
        "conference":"West",
        "division":"Pacific",
        "full_name":"Los Angeles Lakers",
        "name":"Lakers"
        }
      },

  { "first_name":"Kevin",
      "last_name":"Durant",
      "full_name":"Kevin Durant",
      "position":"F",
      "height": "6'10",
      "weight_pounds": 220,
      "photo_url":"https://bdc2020.o0bc.com/wp-content/uploads/2022/08/JUBBVIQ3MG7SWZC5VN7U3ADNBQ-62fa4cc640372-scaled.jpg",
      "team":{
        "abbreviation":"BNN",
        "city":"Brooklyn",
        "conference":"East",
        "division":"Atlantic",
        "full_name":"Brooklyn Nets",
        "name":"Nets"
        }
      }, 

        { "first_name":"Anthony",
      "last_name":"Davis",
      "full_name":"Anthony Davis",
      "position":"PF",
      "height":"6'11",
      "weight_pounds": 260,
      "photo_url":"https://ca-times.brightspotcdn.com/dims4/default/490d734/2147483647/strip/true/crop/1608x1194+0+67/resize/1200x891!/quality/80/?url=https%3A%2F%2Fcalifornia-times-brightspot.s3.amazonaws.com%2Fcf%2Ff4%2Fe13f962a40faabcb583b21d6117a%2Fla-photos-1staff-622049-sp-1006-lakers-heat-finals27-wjs.jpg",
      "team":{
        "abbreviation":"LAL",
        "city":"Los Angeles",
        "conference":"West",
        "division":"Pacific",
        "full_name":"Los Angeles Lakers",
        "name":"Lakers"
        }


      }


        ]





@app.route("/")
def home():
    #this endpoint returns 
    return render_template("index.html")




@app.route("/player", methods= ['POST', 'GET'])
def getPlayer():
    if request.method == 'POST':
        res = request.form 
        json_res = dict(res)
        name = json_res.get('player')
        #
        for player in playerData:
            if name == player["first_name"]:
                return render_template("playerCard.html", name = player["full_name"], team = player["team"]["full_name"], position = player["position"], height = player["height"] , weight = player["weight_pounds"], photo_url = player["photo_url"] ) 



@app.route("/info")
def plyer_info():
    #this endpoint returns JSON
    return jsonify(playerData)






if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)

