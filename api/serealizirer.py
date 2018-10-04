from  api.models import messdaten
from rest_framework import  serializers

class messdatenSerializer(serializers.ModelSerializer):
    """
    Serializing Messdaten
    """
    class Meta:
        model = messdaten
        fields = ("offenname", "O2", "CO2","NO","NO2","SO2","NOX","ETA","Lamda","Losses","Air_temperatur","Gas_temp","Airpressure")