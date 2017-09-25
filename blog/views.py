from django.shortcuts import render, get_object_or_404
from django.shortcuts import HttpResponse
from django.utils import timezone
from .models import Post
from blog.models import Post
import datetime

# Create your views here.
def post_list(request):
    posts = Post.objects.all().order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
	# now = datetime.datetime.now()
	# html = "<html><body>It is now %s.</body></html>" % now
	# return HttpResponse(html)
		
def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post': post})	