
# from rest_framework import serializers
# from .models import (
#     Contacts, Events, Council, Gallery, Workshops, PreviousWorkshops,
#     Lectures, PreviousLectures, Pal, PhdDPPC, PhdCPPC, PhdSPPC,
#     UgCouncil, LanguageTeam, LanguageCourses, BranchRepresentative
# )


# class ContactsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Contacts
#         fields = '__all__'


# class EventsSerializer(serializers.ModelSerializer):
#     icon = serializers.SerializerMethodField()

#     class Meta:
#         model = Events
#         fields = '__all__'

#     def get_icon(self, obj):
#         return obj.icon.url if obj.icon else None


# class CouncilSerializer(serializers.ModelSerializer):
#     photo = serializers.SerializerMethodField()

#     class Meta:
#         model = Council
#         fields = '__all__'

#     def get_photo(self, obj):
#         return obj.photo.url if obj.photo else None


# class GallerySerializer(serializers.ModelSerializer):
#     image = serializers.SerializerMethodField()

#     class Meta:
#         model = Gallery
#         fields = '__all__'

#     def get_image(self, obj):
#         return obj.image.url if obj.image else None


# class WorkshopsSerializer(serializers.ModelSerializer):
#     photo = serializers.SerializerMethodField()

#     class Meta:
#         model = Workshops
#         fields = '__all__'

#     def get_photo(self, obj):
#         return obj.photo.url if obj.photo else None


# class PreviousWorkshopsSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = PreviousWorkshops
#         fields = '__all__'

# class LecturesSerializer(serializers.ModelSerializer):
#     poster = serializers.SerializerMethodField()

#     class Meta:
#         model = Lectures
#         fields = '__all__'

#     def get_poster(self, obj):
#         return obj.poster.url if obj.poster else None


# class PreviousLecturesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PreviousLectures
#         fields = '__all__'


# class PalSerializer(serializers.ModelSerializer):
#     photo = serializers.SerializerMethodField()

#     class Meta:
#         model = Pal
#         fields = '__all__'

#     def get_photo(self, obj):
#         return obj.photo.url if obj.photo else None


# class UgCouncilSerializer(serializers.ModelSerializer):
#     photo = serializers.SerializerMethodField()

#     class Meta:
#         model = UgCouncil
#         fields = '__all__'

#     def get_photo(self, obj):
#         return obj.photo.url if obj.photo else None


# class PhdDPPCSerializer(serializers.ModelSerializer):
#     photo = serializers.SerializerMethodField()

#     class Meta:
#         model = PhdDPPC
#         fields = '__all__'

#     def get_photo(self, obj):
#         return obj.photo.url if obj.photo else None


# class PhdCPPCSerializer(serializers.ModelSerializer):
#     photo = serializers.SerializerMethodField()

#     class Meta:
#         model = PhdCPPC
#         fields = '__all__'

#     def get_photo(self, obj):
#         return obj.photo.url if obj.photo else None


# class PhdSPPCSerializer(serializers.ModelSerializer):
#     photo = serializers.SerializerMethodField()

#     class Meta:
#         model = PhdSPPC
#         fields = '__all__'

#     def get_photo(self, obj):
#         return obj.photo.url if obj.photo else None


# class LanguageTeamSerializer(serializers.ModelSerializer):
#     photo = serializers.SerializerMethodField()

#     class Meta:
#         model = LanguageTeam
#         fields = '__all__'

#     def get_photo(self, obj):
#         return obj.photo.url if obj.photo else None


# class LanguageCoursesSerializer(serializers.ModelSerializer):
#     photo = serializers.SerializerMethodField()

#     class Meta:
#         model = LanguageCourses
#         fields = '__all__'

#     def get_photo(self, obj):
#         return obj.photo.url if obj.photo else None


# class BranchRepresentativesSerializer(serializers.ModelSerializer):
#     photo = serializers.SerializerMethodField()

#     class Meta:
#         model = BranchRepresentative
#         fields = '__all__'

#     def get_photo(self, obj):
#         return obj.photo.url if obj.photo else None


from rest_framework import serializers
from .models import (
    Contacts, Events, Council, Gallery, Workshops, PreviousWorkshops,
    Lectures, PreviousLectures, Pal, PhdDPPC, PhdCPPC, PhdSPPC,
    UgCouncil, LanguageTeam, LanguageCourses, BranchRepresentative, Carousel
)


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'


