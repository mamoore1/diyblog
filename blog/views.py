import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic

from blog.models import Blogger, BlogPost, Comment
from blog.forms import NewCommentForm

# Create your views here.
def home(request):
    """View function for home page of site"""
    num_bloggers = Blogger.objects.count()
    num_blogposts = BlogPost.objects.count()
    num_comments = Comment.objects.count()

    context = {
        'num_bloggers': num_bloggers,
        'num_blogposts': num_blogposts,
        'num_comments': num_comments,
    }

    return render(request, 'home.html', context=context)


class BlogPostListView(generic.ListView):
    model = BlogPost
    paginate_by = 5
    queryset = BlogPost.objects.all().order_by('-post_date')


class BloggerListView(generic.ListView):
    model = Blogger
    paginate_by = 5
    queryset = Blogger.objects.all().order_by('username')


class BlogPostDetailView(generic.DetailView):
    model = BlogPost


class BloggerDetailView(generic.DetailView):
    model = Blogger


@login_required
def blogpost_add_comment(request, pk):
    blogpost = get_object_or_404(BlogPost, pk=pk)

    # If this is a POST request, process the Form data
    if request.method == 'POST':
        form = NewCommentForm(request.POST)
        if form.is_valid():
            blogpost.comment_set.create(blogpost=blogpost, post_time=datetime.datetime.now(),
                                        commenter=request.user, text=form.cleaned_data['comment_text'])
            return HttpResponseRedirect(reverse('blogpost-detail', kwargs={'pk': pk}))
    else:
        form = NewCommentForm()

    context = {
        'form': form,
        'blogpost': blogpost,
    }

    return render(request, 'blog/add_comment.html', context)