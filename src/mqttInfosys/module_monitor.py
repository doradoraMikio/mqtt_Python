import psutil


class ProcessUtilities:

    @staticmethod
    def get_cpu_performance():
        cpu_usage = psutil.cpu_percent()
        return cpu_usage

    @staticmethod
    def get_ram_performance():
        memory_usage = psutil.virtual_memory().percent
        return memory_usage

    @staticmethod
    def get_computer_performance():
        computer_performance = dict()
        computer_performance["cpu"] = ProcessUtilities.get_cpu_performance()
        computer_performance["ram"] = ProcessUtilities.get_ram_performance()
        return computer_performance

