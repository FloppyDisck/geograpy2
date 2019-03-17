Geograpy3
=========

Extract place names from a URL or text, and add context to those names -- for 
example distinguishing between a country, region or city. 


## Install & Setup

Grab the package using `pip` (this will take a few minutes)

    pip install geograpy3

geograpy3 uses [NLTK](http://www.nltk.org/) for entity recognition, so you'll also need 
to download the models we're using. Fortunately there's a command that'll take 
care of this for you. 

    geograpy3-nltk

## Basic Usage

Import the module, give some text or a URL, and presto.

    import geograpy3
    url = 'http://www.bbc.com/news/world-europe-26919928'
    places = geograpy3.get_place_context(url=url)


## Credits

geograpy3 is a fork of [geograpy2](https://github.com/Corollarium/geograpy2) which is a fork of [geograpy](https://github.com/ushahidi/geograpy) this version only has install fixes, python 3 support and is updated to work with the newer iterations of the included libraries.

geograpy3 uses the following excellent libraries:

* [NLTK](http://www.nltk.org/) for entity recognition
* [newspaper](https://github.com/codelucas/newspaper) for text extraction from HTML
* [jellyfish](https://github.com/sunlightlabs/jellyfish) for fuzzy text match
* [pycountry](https://pypi.python.org/pypi/pycountry) for country/region lookups

Geograpy uses the following data sources:

* [GeoLite2](http://dev.maxmind.com/geoip/geoip2/geolite2/) for city lookups
* [ISO3166ErrorDictionary](https://github.com/bodacea/countryname/blob/master/countryname/databases/ISO3166ErrorDictionary.csv) for common country mispellings _via [Sara-Jayne Terp](https://github.com/bodacea)_

Hat tip to [Chris Albon](https://github.com/chrisalbon) for the name.

Released under the MIT license.
