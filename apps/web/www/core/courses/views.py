from django.http import Http404

from adscientiawww.lib.helpers.response_shortcuts import render_response


def view_course(request, degree, course):
    """Views the courses page"""
    if (degree not in ['biochemistry', 'mathematics', 'physics'] and
        course not in ['analysis_i', 'vector_analysis_i']):
        raise Http404
    else:
        return render_response(request, 'courses/%s/%s/index.html' % (degree, course), {})

def view_course_chapter(request, degree, course, chapter):
    """Views the courses page"""
    return render_response(request, 'courses/%s/%s/%s.html' % (degree, course, chapter), {})
