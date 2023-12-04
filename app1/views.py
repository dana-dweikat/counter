from django.shortcuts import render,redirect

# Create your views here.
def root(request):
    if "counter" not in request.session:
        request.session["counter"] = 0
    request.session['counter'] = request.session['counter']+1 
    request.session.save()   




    # if "counter" in request.session:
    #     request.session['counter'] = request.session['counter']+1
    # else :    
    #     request.session['counter'] = 0
    #     request.session['counter'] = request.session['counter']+1
    # request.session.save()

    return render (request,"index.html")


def destroy_session(request):
    del request.session['counter']
    return redirect("/")