from .models import HomeProfile

def oprofile(request):
    info = HomeProfile.objects.get(pk=1)

    context = {
        'info':info
    }

    return context 