from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# The Condition For Seeing The Required Page Login
# @login_required(login_url="login/")
# View the dashboard Page
def dashboard(request):
    # Put the data to be displayed on the page in context
    context={}
    return render(request,'dashboard/dashboard.html', context)
#
#
#
# # The Condition For Seeing The Required Page Login
# @login_required(login_url="login/")
# View the about Page
@login_required(login_url='login/')
def about(request):
    context={}
    return render(request,'dashboard/about.html',context)