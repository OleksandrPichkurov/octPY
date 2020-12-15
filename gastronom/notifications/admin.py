import logging

from django.contrib import admin
from django.conf import settings
from django.forms import TextInput, Textarea
from django.db import models

from telegram import Bot
from telegram.utils.request import Request
from telegram.error import InvalidToken

# from super_inlines.admin import SuperInlineModelAdmin, SuperModelAdmin

from gastronom.settings import CHAT_ID
from notifications.models import Notification, TelegramUser, TelegramIncomeMessage, TelegramReplyMessage
from notifications.tasks import send_telegram_task, send_methods, send_telegram_reply_task

logger = logging.getLogger(__name__)

try:
    request = Request(connect_timeout=0.5, read_timeout=1.0, con_pool_size=8)
    bot = Bot(request=request, token=settings.TOKEN, base_url=settings.PROXY_URL)
except InvalidToken: 
    request = None
    bot = None  


class NotificationAdmin(admin.ModelAdmin):
    model = Notification
    list_display = ('id', 'is_sent', 'sent_time', 'source', 'recipient', 'send_method', 'timestamp', 'subject', 'message')
    extra = 1
    # list_display_links = ['recipient']
    list_filter = ['is_sent', 'source', 'recipient', 'send_method', 'subject']
    autocomplete_fields = ['recipient']

    def send_notifications(self, request, queryset):
        for notification in queryset:
            send_func = send_methods[notification.send_method]
            try:
                send_func(notification.id)

            except Exception as e:
                logger.info(e)
                bot.send_message(chat_id=CHAT_ID, text=str(e))

    def make_unsent(self, request, queryset):
        for notification in queryset:
            notification.sent = False
            notification.save()

    actions = [send_notifications, make_unsent]


def send_reply(TelegramReplyMessageInlineAdmin, request, queryset):
    for reply_message in queryset:
        send_telegram_reply_task.delay(reply_message.id)



class TelegramReplyMessageInlineAdmin(admin.StackedInline): #SuperInlineModelAdmin):
    model = TelegramReplyMessage
    list_display = ('id', 'reply_message', 'reply_to_message')
    extra = 1
    actions = [send_reply]
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '20'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 1, 'cols': 100})},
    }


class TelegramReplyMessageAdmin(admin.ModelAdmin):
    model = TelegramReplyMessage
    list_display = ('id', 'is_sent', 'sent_time', 'reply_message', 'reply_to_message')
    actions = [send_reply]
    extra = 1



class TelegramIncomeMessageInlineAdmin(admin.StackedInline): # SuperInlineModelAdmin):
    model = TelegramIncomeMessage
    extra = 1
    list_display = ('telegramuser', 'id', 'date', 'message_id', 'chat_id', 'text')
    fields = ['telegramuser', 'text']
    inlines = (TelegramReplyMessageInlineAdmin,)
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '20'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 1, 'cols': 100})},
    }


class TelegramIncomeMessageAdmin(admin.ModelAdmin):
    model = TelegramIncomeMessage
    inlines = [TelegramReplyMessageInlineAdmin]
    list_display = ('telegramuser', 'text', 'id', 'date', 'message_id', 'chat_id')


class TelegramUserAdmin(admin.ModelAdmin):
    model = TelegramUser
    list_display = ('id', 'chat_id', 'username', 'user_phone')
    inlines = [TelegramIncomeMessageInlineAdmin]
    list_display_links = ('chat_id', 'username', 'user_phone')
    extra = 1
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '20'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 1, 'cols': 30})},
        }


admin.site.register(Notification, NotificationAdmin)
admin.site.register(TelegramUser, TelegramUserAdmin)
admin.site.register(TelegramIncomeMessage, TelegramIncomeMessageAdmin)
admin.site.register(TelegramReplyMessage, TelegramReplyMessageAdmin)
