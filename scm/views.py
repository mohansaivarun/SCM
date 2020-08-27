from django.http import HttpResponse

def sample(res):
    add="<h2>For Address Book - type 'addressbk' at the suffix of URL</h2>"
    cs="<h2>For Contact Scroing - type 'cscore' at the suffix of URL</h2>"
    doc="<h2>For Document Management - type 'docmgmt' at the suffix of URL</h2>"
    frm="<h2>For Forms - type 'frms' at the suffix of URL</h2>"
    ci="<h2>For Contact Importing - type 'imprt' at the suffix of URL</h2>"
    meet="<h2>For Meeting - type 'meetings' at the suffix of URL</h2>"
    html="<html><h1>This is Starting Page</h1>"+add+cs+doc+frm+ci+meet+"</html>"
    return HttpResponse(html)