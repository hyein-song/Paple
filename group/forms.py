from django import forms
from account.models import Group


class ModifyGroupInfoForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['group_img', 'group_name', 'group_link']
        labels = {
            'group_name': 'Group Name',
            'group_link': 'Group Code',
            'group_img': 'Group Image'
        }
        widgets = {
            'group_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'group_link': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'readonly': True
                }
            )
        }


