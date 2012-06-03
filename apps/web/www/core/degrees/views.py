from adscientiawww.lib.helpers.response_shortcuts import render_response


def viewDegrees(request):
    """Views the degrees page"""  
    return render_response(request, 'degrees/degree.html', {})
