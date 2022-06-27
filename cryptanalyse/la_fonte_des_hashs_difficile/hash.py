import base64, codecs
magic = 'IyEvdXNyL2Jpbi9weXRob24KIyAtKi0gY29kaW5nOiB1dGYtOCAtKi0KaW1wb3J0IHN5cwoKCgojIGZyb20gaHR0cHM6Ly9hc2VjdXJpdHlzaXRlLmNvbS9zdWJqZWN0cy9jaGFwdGVyODgKc2JveCA9IFsnMDExMDAwMTEnLCAnMDExMTExMDAnLCAnMDExMTAxMTEnLCAnMDExMTEwMTEnLCAnMTExMTAwMTAnLCAnMDExMDEwMTEnLCAnMDExMDExMTEnLCAnMTEwMDAxMDEnLCAnMDAxMTAwMDAnLCAnMDAwMDAwMDEnLCAnMDExMDAxMTEnLCAnMDAxMDEwMTEnLCAnMTExMTExMTAnLCAnMTEwMTAxMTEnLCAnMTAxMDEwMTEnLCAnMDExMTAxMTAnLCAnMTEwMDEwMTAnLCAnMTAwMDAwMTAnLCAnMTEwMDEwMDEnLCAnMDExMTExMDEnLCAnMTExMTEwMTAnLCAnMDEwMTEwMDEnLCAnMDEwMDAxMTEnLCAnMTExMTAwMDAnLCAnMTAxMDExMDEnLCAnMTEwMTAxMDAnLCAnMTAxMDAwMTAnLCAnMTAxMDExMTEnLCAnMTAwMTExMDAnLCAnMTAxMDAxMDAnLCAnMDExMTAwMTAnLCAnMTEwMDAwMDAnLCAnMTAxMTAxMTEnLCAnMTExMTExMDEnLCAnMTAwMTAwMTEnLCAnMDAxMDAxMTAnLCAnMDAxMTAxMTAnLCAnMDAxMTExMTEnLCAnMTExMTAxMTEnLCAnMTEwMDExMDAnLCAnMDAxMTAxMDAnLCAnMTAxMDAxMDEnLCAnMTExMDAxMDEnLCAnMTExMTAwMDEnLCAnMDExMTAwMDEnLCAnMTEwMTEwMDAnLCAnMDAxMTAwMDEnLCAnMDAwMTAxMDEnLCAnMDAwMDAxMDAnLCAnMTEwMDAxMTEnLCAnMDAxMDAwMTEnLCAnMTEwMDAwMTEnLCAnMDAwMTEwMDAnLCAnMTAwMTAxMTAnLCAnMDAwMDAxMDEnLCAnMTAwMTEwMTAnLCAnMDAwMDAxMTEnLCAnMDAwMTAwMTAnLCAnMTAwMDAwMDAnLCAnMTExMDAwMTAnLCAnMTExMDEwMTEnLCAnMDAxMDAxMTEnLCAnMTAxMTAwMTAnLCAnMDExMTAxMDEnLCAnMDAwMDEwMDEnLCAnMTAwMDAwMTEnLCAnMDAxMDExMDAnLCAnMDAwMTEwMTAnLCAnMDAwMTEwMTEnLCAnMDExMDExMTAnLCAnMDEwMTEwMTAnLCAnMTAxMDAwMDAnLCAnMDEwMTAwMTAnLCAnMDAxMTEwMTEnLCAnMTEwMTAxMTAnLCAnMTAxMTAwMTEnLCAnMDAxMDEwMDEnLCAnMTExMDAwMTEnLCAnMDAxMDExMTEnLCAnMTAwMDAxMDAnLCAnMDEwMTAwMTEnLCAnMTEwMTAwMDEnLCAnMDAwMDAwMDAnLCAnMTExMDExMDEnLCAnMDAxMDAwMDAnLCAnMTExMTExMDAnLCAnMTAxMTAwMDEnLCAnMDEwMTEwMTEnLCAnMDExMDEwMTAnLCAnMTEwMDEwMTEnLCAnMTAxMTExMTAnLCAnMDAxMTEwMDEnLCAnMDEwMDEwMTAnLCAnMDEwMDExMDAnLCAnMDEwMTEwMDAnLCAnMT'
love = 'RjZQRkZGRaYPNaZGRjZGNjZQNaYPNaZGRkZQRkZGRaYPNaZGNkZQRjZGNaYPNaZGRkZGRjZGRaYPNaZQRjZQNjZGRaYPNaZQRjZQRkZQRaYPNaZQNkZGNjZGRaYPNaZGNjZQNkZQRaYPNaZQRjZQNkZQRaYPNaZGRkZGRjZQRaYPNaZQNjZQNjZGNaYPNaZQRkZGRkZGRaYPNaZQRjZGNjZQNaYPNaZQNkZGRkZQNaYPNaZGNjZGRkZGRaYPNaZGNkZQRjZQNaYPNaZQRjZGNjZQRaYPNaZGNkZQNjZGRaYPNaZQRjZQNjZQNaYPNaZGNjZQRkZGRaYPNaZGNjZGNjZGNaYPNaZGNjZGRkZQRaYPNaZQNkZGRjZQNaYPNaZGRkZGNkZQRaYPNaZGNkZGRkZQNaYPNaZGNkZGNkZGNaYPNaZGRjZGRjZGNaYPNaZQNkZQNjZQRaYPNaZQNjZGNjZQNaYPNaZGRkZGRkZGRaYPNaZGRkZGNjZGRaYPNaZGRjZGNjZGNaYPNaZGRjZQRkZQRaYPNaZQNjZQRkZQNaYPNaZQNjZGNjZGRaYPNaZGRkZQRkZQNaYPNaZQRjZGRkZGRaYPNaZGNjZGNkZGRaYPNaZQRjZQNkZQNaYPNaZQNjZGNkZGRaYPNaZGRjZQNkZQNaYPNaZGNkZQNkZGRaYPNaZQRkZGRkZGNaYPNaZQNkZGRkZQRaYPNaZQRkZQNkZQNaYPNaZQRjZGRkZQRaYPNaZQNjZGRjZQRaYPNaZQRkZGNjZGRaYPNaZQRkZQNjZQNaYPNaZGNjZQNjZQRaYPNaZQRjZQRkZGRaYPNaZGRjZGRkZQNaYPNaZQNkZQNjZGNaYPNaZQNkZQRjZGNaYPNaZGNjZGNjZQNaYPNaZGNjZQRjZQNaYPNaZQRjZQNkZGNaYPNaZGRkZQRkZGNaYPNaZGNkZGRjZQNaYPNaZQNjZGNkZQNaYPNaZGRjZGRkZGNaYPNaZQRjZGRkZGNaYPNaZQNjZQRjZGRaYPNaZGRjZGRjZGRaYPNaZGRkZQNjZQNaYPNaZQNkZGNjZGNaYPNaZQNkZGRjZGNaYPNaZQNjZQRjZGNaYPNaZQRjZQRjZQRaYPNaZQNjZQNkZGNaYPNaZQNkZQNkZQNaYPNaZQRjZGRkZQNaYPNaZGRjZQNjZGNaYPNaZGRjZGNjZGRaYPNaZGNkZQRkZQNaYPNaZQRkZQNjZGNaYPNaZGNjZGNjZQRaYPNaZGNjZGNkZQRaYPNaZGRkZQNkZQNaYPNaZQRkZGRjZQRaYPNaZGRkZQNkZGRaYPNaZGRjZQRjZQNaYPNaZQNkZGNkZGRaYPNaZQRkZQRkZQRaYPNaZGNjZQRkZQRaYPNaZGRjZGNkZQRaYPNaZQRjZQRkZGNaYPNaZGNkZQRjZQRaYPNaZQRkZQRkZQNaYPNaZQRjZGNkZGNaYPNaZGRkZGNkZQNaYPNaZGRkZQRjZGNaYPNaZQRkZQNkZQRaYPNaZQRkZGRjZGNaYPNaZGNkZQRkZGNaYPNaZQNjZQRjZQNaYPNaZGNkZGRjZGNaYPNaZQRkZGRjZQNaYPNaZQNkZQNkZQRaYPNaZQNkZQRkZGNaYPNaZQNjZGRkZQNaYPNaZGNkZQNkZGNaYPNaZGNkZGNkZQNaYPNaZGRjZQNkZGNaYPNa'
god = 'MTExMDEwMDAnLCAnMTEwMTExMDEnLCAnMDExMTAxMDAnLCAnMDAwMTExMTEnLCAnMDEwMDEwMTEnLCAnMTAxMTExMDEnLCAnMTAwMDEwMTEnLCAnMTAwMDEwMTAnLCAnMDExMTAwMDAnLCAnMDAxMTExMTAnLCAnMTAxMTAxMDEnLCAnMDExMDAxMTAnLCAnMDEwMDEwMDAnLCAnMDAwMDAwMTEnLCAnMTExMTAxMTAnLCAnMDAwMDExMTAnLCAnMDExMDAwMDEnLCAnMDAxMTAxMDEnLCAnMDEwMTAxMTEnLCAnMTAxMTEwMDEnLCAnMTAwMDAxMTAnLCAnMTEwMDAwMDEnLCAnMDAwMTExMDEnLCAnMTAwMTExMTAnLCAnMTExMDAwMDEnLCAnMTExMTEwMDAnLCAnMTAwMTEwMDAnLCAnMDAwMTAwMDEnLCAnMDExMDEwMDEnLCAnMTEwMTEwMDEnLCAnMTAwMDExMTAnLCAnMTAwMTAxMDAnLCAnMTAwMTEwMTEnLCAnMDAwMTExMTAnLCAnMTAwMDAxMTEnLCAnMTExMDEwMDEnLCAnMTEwMDExMTAnLCAnMDEwMTAxMDEnLCAnMDAxMDEwMDAnLCAnMTEwMTExMTEnLCAnMTAwMDExMDAnLCAnMTAxMDAwMDEnLCAnMTAwMDEwMDEnLCAnMDAwMDExMDEnLCAnMTAxMTExMTEnLCAnMTExMDAxMTAnLCAnMDEwMDAwMTAnLCAnMDExMDEwMDAnLCAnMDEwMDAwMDEnLCAnMTAwMTEwMDEnLCAnMDAxMDExMDEnLCAnMDAwMDExMTEnLCAnMTAxMTAwMDAnLCAnMDEwMTAxMDAnLCAnMTAxMTEwMTEnLCAnMDAwMTAxMTAnXQoKCgoKZGVmIHN0cmluZzJiaXRzKHM9JycpOgogICAgdG1wID0gW10KICAgIGZvciB4IGluIHMgOgogICAgICAgIGJ5dGUgPSBiaW4ob3JkKHgpKVsyOl0KICAgICAgICBpZiBsZW4oYnl0ZSkgPiA4OgogICAgICAgICAgICBpbmRpY2VzID0gW2kgZm9yIGkgaW4gcmFuZ2UoMCwgbGVuKGJ5dGUpLCA4KV0KICAgICAgICAgICAgcGFydHMgPSBbIiIuam9pbihieXRlW2k6al0pLnpmaWxsKDgpIGZvciBpLGogaW4gemlwKGluZGljZXMsIGluZGljZXNbMTpdK1tOb25lXSldCiAgICAgICAgICAgIHRtcCArPSAocGFydHMpCiAgICAgICAgZWxzZSA6CiAgICAgICAgICAgIGJ5dGUgPSBieXRlLnpmaWxsKDgpCiAgICAgICAgICAgIHRtcC5hcHBlbmQoYnl0ZSkKICAgIHJldHVybiB0bXAKCmRlZiBwYWRkaW5nKGJpbmFyeSk6CiAgICBpZigobGVuKGJpbmFyeSkgKyAxICkgJSAzMiA9PSAwKToKICAgICAgICBiaW5hcnkuYXBwZW5kKCcwMDAwMDAwMScpCiAgICAgICAgYmluYXJ5LmFwcGVuZCgnMDAwMDAwMDAnKQogICAgaWYobGVuKGJpbmFyeSklMzIgIT0gMCBvciBsZW4oYmluYXJ5KSA9PSAwKToKICAgICAgICBiaW5hcnkuYXBwZW5kKCcwMD'
destiny = 'NjZQNjZFpcPvNtVPNtVPNtq2ucoTHtoTIhXTWcozSlrFxyZmVtVG0tZQbXVPNtVPNtVPNtVPNtLzyhLKW5YzSjpTIhMPtaZQNjZQNjZQNaXDbXMTIzVUuipvuuYTVcBtbtVPNtpzImVQ0tVvVXVPNtVTMipvOcVTyhVUWuozqyXTkyovuuXFx6PvNtVPNtVPNtVPNtVUWyplNeCFOmqUVbnJ50XTSonI0cVS4tnJ50XTWonI0cXDbtVPNtpzI0qKWhVUWypjbXMTIzVUAvo3uso3OyXTWcozSlrFx6PvNtVPOzo3VtnFOcovOlLJ5aMFufMJ4bLzyhLKW5XFx6PvNtVPNtVPNtnJ5xMKttCFOcoaDbLzyhLKW5J2yqYQVcPvNtVPNtVPNtLzyhLKW5J2yqVQ0tp2WirSgcozEyrS0XPzEyMvOjnTSmMGRbLzyhLKW5XGbXVPNtVT0tCFOcoaDboTIhXTWcozSlrFxtYlNmZvxXVPNtVUEgpPN9VSgqPvNtVPOzo3VtnFOcovOlLJ5aMFtjYPOfMJ4bLzyhLKW5XFjtoFx6PvNtVPNtVPNtqT1jYzSjpTIhMPu4o3VbLzyhLKW5J2yqYPOvnJ5upayonFfkKFxcPvNtVPOlMKE1pz4tqT1jPtcxMJLtpTuup2HlXTWcozSlrFx6PvNtVPOzo3VtnFOcovOlLJ5aMFtkYTkyovuvnJ5upaxcXGbXVPNtVPNtVPOzo3VtnvOcovOlLJ5aMFucXGbXVPNtVPNtVPNtVPNtLzyhLKW5J2yqVQ0trT9lXTWcozSlrIgcKFjtLzyhLKW5J2cqXDbXMTIzVTWcqUZlnTI4XTWcozSlrFx6PvNtVPObMKusp3ElVQ0tVvVXVPNtVTMipvOvnKDtnJ4tLzyhLKW5BtbtVPNtVPNtVTuyrS9mqUVtXm0tMz9loJS0XTyhqPuvnKDfVQVcYPNaZQW4WlxXVPNtVUWyqUIlovObMKusp3ElPtcxMJLtnPugXGbXVPNtVUOfLJyhVQ0toDbtVPNtLzyhLKW5VQ0tp3ElnJ5aZzWcqUZbpTkunJ4cPvNtVPOjLJExnJ5aXTWcozSlrFxXVPNtVTyzVTkyovuvnJ5upaxcVQ4tZmV6PvNtVPNtVPNtLzyhLKW5VQ0tpTuup2HkXTWcozSlrFxXVPNtVUObLKAyZvuvnJ5upaxcPvNtVPOjnTSmMGVbLzyhLKW5XDbtVPNtpTuup2HlXTWcozSlrFxXVPNtVUAvo3uso3OyXTWcozSlrFxXVPNtVTuup2usp3ElVQ0tLzy0pmWbMKtbLzyhLKW5XDbtVPNtpzI0qKWhVTuup2usp3ElPtbXpTkunJ4tCFNtVvVXnJLtoTIhXUA5pl5upzq2XFN9CFNkBtbtVPNtpUWcoaDbVxS1L3IhVTSlM3IgMJ50VTEioz7QdF4tHzyyovQQbPObLJAbMKVhVRW5MFOvrJHhVvxXMJkcMvOfMJ4bp3ymYzSlM3LcVQ49VQVtBtbtVPNtpTkunJ4tXm0tp3ymYzSlM3MoZI0XVPNtVTMipvOcVTyhVUWuozqyXQVfoTIhXUA5pl5upzq2XFx6PvNtVPNtVPNtpTkunJ4tXm0tVvNvVPftp3ElXUA5pl5upzq2J2yqXDbtVPNtpUWcoaDbnPujoTScovxcPt=='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))