from django.shortcuts import render
from joblib import load
model= load('./savedmodels/model.joblib')
# Create your views here.
def forminfo(request): 
    if request.method == 'POST':
        Time_spent_Alone = float(request.POST.get('Time_spent_Alone', 0.0))
        Stage_fear = float(request.POST.get('Stage_fear', 0.0))
        Social_event_attendance = float(request.POST.get('Social_event_attendance', 0.0))
        Going_outside = float(request.POST.get('Going_outside', 0.0))
        Drained_after_socializing = float(request.POST.get('Drained_after_socializing', 0.0))
        Friends_circle_size = float(request.POST.get('Friends_circle_size', 0.0))
        Post_frequency = float(request.POST.get('Post_frequency', 0.0))
        Stage_fear = 1 if Stage_fear>5 else 0
        Drained_after_socializing = 1 if Drained_after_socializing>5 else 0

        y_pred = model.predict([[Time_spent_Alone, Stage_fear, Social_event_attendance, Going_outside, Drained_after_socializing, Friends_circle_size, Post_frequency]])
        if y_pred[0] == 0:
            y_pred = "Introvert"
        else:
            y_pred = "Extrovert"
      
        return render(request, 'index.html',{'result':y_pred})
    
    return render(request, 'index.html')