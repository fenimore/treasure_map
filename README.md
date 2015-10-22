# Treasure Map

This is an implementation of <a href="https://github.com/polypmer/freestuff-bot">freestuff-bot</a> using [Flask](www.flask.pocoo.org). This web application gathers the freestuff from craiglist and then posts the locations onto an open-street-map/leaflet.js map. It can be run with gunicorn app:app (or just by running app.py), or found wsgi deployed [here](http://treasure.plyp.org).<hr>
<img src="https://github.com/polypmer/treasure-map/blob/master/static/img/noun_89070.png" width="100px"></img>

## Dependencies
* requests
* beautifulsoup4
* python 3.x
* Flask & Jinja2
* folium
* [see requirements.txt]

## Application Intereface
Something like this subject to change:
<ul>
<li>domain.com/location - for a quantity of 9</li>
<li>domain.com/location/**map** for a quantity of 9</li>
<li>domain.com/location/**map**/quantity  - for more or less entries , **geocoder crashes around 20**</li>
</ul>

## TODO:
* Make X's for mappify's Map creation (for pirate theme...)
* Add form for user address
* Add color scheme to legend
* **Loading screen**!!! -- change
* Give it some style, jeez
* Some sort of absolute URL flaskish thing needs to happen

### Issues:
* Loader gif doesn't work?
* Location problem:
    - Certain cities are two words
        - newyork, sanfrac
        - this poses an issue for geopy craigslist interpolation
    - Some cities are also cities elsewhere
        - geopy doesn't descriminate
    - create dict or somehow work through the locations
    - Only a few locations have a supported map-center init
        - Others have to zoom out. Yuck.
* Store stuffs list in a session??
    - pass it through a link?
    - cut down load time...
