victims-hash
============

Hashing mechanism used by victims to produce a unique fingerprint for a
given archive. Currently supports .jar, .gem, .egg files.

    from victims_hash.fingerprint import fingerprint
    data = fingerprint('file.jar')

    from victims_hash.metadata import extract_metadata
    md = extract_metadata('file.jar')

autoprocess
-----------
victims-hash includes a inotify based autoprocess service which can store results
back to a mongodb database.

    $ cat mongodb.cfg
    host=127.0.0.1
    port=27017
    database=mydb
    collection=hashes
    $ victims-hash-autoprocess --workers 5 --store mongo --config mongodb.cfg --directory watched_dir &

