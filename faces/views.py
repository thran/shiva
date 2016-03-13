from constance import config
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic import View


class Home(View):
    def get(self, request):

        return render(request, "home.html", {
            "message": config.INFO_TEXT,
        })

home = ensure_csrf_cookie(Home.as_view())
