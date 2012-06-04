from django.http import Http404

from adscientiawww.lib.helpers.response_shortcuts import render_response


def viewDegrees(request, degree):
    """Views the degrees page"""
    if degree not in ['mathematics', 'physics']:
        raise Http404
    else:
        return render_response(request, 'degrees/%s.html' % degree, {})
