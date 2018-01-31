import sys
import time
import logging
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
import os,subprocess, errno

class FBXEvnetHandler(FileSystemEventHandler):

    def dispatch_task(self, abs_src_path):

        filename = os.path.splitext(abs_src_path)[0]
        extension = os.path.splitext(abs_src_path)[1]
        # logging.info("dispatch_task")
            
        if extension == ".fbx" or extension == ".dae":
            if '\\Model' in abs_src_path:
                if not '_root' in abs_src_path:
                    self.fix_rootmotion(abs_src_path)
        if extension == ".fbx" or extension == ".dae":
            if '\\Animations' in abs_src_path:
                if not '_root' in abs_src_path:
                    self.fix_rootmotion(abs_src_path)
        elif extension == ".dat":
            logging.info("dat")
            if '\\Adam' in abs_src_path:
                self.generate_lipsync_fbx(abs_src_path, os.path.abspath("../Arts/Model/RootMotion/adam_normalize_root.fbx"))
            elif '\\Doctor' in abs_src_path:
                self.generate_lipsync_fbx(abs_src_path, os.path.abspath("../Arts/Model/RootMotion//doctor_normalize_root.fbx"))
            elif '\\Amy' in abs_src_path:
                self.generate_lipsync_fbx(abs_src_path, os.path.abspath("../Arts/Model/RootMotion//amy_normalize_root.fbx"))
            

    def fix_rootmotion(self, input_path):
        filename = os.path.splitext(os.path.basename(input_path))[0]
        directory = os.path.dirname(input_path)
        export_directory = os.path.join(directory, 'RootMotion')
        logging.info("export directory: " + export_directory)
        try:
            os.makedirs(export_directory)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise

        output_path = os.path.join(export_directory, filename + '_root.fbx')
        python_path = os.path.abspath("rootmotion_fix.py")
        cmd = ["bash", "-c", "/cygdrive/c/Program\ Files/Blender\ Foundation/Blender/blender.exe --background --python"
        + " \"" + python_path + "\"" + " \"" + input_path + "\"" + " \"" + output_path + "\""]
        logging.info(cmd[2])
        subprocess.call(cmd, shell=True)


    def generate_lipsync_fbx(self, input_path, model_path):
        filename = os.path.splitext(input_path)[0]

        output_path = filename + ".fbx"
        python_path = os.path.abspath("lipsync.py")
        logging.info("model path: " + model_path)
        
        cmd = ["bash", "-c", "/cygdrive/c/Program\ Files/Blender\ Foundation/Blender/blender.exe --background --python"
        + " \"" + python_path + "\"" + " \"" + input_path + "\"" + " \"" + output_path + "\"" + " \"" + model_path + "\""]
        logging.info(cmd[2])
        subprocess.call(cmd, shell=True)


    def on_moved(self, event):
        super(FBXEvnetHandler, self).on_moved(event)

        what = 'directory' if event.is_directory else 'file'
        # logging.info("Moved %s: from %s to %s", what, event.src_path, event.dest_path)

    def on_created(self, event):
        super(FBXEvnetHandler, self).on_modified(event)

        what = 'directory' if event.is_directory else 'file'
        abs_src_path = os.path.abspath(event.src_path)
        if ('.git' in event.src_path):
            return
        logging.info("Create %s: %s", what, event.src_path)

        # argument = 'sh -c echo 123'
        # os.chdir(r"c:\cygwin64\bin")
        # dest_path 

        if what == 'file':
            self.dispatch_task(abs_src_path)

        # logging.info("Created %s: %s", what, event.src_path)

    def on_deleted(self, event):
        super(FBXEvnetHandler, self).on_deleted(event)

        what = 'directory' if event.is_directory else 'file'
        # logging.info("Deleted %s: %s", what, event.src_path)
    

    def on_modified(self, event):
        super(FBXEvnetHandler, self).on_modified(event)

        what = 'directory' if event.is_directory else 'file'
        abs_src_path = os.path.abspath(event.src_path)
        if ('.git' in event.src_path):
            return
        logging.info("Modified %s: %s", what, event.src_path)
        if what == 'file':
            self.dispatch_task(abs_src_path)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
   
    logging.info("monitor path: " + os.path.abspath(path))
    # logging.info(123)
    event_handler = FBXEvnetHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()