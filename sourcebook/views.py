from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, UpdateView, DeleteView, TemplateView
from .models import Book, Page, Source


@login_required
def index(request):
    """IndexView"""
    template_name = 'sourcebook/index.html'
    return render(request, template_name)


@login_required
def book(request, book):
    """book"""
    template_name = 'sourcebook/book_base.html'
    try:
        book_query = Book.objects.filter(id=book)
        for tmp in book_query:
            title = tmp.name
        page_query = Page.objects.filter(book_id=book)
    except:
        title = 'Book Error'
        page_query = 'Page Error'
    context = {
        'title':title,
        'page':page_query,
    }
    return render(request, template_name, context)


class PageView(LoginRequiredMixin, TemplateView):
    """page"""
    def __init__(self):
        self.template_name = 'sourcebook/page_base.html'
        self.context = {}


    def get(self, request, book, page):
        try:
            page_query = Page.objects.filter(id=page)
            for tmp in page_query:
                self.context['title'] = tmp.name
            self.context['source'] = Source.objects.filter(page_id=page)
            self.context['text'] = 'test'

        except:
            self.context['title'] = 'Page Error'
            self.context['source'] = 'Source Error'

        return render(request, self.template_name, self.context)

    def post(self, request, book, page):
        if request.method == 'POST':
            if 'BtnRgsBox' in request.POST:
                if request.POST.get('TxtComment') != "":
                    Source(page_id=page, text=request.POST.get('TxtComment'), text_flg=0).save()
            elif 'BtnRgsArea' in request.POST:
                if request.POST.get('TxtCode') != "":
                    Source(page_id=page, text=request.POST.get('TxtCode'), text_flg=1).save()

        return redirect('sourcebook:Page', book=book, page=page)


class SourceUpdateView(LoginRequiredMixin, TemplateView):
    """SourceのUpdateとDelete"""
    def __init__(self):
        self.template_name = 'sourcebook/source_update.html'
        self.context = {}

    def get(self, request, book, page, source):
        try:
            self.context['text'] = Source.objects.get(id=source)
        except:
            pass
        return render(request, self.template_name, self.context)

    def post(self, request, book, page, source):
        if request.method == 'POST':
            try:
                if 'BtnUpdate' in request.POST:
                    if request.POST.get('TxtSource') != "":
                        Source.objects.filter(id=source).update(text=request.POST.get('TxtSource')).save()

                elif 'BtnDelete' in request.POST:
                    # ここで削除についてYesNoチェック
                    Source.objects.filter(id=source).delete().save()

                elif 'BtnBack' in request.POST:
                    return redirect('sourcebook:Page', book=book, page=page)
            except:
                # 更新できませんでしたのメッセージ
                pass

        return redirect('sourcebook:Page', book=book, page=page)
        

# Create your views here.
