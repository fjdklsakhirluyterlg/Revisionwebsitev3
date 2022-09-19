from flask import Flask, render_template, url_for, request, redirect, send_from_directory, send_file, flash, jsonify, Blueprint, Response, abort
from . import app

songs = Blueprint("songs", __name__)

@songs.route("/other/whos-a-folly-good-fellow")
def whos_a_jolly_good_fellow():
    x = """
    For he's a jolly good fellow.
    For he's a jolly good fellow.
    For he's a jolly good fellow!
    Which nobody can deny.
    Which nobody can deny.
    Which nobody can deny.
    For he's a jolly good fellow.
    Which nobody can deny.
    
    hahahahahha
    """
    return x

@songs.route("/songs/cocunut")
def cocunut_song():
    a = """
    The coconut nut is a giant nut
    If you eat too much, you'll get very fat
    Now, the coconut nut is a big, big nut
    But this delicious nut is not a nut
    
    It's the coco fruit (it's the coco fruit)
    Of the coco tree (of the coco tree)
    From the coco palm family
    
    There are so many uses of the coconut tree
    You can build a big house for the family
    All you need is to find a coconut man
    If he cuts the tree, he gets the fruit free
    
    It's the coco fruit (it's the coco fruit)
    Of the coco tree (of the coco tree)
    From the coco palm family
    
    The coconut bark for the kitchen floor
    If you save some of it, you can build a door
    Now, the coconut trunk, do not throw this junk
    If you save some of it, you'll have the second floor
    
    The coconut wood is very good
    It can stand 20 years if you pray it would
    Now, the coconut root, to tell you the truth
    
    You can throw it or use it as firewood
    The coconut leaves, good shade it gives
    For the roof, for the walls up against the eaves
    Now, the coconut fruit, say my relatives
    
    Make good cannonballs up against the eaves
    It's the coco fruit (it's the coco fruit)
    Of the coco tree (of the coco tree)
    
    From the coco palm family
    The coconut nut is a giant nut
    If you eat too much, you'll get very fat
    Now, the coconut nut is a big, big nut
    
    But this delicious nut is not a nut
    It's the coco fruit (it's the coco fruit)
    Of the coco tree (of the coco tree)
    
    From the coco palm family
    It's the coco fruit (it's the coco fruit)
    Of the coco tree (of the coco tree)
    From the coco palm family
    
    It's the coco fruit (it's the coco fruit)
    Of the coco tree (of the coco tree)
    From the coco palm family
    
    Ole!
    """
    return a

@songs.route("/songs/rickroll")
def rickroll_bcs_i_like_it():
    a = """
    We're no strangers to love
    You know the rules and so do I (do I)
    A full commitment's what I'm thinking of
    You wouldn't get this from any other guy
    
    I just wanna tell you how I'm feeling
    Gotta make you understand
    
    Never gonna give you up
    Never gonna let you down
    Never gonna run around and desert you
    Never gonna make you cry
    Never gonna say goodbye
    Never gonna tell a lie and hurt you
    
    We've known each other for so long
    Your heart's been aching, but you're too shy to say it (say it)
    Inside, we both know what's been going on (going on)
    We know the game and we're gonna play it
    
    And if you ask me how I'm feeling
    Don't tell me you're too blind to see
    
    Never gonna give you up
    Never gonna let you down
    Never gonna run around and desert you
    Never gonna make you cry
    Never gonna say goodbye
    Never gonna tell a lie and hurt you
    Never gonna give you up
    Never gonna let you down
    Never gonna run around and desert you
    Never gonna make you cry
    Never gonna say goodbye
    Never gonna tell a lie and hurt you
    
    We've known each other for so long
    Your heart's been aching, but you're too shy to say it (to say it)
    Inside, we both know what's been going on (going on)
    We know the game and we're gonna play it
    
    I just wanna tell you how I'm feeling
    Gotta make you understand
    
    Never gonna give you up
    Never gonna let you down
    Never gonna run around and desert you
    Never gonna make you cry
    Never gonna say goodbye
    Never gonna tell a lie and hurt you
    
    Never gonna give you up
    Never gonna let you down
    Never gonna run around and desert you
    Never gonna make you cry
    Never gonna say goodbye
    Never gonna tell a lie and hurt you
    
    Never gonna give you up
    Never gonna let you down
    Never gonna run around and desert you
    Never gonna make you cry
    Never gonna say goodbye
    Never gonna tell a lie and hurt you
    """
    return a

app.register_blueprint(songs, url_prefix="/")