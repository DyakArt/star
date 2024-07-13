from django import forms
import re


class JobResponseForm(forms.Form):
    job_title = forms.CharField()
    full_name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    phone = forms.CharField(max_length=12)
    accept_policy = forms.BooleanField(
        error_messages={'required': 'Необходимо согласиться с политикой конфиденциальности.'})

    def clean_full_name(self):
        full_name = self.cleaned_data['full_name']
        if not re.match(r'^[А-Яа-яЁё\s]+$', full_name):
            raise forms.ValidationError("ФИО должно содержать только русские буквы и пробелы.")
        return full_name

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if not re.match(r'^(\+7\d{10}|8\d{10}|[0-9]{2}-[0-9]{2})$', phone):
            raise forms.ValidationError("Введите корректный номер телефона.")
        return phone
