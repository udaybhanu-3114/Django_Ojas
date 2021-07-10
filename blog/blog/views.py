from django.shortcuts import render

from django.http import HttpResponse


posts = [

		{
			'author':'Uday',
			'title':'Blog post1',
			'content':'First post content',
			'date_posted':'June 17,2021'
		},
		{
			'author':'Vijay',
			'title':'Blog post2',
			'content':'Second post content',
			'date_posted':'June 19,2021'
		}

]

def home(request):

	context = {
		'posts':posts
	}
	#return HttpResponse('<h1>Blog Home</h1>')

	return render(request,'blog/home.html',context)

def about(request):
	#return HttpResponse('<h1>Blog About</h1>')
	
	return render(request,'blog/about.html',{'title':'About'})

