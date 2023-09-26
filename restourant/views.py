from .models import  CategoryProductsModel, ProductsModel, TableModel, Booking, AboutModel
from django.views.generic import *
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from restourant.forms import BookingForm


# Create your views here.

def log_in(request):
    if request.method == "POST":
        username = request.POST.get("email")
        pass1 = request.POST.get("pass1")
        user = authenticate(username=username, password=pass1)

        print(username)
        print(pass1)
        if user:
            login(request, user)
            print("login success")
            return redirect("/")
        else:
            messages.error(request, 'Please Enter Valid Credentials!')
            return render(request, "pages/login.html")
    else:
        return render(request, 'pages/register.html')


def register(request):
    if request.method == "POST":

        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        if len(username) > 15:
            messages.error(request, "*Your user name must be under 10 characters")
            return render(request, 'pages/register.html')

        if not username.isalnum():
            messages.error(request, "*User name should only contain letters and numbers")
            return render(request, 'pages/register.html')
        SpecialSym = ['$', '@', '#', '%']

        if len(pass1) < 6:
            messages.error(request, '''*Password's length should be at least 6''')

            return render(request, 'pages/register.html')

        if len(pass1) > 20:
            messages.error(request, '''*Password's length should be not be greater than 20''')

            return render(request, 'pages/register.html')

        if not any(char.isdigit() for char in pass1):
            messages.error(request, '*Password should have at least one numeric / digit')

            return render(request, 'pages/register.html')

        if not any(char.isupper() for char in pass1):
            messages.error('*Password should have at least one uppercase letter')

            return render(request, 'pages/register.html')

        if not any(char.islower() for char in pass1):
            messages.error(request, '*Password should have at least one lowercase letter')

            return render(request, 'pages/register.html')

        user_obj = User.objects.create(username=username, email=email)
        user_obj.set_password(pass1)
        user_obj.save()
        return render(request, "pages/login.html")

    return render(request, 'pages/login.html')


# END   LOGIN


class HomeView(TemplateView):
    template_name = 'home.html'



class CategoryView(ListView):
    template_name = "home.html"
    model = CategoryProductsModel
    context_object_name = 'category_data'


class ProductView(ListView):
    template_name = 'home.html'
    model = ProductsModel
    queryset = TableModel.objects.all()

 

class PalovView(ListView):
    template_name = 'pages/palov.html'
    model = ProductsModel
   


class KebabView(ListView):
    template_name = 'pages/kebab.html'
    model = ProductsModel


class DessertView(ListView):
    template_name = 'pages/dessert.html'
    model = ProductsModel



class DrinksView(ListView):
    template_name = 'pages/drinks.html'
    model = ProductsModel


class SteakView(ListView):
    template_name = 'pages/steak.html'
    model = ProductsModel


class SaladsView(ListView):
    template_name = 'pages/salads.html'
    model = ProductsModel
    queryset = ProductsModel.objects.all()


class LocationView(TemplateView):
    template_name = './pages/location.html'
    context_object_name = 'location_data'



class AboutView(ListView):
    model = AboutModel
    template_name = "./pages/about.html"
    context_object_name = 'about_data'












def table_view(request):
    tables = TableModel.objects.filter()
    return render(request, 'booking/table_list.html', {'tables': tables})


def book_table(request, table_id):
    if request.method == 'POST':
        tables = TableModel.objects.get(id=table_id)
        guest_name = request.POST['guest_name']
        check_in_date = request.POST['check_in_date']
        check_out_date = request.POST['check_out_date']
        booking = Booking.objects.create(table=tables, guest_name=guest_name, check_in_date=check_in_date,
                                         check_out_date=check_out_date)
        # Perform any additional logic or operations
        return redirect('booking_success')
    else:
        table = TableModel.objects.get(id=table_id)
        return render(request, 'pages/book_table.html', {'table': table})


def booking_detail(request, ):
    booking = Booking.objects.get()
    return render(request, 'pages/booking_detail.html', {'booking': booking})


def booking_success(request):
    return render(request, 'pages/booking_success.html')


def booking_view(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            table_number = form.cleaned_data['table_number']
            check_in_date = form.cleaned_data['check_in_date']
            check_out_date = form.cleaned_data['check_out_date']
            guest_name = form.cleaned_data['guest_name']

            table = TableModel.objects.get(table_number=table_number)
            if table.availability:
                booking = Booking.objects.create(table=table, check_in_date=check_in_date,
                                                 check_out_date=check_out_date,
                                                 guest_name=guest_name)
                table.availability = False
                table.save()
                return redirect('booking_success')
            else:
                return redirect('booking_failed')
    else:
        form = BookingForm()
    return render(request, 'book_table.html', {'form':form  })




class Drinks(ListView):
    model = ProductView
    template_name = './pages/drinks'
    queryset = TableModel.objects.all()

