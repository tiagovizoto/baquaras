from django.forms import ModelForm
from .models import BackTestTryd


class BackTestTrydForm(ModelForm):
    class Meta:
        model = BackTestTryd
        fields = ['paper', 'opening', 'closing', 'tome_total', 'amount', 'type_operation', 'average_price_buy',
                  'average_price_sell', 'result_close', 'result_open', 'result_total', 'date_operation',
                  'cost_operation', 'tet', 'mep', 'men', 'balance_result']
git add