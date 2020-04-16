from django.shortcuts import render
from .forms import SintomasForm
# Create your views here.
def sintomas(request):
    if request.method == "POST":
        form = SintomasForm(request.POST)
        if form.is_valid():
            try:
                return redirect('/')
            except:
                pass
    else:
            form = SintomasForm()
    return render(request,'sintomas/sintomas.html',{'form':form})
