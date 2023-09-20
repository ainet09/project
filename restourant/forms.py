from django import forms
from restourant.models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['table', 'check_in_date', 'check_out_date', 'guest_name', ]