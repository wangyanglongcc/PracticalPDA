import os
import glob

def rename_and_move(path,target_path):
    if not os.path.exists(target_path): os.makedirs(target_path)
    # remove process data
    d_id = path.split('\\')[-1]
    for file in glob.glob(os.path.join(path,'*.*')):
        filename = os.path.basename(file)
        filename = os.path.splitext(filename)[0]+'_process_' + str(d_id) + os.path.splitext(filename)[-1]
        newfile = os.path.join(target_path,filename)
        os.renames(file,newfile)
    # remove result data
    for file in glob.glob(os.path.join(path,'result','*.*')):
        filename = os.path.basename(file)
        filename = os.path.splitext(filename)[0] + '_result_' + str(d_id) + os.path.splitext(filename)[-1]
        newfile = os.path.join(target_path,filename)
        os.renames(file, newfile)

if __name__ == '__main__':
    path = os.path.join('D:\\yuqing\\model_output', 'TJZ_JW - 副本')
    target_path = os.path.join('D:\\yuqing\\model_output', 'TJZ_JW - 副本')
    rename_and_move(path,target_path)
    # for m in ['1813',]:
    #     for i in range(10):
    #         index = m + '_' + str(i)
    #         path = os.path.join('D:\\yuqing\\model_output', index)
    #         target_path = os.path.join('D:\\yuqing\\model_output', m)
    #         rename_and_move(path,target_path)


