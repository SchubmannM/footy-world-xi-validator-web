from django.template.response import TemplateResponse
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET"])
def index(request):
    return TemplateResponse(request, "index.html", {})
