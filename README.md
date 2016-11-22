# Treasure Map

This is an implementation of my <a href="https://github.com/polypmer/freestuffs">freestuffs</a> package using [Flask](https://www.flask.pocoo.org). This web application gathers the freestuff from craiglist and then posts the locations onto an open-street-map/leaflet.js map. It can be run with gunicorn app:app (or just by running app.py), or found wsgi deployed [here](http://treasure.plyp.org).

The **freestuffs** package is documented on [readthedocs](http://freestuffs.readthedocs.io/en/latest/). The Treasure Map is currently deployed [here](http://treasure.plyp.org).

## Requirements

Treasure Map and freestuffs should work with Python 3.x

* freestuffs
* requests
* beautifulsoup4
* Flask & Jinja2
* folium 0.2.0

## API

> `domain.com/<location> `- for a quantity of 9

> `domain.com/<location>/map` for a quantity of 9

> `domain.com/<location>/map/<quantity>`  - for more or less stuffs


## TODO:
* Make an `X` for `mappify`'s Map creation
* Fuzzy matching for city names

## License:

<pre>Fenimore Love 2016 MIT

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

BEWARE EXCESSIVE ACCUMULATION</pre>
