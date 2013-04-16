
from archive.archive import Archive


def fingerprint(file, io=None):
    if file and io:
        raise Exception("Can not process filename and IO.")

    archive_instance = None
    if not io:
        io = open(file, "r")

    try:
        if file.endswith(".jar"):
            from archive.reader.jar import JarReader
            archive_instance = Archive(JarReader(io)).fingerprint()

        elif file.endswith(".gem"):
            from archive.reader.gem import GemReader
            archive_instance = Archive(GemReader(io)).fingerprint()

        elif file.endswith(".egg"):
            from archive.reader.egg import EggReader
            archive_instance = Archive(EggReader(io)).fingerprint()

        if not archive_instance:
            raise NotImplementedError("No support for %s files." % file)
        return archive_instance

    except Exception, ex:
        # Blind raising ...
        raise ex
    finally:
        # Always make sure the file is closed.
        if not io.closed:
            io.close()
