# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cellphones', '0011_auto_20160813_0500'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('street', models.CharField(max_length=300, blank=True, null=True)),
                ('district', models.CharField(max_length=50, blank=True, null=True)),
                ('city', models.CharField(max_length=50, choices=[(1, ' An Giang'), (2, ' Bà Rịa Vũng Tàu'), (3, ' Bạc Liêu'), (4, ' Bắc Kạn'), (5, ' Bắc Giang'), (6, ' Bắc Ninh'), (7, ' Bến Tre'), (8, ' Bình Dương'), (9, ' Bình Định'), (10, ' Bình Phước'), (11, ' Bình Thuận'), (12, ' Cà Mau'), (13, ' Cao Bằng'), (14, ' Cần Thơ – Hậu Giang'), (15, ' TP. Đà Nẵng'), (16, ' ĐắkLắk – Đắc Nông'), (17, ' Đồng Nai'), (18, ' Đồng Tháp'), (19, ' Gia Lai'), (20, ' Hà Giang'), (21, ' Hà Nam'), (22, ' TP. Hà Nội'), (24, ' Hà Tĩnh'), (25, ' Hải Dương'), (26, ' TP. Hải Phòng'), (27, ' Hoà Bình'), (28, ' Hưng Yên'), (29, ' TP. Hồ Chí Minh'), (30, ' Khánh Hoà'), (31, ' Kiên Giang'), (32, ' Kon Tum'), (33, ' Lai Châu – Điện Biên'), (34, ' Lạng Sơn'), (35, ' Lao Cai'), (36, ' Lâm Đồng'), (37, ' Long An'), (38, ' Nam Định'), (39, ' Nghệ An'), (40, ' Ninh Bình'), (41, ' Ninh Thuận'), (42, ' Phú Thọ'), (43, ' Phú Yên'), (44, ' Quảng Bình'), (45, ' Quảng Nam'), (46, ' Quảng Ngãi'), (47, ' Quảng Ninh'), (48, ' Quảng Trị'), (49, ' Sóc Trăng'), (50, ' Sơn La'), (51, ' Tây Ninh'), (52, ' Thái Bình'), (53, ' Thái Nguyên'), (54, ' Thanh Hoá'), (55, ' Thừa Thiên Huế'), (56, ' Tiền Giang'), (57, ' Trà Vinh'), (58, ' Tuyên Quang'), (59, ' Vĩnh Long'), (60, ' Vĩnh Phúc'), (61, ' Yên Bái')], null=True, blank=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('description', models.TextField(max_length=300, blank=True, null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('original_price', models.FloatField(blank=True, null=True)),
                ('deduction', models.FloatField(default=0)),
                ('delivered_cost', models.FloatField(blank=True, null=True)),
                ('total_price', models.FloatField(blank=True, null=True)),
                ('checkout_date', models.DateTimeField()),
                ('delivering_estimate_date', models.DateField(blank=True, null=True)),
                ('delivered_date', models.DateTimeField(blank=True, null=True)),
                ('payment_type', models.SmallIntegerField(choices=[(1, 'VISA/CARD'), (2, 'CASH - COD')], blank=True, null=True)),
                ('card_number', models.CharField(max_length=16, blank=True, null=True, validators=[django.core.validators.RegexValidator(message='Card number must be entered numeric only', regex='^\\d{16}$')])),
                ('shipping_address', models.TextField(blank=True, null=True)),
                ('description', models.TextField(max_length=500)),
                ('order_status', models.SmallIntegerField(choices=[(1, 'SHOPPING'), (2, 'CHECK OUT'), (3, 'ON DELIVER'), (4, 'DELIVERED'), (5, 'CANCELLED'), (6, 'RETURNING'), (7, 'RETURNED'), (8, 'INACTIVE')], default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(to='mycart.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('price', models.FloatField()),
                ('original_price', models.FloatField()),
                ('discounted_price', models.FloatField(blank=True, null=True)),
                ('item', models.ForeignKey(to='cellphones.Device')),
                ('order', models.ForeignKey(to='mycart.Order')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(through='mycart.OrderItem', to='cellphones.Device'),
        ),
    ]
