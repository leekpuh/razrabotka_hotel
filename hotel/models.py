from django.db import models


class Guest(models.Model):
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    patronimyc = models.CharField(null=True, blank=True, max_length=50, verbose_name='Отчество')
    phone = models.PositiveBigIntegerField(verbose_name='Контактный номер')
    email = models.CharField(max_length=50, verbose_name='E-mail')

    def __str__(self):
        return '{} {} {}'.format(self.last_name, self.first_name,
                                 self.patronimyc or '')

    class Meta:
        verbose_name = 'Данные гостя'
        verbose_name_plural = 'Данные гостей'


class Room_type(models.Model):
    room_type = models.CharField(max_length=50, verbose_name='Тип номера')
    beds = models.CharField(max_length=50, verbose_name='Количество кроватей')
    cost = models.IntegerField(verbose_name='Цена за 1 ночь')
    description = models.CharField(max_length=500, verbose_name='Описание номера')

    def __str__(self):
         return '{} - {}'.format(self.room_type, self.beds)

    class Meta:
        verbose_name = 'Тип номера'
        verbose_name_plural = 'Типы номеров'


class Room(models.Model):

    room_number = models.IntegerField(verbose_name='Номер')
    room_floor = models.IntegerField(verbose_name='Этаж')
    id_room_type = models.ForeignKey(Room_type, on_delete=models.CASCADE, verbose_name='Тип номера')

    def __str__(self):
        return '{} - {} | {}'.format(self.room_number, self.room_floor, self.id_room_type)

    class Meta:
        verbose_name = 'Номер'
        verbose_name_plural = 'Номера'


class Booking(models.Model):
    booking_date = models.DateField(verbose_name='Дата брони')
    checkin_date = models.DateTimeField(null=True, blank=True, verbose_name='Дата въезда')
    checkout_date = models.DateTimeField(null=True, blank=True, verbose_name='Дата выезда')
    number_of_nights = models.IntegerField(verbose_name='Кол-во ночей')
    id_guest = models.ForeignKey(Guest, on_delete=models.CASCADE, verbose_name='Регистрация клиента')
    id_room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name='Бронь номера')
    total_cost = models.IntegerField(default=0, verbose_name='Общая стоимость')

    def __str__(self):
        return '{} {} ({})'.format(self.id_guest, self.booking_date, self.id_room)

    class Meta:
        unique_together = ('checkin_date', 'id_room')
        verbose_name = 'Бронирование номера'
        verbose_name_plural = 'Бронирование номеров'

    def save(self, *args, **kwargs):
        self.total_cost = int(self.id_room.id_room_type.cost) * int(self.number_of_nights)
        super().save(*args, **kwargs)