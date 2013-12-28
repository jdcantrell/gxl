from __future__ import with_statement
import json
import datetime

from fabric.api import *

env.hosts = ['jd@goodrobot.net']

def build_min():
  with settings(warn_only=True):
    run('bundle exec compass compile --output-style=compressed --force')

@task
def build():
  with settings(warn_only=True):
    run('bundle exec compass compile')


@task
def deploy():
  build_min()
  put('build/gxl.css', '~/gxl.min.css')
  put('images', '~/')
  sudo('mv ./gxl.min.css /srv/http/static/gxl/')
  sudo('rm -rf /srv/http/static/gxl/images')
  sudo('mv ./images /srv/http/static/gxl/images')

@task
def deplay_docs():
  build()
