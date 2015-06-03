import os
from flask import Flask, render_template, send_from_directory
import stuff, mappify

# initialization
app = Flask(__name__)
app.config.update(
    DEBUG = True,
)

# controllers
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'ico/favicon.ico')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route("/")
def index():
    return render_template('index.html')
    
@app.route('/<location>')
def welcome(location):
    stuffs = stuff.gather_stuff(location, 9)
    # Somehow iterate the dict construction? Yeah.. that.
    things = [ # Array of first five Dicts
        {
            'url': stuffs[0].url, 
            'image': stuffs[0].image, 
            'place': stuffs[0].location,
            'title': stuffs[0].thing
        },
        {
            'url': stuffs[1].url,
            'image': stuffs[1].image,
            'place': stuffs[1].location,
            'title': stuffs[1].thing
        },
        {
            'url': stuffs[2].url, 
            'image': stuffs[2].image,
            'place': stuffs[2].location,
            'title': stuffs[2].thing
        },
        {
            'url': stuffs[3].url, 
            'image': stuffs[3].image,
            'place': stuffs[3].location,
            'title': stuffs[3].thing
        },
        {
            'url': stuffs[4].url, 
            'image': stuffs[4].image,
            'place': stuffs[4].location,
            'title': stuffs[4].thing
        },
                {
            'url': stuffs[5].url, 
            'image': stuffs[5].image,
            'place': stuffs[5].location,
            'title': stuffs[5].thing
        },
        {
            'url': stuffs[6].url, 
            'image': stuffs[6].image,
            'place': stuffs[6].location,
            'title': stuffs[6].thing
        },
        {
            'url': stuffs[7].url, 
            'image': stuffs[7].image,
            'place': stuffs[7].location,
            'title': stuffs[7].thing
        },
        {
            'url': stuffs[8].url, 
            'image': stuffs[8].image,
            'place': stuffs[8].location,
            'title': stuffs[8].thing
        },
    ]
    ### Not quite worked out yet ^^^
    return render_template('view.html', things=things, location=location)  # render a template
    # location = location... brilliant

@app.route('/<location>/map')
def show_map(location):
    stuffs = stuff.gather_stuff(location, 9)
    try:
        mappify.post_map(stuffs)
    except:
        error_string = "<h2>Woops, the mapping script crashed, try again?</h2>"
        f = open('raw_map.html', 'w') # Write to html page, problem sorrry
        f.write(error_string)
        f.close()
    return render_template('map.html', location=location)
    
@app.route('/<location>/map/<quantity>')
def show_map_more(location):
    stuffs = stuff.gather_stuff(location, quantity)
    try:
        mappify.post_map(stuffs)
    except:
        error_string = "<h2>Woops, the mapping script crashed, reload, maybe with a smaller amount of stuff</h2>"
        f = open('raw_map.html', 'w') # Write to html page, problem sorrry
        f.write(error_string)
        f.close()
    return render_template('map.html', location=location)

# launch
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
