import genomelink
#report = genomelink.Report.fetch(name='eye-color', population='european', token = 'GENOMELINKTEST')
#print(report.summary['text'])




def scopeing():
    authorize_url = genomelink.OAuth.authorize_url(scope=['report:eye-color report:beard-thickness report:morning-person'])
    reports = []
    if session.get('oauth_token'):
        for name in ['eye-color', 'beard-thickness', 'morning-person']:
            reports.append(genomelink.Report.fetch(name=name, population='european', token=session['oauth_token']))
            print(report.summary['text'])
            
def match_traits(queries, region, apitoken):
#queries = 'eye-color'
#region = 'european'
#apitoken = 'GENOMELINKTEST'

    report = genomelink.Report.fetch(name= queries, population = region , token = apitoken)
    print(report.summary['text'])
