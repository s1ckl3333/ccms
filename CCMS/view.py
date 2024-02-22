from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, World!")

def mission(request):
    msg="The College of Computing and Multimedia Studies shall produce competent and \
        innovative professionals or Technopreneurs in the Information and Communication \
            Technology (ICT) industry adequately prepared in the practice of their profession\
                  supportive of national development goals and standards of global excellence.\
    <h1/>"
    return HttpResponse(msg)

def vission(request):
    msg="<h1>Name: Jethro D. Labitigan<br>\
        Email: jetjetlabitigan@gmail.com\
    <h1/>"
    return HttpResponse(msg)

def objectives(request):
    msg="<h1>Name: Jethro D. Labitigan<br>\
        Email: jetjetlabitigan@gmail.com\
    <h1/>"
    return HttpResponse(msg)