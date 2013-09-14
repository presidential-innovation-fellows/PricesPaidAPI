# This should actually be renamed so that it is not confused
# with the file of the same name in PricesPaidGUI
from bottle import Bottle, run, template,request,TEMPLATE_PATH,static_file

from SearchApi import searchApiSolr

from ppApiConfig import PathToDataFiles,URLToSolr

app = Bottle()

import auth

def convertPSCToLegalPattern(str):
    if (str is None) or (str == 'None') or (str == ''):
        return '*';
    else:
        return str;

# this needs to be improved, but basically,
# we don't want them to do a blank search.
# it could be prevented at the GUI layer as well.
def convertSearchStringToLegalPattern(str):
    if (str is None) or (str == 'None') or (str == ''):
        return 'nothing at all, choose something';
    else:
        return str;


@app.route('/hello',method='GET')
def trivtest():
    return "true"

@app.route('/',method='POST')
def apisolr():
    user = request.forms.get('username')
    password = request.forms.get('password')
    print "user" + user;
    print "password" + password;
    if (not auth.does_authenticate(user,password)):
        return template('BadAuthentication')        
    search_string = request.forms.get('search_string')
    psc_pattern = request.forms.get('psc_pattern')
    search_string = convertSearchStringToLegalPattern(search_string);
    psc_pattern = convertPSCToLegalPattern(psc_pattern);
    print "APISOLR search_string" + search_string
    print "PSCSOLR search_string" + psc_pattern
    return searchApiSolr(URLToSolr,PathToDataFiles,search_string,psc_pattern)



