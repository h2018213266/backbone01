import os
import sys
sys.path.insert(0,os.getcwd())
from utils.train_utils import get_info

def main():
    classes_path    = 'datas/annotations.txt'
    datasets_path   = 'D:/DR/datasets/first_dataset'  # 和上面\不同
    datasets        = ["train", "test"]
    classes, indexs = get_info(classes_path)
    
    for dataset in datasets:# train或者test
        txt_file = open('datas/' + dataset + '.txt', 'w') #创建txt文件
        datasets_path_ = os.path.join(datasets_path, dataset) # 'D:/DR/datasets+train
        classes_name = os.listdir(datasets_path_) # 'D:/DR/datasets/train/NDR..list
        
        for name in classes_name:
            if name not in classes:
                continue
            cls_id = indexs[classes.index(name)] # 对应annotation中的注释
            images_path = os.path.join(datasets_path_, name)# 'D:/DR/datasets/train/NDR..
            images_name = os.listdir(images_path)# # 'D:/DR/datasets/train/0/7001-001.jpg..list
            for photo_name in images_name:
                _, postfix = os.path.splitext(photo_name)
                if postfix not in ['.jpg', '.png', '.jpeg','.JPG', '.PNG', '.JPEG']:
                    continue
                txt_file.write('%s'%(os.path.join(images_path, photo_name)) + ' ' + str(cls_id)) # 路径名  注释
                txt_file.write('\n')
        txt_file.close()
if __name__ == "__main__":
    main()
