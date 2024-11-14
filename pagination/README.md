# **Pagination in DRF**

Django REST Framework (DRF) offers three main types of pagination to help manage large datasets efficiently:

1. **Page Number Pagination**:
- Divides data into pages and allows users to navigate through pages using page numbers.
- Example: `PageNumberPagination`

2. **Limit Offset Pagination**:
- Provides a fixed number of items (the "limit") per page and allows users to navigate through pages using an offset.
- Example: `LimitOffsetPagination`

3. **Cursor Pagination**:
- Uses a unique cursor value (e.g., a timestamp or database row ID) to navigate between pages.
- Example: `CursorPagination`

Each pagination style has its own use cases and can be configured in the `settings.py` file or on a per-view basis. 


### **For global pagination**
```python
REST_FRAMEWORK = {
   'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 5,
}
```