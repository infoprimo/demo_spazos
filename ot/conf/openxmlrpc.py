# coding: utf-8
import xmlrpclib

class OpenConn:
    def __init__(self, settings):
        self.hostname = settings['hostname']
        self.port = settings['port']
        self.database = settings['database']
        self.username = settings['username']
        self.password = settings['password']

        sock_common = xmlrpclib.ServerProxy('http://%s:%s/xmlrpc/common' % (self.hostname, self.port))
        self.uid = sock_common.login(self.database, self.username, self.password)

        self.sock = xmlrpclib.ServerProxy('http://%s:%s/xmlrpc/object' % (self.hostname, self.port))

    def sock_execute(self, model_name, action, *args):
        #print "xmlrpc  : ",model_name, action, args
        return self.sock.execute(self.database, self.uid, self.password, model_name, action, *args)
