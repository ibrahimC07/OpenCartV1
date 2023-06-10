import inspect
import logging
import os


# class LogGen():
#     @staticmethod
#     def loggen():
#         path = "/Users/ibrahimcelikel/PycharmProjects/OpencartV1/logs/automation.log"
#         logging.basicConfig(filename=path,
#                             format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
#         logger = logging.getLogger()
#         logger.setLevel(logging.DEBUG)
#         return logger

class LogGen:
    @staticmethod
    def loggen():
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.DEBUG)
        fh = logging.FileHandler("/Users/ibrahimcelikel/PycharmProjects/OpencartV1/logs/automation.log")
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        return logger
