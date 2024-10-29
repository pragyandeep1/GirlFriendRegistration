from django.shortcuts import render
from testapp.forms import NameForm
from testapp.forms import AgeForm
from testapp.forms import GfForm

# Create your views here.
def name_view(request):
    form = NameForm()
    return render(request,'testapp/name.html',{'form':form})

def age_view(request):
    name = request.GET['name']
    request.session['name'] = name
    form = AgeForm()
    return render(request,'testapp/age.html',{'form':form,'name':name})

def gf_view(request):
    name = request.session['name']
    age = request.GET['age']
    request.session['age'] = age
    form = GfForm()
    return render(request, 'testapp/gf.html', {'form': form, 'name': name})

def results_view(request):
    gf = request.GET['gf']
    request.session['gf'] = gf
    name = request.session['name']
    age = request.session['age']
    return render(request,'testapp/results.html')