
from rest_framework import viewsets
from .models import Guide
from .serializers import GuideSerializer
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from rest_framework.exceptions import NotAuthenticated


def custom_unauthorized_page(request):
    html_content = """
                <html>
                <body>
                    <center>
                    <h1>Hello, Folks!!</h1>
                    <p>error found 403</p>
                    </center>
                </body>
                </html>
            """
    return HttpResponse(html_content)


class GuideViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Guide.objects.all()
    serializer_class = GuideSerializer

    # def handle_exception(self, exc):
    #     print("Hello")
    #     print(type(exc))
    #     # if exc == "Authentication credentials were not provided.":
    #     if isinstance(exc, NotAuthenticated):
    #         print("hel")
    #         return HttpResponseRedirect('/unauthorized/')  # Use the URL pattern name if defined
    #     return super().handle_exception(exc)