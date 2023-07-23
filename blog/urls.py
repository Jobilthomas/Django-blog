from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.startingPageView.as_view(), name="starting-page"),
    path("posts", views.allPostView.as_view(), name="posts-page"),
    path("read-later", views.readLaterView.as_view(), name="read-later"),
    path("posts/<slug:slug>", views.postDetailView.as_view(), name="post-detail-page")
] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
