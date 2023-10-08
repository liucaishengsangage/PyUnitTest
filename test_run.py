import subprocess



maya_path = "C:/Program Files/Autodesk/Maya2024/bin/maya.exe"

tpath = "D:/TD/AutomationUnitTest/PyUnitTest/PyUnitTest"
start_cmd = ' '.join([maya_path, ''])
start_cmd = ' '.join([start_cmd, '-command'])
cmd_string = '''"python(\\"import sys;temppath = \\'%s/\\';sys.path.append(temppath);print(\'run success!!!!\');\\")"'''  % (tpath)
start_cmd = ' '.join([start_cmd, cmd_string])
#,shell=True,stdout=subprocess.PIPE
subprocess.Popen(start_cmd)

 