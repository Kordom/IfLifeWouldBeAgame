from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    max_hp = models.IntegerField("Max Health",default=100)
    hp = models.IntegerField("Current Health",default=100)
    energy = models.IntegerField("Current Energy",default=100)
    max_energy = models.IntegerField("Max Energy",default=100)
    xp = models.IntegerField("Experience",default=0)

    def __str__(self):
        return f"Player with username: {self.user.username}"

    # TODO decide how to get attrs
    @property
    def get_attributes(self):
        return None

class PersonalAttributes(models.Model):
    player = models.OneToOneField(Player, on_delete=models.CASCADE)

    GENDER_CHOICE = [
        ("M", "Male"),
        ("F", "Female")
    ]

    age = models.IntegerField("Age",validators=[MaxValueValidator(70), MinValueValidator(10)])
    height = models.IntegerField("Height", validators=[MaxValueValidator(280), MinValueValidator(50)])
    weight = models.FloatField("Weight", validators=[MaxValueValidator(500.0), MinValueValidator(20.0)])
    gender = models.CharField("Gender",choices=GENDER_CHOICE)

    def __str__(self):
        return f"Personal Attributes of {self.player}"

    # TODO decide how to get attrs
    @property
    def get_attributes(self):
        return None

class PhysicalAttributes(models.Model):
    player = models.OneToOneField(Player, on_delete=models.CASCADE)

    daily_steps = models.IntegerField("Daily Steps", validators=[MaxValueValidator(30000), MinValueValidator(0)])
    sleep_hours = models.FloatField("Sleep Hours", validators=[MaxValueValidator(16.0), MinValueValidator(0)])
    exercise_per_week = models.IntegerField("Exercise per Week", validators=[MaxValueValidator(7), MinValueValidator(0)])
    water_intake = models.FloatField("Water Intake", validators=[MaxValueValidator(10.0), MinValueValidator(0)])

    def __str__(self):
        return f"Physical Attributes of {self.player}"

    # TODO decide how to get attrs
    @property
    def get_attributes(self):
        return None

class MentalAttributes(models.Model):
    player = models.OneToOneField(Player, on_delete=models.CASCADE)

    reading_time = models.FloatField("Reading Time Per Week", validators=[MaxValueValidator(30), MinValueValidator(0)])
    meditation_time = models.FloatField("Meditation Time Per Week", validators=[MaxValueValidator(20), MinValueValidator(0)])

    def __str__(self):
        return f"Mental Attributes of {self.player}"

    # TODO decide how to get attrs
    @property
    def get_attributes(self):
        return None

class PlayerStats(models.Model):
    player = models.OneToOneField(Player, on_delete=models.CASCADE)

    strength = models.IntegerField("Strenght", default=10)
    dexterity = models.IntegerField("Dexterity", default=10)
    vitality = models.IntegerField("Vitality", default=10)
    intelligence = models.IntegerField("Intelligence", default=10)
    charisma = models.IntegerField("Charisma", default=10)

    def __str__(self):
        return f"Stats for {self.player}"

    # TODO decide how to get attrs
    @property
    def get_attributes(self):
        return None