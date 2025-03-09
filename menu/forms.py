from django import forms


class RatingForm(forms.Form):
    STAR_CHOICES = [
        (1, "1 звезда"),
        (2, "2 звезды"),
        (3, "3 звезды"),
        (4, "4 звезды"),
        (5, "5 звезд"),
    ]

    stars = forms.ChoiceField(
        choices=STAR_CHOICES,
        widget=forms.RadioSelect,
        label="Оцените фильм"
    )