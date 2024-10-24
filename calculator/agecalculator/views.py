from django.shortcuts import render
from django.utils import timezone
 
def calculate_age(birth_date, calc_date):
    # Convert string date to datetime.date
    birth_date = timezone.datetime.strptime(birth_date, '%Y-%m-%d').date()
    calc_date = timezone.datetime.strptime(calc_date, '%Y-%m-%d').date()
   
    age = calc_date.year - birth_date.year - ((calc_date.month, calc_date.day) < (birth_date.month, birth_date.day))
    return age
 
def home(request):
    age = None
    if request.method == 'POST':
        birth_date = request.POST.get('birth_date')
        calc_date = request.POST.get('calc_date')
       
        if birth_date and calc_date:
            age = calculate_age(birth_date, calc_date)
            return render(request, 'agecalclator/result.html', {'age': age})
   
    return render(request, 'agecalclator/home.html')
 
 
 
def home(request):
    return render(request, 'agecalclator/home.html')
 
def calculater1(request):
    return render(request, 'agecalclator/calculater.html')
 
def about(request):
    return render(request, 'agecalclator/about.html')
 
def contact(request):
    return render(request, 'agecalclator/contact.html')
 

   
 
