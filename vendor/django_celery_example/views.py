from ftplib import FTP 
from urlparse import urlparse 

from django.views.decorators.csrf import csrf_exempt 
from django.http import HttpResponse 

from .forms import RegistrationForm 
#from .utilities import create_user 
from .tasks import add_to_count 



@csrf_exempt
def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
        #create_user(form.cleaned_data)
            return HttpResponse('success')


def test_async(request):
    add_to_count.delay()
    return HttpResponse('Your async request is processing.')


def test_ftp_download(request):
    url = "ftp://ftp.ddbj.nig.ac.jp/ddbj_database/dra/fastq/ERA021/ERA021502/ERX010282/ERR029554_1.fastq.bz2"
    parsed_url = urlparse(url)
    ftp = FTP(parsed_url.netloc)
    ftp.login()
    file_name = parsed_url.path.split('/')[-1:][0]
    path = parsed_url.path[:-len(file_name)]
    ftp.cwd(path)
    ftp.retrbinary('RETR ' + file_name, open(file_name, 'wb').write)
    ftp.quit()
    return HttpResponse('success')
