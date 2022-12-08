from Globals import *

def imgMasking():
    for root, dirs,files in os.walk(images_folder):
        for i,file in enumerate(files):
            path= os.path.join(root,file)
            img=cv.imread(path)
            # cv.imshow('orginal',img)

            hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)

            mask=cv.inRange(hsv,low,high)
            imask = mask>0
            orange = np.zeros_like(img, np.uint8)
            orange[imask] = img[imask]

            #combining two images in one 
            vertical_concat = np.concatenate((img, orange), axis=0)

            #resizing the rainbow image for easier comparison
            if(i==1):
                scale_percent = 60 
                width = int(vertical_concat.shape[1] * scale_percent / 100)
                height = int(vertical_concat.shape[0] * scale_percent / 100)
                dim = (width, height)
            
                resized = cv.resize(vertical_concat, dim, interpolation = cv.INTER_AREA)
                cv.imshow("Vertical plot resized Rainbow", resized)
                cv.waitKey()
                cv.destroyAllWindows()
                cv.waitKey(1)
            else:
                cv.imshow("Vertical plot coloring pencils", vertical_concat)
                cv.waitKey()
                cv.destroyAllWindows()
                cv.waitKey(1)
