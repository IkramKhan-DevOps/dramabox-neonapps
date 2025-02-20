from django import forms
from src.services.drama.models import Tag, Language, Category, Season, Episode, Actor


class DramaSeriesTagForm(forms.Form):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Select Tags to Link"
    )


class DramaSeriesLanguageForm(forms.Form):
    languages = forms.ModelMultipleChoiceField(
        queryset=Language.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Select Languages to Link"
    )


class DramaSeriesCategoryForm(forms.Form):
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        help_text="Select categories to link to this drama series."
    )



class DramaSeriesCastForm(forms.Form):
    actors = forms.ModelMultipleChoiceField(
        queryset=Actor.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        help_text="Select actors to add to the cast."
    )

class SeasonForm(forms.ModelForm):
    release_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        help_text="Select the release date of this season."
    )

    class Meta:
        model = Season
        fields = ['season_number', 'release_date', 'description']


class EpisodeForm(forms.ModelForm):
    release_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        help_text="Select the release date of this episode."
    )

    class Meta:
        model = Episode
        fields = ['title', 'description', 'episode_number', 'release_date',
                  'duration', 'is_free','is_active'
                  ]
