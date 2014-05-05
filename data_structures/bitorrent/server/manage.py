#!/usr/bin/env python
import eventlet
eventlet.monkey_patch()

from flask.ext.script import Manager

from trackpy import create_app


if __name__ == "__main__":
  manager = Manager(create_app)

  manager.add_option('-c', '--config', dest='config', required=False)

  manager.run()
