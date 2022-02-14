from django import forms
from .models import task

class TaskForm(forms.Form):
	title= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'タイトル'}), label=False)
	due= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'何時までに！？'}), label=False)

	class Meta:
		model = task
		fields = ['title', 'due']


class UpdateForm(forms.ModelForm):
	title= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'タイトル'}))

	class Meta:
		model = task
		fields = ['title', 'due', 'complete']