from django import forms
import datetime

from django.utils import formats



def widget_attrs(placeholder):
    return {'class': 'form-group input-lg', 'placeholder': placeholder}


def form_kwargs(widget, label='', max_length=128):
    return {'widget': widget, 'label': label, 'max_length': max_length}


class TodoForm(forms.Form):
    title = forms.CharField(
        **form_kwargs(
            widget=forms.TextInput(attrs=widget_attrs('to do title'))
        )
    )
    description = forms.CharField(
        **form_kwargs(
            widget=forms.TextInput(attrs=widget_attrs('to do description'))
        )
    )



class TodoListForm(forms.Form):
    title = forms.CharField(
        **form_kwargs(
            widget=forms.TextInput(
                attrs=widget_attrs('To Do List Title')
            )
        )
    )
