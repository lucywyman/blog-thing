#!/bin/env python
"""
This is the blob of python that powers my blog thing.
"""

import yaml
from jinja2 import Environment, FileSystemLoader
from os import getcwd, path, makedirs
from docutils.core import publish_parts
from shutil import copy2

metadata_file = 'metadata.yml'

# I decided to make this global. I think there are a few hacks I need to get
# rid of becuase of this change. If something doesn't make sense and looks
# like a hack it's becuase this wasn't global initially.
with open(metadata_file, 'r') as f:
    md = yaml.load(f)
archive_cutoff = md['archive_cutoff']


def collect():
    """
    Collects a site's metadata.
    """
    d = []

    for t in md['listing']:
        t[list(t.keys())[0]] = md['sourcedir']+t[list(t.keys())[0]]
        d.append(collect_single(t))

    d.append(collect_single({md['title']: md['homepage']}))

    return d


def collect_single(info=None):
    """
    Collects metada for a given rst file.
    """

    md = {}
    md['title'] = list(info.keys())[0]
    md['filename'] = info[md['title']]
    md['url'] = '/'+md['filename'].replace('.rst','')+'/'
    return md


def render():
    """
    Renders the site.
    """
    md = collect()
    print(md)

    for element in md:
        render_single(element)


def render_single(info=None):
    """
    Renders a given rst file.
    """

    file_content = {}

    with open(info['filename']) as f:
        file_content = publish_parts(f.read(), writer_name='html')

    title = info['title']
    body = file_content
    nav = collect()
    archive_url='/archive/'

    for element in body:
        body[element].replace('\\n','')

    with open('article.jinja', 'r') as f:
        loader = FileSystemLoader(getcwd())
        env = Environment(loader=loader)
        template = env.get_template('article.jinja')
        page = template.render(title=title,
           article=body,
           style='style.css',
           archive_url=archive_url,
           archive_cutoff=archive_cutoff,
           navigation=nav)

    try:
        makedirs('./build/')
        copy2('./style.css', './build/style.css')
    except:
        pass

    if info['url'] == '/index/':
        with open('./build/'+'index.html', 'w') as f:
            f.write(page)
    else:
        try:
            makedirs('./build/'+info['url'])
        except:
            pass
        with open('./build/'+info['url']+'index.html', 'w') as f:
            f.write(page)
            copy2('./style.css', './build/'+info['url']+'/style.css')
    archive()


def archive():
    """
    Returns the url for the archive and generates the archive page.
    requries the existences of a ./archive.jinja file
    """
    tmp = collect()
    info = []

    for i in tmp:
        if i['filename'] != 'index.rst':
            info.append(i)

    with open('archive.jinja', 'r') as f:
        loader = FileSystemLoader(getcwd())
        env = Environment(loader=loader)
        template = env.get_template('archive.jinja')
        page = template.render(style='style.css',
                               archive_url='/archive/',
                               archive_cutoff=archive_cutoff,
                               page_list=info)

    try:
        makedirs('./build/')
        copy2('./style.css', './build/style.css')
    except:
        pass

    try:
        makedirs('./build/archive/')
    except:
        pass
    with open('./build/archive/index.html', 'w') as f:
        f.write(page)
        copy2('./style.css', './build/archive/style.css')


if __name__ == '__main__':
    render()
