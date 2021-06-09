import subprocess
subprocess.call("./bin.sh", shell=True)
from core.base import Base

class Test(Base):
  def initialize(self):
    print("starting..")

  def update(self):
    pass

#create an instance of this class and run the program

Test().run()
# https://github.com/Namanskshetty/pyopengl
