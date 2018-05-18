from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return render(request,'main/index.html')

def postsApi(request, postId = None):
	if request.method == 'GET':
		if(postId == None):
			return "GET ALL"
		else:
			return postId
	elif request.method == "POST":
		return "Create POST"
	else:
		return "Delete POST"
