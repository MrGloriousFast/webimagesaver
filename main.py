import urllib.request
import datetime
import os

# all links to images we want to save
websites = {}
websites['kreuzung']     = 'https://webcam.hrz.tu-darmstadt.de/Residenzschloss/current.jpg'
websites['karo5']        = 'https://webcam.hrz.tu-darmstadt.de/TU-Darmstadt-karo-5/current.jpg'
websites['darmstadtium'] = 'https://webcam.hrz.tu-darmstadt.de/Schloss-view-WKZ/current.jpg'
websites['cafe']         = 'https://webcam.hrz.tu-darmstadt.de/Neubau-603qm/current.jpg'
websites['flugfeld']     = 'https://webcam.hrz.tu-darmstadt.de/Tower/current.jpg'

# do this for every image we want to save
for site in websites:
    # get the current time
    # note that the server might be off by one minute due to delays in the server
    # we will still save the time we took the image from the website instead of the image time
    time_now = datetime.datetime.now()
    
    # where we want to save it
    name_folder = 'images/'+site+'/'+str(datetime.datetime.today().strftime('%Y-%m-%d'))
    
    # name of one image
    name_image = str(datetime.datetime.today().strftime('%Y-%m-%d_%H-%M'))+'.jpg'

    #complete path consists of folder and image
    complete_path = name_folder+'/'+name_image

    # create a folder if needed
    if not os.path.exists(name_folder):
        os.makedirs(name_folder)

    # actually try to get the image
    try:
        img = urllib.request.urlretrieve(websites[site], complete_path)
    except:
        # if it fails it will not do anything at all. the image will just miss
        # i could write it into a log file but when the power goes out or anything at all the logfile will not be complete, so better not to write anything at all
        pass
