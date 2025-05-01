from django.shortcuts import render
from .models import Post
from django.http import HttpResponse
from django.db.models import Q
from django.urls import reverse_lazy

from django.views.generic import UpdateView, DeleteView



def postReader(request):
    posts = Post.objects.all().order_by('-id')
    return render(request, 'post.html', {'posts': posts})


# class postDetailView(DetailView):
#     model = Post
#     template_name = "post_detail.html"


def post_detail(request, pk):
    item = Post.objects.get(id=pk)
    return render(request, 'post_detail.html', {'post':item})


class PostUpdateView(UpdateView):
    model = Post
    template_name = "post_edit.html"
    fields = ['title', 'content']


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('posts')



# def postReader(request):
#     # posts = Post.objects.filter(Q(title__startswith='N') & Q(id__lte=1))
#     # posts = Post.objects.all().order_by('-publish')
#     # posts = Post.objects.all().order_by('title')
#     posts = Post.objects.all()[1:7]

#     # q1 = Post.objects.filter(Q(id=10))
#     # q2 = Post.objects.filter(Q(id=1))
#     # posts = q1.union(q2)

#     forign = Post.objects.select_related("author").get(id=1).author.name
#     print(forign)

#     # new = Post.objects.create(
#     #     title='Euro news', author=posts.author.name[0], content="On sndsd sdnabdabsd sdnmdabnvnsbdadejj dnma dwebdd asd nadmna djhhj  wdrf."
#     # )

#     # new = Post.objects.get(id=5)
#     # new.title = "Men ozgardim"

#     # e = Post.objects.get(id=21).delete() #Bu ham togri
#     # e = Post.objects.get(id=21)
#     # e.delete()

#     # new.save()

#     posts_list = ''
#     for post in posts:
#         posts_list += f"<li><strong>{post.title}</strong><br>{post.content}<br><em>{forign}</em></li>"

#     return HttpResponse(f"<ul>{posts_list}</ul>{forign}")


# def hello_world(request):
#     posts = Post.objects.all()
#     context = {
#         "posts": posts
#     }

#     return render(request, 'post.html', context)
























# from django.http import HttpResponse
# from .models import Post
# from django.db.models import Q

    # # posts = Post.objects.all()
    # # posts = Post.objects.filter(title__contains="oʻsimlik")
    # # posts = Post.objects.filter(title__startswith="a")
    # # posts = Post.objects.filter(title__startswith='N', content__contains='klassik')
    # # posts = Post.objects.filter(title__startswith="K", author__name='Omonulla')
    # # posts = Post.objects.filter(author__age__gt=30)
    # # posts = Post.objects.filter(author__age__lt=25)
    # # posts = Post.objects.filter(author__age__lte=29)
    # # posts = Post.objects.filter(author__age__gt=25)
    # # posts = Post.objects.filter(Q(title__startswith="N") & ~Q(author__name="Fitrat"))
    # # posts = Post.objects.filter(Q(title__startswith="N") | Q(titile__startswith="K"))
    # posts = Post.objects.filter(Q(title__startswith="G") & Q(author__age__lte=30))
    # posts_list = ''
    # for post in posts:
    #     posts_list += f"<strong>{post.title}</strong><br>{post.content}<br><i>{post.author}</i><hr>"
    
    # return HttpResponse(f"<ol>{posts_list}</ol>")

