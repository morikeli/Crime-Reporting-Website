from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from PIL import Image

class PolicePosts(models.Model):
    id = models.CharField(max_length=25, primary_key=True, unique=True, editable=False)
    name = models.CharField(max_length=100, blank=False, unique=True)   # name of the police station
    mobile_no = PhoneNumberField(db_column='Mobile No. 1')
    mobile_no_sec = PhoneNumberField(db_column='Mobile No. 2')  # mobile no. 2 - named. 'sec' is short form for secondary
    county = models.CharField(max_length=50, blank=False)
    sub_county = models.CharField(max_length=80, blank=False)
    constituency = models.CharField(max_length=80, blank=False)
    ward = models.CharField(max_length=80, blank=False)
    longitude = models.FloatField(null=True, blank=False)
    latitude = models.FloatField(null=True, blank=False)
    address = models.CharField(max_length=30, blank=False)
    img_file = models.ImageField(upload_to='Stations/', default='station.png')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        super(PolicePosts, self).save(*args, **kwargs)

        img = Image.open(self.img_file.path)

        if img.height > 500 and img.width > 500:
            output_size = (500, 500)
            img.thumbnail(output_size)
            img.save(self.img_file.path)

    class Meta:
        ordering = ['county', 'name']
        verbose_name_plural = 'Police stations'

class SuspectsRecords(models.Model):
    id = models.CharField(max_length=25, primary_key=True, unique=True, editable=False)
    name = models.CharField(max_length=70, blank=False)
    alias = models.CharField(max_length=30, blank=True)
    gender = models.CharField(max_length=7, blank=False)
    county_origin = models.CharField(max_length=50, blank=True)
    subcounty_origin = models.CharField(max_length=80, blank=True)
    constituency_origin = models.CharField(max_length=80, blank=True)
    location_origin = models.CharField(max_length=80, blank=True)
    suspect_dp = models.ImageField(upload_to='Suspects/Images/', default='default.png')
    bounty = models.PositiveIntegerField(default=0, blank=True)
    crime = models.CharField(max_length=50, blank=False)
    status = models.CharField(max_length=20, blank=False)
    last_seen_county = models.CharField(max_length=50, blank=True)
    last_seen_location = models.CharField(max_length=80, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        super(SuspectsRecords, self).save(*args, **kwargs)

        img_file = Image.open(self.suspect_dp.path)

        if img_file.height > 480 and img_file.width > 640:
            output_size = (480, 640)
            img_file.thumbnail(output_size)
            img_file.save(self.suspect_dp.path)
    
    class Meta:
        ordering = ['name', 'crime']
        verbose_name_plural = 'Suspects records'

