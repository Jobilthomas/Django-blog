from django.shortcuts import render
from .models import Post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .forms import commentForm
from django.views import View
from django.http import HttpResponseRedirect, HttpResponse,JsonResponse
from django.urls import reverse

# Create your views here.

class startingPageView(ListView):
     model = Post
     template_name = "blog/index.html"
     context_object_name = "posts"
     
     def get_queryset(self):
         qs = super().get_queryset()
         qs = qs.order_by("-pk")[:3]
         return qs
     


'''def starting_page(request):
     posts = Post.objects.all()
     return render(request, "blog/index.html", {
          "posts": posts
     })'''
     
class allPostView(ListView):
     model = Post
     ordering = ["-pk"]
     context_object_name = "posts"
     template_name = "blog/all_post.html"
  
  
class postDetailView(View):
     
     def is_stored_post(self, request, post_id):
          stored_posts = request.session.get("stored_posts")
          if stored_posts is not None:
               is_saved_for_later = post_id in stored_posts
          else:
               is_saved_for_later = False
          return is_saved_for_later
     
     def get(self, request, slug):
          post = Post.objects.get(slug=slug)
          form = commentForm()
          return render(request, "blog/post_detail.html", {
               "post": post,
               "form": form,
               "comments": post.comments.all().order_by("-id"),
               "saved_for_later": self.is_stored_post(request, post.id)
          })
          
     def post(self, request, slug):
          post = Post.objects.get(slug=slug)
          form = commentForm(request.POST)
          if form.is_valid():
               comment = form.save(commit=False)
               comment.post = post
               comment.save()
               comment_text = comment.comment
               comment_name = comment.user_name
               return JsonResponse({
                    "comment_text": comment_text,
                    "comment_name": comment_name
               })
               #return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))
          else:
               errors = form.errors.as_json()
               return JsonResponse({
                    'errors': errors
               }, status=400)
          

class readLaterView(View):
     def get(self, request):
          stored_posts = request.session.get("stored_posts")
          context = {}
          if stored_posts is None or len(stored_posts) == 0:
               context["posts"] = []
               context["there_is_stored_posts"] = False
          else:
               posts = Post.objects.filter(id__in=stored_posts)
               context["posts"] = posts
               context["there_is_stored_posts"] = True
          return render(request, "blog/read_later.html", context)


     def post(self, request):
          post_id = int(request.POST["post_id"])
          stored_posts = request.session.get("stored_posts")
          if stored_posts is None:
               stored_posts = []
          if post_id not in stored_posts:
               stored_posts.append(post_id)
          else:
               stored_posts.remove(post_id)
          request.session["stored_posts"] = stored_posts
          return HttpResponseRedirect("/")
                        
     
     

'''class postDetailView(DetailView):
     model = Post
     template_name = "blog/post_detail.html"
     context_object_name = "post"'''

 
def posts(request):
     pass
 
def post_detail(request):
     pass
 
