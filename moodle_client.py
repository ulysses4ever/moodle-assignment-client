#!/usr/bin/python

#-----------------------------------------------------------------------
#
# This script allows to post new assignment description to Moodle.
# It accepts three parameters:
#   -f FILE or --file FILE -- file with new description text.
#                             NOTE: if omitted or - given we read stdin.
#   -i ID   or --id ID     -- ID of a assignment to be edited (you may
#                             get one from address bar in a browser).
#   -t TOK  or --token TOK -- security token. You may get one 
#                             from Ulysses.
#   -h      or --help      -- help message (optional).
#
# Requires Python 2.7.
#-----------------------------------------------------------------------

import sys
import argparse
import xmlrpclib

parser = argparse.ArgumentParser(
            description='Send XML-RPC request to Moodle custom web service' \
                        'for updating assignment text.')
parser.add_argument('-f', '--file', dest='file', type=argparse.FileType('r'),
                    default=sys.stdin, help='file to read new contents')
parser.add_argument('-i', '--id', dest='id', type=int, 
                   required=True, help='Updating assignment id')
parser.add_argument('-t', '--token', dest='token', 
                   required=True, help='Authorization token')
args = parser.parse_args()

domainname = 'http://edu.mmcs.sfedu.ru'
command = '/webservice/xmlrpc/server.php?wstoken=';

srv = xmlrpclib.ServerProxy(domainname + command + args.token)
print srv.local_ws_assign_update_description(args.id, args.file.read())

