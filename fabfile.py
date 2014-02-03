from __future__ import with_statement
import json
import datetime

from fabric.api import *
from fabric.context_managers import path

env.hosts = ['jd@goodrobot.net']

@task
def css_min():
  local('bundle exec compass compile --output-style=compressed --force')

@task
def css():
  local('bundle exec compass compile')

@task
def docs():
  local('bundle exec hologram ./hologram.yml')

@task
def all():
  css()
  docs()

@task
def deploy():
  css_min()
  put('build/gxl.css', '~/gxl.min.css')
  put('images', '~/')
  sudo('mv ./gxl.min.css /srv/http/static/gxl/')
  sudo('rm -rf /srv/http/static/gxl/images')
  sudo('mv ./images /srv/http/static/gxl/images')
