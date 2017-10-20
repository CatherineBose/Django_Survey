from django.shortcuts import render, HttpResponse, redirect

# the index function is called when root is visited
def index(request):
    if not 'count'in request.session:
        request.session['count'] = 0
    return render (request, "survey1/index.html")

def process(request):
    if request.method == "POST":
        request.session['name'] = request.POST['name'],
        request.session['location'] = request.POST['location'],
        request.session['language'] =  request.POST['language'],
        request.session['comment'] = request.POST['comment'],
    if "count" in request.session:
        request.session['count'] += 1
    return redirect("/result")

def result(request):
    return render(request, "survey1/result.html")