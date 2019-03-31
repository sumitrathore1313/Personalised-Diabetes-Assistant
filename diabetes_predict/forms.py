from django import forms

class diabeticForms1(forms.Form):
    GENDER_CHOICES = [(False, 'MALE'), (True, 'FEMALE')]
    age = forms.IntegerField()
    weight = forms.IntegerField(label="Weight (KG)")
    height = forms.IntegerField(label="Height (CM)")
    gender = forms.ChoiceField(choices = GENDER_CHOICES, widget=forms.RadioSelect)

class diabeticForms2(forms.Form):

    FAMILY_HISTORY_CHOICE = [(True, 'Yes'), (False, 'No')]
    SEDENTARY_LIFESTYLE = [(True, 'Yes'), (False, 'No')]
    GESTATIONAL_CHOICES = [(True, 'Yes'), (False, 'No')]
    HYPERTENSION = [(True, 'Yes'), (False, 'No')]
    DYSLIPIDEMIA = [(True, 'Yes'), (False, 'No')]

    family_history = forms.BooleanField(required=False, label="My first degree relative has diabetes")
    sedentary_lifestyle = forms.BooleanField(required=False, label="My level of physical activity can be called sedentary")
    gestational_diabetes = forms.BooleanField(required=False, label="I have been diagnosed with diabetes during pregnancy")
    hypertension = forms.BooleanField(required=False, label="I have hypertension")
    dyslipidemia = forms.BooleanField(required=False, label="I have high blood cholestrol")

    def __init__(self, *args, **kwargs):
        enable_my_bool = kwargs.pop('enable_my_bool', True) # True is the default
        super(diabeticForms2, self).__init__(*args, **kwargs)
        if not enable_my_bool:
            self.fields.pop('gestational_diabetes')




