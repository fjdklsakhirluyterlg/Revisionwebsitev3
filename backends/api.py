from flask_restful import Resource, Api
from flask import Flask, render_template, url_for, request, redirect, send_from_directory, send_file, flash, jsonify, Blueprint, Response, abort
import random
from . import api

class Randomz(Resource):
    def get(self):
        def randoms():
            r = lambda: random.randint(0,255)
            return ['#%02X%02X%02X' % (r(),r(),r())]
        
        def fortune():
            list = ['You will make at least 5 pounds', 'You will watch mr beast in the next week', 'You will quit your job', 'Your next phone will be able to run Genshin impact']
            return random.choice(list)
        
        def fact():
            list = ['Take an angle A, find out what sin(A)^2 + cos(A)^2 is', 'There are more than 6 million parts in an A380', 'Francium is the most reactive element in the world', 'Jeff Bezos could buy 2 million tesla model y', 'Japan has the highest debt to GDP ratio in the world with 234%', 'Monaco should score 1.04 on the Human Development Index (HDI), a scale from 0 - 1', 'Valeriepieris circle is a circle of 4000km in radius and can fit more than half the worlds population', 'Mr beasts waarehous costs more than 14 million']
            return random.choice(list)
        
        x = random.randint(0 ,1000)
        y = randoms()
        z = fortune()
        a = fact()

        return {'number': x, 'hex colour': y, 'fortune': z, 'fact': a}

api.add_resource(Randomz, '/api/random')
