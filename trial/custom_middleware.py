from django.http import HttpResponseForbidden
from django.shortcuts import render

class Custom403Middleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if response.status_code == 403:
            return self.handle_403(request)
        return response

    def handle_403(self, request):
        # You can render a custom error page here.
        return render(request, 'employee_register/error.html', status=403)