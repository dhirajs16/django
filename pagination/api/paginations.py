from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

class MyPageNumberPagination(PageNumberPagination):
    page_size = 5 # default page size
    page_size_query_param = 'record' # to take dynamic input for page size as "?record = 5"
    max_page_size = 10
    
    page_query_param = 'set'
    
    last_page_strings = 'end' # default string is 'last'
    
class MyLimitOffsetPagination(LimitOffsetPagination):
    '''
    limit means no. of records in each page
    offset mean the (n+1)th record to start the page with
    '''
    default_limit = 5 # default no. of records in each page
    max_limit = 7
    # limit_query_param = 'range'
    # offset_query_param = 'start'
    # limit_query_description = 'hello there'
    # offset_query_description  = 'hello again'