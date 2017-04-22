from datetimewidget.widgets import DateTimeWidget, DateWidget, TimeWidget
from django import forms
from django.contrib.auth.models import User
from django.db import models
from django_select2.forms import ModelSelect2MultipleWidget

from profile_manager.models import Profile
from .models import Badge, BadgeAssertion


def make_custom_datetimefield(f):
    formfield = f.formfield()
    dateTimeOptions = {
        'showMeridian': False,
        # 'todayBtn': True,
        'todayHighlight': True,
        'minuteStep': 5,
        'pickerPosition': 'bottom-left',
    }

    if isinstance(f, models.DateTimeField):
        formfield.widget = DateTimeWidget(usel10n=True, options=dateTimeOptions, bootstrap_version=3)
    elif isinstance(f, models.DateField):
        formfield.widget = DateWidget(usel10n=True, options=dateTimeOptions, bootstrap_version=3)
        # formfield.widget = SelectDateWidget()
    elif isinstance(f, models.TimeField):
        formfield.widget = TimeWidget(usel10n=True, options=dateTimeOptions, bootstrap_version=3)

    return formfield


class BadgeForm(forms.ModelForm):
    formfield_callback = make_custom_datetimefield

    class Meta:
        model = Badge
        fields = '__all__'
        # exclude = None


class BadgeAssertionForm(forms.ModelForm):
    class Meta:
        model = BadgeAssertion
        # fields = '__all__'
        exclude = ['ordinal', 'issued_by', 'semester']

    def __init__(self, *args, **kwds):
        super(BadgeAssertionForm, self).__init__(*args, **kwds)
        self.fields['user'].queryset = User.objects.order_by('profile__first_name', 'username')
        self.fields['user'].label_from_instance = lambda obj: "%s (%s)" % (obj.profile, obj.username)


class StudentsCustomTitleWidget(ModelSelect2MultipleWidget):
    model = Profile
    # queryset = Profile.objects.all()
    search_fields = [
        'first_name__istartswith',
        'last_name__istartswith',
        'preferred_name__istartswith',
    ]

    # SHOULD BE USING USER NOT PROFILE!
    # model = User
    # search_fields = [
    #     'first_name__istartswith',
    #     'last_name__istartswith',
    #     'username__istartswith',
    # ]
    #
    # def label_from_instance(self, obj):
    #     return obj.get_full_name().upper()


class BulkBadgeAssertionForm(forms.Form):
    badge = forms.ModelChoiceField(queryset=Badge.objects.all_manually_granted(),
                                   required=True)
    students = forms.ModelMultipleChoiceField(queryset=Profile.objects.all(),
                                              widget=StudentsCustomTitleWidget())
