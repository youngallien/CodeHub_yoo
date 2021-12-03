#folder: 包含N个场景的.png文件, 每个场景包含索引0,1,2,...多个.png文件
#process: folder下面生成N个folder, 分别包含N个场景中的所有.png文件

import os

def run(folder):
    picList = os.listdir(folder)
    rename = folder + "\\" + "0000"
    #os.makedirs(rename)
    for pic in picList:
        
        if pic.endswith(".png"):
            names = pic.split("_")
            index = names[5]
            #print(index)
            
            if index == '0':
                renames = names[2:5] + [names[6].split(".")[0]]
                #rename.append(names[6].split(".")[0])
                rename = folder + "\\" + "_".join(renames)
                #print(rename)
                #ret = os.path.isdir(rename)
                if not os.path.isdir(rename): 
                    os.makedirs(rename)
                    print("Create folder: ", rename)
                else:
                    while os.path.isdir(rename): 
                        print("Exist folder: ", rename)
                        renames[2] = str(float(renames[2]) + 0.01)
                        rename = folder + "\\" +  "_".join(renames)
                    os.makedirs(rename)
                    print("Create folder: ", rename)
            
            print(pic, " --> ", rename)
            moveCmd = "move " + folder + "\\" + pic + " " + rename
            print(moveCmd)
            os.system(moveCmd)

    print("Done!")
    return 0

def main():

    targetFolder = "G:\\SrData\\png"
    run(targetFolder)

    return 0 

if __name__ == "__main__":
    print("main: \n")
    main()
