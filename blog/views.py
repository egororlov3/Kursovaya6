from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import ListView, DetailView
from blog.models import BlogPost


@method_decorator(cache_page(60 * 5), name='dispatch')
class BlogListView(LoginRequiredMixin, ListView):
    model = BlogPost
    template_name = 'blog/blog_list.html'
    context_object_name = 'blogs'


class BlogDetailView(LoginRequiredMixin, DetailView):
    model = BlogPost
    template_name = 'blog/blog_detail.html'
    context_object_name = 'blog'

    def get(self, request, *args, **kwargs):
        blog = self.get_object()
        blog.views += 1
        blog.save()

        return super().get(request, *args, **kwargs)
