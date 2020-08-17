from django import forms

from player.models import Player


class AddPlayerForm(forms.ModelForm):

    class Meta:
        model = Player
        fields = ('first_name', 'last_name', 'jersey_no',
                  'image', 'country', 'team')

    def __init__(self, *args, **kwargs):
        super(AddPlayerForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update(
            {'class': 'form-control', 'required': True})
        self.fields['last_name'].widget.attrs.update(
            {'class': 'form-control', 'required': True})
        self.fields['image'].widget.attrs.update(
            {'class': 'form-control', 'required': True})
        self.fields['country'].widget.attrs.update(
            {'class': 'form-control', 'required': True})
        self.fields['jersey_no'].widget.attrs.update(
            {'class': 'form-control', 'required': True})
        self.fields['team'].widget.attrs.update(
            {'class': 'form-control', 'required': True})
