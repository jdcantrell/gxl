from __future__ import with_statement
import json
import datetime

from fabric.api import *
from fabric.context_managers import path

env.hosts = ['jd@goodrobot.net']

@task
def build_min():
  local('compass compile --output-style=compressed --force')

@task
def build():
  local('/Users/jcantrell/.rbenv/shims/compass compile')

@task
def deploy():
  build_min()
  put('build/gxl.css', '~/gxl.min.css')
  put('images', '~/')
  sudo('mv ./gxl.min.css /srv/http/static/gxl/')
  sudo('rm -rf /srv/http/static/gxl/images')
  sudo('mv ./images /srv/http/static/gxl/images')
