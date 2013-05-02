import os
import StringIO
import gzip
import mimetypes
from django.core.files.storage import Storage, File
from google.appengine.api import files

class GcsFile(File):
    pass

class GcsStorage(Storage):
    bucket_name = 'frlpix'
    overwrite = False

    def __init__(self):
        pass
    
    def _get_or_create_bucket(self, name):
        pass

    def _clean_name(self, name):
        if os.pathsep != '/':
            name = name.replace( os.pathsep, '/' )
        return name

    def _compress_content(self, content):
        zbuf = StringIO()
        zfile = gzip.GzipFile(mode='wb', compresslevel=6, fileobj=zbuf)
        try:
            zfile.write( content.read() )
        finally:
            zfile.close()
        zbuf.seek(0)
        content.file = zbuf
        content.seek(0)
        return content
    
    
    
    def _open(self, name, mode='rb'):
        f = GcsFile(name, mode, self)
        if not f.key:
            raise IOError('File does not exist %s' % name)
        return f


    def _save(self, name, content):
        full_name = '/gs/%s/%s' % (self.bucket_name, name)
        content_type = getattr(content, 'content_type', 
            mimetypes.guess_type(name)[0] or 'application/octet-stream' )
        writable_name = files.gs.create(full_name, content_type)
        with files.open( writable_name, 'a') as f:
            f.write( content )
        files.finalize(writable_name)
        return name
    
    def delete(self, name):
        full_name = '/gs/%s/%s' % (self.bucket_name, name)
        files.delete(full_name)

    def exists(self, name):
        path = '/gs/%s' % self.bucket_name
        listdir = files.listdir(path, prefix= '/' + name)
        if len(listdir) == 1:
            return True
        else:
            return False
            
    def listdir(self, name):
        pass
    
    def size(self, name):
        pass
    
    def url(self, name):
        
        name = self._normalize_name(self._clean_name(name))
        if self.custom_domain:
            return "%s//%s/%s" % (self.url_protocol,
                                  self.custom_domain, name)
        return self.connection.generate_url(self.querystring_expire,
            method='GET', bucket=self.bucket.name, key=self._encode_name(name),
            query_auth=self.querystring_auth, force_http=not self.secure_urls)

    def get_available_name(self, name):
        if self.overwrite:
            return name
        else:
            return super(GcsStorage, self).get_available_name(name)

        