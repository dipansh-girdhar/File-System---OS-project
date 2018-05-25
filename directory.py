# -*- coding: utf-8 -*-
"""
@author: Jarvis
"""

from uuid import uuid4
 from datetime import date
+from src.file import File
 
 class Directory:
 
@@ -15,16 +16,25 @@ def is_directory(self):
         return True
 
     def search(self, file_name):
-        pass
+        for files in self.sub_files:
+            if files.name == file_name:
+                return files
 
     def create(self, file_name):
-        pass
+        self.sub_files.append(File(file_name, '')) # TODO
 
-    def delete(self):
-        pass
+    def delete(self, force):
+        if not self.isEmpty() and not force:
+            return False
+        del self.sub_files
+        return True
 
     def rename(self, initial_name, final_name):
-        pass
+        for files in self.sub_files:
+            if files.name == initial_name:
+                files.name = final_name
+                return True
+        return False
 
     def traverse(self):
         pass
 
     def delete_file(self, file_name):
         i = -1
         for files in self.sub_files:
             i += 1
             if not files.is_directory() and files.name == file_name:
                 self.size -= files.size
                 self.last_modified = date.today()
                 self.sub_files.pop(i)
                 files.delete()
                 return True
         return False
+
+    def isEmpty(self):
+        if self.sub_files:
+            return False
+        return True
  
10  src/process.py
@@ -58,3 +58,13 @@ def skip(self, index):
                 return True
 
         return False
+
+    def delete_directory(self, directory_name, force):
+        i = -1
+        for directories in self.current_directory.sub_files:
+            i += 1
+            if directories.name == directory_name and directories.is_directory():
+                directories.delete(force)
+                self.current_directory.sub_files.pop(i)
+                return True
+        return False