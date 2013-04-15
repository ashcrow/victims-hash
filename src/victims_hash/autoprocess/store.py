

def echo(filename, data, config):
    """
    Prints results out for testing.
    """
    print filename, data


def victims(filename, data, config):
    """
    Saves back to victims mongodb.

    Config expected to be like so::

       host=127.0.0.1
       port=1234
       database=mydb
       collection=data
    """
    import os.path
    from pymongo import Connection

    connection = Connection(config['host'], int(config['port']))
    db = getattr(connection, config['database'])

    db[config['collection']].update(
        {'name': os.path.basename(filename)},
        {'$set': {'hashes': data['hashes'], 'meta': data['meta']}})
