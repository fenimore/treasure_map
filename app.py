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
from flask import Flask, render_template, send_from_directory, request
import stuff, mappify
from datetime import datetime


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

@app.route('/<location>')
def welcome(location):
    """Display listings"""
    stuffs = stuff.gather_stuff(location, 9)
    # Somehow iterate the dict construction? Yeah.. that.
    things =[]
    for x in range(9):
        thing = {
            'url': stuffs[x].url,
            'image': stuffs[x].image,
            'place': stuffs[x].location,
            'title': stuffs[x].thing
            }
        things.append(thing)
    ### Not quite worked out yet ^^^
    rlocation = refine_city_name(location) # Load button breaks if I dont' distinguish
    return render_template('view.html', things=things, location=location, rlocation=rlocation)  # render a template
    # location = location... brilliant

@app.route('/<location>/map')
def show_map(location):
    stuffs = stuff.gather_stuff(location, 9)
    mappify.post_map(stuffs)
    
    css_override = os.path.join(app.root_path, 'static', 'css', 'style.css')
    
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
    startTime = datetime.now() # time speed of script
    stuffs = stuff.gather_stuff(location, quantity)
    mappify.post_map(stuffs)
    #ten = 9
    #if int(quantity) < ten:
    #    ten = int(quantity) - 1
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
            stuffs = stuff.gather_stuff(location, 9)
            mappify.post_map(stuffs, address)
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
