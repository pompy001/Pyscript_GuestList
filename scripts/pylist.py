"""
PylistTemplate and PyItemTemplate from https://github.com/pyscript/pyscript/blob/main/pyscriptjs/src/pyscript.py
"""

import datetime as dt



class PyItem(PyItemTemplate):
    def on_click(self,evt=None):
        self.data["deleted"] = not self.data["deleted"]
        self.strike(self.data["deleted"])
        self.select("input").element.checked = self.data["deleted"]

    def render_content(self):
        shwstr=f"Name : {self.data[self.labels[0]]}, Email_id : {self.data[self.labels[1]]}, Invited_at : {self.data[self.labels[2]]}"
        return shwstr

class PyList(PyListTemplate):
    item_class = PyItem

    def add(self,item):
        # check item is str or not
        if isinstance(item , str):
            name,email= [x.strip() for x in item.split(',')]
            item = {"name":name,"email":email, "deleted":False ,"created at":dt.now()}
        
        super().add(item, labels=['name','email',"created at"])

