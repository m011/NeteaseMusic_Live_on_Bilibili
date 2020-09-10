#!/usr/bin/env python
# -*- coding: utf-8 -*-
import asyncio

from quart import Quart

from live.room import Room
from live.views import bluepoint

Application = Quart(__name__)

Application.jinja_env.auto_reload = True
Application.register_blueprint(bluepoint)

if __name__ == "__main__":

    room = Room()
    room.connect()

    Application.run()
