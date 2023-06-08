from .models import Location

def menu_links(request):
    links = Location.objects.all()
    return dict(links_location=links)