# -*- coding: utf-8 -*-

"""
Copyright (c) 2021 Keijack Wu

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


import os
import sys
from simple_http_server import Response
from simple_http_server.logger import get_logger
from jinja2 import Environment, FileSystemLoader
from typing import Dict

name = "simple_http_server_jinja"
version = "0.0.1"

_logger = get_logger("simple_http_server_jinja")

DEFAULT_TAG = "default"
ENVS: Dict[str, Environment] = {}


def set_env(env: Environment, tag: str = DEFAULT_TAG):
    ENVS[tag] = env


def get_project_dir() -> str:
    mpath = os.path.dirname(sys.modules['__main__'].__file__)
    _logger.debug(f"Path of module[main] is {mpath}")
    return mpath


def get_env(tag: str = DEFAULT_TAG) -> Environment:
    if tag not in ENVS:
        searchpath = os.path.join(get_project_dir(), "templates")
        _logger.info(
            f"Cannot find env in tag[#{tag}], create a default one which templates should in {searchpath}")
        ENVS[tag] = Environment(loader=FileSystemLoader(searchpath))
    return ENVS[tag]


class JinjaView(Response):

    def __init__(self, name, kwargs={},
                 env_tag=DEFAULT_TAG,
                 status_code: int = 200,
                 headers: Dict[str, str] = None):
        env = get_env(env_tag)
        tpl = env.get_template(name)
        body = tpl.render(kwargs)
        super().__init__(status_code, headers, body=body)
