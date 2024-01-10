from django.shortcuts import render
from .forms import ReservationForm

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def booking(request):
    return render(request, 'booking.html')

def contact(request):
    return render(request, 'contact.html')

def menu(request):
    return render(request, 'menu.html')

def service(request):
    return render(request, 'service.html')

def table_booking(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')
    else:
        form = ReservationForm()

    return render(request, 'reservations/book_table.html', {'form': form})

def team(request):
    return render(request, 'team.html')

def terms(request):
    return render(request, 'terms&condition.html')

def testimonial(request):
    return render(request, 'testimonial.html')

def success(request):
    return render(request, 'success_page.html')
