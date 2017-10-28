#!/usr/bin/python
# -*- coding: utf-8 -*-

####
# Copyright (C) 2009-2015 Kim Gerdes
# kim AT gerdes. fr
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This script is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE
# See the GNU General Public License (www.gnu.org) for more details.
#
# You can retrieve a copy of the GNU General Public License
# from http://www.gnu.org/.  For a copy via US Mail, write to the
#     Free Software Foundation, Inc.
#     59 Temple Place - Suite 330,
#     Boston, MA  02111-1307
#     USA
####
from __future__ import print_function
import os
import cgitb
import cgi
cgitb.enable()


def print_html_header():
    print(open('templates/q_htmlheader.html', 'r').read())


def print_headline():
    print(open('templates/q_headline.html', 'r').read())


def print_footer():
    print("</div>")
    print("</body></html>")


def print_export():
    print(open('templates/q_export.html', 'r').read())


def print_forms():
    print(open('templates/q_forms.html', 'r').read())


def print_menues():
    print(open('templates/q_menus.html', 'r').read())


def print_dialogs():
    print(open('templates/q_dialogs.html', 'r').read())


def start():
    form = cgi.FieldStorage()
    thisfile = os.environ.get('SCRIPT_NAME', ".")
    print("Content-Type: text/html\n")  # blank line: end of headers


def main():
    start()
    print_html_header()
    print_headline()
    print_forms()
    print_export()
    print_menues()
    print_dialogs()
    print_footer()


if __name__ == "__main__":
    main()