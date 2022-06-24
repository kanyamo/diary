from django.shortcuts import render
from django.views import generic
from .forms import InquiryForm
import logging
from django.urls import reverse_lazy
from django.contrib import messages

logger = logging.getLogger(__name__)  # ロガーを取得


class IndexView(generic.TemplateView):
    template_name = "index.html"


class InquiryView(generic.FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm
    success_url = reverse_lazy('diary:inquiry')

    def form_valid(self, form):
        form.send_email()  # メール送信メソッドを取得
        messages.success(self.request, 'メッセージを送信しました。')
        logger.info('Inquiry sent by {}'.format(
            form.cleaned_data['name']))  # ログを出力
        return super().form_valid(form)
