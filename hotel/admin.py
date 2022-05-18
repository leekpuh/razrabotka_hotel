from django.contrib import admin

from .models import Guest, Room, Room_type, Booking

class GuestAdmin(admin.ModelAdmin):
    search_fields = ['phone', 'first_name', 'last_name', 'patronimyc', 'email']

class BookingAdmin(admin.ModelAdmin):
    search_fields = ['booking_date', 'checkin_date', 'checkout_date',
                     'number_of_nights', 'total_cost', 'id_guest__last_name',
                     'id_guest__first_name', 'id_guest__patronimyc']

class RoomTypeAdmin(admin.ModelAdmin):
    search_fields = ['room_type', 'beds', 'cost', 'description']

class RoomAdmin(admin.ModelAdmin):
    search_fields = ['room_number', 'room_floor']

admin.site.register(Guest,GuestAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Room_type, RoomTypeAdmin)
admin.site.register(Booking, BookingAdmin)