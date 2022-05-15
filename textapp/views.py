from django.shortcuts import render
from .forms import EditorForm

def main(request):
    form=EditorForm()
    context={'form':form}
    return render(request,'textapp/index.html',context)