class EventsSerializer(serializers.ModelSerializer):
    icon = serializers.SerializerMethodField()

    class Meta:
        model = Events
        fields = '__all__'

    def get_icon(self, obj):
        request = self.context.get('request')
        if obj.icon and request:
            return request.build_absolute_uri(obj.icon.url)
        elif obj.icon:
            return obj.icon.url
        return None


class CouncilSerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField()

    class Meta:
        model = Council
        fields = '__all__'

    def get_photo(self, obj):
        request = self.context.get('request')
        if obj.photo and request:
            return request.build_absolute_uri(obj.photo.url)
        elif obj.photo:
            return obj.photo.url
        return None


class GallerySerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Gallery
        fields = '__all__'

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)
        elif obj.image:
            return obj.image.url
        return None


class WorkshopsSerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField()

    class Meta:
        model = Workshops
        fields = '__all__'

    def get_photo(self, obj):
        request = self.context.get('request')
        if obj.photo and request:
            return request.build_absolute_uri(obj.photo.url)
        elif obj.photo:
            return obj.photo.url
        return None


class PreviousWorkshopsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreviousWorkshops
        fields = '__all__'


class LecturesSerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField()

    class Meta:
        model = Lectures
        fields = '__all__'

    def get_photo(self, obj):
        request = self.context.get('request')
        if obj.photo and request:
            return request.build_absolute_uri(obj.photo.url)
        elif obj.photo:
            return obj.photo.url
        return None


class PreviousLecturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreviousLectures
        fields = '__all__'


class PalSerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField()

    class Meta:
        model = Pal
        fields = '__all__'

    def get_photo(self, obj):
        request = self.context.get('request')
        if obj.photo and request:
            return request.build_absolute_uri(obj.photo.url)
        elif obj.photo:
            return obj.photo.url
        return None


class UgCouncilSerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField()

    class Meta:
        model = UgCouncil
        fields = '__all__'

    def get_photo(self, obj):
        request = self.context.get('request')
        if obj.photo and request:
            return request.build_absolute_uri(obj.photo.url)
        elif obj.photo:
            return obj.photo.url
        return None


class PhdDPPCSerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField()

    class Meta:
        model = PhdDPPC
        fields = '__all__'

    def get_photo(self, obj):
        request = self.context.get('request')
        if obj.photo and request:
            return request.build_absolute_uri(obj.photo.url)
        elif obj.photo:
            return obj.photo.url
        return None


class PhdCPPCSerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField()

    class Meta:
        model = PhdCPPC
        fields = '__all__'

    def get_photo(self, obj):
        request = self.context.get('request')
        if obj.photo and request:
            return request.build_absolute_uri(obj.photo.url)
        elif obj.photo:
            return obj.photo.url
        return None


class PhdSPPCSerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField()

    class Meta:
        model = PhdSPPC
        fields = '__all__'

    def get_photo(self, obj):
        request = self.context.get('request')
        if obj.photo and request:
            return request.build_absolute_uri(obj.photo.url)
        elif obj.photo:
            return obj.photo.url
        return None


class LanguageTeamSerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField()

    class Meta:
        model = LanguageTeam
        fields = '__all__'

    def get_photo(self, obj):
        request = self.context.get('request')
        if obj.photo and request:
            return request.build_absolute_uri(obj.photo.url)
        elif obj.photo:
            return obj.photo.url
        return None


class LanguageCoursesSerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField()

    class Meta:
        model = LanguageCourses
        fields = '__all__'

    def get_photo(self, obj):
        request = self.context.get('request')
        if obj.photo and request:
            return request.build_absolute_uri(obj.photo.url)
        elif obj.photo:
            return obj.photo.url
        return None


class BranchRepresentativesSerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField()

    class Meta:
        model = BranchRepresentative
        fields = '__all__'

    def get_photo(self, obj):
        request = self.context.get('request')
        if obj.photo and request:
            return request.build_absolute_uri(obj.photo.url)
        elif obj.photo:
            return obj.photo.url
        return None


class CarouselSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Carousel
        fields = '__all__'

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)
        elif obj.image:
            return obj.image.url
        return None
