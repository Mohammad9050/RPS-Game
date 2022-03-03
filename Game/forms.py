from django import forms


class ObjGameForm(forms.Form):
    CHOICES = [('rock', 'Rock'),
               ('scissor', 'Scissor'),
               ('paper', 'Paper')]
    opinion = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
