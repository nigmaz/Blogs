# C:\Users\Admin\AppData\Roaming\Sublime Text\Packages\Cmd

# https://stackoverflow.com/questions/18606682/how-can-i-open-command-line-prompt-from-sublime-in-windows7
import os, sublime_plugin
class CmdCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        file_name=self.view.file_name()
        path=file_name.split("\\")
        current_driver=path[0]
        path.pop()
        current_directory="\\".join(path)
        command= "cd "+current_directory+" & "+current_driver+" & start cmd"
        os.system(command)