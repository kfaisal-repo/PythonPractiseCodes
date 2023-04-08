import sys,platform,os,datetime
class Print_python_version:
    def __init__(self):
        pass
    def print_version_using_sys_module(self):
        return (sys.version,sys.version_info)
    def print_version_using_platform_module(self):
        return (platform.version(),platform.python_version_tuple())
    def curr_date_time(self):
        print(datetime.datetime.now())

##########################################################################################################



obj_version=Print_python_version()

print(obj_version.print_version_using_sys_module())
print(obj_version.print_version_using_platform_module())
print(obj_version.curr_date_time())