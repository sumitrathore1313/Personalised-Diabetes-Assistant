from django.shortcuts import render
from .forms import Entry
from .models import Glucose
# Create your views here.
from Predict import pred, getVector

def dashboard_index(request):
    form = Entry()
    top_n_rec = Glucose.objects.all()
    print(top_n_rec)
    insulin = ' '
    calories = ' '
    if Glucose.objects.all():
        gluc = Glucose.objects.all().latest('datetime')
        data = {"glucose": gluc.glucose, "sleep": gluc.sleep, "weight": gluc.weight,
                "excersize": gluc.duration_of_exercise}
        insulin = pred(getVector(data))
        calories = insulin // 2 + 5
        current_glucose = gluc.glucose
    else:
        current_glucose = ""
    context_dict = {'form':form, 'log':top_n_rec, 'insulin':insulin, 'calories':calories, 'gluc':current_glucose}
    if request.method == "POST" :
        form = Entry(request.POST)

        if form.is_valid() :
            gluc = form.save(commit=True)
            print(gluc)
            data = {"glucose": gluc.glucose, "sleep": gluc.sleep, "weight": gluc.weight, "excersize": gluc.duration_of_exercise}
            insulin = pred(getVector(data))
            calories = insulin//2 + 5
            current_glucose = gluc.glucose
            # pred_ins, pred_cal = useNeuralNet(latest_entry)
    
    return render(request, 'diabetes_tracker/dashboard.html', {'form':form, 'log':top_n_rec, 'insulin':insulin, 'calories':calories, 'gluc':current_glucose})




