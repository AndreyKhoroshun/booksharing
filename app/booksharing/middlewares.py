from time import time
from books.models import Log


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time()
        response = self.get_response(request)
        end = time()
        session_time = end - start
        Log.objects.create(path=request.path, method=request.method, time=session_time)
        return response
