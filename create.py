from fs.memoryfs import MemoryFS
from fs.expose import fuse 
fs = MemoryFS() # create an in memory file system
fs.createfile('filename.txt') # creating an empty file
fs.setcontents('filename.txt', 'contents of file') # putting content into the file.
from fs.osfs import OSFS
home_fs = OSFS('/') # 
home_fs.makedir('/home/dave/scratch/ramdrive', allow_recreate=True) # have to make a directory for us to mount our memory file system on.
mp = fuse.mount(fs, '/home/dave/scratch/ramdrive') # exposes fs to everything else on machine. (ie: other system calls can see these files)
mp.path # in case you need the path to the files created.
mp.unmount() # files are no longer being exposed via fuse
home_fs.removedir('/home/dave/scratch/ramdrive/') #remove the real file system directory when done.


fs.remove('filename.txt')

home_fs.close()
fs.close()



# creating a ramdrive like this wont work for my desired task, as other external applications cannot write to the directory. They only have read access.




