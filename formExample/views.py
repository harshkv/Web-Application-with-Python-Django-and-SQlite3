from django.shortcuts import render
from formExample.forms import FormExample

# Create your views here.
# def formexample(request):
#     print(request.method)
#     print(request.GET)
#     form =FormExample()
#     dl = {
#         'form':form
#     }
#     return render(request,'form_example.html',dl)




def formexample(request):
    form =FormExample()
    if request.method == 'POST':
        form = FormExample(request.POST)
        if form.is_valid():
            pass
    dl = {
        'form':form
    }
    return render(request,'form_example.html',dl)
