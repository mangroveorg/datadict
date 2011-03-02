#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4

"""
    Setup the connection singleton
"""

import connection

if not hasattr(connection, 'db'):
    url, server, db = connection.connect()
    connection.url = url
    connection.server = server
    connection.db = db
