# coding=utf-8
import os

from simpleconfigparser import simpleconfigparser

from get_argv import config_dir

defaults = {
    'general': {
        'ip': '0.0.0.0',
        'port': '6767',
        'base_url': '/',
        'path_mappings': '[]',
        'debug': 'False',
        'branch': 'master',
        'auto_update': 'True',
        'single_language': 'False',
        'minimum_score': '90',
        'use_scenename': 'True',
        'use_postprocessing': 'False',
        'postprocessing_cmd': '',
        'use_sonarr': 'False',
        'use_radarr': 'False',
        'path_mappings_movie': '[]',
        'serie_default_enabled': 'False',
        'serie_default_language': '[]',
        'serie_default_hi': 'False',
        'movie_default_enabled': 'False',
        'movie_default_language': [],
        'movie_default_hi': 'False',
        'page_size': '25',
        'minimum_score_movie': '70',
        'use_embedded_subs': 'True',
        'only_monitored': 'False',
        'adaptive_searching': 'False',
        'enabled_providers': ''
},
    'auth': {
        'type': 'None',
        'username': '',
        'password': ''
},
    'sonarr': {
        'ip': '127.0.0.1',
        'port': '8989',
        'base_url': '/',
        'ssl': 'False',
        'apikey': '',
        'full_update': 'Daily'
},
    'radarr': {
        'ip': '127.0.0.1',
        'port': '7878',
        'base_url': '/',
        'ssl': 'False',
        'apikey': '',
        'full_update': 'Daily'
},
    'proxy': {
        'type': 'None',
        'url': '',
        'port': '',
        'username': '',
        'password': '',
        'exclude': 'localhost,127.0.0.1'
},
    'opensubtitles': {
        'username': '',
        'password': ''
},
    'addic7ed': {
        'username': '',
        'password': ''
},
    'legendastv': {
        'username': '',
        'password': ''
}}

settings = simpleconfigparser(defaults=defaults)
settings.read(os.path.join(config_dir, 'config', 'config.ini'))

base_url = settings.general.base_url

# sonarr url
if settings.sonarr.getboolean('ssl'):
    protocol_sonarr = "https"
else:
    protocol_sonarr = "http"

if settings.sonarr.base_url == '':
    settings.sonarr.base_url = "/"
if not settings.sonarr.base_url.startswith("/"):
    settings.sonarr.base_url = "/" + settings.sonarr.base_url
if settings.sonarr.base_url.endswith("/"):
    settings.sonarr.base_url = settings.sonarr.base_url[:-1]

url_sonarr = protocol_sonarr + "://" + settings.sonarr.ip + ":" + settings.sonarr.port + settings.sonarr.base_url
url_sonarr_short = protocol_sonarr + "://" + settings.sonarr.ip + ":" + settings.sonarr.port

# radarr url
if settings.radarr.getboolean('ssl'):
    protocol_radarr = "https"
else:
    protocol_radarr = "http"

if settings.radarr.base_url == '':
    settings.radarr.base_url = "/"
if not settings.radarr.base_url.startswith("/"):
    settings.radarr.base_url = "/" + settings.radarr.base_url
if settings.radarr.base_url.endswith("/"):
    settings.radarr.base_url = settings.radarr.base_url[:-1]

url_radarr = protocol_radarr + "://" + settings.radarr.ip + ":" + settings.radarr.port + settings.radarr.base_url
url_radarr_short = protocol_radarr + "://" + settings.radarr.ip + ":" + settings.radarr.port