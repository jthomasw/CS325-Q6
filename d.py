class Logger:
    def log(self, message):
        raise NotImplementedError("Subclasses must implement log method.")

class ConsoleLogger(Logger):
    def log(self, message):
        print("[Console] ", message)

class FileLogger(Logger):
    def __init__(self, file_name):
        self.file_name = file_name

    def log(self, message):
        with open(self.file_name, 'a') as file:
            file.write("[File] " + message + "\n")

class LogManager:
    def __init__(self, logger):
        self.logger = logger

    def log_message(self, message):
        self.logger.log(message)

def main():
    console_logger = ConsoleLogger()
    file_logger = FileLogger("log.txt")

    log_manager = LogManager(console_logger)
    log_manager.log_message("This is a log message.")

    log_manager = LogManager(file_logger)
    log_manager.log_message("This is another log message.")

if __name__ == "__main__":
    main()