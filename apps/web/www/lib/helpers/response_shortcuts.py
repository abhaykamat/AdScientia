from django.template import RequestContext
from django.template.loader import render_to_string
from django.shortcuts import render_to_response
 	
def render_response(req, *args, **kwargs):
    kwargs['context_instance'] = RequestContext(req)
    return render_to_response(*args, **kwargs)

def render_string(req, *args, **kwargs):
    kwargs['context_instance'] = RequestContext(req)
    return render_to_string(*args, **kwargs)
