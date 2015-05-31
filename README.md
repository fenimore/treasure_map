# Treasure Map in Flask

This is an implementation of <a href="https://github.com/polypmer/freestuff-bot">freestuff-bot</a> using [Flask](www.flask.pocoo.org). This web application gathers the freestuff from craiglist and then posts the locations onto an open-street-map. I haven't figured out how to deploy this yet... but it can be run with gunicorn (or just running app.py) by gunicorn app:app. 

## Dependencies
* requests
* beautifulsoup4
* python 3.x
* Flask
* folium
* gunicorn (kinda)
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
* Navigation-bar | Bootstrap
* Make X's for mappify's Map creation (for pirate theme...)
* Fancy Legend, floating perhaps...
* 404 error page...
* **Loading screen**!!! I have an idea for this

### Issues:
* Major location problem, only five cities work?
    - get list of cities names
    - create dict/key?
    - make it easy for users to see
* My gosh get this deployed some how!
    - what a nightmare this is...
* Store stuffs list in a session??
    - pass it through a link? 
    - cut down load time...

