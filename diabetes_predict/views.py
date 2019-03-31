from django.shortcuts import render, redirect
from django.http import HttpResponse
from . forms import diabeticForms1, diabeticForms2
from diabetes_tracker.views import dashboard_index
import requests

# Create your views here.
def index(request):
    forms1 = diabeticForms1()

    if request.method == 'POST':
        form = diabeticForms1(request.POST)

        if form.is_valid() :
            age = form.cleaned_data['age']
            weight = form.cleaned_data['weight']
            height = form.cleaned_data['height']
            sex = form.cleaned_data['gender']
            bmi = weight*10000//height**2
            if bmi >= 26.0 and age >= 45.0 :
                return redirect(other5ques, sex = sex)
            else :
                return HttpResponse('Onto the exercise recommendations')

    return render(request, 'index.html', {'forms1': forms1})

def other5ques(request, sex):
    forms2 = diabeticForms2()
    if sex == 'False' :
        forms2 = diabeticForms2(enable_my_bool = False)

    if request.method == 'POST' :
        form = diabeticForms2(request.POST)
        if form.is_valid() :
            family_hist = form.cleaned_data['family_history']
            sedentary = form.cleaned_data['sedentary_lifestyle']
            hypertension = form.cleaned_data['hypertension']
            dyslipidemia = form.cleaned_data['dyslipidemia']
            if sex == 'True' :
                gestational_diabetes = form.cleaned_data['gestational_diabetes']
                if family_hist or sedentary or hypertension or dyslipidemia or gestational_diabetes:
                    return redirect(dashboard_index)
                else :
                    return HttpResponse('Onto the exercise recommendations')
            else:
                if family_hist or sedentary or hypertension or dyslipidemia :
                    return redirect(dashboard_index)
                else :
                    return HttpResponse('Onto the exercise recommendations')
    return render(request, 'diabetic_ques/diabetic_ques.html', {'forms2': forms2})
