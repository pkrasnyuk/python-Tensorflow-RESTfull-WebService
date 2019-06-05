class Configuration:
    __host = None
    __port = 0
    __loggingName = None
    __loggingFile = None

    def __init__(self, host, port, logging_name, logging_file):
        self.__host = host
        self.__port = port
        self.__loggingName = logging_name
        self.__loggingFile = logging_file

    def __str__(self):
        return " Host: {0}\n Port: {1}\n Logging Name: {2}\n Logging file: {3}" \
            .format(self.__host, self.__port, self.__loggingName, self.__loggingFile)

    @property
    def host(self):
        return self.__host

    @property
    def port(self):
        return self.__port

    @property
    def logging_name(self):
        return self.__loggingName

    @property
    def logging_file(self):
        return self.__loggingFile
