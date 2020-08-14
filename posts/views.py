from django.shortcuts import render, redirect
from .models import Post, Like
from profiles.models import Profile
from .forms import PostModelForm
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required

@login_required(login_url='accounts:login')
def post_create_and_list_view(request):
    qset = Post.objects.all()
    profile = Profile.objects.get(user=request.user)

    p_form = PostModelForm(request.POST or None, request.FILES or None)
    post_added = False

    profile = Profile.objects.get(user=request.user)
    
    if p_form.is_valid():
        instance = p_form.save(commit=False)
        instance.author = profile
        instance.save()
        p_form = PostModelForm()
        post_added = True

    context = {
        'qset' : qset,
        'profile' : profile,
        'p_form' : p_form,
        'post_added' : post_added
    }

    return render(request, 'posts/main.html',context)

@login_required(login_url='accounts:login')
def like_unlike_post(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = Post.objects.get(id=post_id)
        profile = Profile.objects.get(user=user)

        if profile in post_obj.liked.all():
            post_obj.liked.remove(profile)
        else:
            post_obj.liked.add(profile)
        like, created = Like.objects.get_or_create(user=profile, post_id=post_id)

        if not created:
            if like.value=='Like':
                like.value='Unlike'
            else:
                like.value='Like'
        else:
            like.value='Like'
            post_obj.save()
            like.save()
    
    # return redirect('posts:main-post-view')
        return HttpResponse()

def post_serialized_view(request):
    data = list(Post.objects.values())
    return JsonResponse(data, safe=False)