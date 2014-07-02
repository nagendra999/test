from urlparse import urlparse 
from ftplib import FTP 

url = "ftp://ftp.ddbj.nig.ac.jp/ddbj_database/dra/fastq/ERA021/ERA021502/ERX010282/ERR029554.fastq.bz2"
parsed_url = urlparse(url)
ftp = FTP(parsed_url.netloc)
ftp.login()
file_name = parsed_url.path.split('/')[-1:][0]
print file_name 
path = parsed_url.path[:len(file_name)]
print path 
ftp.cwd(path)
#ftp.retrbinary('RETR ' + file_name, open(file_name, 'wb').write)
ftp.quit()

