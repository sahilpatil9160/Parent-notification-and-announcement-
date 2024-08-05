from django import forms
from .models import StuModel,MaModel

class StuForm(forms.ModelForm):
	class Meta:
		model = StuModel
		fields = '__all__'
		
		labels = {
				'Rno': ('Roll No'),
				'Name': ('Student Name'),
				'Email_Id': ('Parents Email Id'),
				'Phone': ('Mobile No'),
			}

		widgets = {
				'Rno':forms.Textarea(attrs={"rows":2,"cols":50,"style":'resize:none','placeholder':'Enter Roll NO'}),

				'Name':forms.Textarea(attrs={"rows":2,"cols":50,"style":'resize:none','placeholder':'eg. First Name Last Name'}),


				'Email_Id':forms.Textarea(attrs={"rows":2,"cols":50,"style":'resize:none','placeholder':'Enter Parents Email ID'}),

				'Phone':forms.Textarea(attrs={"rows":2,"cols":50,"style":'resize:none','placeholder':'Enter Parents Mobile No'}),


				'Department':forms.Textarea(attrs={"rows":2,"cols":50,"style":'resize:none','placeholder':'eg. CO/AIDS/CSD'}),


				'Semester':forms.Textarea(attrs={"rows":2,"cols":50,"style":'resize:none','placeholder':'Enter Semester'}),


				'Division':forms.Textarea(attrs={"rows":2,"cols":50,"style":'resize:none','placeholder':'eg.A/B/C'})
			}



class MaForm(forms.ModelForm):
	class Meta:
		model = MaModel
		fields = '__all__'