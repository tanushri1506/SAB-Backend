from django.db import models

class Contacts(models.Model):
    role = models.CharField(max_length=200, blank=True)
    name = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)

    class Meta:
        verbose_name_plural = "Contacts"

    def __str__(self):
        return self.name or "Unnamed Contact"


class Council(models.Model):
    name = models.CharField(max_length=200)
    post = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    linkedin = models.URLField(blank=True)
    photo = models.ImageField(upload_to='councils/', blank=True, null=True)

    class Meta:
        verbose_name_plural = "Council"

    def __str__(self):
        return self.name


class Events(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField(blank=True)
    icon = models.ImageField(upload_to='events/', blank=True, null=True)

    class Meta:
        verbose_name_plural = "Events"

    def __str__(self):
        return self.title


class Gallery(models.Model):
    label = models.CharField(max_length=200)
    image = models.ImageField(upload_to='gallery/')

    class Meta:
        verbose_name_plural = "Gallery"

    def __str__(self):
        return self.label
    

class Workshops(models.Model):
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='workshops/')
    instructors = models.JSONField(default=list, blank=True, null=True)
    mode = models.CharField(max_length=50)
    date = models.CharField(max_length=100)
    fees = models.CharField(max_length=50)
    url = models.URLField()
    schedule = models.JSONField(default=list)
    highlights = models.JSONField(default=list)
    location = models.CharField(max_length=200)
    benefits = models.TextField()
    class Meta:
        verbose_name_plural = "Workshops"
    def __str__(self):
        return self.title
    

class PreviousWorkshops(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField(blank=True)
    alt = models.CharField(max_length=200)
    class Meta:
        verbose_name_plural = "PreviousWorkshops"

    def __str__(self):
        return self.title


class Lectures(models.Model):
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='lectures/')
    instructors = models.JSONField(default=list, blank=True, null=True)
    mode = models.CharField(max_length=50)
    date = models.CharField(max_length=100)
    fees = models.CharField(max_length=50)
    url = models.URLField()
    schedule = models.JSONField(default=list)
    highlights = models.JSONField(default=list)
    location = models.CharField(max_length=200)
    benefits = models.TextField()
    class Meta:
        verbose_name_plural = "Lectures"
    def __str__(self):
        return self.title
    

class PreviousLectures(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField(blank=True)
    alt = models.CharField(max_length=200)
    class Meta:
        verbose_name_plural = "PreviousLectures"

    def __str__(self):
        return self.title


class Pal(models.Model):
    name = models.CharField(max_length=200)
    post = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    linkedin = models.URLField(blank=True)
    photo = models.ImageField(upload_to='pal/', blank=True, null=True)

    class Meta:
        verbose_name_plural = "Pal"

    def __str__(self):
        return self.name

class UgCouncil(models.Model):
    name = models.CharField(max_length=200)
    post = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    linkedin = models.URLField(blank=True)
    photo = models.ImageField(upload_to='ug-council/', blank=True, null=True)

    class Meta:
        verbose_name_plural = "UgCouncil"

    def __str__(self):
        return self.name

class PhdDPPC(models.Model):
    name = models.CharField(max_length=200)
    post = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    linkedin = models.URLField(blank=True)
    photo = models.ImageField(upload_to='dppc/', blank=True, null=True)

    class Meta:
        verbose_name_plural = "PhdDPPC"

    def __str__(self):
        return self.name

class PhdCPPC(models.Model):
    name = models.CharField(max_length=200)
    post = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    linkedin = models.URLField(blank=True)
    photo = models.ImageField(upload_to='cppc/', blank=True, null=True)

    class Meta:
        verbose_name_plural = "PhdCPPC"

    def __str__(self):
        return self.name

class PhdSPPC(models.Model):
    name = models.CharField(max_length=200)
    post = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    linkedin = models.URLField(blank=True)
    photo = models.ImageField(upload_to='sppc/', blank=True, null=True)

    class Meta:
        verbose_name_plural = "PhdSPPC"

    def __str__(self):
        return self.name

class LanguageTeam(models.Model):
    name = models.CharField(max_length=200)
    post = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    linkedin = models.URLField(blank=True)
    photo = models.ImageField(upload_to='language/', blank=True, null=True)

    class Meta:
        verbose_name_plural = "LanguageTeam"

    def __str__(self):
        return self.name


class LanguageCourses(models.Model):
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='lectures/')
    instructors = models.JSONField(default=list, blank=True, null=True)
    mode = models.CharField(max_length=50)
    date = models.CharField(max_length=100)
    fees = models.CharField(max_length=50)
    url = models.URLField()
    schedule = models.JSONField(default=list)
    highlights = models.JSONField(default=list)
    location = models.CharField(max_length=200)
    benefits = models.TextField()
    class Meta:
        verbose_name_plural = "LanguageCourses"
    def __str__(self):
        return self.title
    
