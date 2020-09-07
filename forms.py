from .models import ExtraInfo
from django.forms import ModelForm

class ExtraInfoForm(ModelForm):
    """
    The fields on this form are derived from the ExtraInfo model in models.py.
    """
    def __init__(self, *args, **kwargs):
        super(ExtraInfoForm, self).__init__(*args, **kwargs)
 
        self.fields['branch'].error_messages = {
            "required": u"Please enter your branch.",
            #"invalid": u"Sorry, you may have entered a non-existent branch.",
        }
        
        self.fields['enrollment_year'].error_messages = {
            "required": u"Enter your year of joining.",
            #"invalid": u"Sorry, you may have entered an invalid year.",
        }

       self.fields['preferred_lang'].error_messages = {
            "required": u"Your preferred medium of language.",
            #"invalid": u"Sorry, you may have entered a non-existent language",
        }

        self.fields['preferred_multimedia'].error_messages = {
            "required": u"Your preferred medium of learning.",
            #"invalid": u"Sorry, you may have a non-existent medium.",
        }
       
        self.fields['interests'].error_messages = {
            "required": u"Please enter your areas of interests.",
            #"invalid": u"Sorry, you may have a non-existent medium.",
        }

    class Meta(object):
        model = ExtraInfo
        fields = ('branch', 'enrollment_year', 'preferred_lang', 'preferred_multimedia', 'interests')

