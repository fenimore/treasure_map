"""


The MIT License (MIT)

Copyright (c) 2016 Fenimore

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, 
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR 
PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE 
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE 
OR OTHER DEALINGS IN THE SOFTWARE.


"""


import os
from datetime import datetime

import folium
from flask import Flask, render_template, send_from_directory, request

import stuff, mappify
from freestuffs.stuff_scraper import StuffScraper
from freestuffs.stuff_charter import StuffCharter
from city_list import CITIES

# initialization
app = Flask(__name__)
app.config.update(
    DEBUG = True,
)

def refine_city_name(location):
    """display User-friendly city name"""
    if location == 'newyork': # does this have to capitalized
        loc = 'New York'
    elif location == 'washingtondc':
        loc = 'Washington D.C.'
    elif location == 'sanfrancisco':
        loc = 'San Francisco'
    else:
        loc = location
    return loc

"""Routes"""
@app.route('/favicon.ico')
def favicon():
    """Serve favicon"""
    return send_from_directory(os.path.join(app.root_path, 'static'), 'ico/favicon.ico')

@app.errorhandler(404)
def page_not_found(e):
    """Render 404."""
    return render_template('404.html'), 404

@app.route("/")
def index():
    """Render index."""
    return render_template('index.html')


@app.route("/cities")
def list_cities():
    """Display valid city names."""
    return str(CITIES)


@app.route('/<location>')
def list_stuff(location):
    """Display listings"""
    stuffs = StuffScraper(location, 9).stuffs
    things =[]
    for x in range(9):
        thing = {
            'url': stuffs[x].url,
            'image': stuffs[x].image,
            'place': stuffs[x].location,
            'title': stuffs[x].thing
            }
        things.append(thing)
    refined_loc = refine_city_name(location)
    return render_template('view.html', things=things, location=location, rlocation=refined_loc)
    # location = location... brilliant


@app.route('/<location>/map')
def show_map(location):
    """Display 10 items in given city, default"""
    stuffs = StuffScraper(location, 9, precise=True).stuffs
    treasure_map = StuffCharter(stuffs, zoom=12)
    folium_figure = treasure_map.treasure_map.get_root()
    folium_figure.header._children['bootstrap'] = folium.element.CssLink('/static/css/style.css')
    folium_figure.header._children['Woops'] = folium.element.CssLink('/static/css/map.css')
    map_path = os.path.join(app.root_path, 'templates', 'raw_map.html')
    treasure_map.save_map(map_path=map_path)
    things =[]
    for x in range(9): # Display listings on map
        thing = {
            'url': stuffs[x].url,
            'image': stuffs[x].image,
            'place': stuffs[x].location,
            'title': stuffs[x].thing
            }
        things.append(thing)
    location = refine_city_name(location)
    return render_template('map.html', location=location, things=things)

@app.route('/<location>/map/<quantity>')
def show_map_more(location, quantity):
    """Display a specified amount of stuffs on map"""
    startTime = datetime.now() # time speed of script
    stuffs = StuffScraper(location, quantity, precise=True).stuffs
    treasure_map = StuffCharter(stuffs, zoom=12)
    folium_figure = treasure_map.treasure_map.get_root()
    folium_figure.header._children['bootstrap'] = folium.element.CssLink('/static/css/style.css')
    folium_figure.header._children['Woops'] = folium.element.CssLink('/static/css/map.css')
    map_path = os.path.join(app.root_path, 'templates', 'raw_map.html')
    treasure_map.save_map(map_path=map_path)
    things =[]
    for x in range(int(quantity)):
        thing = {
            'url': stuffs[x].url,
            'image': stuffs[x].image,
            'place': stuffs[x].location,
            'title': stuffs[x].thing
            }
        things.append(thing)
    location = refine_city_name(location)
    score = datetime.now() - startTime # efficacy?
    return render_template('map.html', location=location, things=things, score=score)

@app.route('/me', methods=['POST'])
def me():
    if request.method == 'POST':
            location = request.form['location']
            address = request.form['address']
            #address = address + ', ' + location # this messes up if the city isn't the same as the address
            stuffs = StuffScraper(location, 9, precise=True).stuffs
            treasure_map = StuffCharter(stuffs, address=address, zoom=12)
            folium_figure = treasure_map.treasure_map.get_root()
            folium_figure.header._children['bootstrap'] = folium.element.CssLink('/static/css/style.css')
            folium_figure.header._children['Woops'] = folium.element.CssLink('/static/css/map.css')
            map_path = os.path.join(app.root_path, 'templates', 'raw_map.html')
            treasure_map.save_map(map_path=map_path)
            things =[]
            for x in range(9):
                thing = {
                    'url': stuffs[x].url,
                    'image': stuffs[x].image,
                    'place': stuffs[x].location,
                    'title': stuffs[x].thing
                    }
                things.append(thing)
            location = refine_city_name(location)
            return render_template('map.html', location=location, things=things, address=address)


# launch
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

# Form for searching items
# Form takes in city, as well?
