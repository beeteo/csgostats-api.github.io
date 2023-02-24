from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def mainer():
    return jsonify({'welcome to csgostats api :)': 'thanks 4 using', "endpoints": ['https://beete.xyz/csgo/stats/api?steam64ID=PLAYERID']})

app.run()
