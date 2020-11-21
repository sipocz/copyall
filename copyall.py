import os
import datetime as dt
import shutil

def searchfiles(outFileName, extension='.jpg', folder='F:\\', deltaTime=3600 * 24*1000000):
    """
    ***************************
    Listát készít egy adott könyvtárban lévő megadott kiterjesztésű fájlokból rekurzívan.
    A listát eltárolja a outFileName -ban megadott helyre
    Csak azokat a fájlokat veszi figyelembe, amelyek kora kisebb mint a megadott idő [sec]
    ***************************
    :param outFileName:     ide menti a kimeneti listát
    :param extension:       ezeket a fájlokat keresi
    :param folder:          ebben a könyvtárban keres
    :param deltaTime:       ilyen korú, vagy fiatalabb fájlokat keresi [sec]-ben kell megadni!!
    :return: ---
    """
    "Create a txt file with all the file of a type"
    currentDateTimeStamp = dt.datetime.now().timestamp()
    # print (currentDateTimeStamp)
    with open(outFileName, "w", encoding="utf-8") as filewrite:
        for r, _, f in os.walk(folder):
            for file in f:
                if file.endswith(extension):
                    # print(r+file)
                    fname = r + "\\" + file
                    fileTimeStamp = os.path.getctime(fname)
                    # print(fileTimeStamp)
                    if (currentDateTimeStamp - fileTimeStamp) <= deltaTime: 
                        filewrite.write(f"{fname}\n")


def listfiles( extension='.jpg', folder='F:\\'):
    """
    ***************************
    Listát készít egy adott könyvtárban lévő megadott kiterjesztésű fájlokból rekurzívan.
    ***************************
   
    :param extension:       ezeket a fájlokat keresi
    :param folder:          ebben a könyvtárban keres
    
    :return: the list of the founded files
    """
    
    currentDateTimeStamp = dt.datetime.now().timestamp()
    # print (currentDateTimeStamp)
    out=[]
    for r, _, f in os.walk(folder):
        for file in f:
            if file.endswith(extension):
                # print(r+file)
                fname = r + "\\" + file
                afile=(r,file)
                    
                    # print(fileTimeStamp)
                out.append(afile)          
    return(out)

def copyfiletype(source,dest,type):

    filelista=listfiles(extension=type,folder=source)
    for i in filelista:
        dir_name = i[0]
        dirname=dest+i[0][2:]+"\\"
        os.makedirs(dirname, exist_ok=True)
        print(dirname)
        destfilename=dirname+i[1]
        try:
            shutil.copyfile(i[0]+"\\"+i[1],destfilename)
        except:
            print(destfilename)
            


filelista=listfiles()

print(listfiles(".mp3",folder='F:\\'))