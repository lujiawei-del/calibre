#!/usr/bin/env python2
# vim:fileencoding=UTF-8:ts=4:sw=4:sta:et:sts=4:ai
from __future__ import absolute_import, division, print_function, unicode_literals

__license__   = 'GPL v3'
__copyright__ = '2011, Kovid Goyal <kovid@kovidgoyal.net>'
__docformat__ = 'restructuredtext en'


class NoSuchFormat(ValueError):
    pass


class NoSuchBook(KeyError):

    def __init__(self, book_id):
        KeyError.__init__(self, 'No book with id: {} in database'.format(book_id))
        self.book_id = book_id
