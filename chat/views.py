from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


def home(request):
	# return HttpResponse("Chat Home")
	return render(request, 'chat_home.html')



def showchatpage(request, room_name, person_name):
	return render(request, 'chat_screen.html', {'room_name':room_name, 'person_name':person_name})
	# return HttpResponse("Chat page " +room_name+" "+ person_name)