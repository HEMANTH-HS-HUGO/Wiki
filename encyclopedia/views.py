from django.shortcuts import render
from django.http import HttpRequest
from . import util

import markdown
import random

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):

    if title in util.list_entries():
       
        html_page= markdown.markdown(util.get_entry(title))

        return render(request, "encyclopedia/entry.html",{
            "title" : title,
            "html_page" : html_page
        })
    else:
        return render(request,"encyclopedia/error.html",{
            "error_msg" : title + " not found"
        } )

def search(request):
    if request.method == "POST":  #is typically used to determine the HTTP method used in an incoming request
        searching_for = request.POST['q']  #appears to be an attempt to access POST data from an incoming request.
        all_entries = util.list_entries()
        sub_strings_list = []
        if util.get_entry(searching_for) is None:
            for entry in all_entries:
                    if searching_for.lower() in entry.lower():
                        sub_strings_list.append(entry)
            return render(request,"encyclopedia/search.html",{
                            "sub_strings_list" : sub_strings_list,
                            "searching_for" : searching_for
                            })
            
        else:
            entry_content = util.get_entry(searching_for)
            html_page= markdown.markdown(entry_content)
            if html_page is not None:
                return render(request, "encyclopedia/entry.html",{
                        "title" : searching_for,
                        "html_page" : html_page
                })
            
def create(request):
    if request.method == "GET": 
        return render(request, "encyclopedia/create.html")
    else:
        title = request.POST['title']
        content = request.POST['content']
        entries = util.list_entries()
        if title in entries:
            return render(request, "encyclopedia/error.html", {
                "error_msg" : title + ", This page is already exist"
            })
        else:
            util.save_entry(title, content)
            show_content = util.get_entry(title)
            html_page = markdown.markdown(show_content)
            return render(request, "encyclopedia/entry.html",{
                "title" : title,
                "html_page" : html_page
            })
        
def edit(request):
    if request.method =="POST":
        title = request.POST['title']
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit.html",{
                "title" : title,
                "content" : content
            })
    
def save_it(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        util.save_entry(title, content)
        show_content = util.get_entry(title)
        html_page = markdown.markdown(show_content)
        return render(request, "encyclopedia/entry.html",{
                "title" : title,
                "html_page" : html_page
            })
    
def random_page(request):
     entries = util.list_entries()
     random_page = random.choice(entries)
     random_content = util.get_entry(random_page)
     html_page = markdown.markdown(random_content)
     return render(request, "encyclopedia/entry.html",{
                "title" : random_page,
                "html_page" : html_page
            })