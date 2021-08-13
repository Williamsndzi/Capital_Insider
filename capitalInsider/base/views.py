from django.shortcuts import render
from services.models import Services
from contact.models import ContactInfo, SocialNetwork

# Create your views here.
def footer(request):
    services = Services.objects.all()[:6]
    print(f"===================>>>>> {services}")
    titles = map(lambda service: {service.id, service.title } , services)
    contact_info = ContactInfo.objects.all()
    social_icons = SocialNetwork.objects.all()

    context = {
        "titles": titles,
        "contact_info": contact_info,
        "social_icons": social_icons
    }
    return render(request, 'footer.html', context)
