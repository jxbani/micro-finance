# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-22 14:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('micro_admin', '0010_auto_20160804_1044'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupMemberLoanAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_amount', models.DecimalField(decimal_places=6, max_digits=19)),
                ('loan_repayment_period', models.IntegerField()),
                ('loan_repayment_every', models.IntegerField()),
                ('loan_repayment_amount', models.DecimalField(blank=True, decimal_places=6, max_digits=19, null=True)),
                ('total_loan_amount_repaid', models.DecimalField(decimal_places=6, default=0, max_digits=19)),
                ('interest_charged', models.DecimalField(decimal_places=6, default=0, max_digits=19)),
                ('total_interest_repaid', models.DecimalField(decimal_places=6, default=0, max_digits=19)),
                ('total_loan_paid', models.DecimalField(decimal_places=6, default=0, max_digits=19)),
                ('total_loan_balance', models.DecimalField(decimal_places=6, default=0, max_digits=19)),
                ('loanprocessingfee_amount', models.DecimalField(decimal_places=6, default=0, max_digits=19)),
                ('no_of_repayments_completed', models.IntegerField(default=0)),
                ('principle_repayment', models.DecimalField(blank=True, decimal_places=6, max_digits=19, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='micro_admin.Client')),
                ('group_loan_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='micro_admin.LoanAccount')),
            ],
        ),
    ]
