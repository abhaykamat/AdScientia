from adscientiawww.lib.helpers.response_shortcuts import render_response


def viewHome(request):
    """Views the home page"""  
    return render_response(request, 'home/home.html', {})
