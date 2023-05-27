from ..models import Historia

def get_historias():
    queryset = Historia.objects.all().order_by('-dateTime')[:10]
    return (queryset)

def create_historia(form):
    historia = form.save()
    historia.save()
    return ()