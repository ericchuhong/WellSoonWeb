#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Chuhong Ma'

'''
JSON API definition
'''

import json, logging, inspect, functools

class Page(object):

    def __init__(self, item_count, page_index=1, page_size=10):
        '''
        Init Pagination by item_count, page_index and page_size.
        :param item_count:
        :param page_index:
        :param page_size:
        :return:
        '''
        self.item_count = item_count
        self.page_size = page_size
        self.page_count = item_count // page_size + (1 if item_count % page_size > 0 else 0)
        if (item_count == 0) or (page_index > self.page_count):
            self.offset = 0
            self.limit = 0
            self.page_index = 1
        else:
            self.page_index = page_index
            self.offset = self.page_size
            self.limit = self.page_size
        self.has_nex = self.page_index < self.page_count
        self.has_previous = self.page_index > 1


class APIError(Exception):
    '''
    the base APIError which contains error(required), data(optional) and message(optional)
    '''
    def __init__(self, error, data='', message=''):
        super(APIError,self).__init__(message)
        self.error = error
        self.data = data
        self.message = message

class APIValueError(APIError):
    '''
    Indicate the input value has error or invalid. The data specifies the error field of input form.
    '''
    def __init__(self, field, message=''):
        super(APIValueError, self).__init__('value:invalid', field, message)

class APIResourceNotFoundError(APIError):
    '''
    Indicate the resource was not found. The data specifies the resource name.
    '''
    def __init__(self, field, message=''):
        super(APIResourceNotFoundError, self).__init__('value:notfound',field, message)

class APIPermissionError(APIError):
    '''
    Indicate the api has no permission.
    '''
    def __init__(self, message=''):
        super(APIPermissionError, self).__init__('permission:forbidden', 'permission', message)