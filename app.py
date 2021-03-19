from stories import *
import re
from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "rly-secrt-guyz"

debug = DebugToolbarExtension(app)


@app.route('/madlib/')
def show_home():
    return render_template("home.html", story_map=story_map)

@app.route('/madlib/<id>/generate')
def show_generate(id):
    story = stories[id]
    words_needed = [word for word in story.prompts]
    words_needed.sort()
    display_words = [re.sub('[\d?]', '', word.replace('_', ' ')).strip()
                     for word in words_needed]
    return render_template("generator.html", display_words=display_words,
                           words_needed=words_needed, story_id=id, len=len(words_needed))

@app.route('/madlib/<id>/story')
def show_story(id):
    story = stories[id]
    text_story = story.template
    word_dict = dict()
    for variable in request.args:
        word_dict[variable] = request.args.get(variable)
    for key in word_dict.keys():
        text_story = text_story.replace(f'{{{key}}}', word_dict[key])

    return render_template("story.html", text_story=text_story,
                           story_title=story_map[int(id)])
