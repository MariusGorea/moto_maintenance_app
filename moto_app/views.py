from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from vininfo import Vin

from .forms import OwnerForm
from .models import Motorycycle, SoldPart

# Create your views here.

from django.http import HttpResponse


def index(request):
    context = {}
    if request.method == "POST":
        vin_code = request.POST.get("vin", "")
        # Pass the VIN number into Vin methods
        vin = Vin(vin_code)
        context = {'vin': vin}
                   # prints vehicle's country
        print(vin.country)

                   # prints vehicle's manufacturer
        print(vin.manufacturer)

                   # prints vehicle manufacturer's region
        print(vin.region)
                   # prints vehicle years
        print(vin.years)

    return render(request, 'homepage.html', context)

def list(request):
    toate_motocicletele = Motorycycle.objects.all()
    print(str(toate_motocicletele))
    context = {"toate_motocicletele": toate_motocicletele}
    return render(request, 'list.html', context)

def tables(request):
    context = {}
    motociclete_cu_costuri = []
    toate_motocicletele = Motorycycle.objects.all()
    for motorcycle in toate_motocicletele:
        motociclete_cu_costuri.append({'motorcycle':motorcycle, 'expense': motorcycle_total(motorcycle)})

    # print(str(toate_motocicletele))
    # motociclete_cu_costuri=[d for d in map(lambda motorcycle:c, [m for m in toate_motocicletele])]
    context = {"motociclete_cu_costuri": motociclete_cu_costuri}
    return render(request, 'tables.html', context)


def motorcycle_total(motorcycle):
    sold_parts=SoldPart.objects.filter(motorcycle=motorcycle)
    totals=[t for t in map(lambda sold_part:sold_part.quantity*sold_part.part.price, sold_parts)]
    total=sum(totals)
    return total

def register_view(request):
    if request.method == 'POST':
        # instantiem cele 2 formulare folosind datele din dictionarul request.POST
        user_form = UserCreationForm(data=request.POST)
        client_profile_form = OwnerForm(data=request.POST)
        if user_form.is_valid() and client_profile_form.is_valid():
            user = user_form.save()
            client_profile = client_profile_form.save()
            # salvam profilul de client si facem un update la coloana user si legam de user-ul creat mai sus
            client_profile.user = user
            client_profile.save()
            return redirect('/')
    else:  # method=get
        # instantiem 2 formulare goale si le trimitem catre template
        user_form = UserCreationForm()
        client_profile_form = OwnerForm()
    # Pe get, formularele sunt goale. Pe post, formularele sunt cele instantiate mai sus in if(populate).
    return render(request, 'register.html', {'user_form': user_form, 'client_profile_form': client_profile_form})
