from django.db import models

from uuid import uuid4

class ControlProfile(models.Model):

    class Temperatures(models.TextChoices):
        SIXTEEN = '16'
        SEVENTEEN = '17'
        EIGHTEEN = '18'
        NINETEEN = '19'
        TWENTY = '20'
        TWENTY_ONE = '21'
        TWENTY_TWO = '22'
        TWENTY_THREE = '23'
        TWENTY_FOUR = '24'
        TWENTY_FIVE = '25'
        TWENTY_SIX = '26'
        TWENTY_SEVEN = '27'
        TWENTY_EIGHT = '28'
        TWENTY_NINE = '29'
        THIRTY = '30'

    class Modes(models.TextChoices):
        AUTO = "Auto"
        COOL = "Cool"
        DRY = "Dry"
        FAN = "Fan"
        #HEAT

    class Options(models.TextChoices):
        TWO_STEP = '2-Step'
        FAST = 'Fast'
        CONFORT = 'Confort'
        SINGLE_USER = 'Single User'
        QUIET = 'Quiet'
        DLIGHT_COOL = "D'light Cool"
        VIRUS_DOCTOR = 'Virus Doctor'

    class Settings(models.TextChoices):
        USAGE = 'Usage'
        CLEAN = 'Clean'
        BEEP = 'Beep'
        FILTER_RESET = 'Filter Reset'


    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    temperature = models.CharField(max_length=2,
            choices=Temperatures.choices,
            default=Temperatures.TWENTY_FIVE)
    mode = models.CharField(max_length=4,
            choices=Modes.choices,
            default=Modes.COOL)
    option = models.CharField(max_length=12,
            choices=Options.choices,
            default=Options.QUIET)
    swing = models.BooleanField(default=False)
    #is_active = models.BooleanField(default=False)
   # settings = models.CharField(max_length=12,
   #         choices=Settings.choices)

    def is_upperclass(self):
        return self.temperature in {
                self.Temperatures.SIXTEEN,
                self.Temperatures.THIRTY
        }

    def __str__(self):
        swing = 'SwingOn' if self.swing else 'SwingOff'
        control_profile_name = f"{self.mode.lower()}\
                {self.option.capitalize()}\
                {self.temperature.capitalize()}\
                {swing}".split()
        control_profile_name = "".join(control_profile_name)

        return str(control_profile_name)

    class Meta:
        unique_together = ['temperature', 'mode', 'option', 'swing']

#TODO: Store the profilename when creating the object or
# return the profilename on the restapi as a custom field???
