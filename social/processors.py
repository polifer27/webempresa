from .models import Link

def ctx_dict(request):
    ctx = {}
    links = Link.objects.all()
    for link in links:
        ctx[link.key] = link.url  # a la clave link.key le doy el valor link.url
                                  # con esto generamos un diccionario con las redes sociales    
    return ctx