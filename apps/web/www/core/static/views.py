from adscientiawww.lib.helpers.response_shortcuts import render_response


def view_about(request):
    """Views the about page"""
    return render_response(request, 'static/about.html', {})
