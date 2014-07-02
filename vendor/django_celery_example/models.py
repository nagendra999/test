from urlparse import urlparse 
from ftplib import FTP 

from django.db import models


"""
class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='user_profile')
    token = models.CharField(max_length=32)

"""

class SampleCount(models.Model):
    num = models.IntegerField(default=0)


class store_fastq(models.Model):
    url = "ftp://ftp.ddbj.nig.ac.jp/ddbj_database/dra/fastq/ERA021/ERA021502/ERX010282/ERR029554_1.fastq.bz2"
    parsed_url = urlparse(url)
    ftp = FTP(parsed_url.netloc)
    ftp.login()
    file_name = parsed_url.path.split('/')[-1:][0]
    path = parsed_url.path[:-len(file_name)]
    ftp.cwd(path)
    ftp.retrbinary('RETR ' + file_name, open(file_name, 'wb').write)
    ftp.quit()
