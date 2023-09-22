from django.shortcuts import render

from django.http import HttpResponse


def home_page_view(request):
    html_content = """
            <html>
            <body>
                <center>
                <h1>Hello, Folks!!</h1>
                <p>This is a Employee management web page.</p>
                </center>
            </body>
            </html>
        """
    return HttpResponse(html_content)
