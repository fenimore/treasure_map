# Treasure Map in Flask

This is an implementation of <a href="https://github.com/polypmer/freestuff-bot">freestuff-bot</a> using [Flask](www.flask.pocoo.org). This web application gathers the freestuff from craiglist and then posts the locations onto an open-street-map. It can be run with gunicorn app:app (or just by running app.py).  Unfortunetaly, the Heroku ip is automatically blocked by craigslist. Also, at the moment, using dreamhost's passenger doesn't work. I'm holding up for fastcgi.

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
* A lot, namely re-write completely.
    - combine view and map page. with some jquery
* Make X's for mappify's Map creation (for pirate theme...)
* Fancy **Legend**, floating perhaps...
* **Loading screen**!!!

### Issues:
* Premature header? 
* Major location problem, only five cities work?
    - get list of cities names
    - create dict/key?
    - make it easy for users to see
* My gosh get this deployed some how!
    - what a nightmare this is...
* Store stuffs list in a session??
    - pass it through a link? 
    - cut down load time...

