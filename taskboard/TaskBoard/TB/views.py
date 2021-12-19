from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Article, Response
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ArticleForm, ResponseForm, DecisionForm
from .filters import ResponseFilter
from .tasks import send_notification
from django.shortcuts import redirect


class ArticleList(ListView):
    model = Article
    template_name = 'articles.html'
    context_object_name = 'articles'
    ordering = ['-id']
    paginate_by = 10


class ArticleCreateView(LoginRequiredMixin, CreateView):
    template_name = 'article_create.html'
    form_class = ArticleForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(ArticleCreateView, self).form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'article_create.html'
    form_class = ArticleForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Article.objects.get(pk=id)



class ArticleDetail(LoginRequiredMixin, DetailView):
    model = Article
    template_name = 'article_detail.html'
    context_object_name = 'article'
    queryset = Article.objects.all()

    def get_object(self, *args, **kwargs):
        id = self.kwargs.get('pk')
        obj = Article.objects.get(pk=id)

        return obj

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        id = self.kwargs.get('pk')
        self.request.session['my_article_id'] = id
        obj = Article.objects.get(pk=id)
        author = obj.author
        user = self.request.user
        is_owner = author == user

        context['owner'] = is_owner
        return context


class ArticleDeleteView(LoginRequiredMixin, DeleteView):

    template_name = 'article_delete.html'
    queryset = Article.objects.all()
    success_url = '/articles/'


class ResponseCreateView(LoginRequiredMixin, CreateView):
    template_name = 'response_create.html'
    form_class = ResponseForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        id = self.request.session.get('my_article_id')
        article = Article.objects.get(pk=id)
        form.instance.article = article
        return super(ResponseCreateView, self).form_valid(form)

    def post(self, request):
        super(ResponseCreateView, self).post(request)
        response = self.object
        send_notification(response.pk)

        return redirect('articles')

    def get_success_url(self):
        return '/articles/'


class ResponseUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'article_create.html'
    form_class = DecisionForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Response.objects.get(pk=id)

    def get_success_url(self):
        return '/articles/responses'



class ResponseList(LoginRequiredMixin, ListView):
    model = Response
    template_name = 'responses.html'
    context_object_name = 'responses'
    ordering = ['-id']
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ResponseFilter(self.request.GET, queryset=self.get_queryset())
        context['my_user'] = self.request.user
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return ResponseFilter(self.request.GET, queryset=queryset).qs

