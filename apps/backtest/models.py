from django.db import models
from utils.models import BaseModel
from model_utils.models import TimeStampedModel, SoftDeletableModel


class BackTestTryd(BaseModel, TimeStampedModel, SoftDeletableModel):
    paper = models.CharField(max_length=10)
    opening = models.TimeField()
    closing = models.TimeField()
    time_total = models.TimeField()
    amount = models.IntegerField()
    type_operation = models.CharField(max_length=1 ,choices=[('C', 'COMPRA'), ('V', 'VENDA')])
    average_price_buy = models.DecimalField(max_digits=12, decimal_places=5)
    average_price_sell = models.DecimalField(max_digits=12, decimal_places=5)
    result_close = models.DecimalField(max_digits=12, decimal_places=5)
    result_open = models.DecimalField(max_digits=12, decimal_places=5)
    result_total = models.DecimalField(max_digits=12, decimal_places=5)
    date_operation = models.DateField()
    cost_operation = models.DecimalField(max_digits=12, decimal_places=2)
    tet = models.TimeField()
    mep = models.DecimalField(max_digits=12, decimal_places=2)
    men = models.DecimalField(max_digits=12, decimal_places=2)
    balance_result = models.DecimalField(max_digits=12, decimal_places=2)
