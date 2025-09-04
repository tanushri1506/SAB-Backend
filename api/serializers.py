from rest_framework import serializers
from .models import Contacts, Events,Council,Gallery,Workshops, PreviousWorkshops,Lectures,PreviousLectures,Pal,PhdDPPC,PhdCPPC,PhdSPPC,UgCouncil,LanguageTeam,LanguageCourses

class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'

class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'

class CouncilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Council
        fields = '__all__'

class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'



class WorkshopsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workshops
        fields = '__all__'  

class PreviousWorkshopsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreviousWorkshops
        fields = '__all__'

class LecturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lectures
        fields = '__all__'  

class PreviousLecturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreviousLectures
        fields = '__all__'

class PalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pal
        fields = '__all__'

class UgCouncilSerializer(serializers.ModelSerializer):
    class Meta:
        model = UgCouncil
        fields = '__all__'

class PhdDPPCSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhdDPPC
        fields = '__all__'

class PhdCPPCSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhdCPPC
        fields = '__all__'

class PhdSPPCSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhdSPPC
        fields = '__all__'

class LanguageTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = LanguageTeam
        fields = '__all__'

class LanguageCoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = LanguageCourses
        fields = '__all__'