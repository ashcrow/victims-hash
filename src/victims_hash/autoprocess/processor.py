
from victims_hash import fingerprint, metadata


def process(filename, store, config={}):
    """
    Processes a single archive and pushes the data into the store.

    :Parmeters:
       - `filename`: Archive filename.
       - `store`: Store to use.
       - `config`: Configuration dictionary to pass to the store.
    """
    data = {}
    data.update(fingerprint.fingerprint(filename))
    data.update(metadata.extract_metadata(filename))
    store(filename, data, config)
