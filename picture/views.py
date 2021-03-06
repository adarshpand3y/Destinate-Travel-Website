from django.shortcuts import render
from .models import *
import datetime
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage


# Create your views here.
def index(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        title = request.POST.get('title')
        message = request.POST.get('message')
        review = Review(firstname=firstname, lastname=lastname, email=email, title=title, message=message, datetime=datetime.datetime.now()) 
        review.save()
        messages.success(request, 'Your review has been submitted successfully!')
    top_three_posts = Post.objects.all().order_by('-views')[0:3]
    recent_three_reviews = Review.objects.all().order_by('-datetime')[0:4]
    context = {'recentReviews': recent_three_reviews, 'topPosts': top_three_posts}
    return render(request, 'index.html', context)

def images(request):
    page_num = request.GET.get('page', 1)
    allPosts = Post.objects.all().order_by('-pub_date')
    p = Paginator(allPosts, 9)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)
    context = {'Post': page, 'this_page_num': page_num, 'num_of_pages': p.num_pages}
    return render(request, 'images.html', context)

def image(request, pk):
    post = Post.objects.get(id=pk)
    post.views = post.views + 1
    post.save()
    context = {'post': post}
    return render(request, 'image.html', context)

def team(request):
    members = TeamMember.objects.all()
    context = {'members': members}
    return render(request, 'team.html', context)

def contact(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = Contact(firstname=firstname, lastname=lastname, email=email, message=message, datetime=datetime.datetime.now()) 
        contact.save()
        messages.success(request, 'Your contact form has been submitted successfully!')
    return render(request, 'contact.html')

def member(request, mem_id):
    team_member = TeamMember.objects.get(id=mem_id)
    context = {'member': team_member}
    return render(request, 'member.html', context)

def search(request):
    allPosts = Post.objects.none()
    query = request.GET['query']
    search_filter = request.GET['dropdown']
    if len(query)<50:
        if search_filter == 'All Posts':
            allPosts = allPosts.union(Post.objects.filter(picture_name__icontains=query), Post.objects.filter(description__icontains=query), Post.objects.filter(location__icontains=query), Post.objects.filter(area__icontains=query), Post.objects.filter(city__icontains=query), Post.objects.filter(state__icontains=query), Post.objects.filter(posted_by__icontains=query))
        elif search_filter == 'Post by a Member':
            allPosts = allPosts.union(Post.objects.filter(posted_by__icontains=query))
        elif search_filter == 'Picture Title':
            allPosts = allPosts.union(Post.objects.filter(picture_name__icontains=query))
        elif search_filter == 'Picture Description':
            allPosts = allPosts.union(Post.objects.filter(description__icontains=query))
        elif search_filter == 'Location':
            allPosts = allPosts.union(Post.objects.filter(location__icontains=query))
        elif search_filter == 'Area':
            allPosts = allPosts.union(Post.objects.filter(area__icontains=query))
        elif search_filter == 'City':
            allPosts = allPosts.union(Post.objects.filter(city__icontains=query))
        elif search_filter == 'State':
            allPosts = allPosts.union(Post.objects.filter(state__icontains=query))
        allPosts = allPosts.order_by('-pub_date')
    if allPosts.count() == 0:
        messages.error(request, 'No results found.')
    context = {'allPosts': allPosts, 'query': query}
    return render(request, 'search.html', context)