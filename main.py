import os
import cv2

import labelimg_xml

path_dir = os.getcwd()
original_dir = path_dir + '/original/'
result_dir = path_dir + '/result/'
current_filename = ''


def print_box(boxes, img):
    """
    bounding box 이미지에 출력해서 저장
    """
    print('print_box', end='', flush=True)
    names = ['WBC', 'RBC', 'Platelet']
    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
    for i, item in enumerate(boxes):
        color = colors[names.index(item[0])]
        xmin = item[1]
        ymin = item[2]
        xmax = item[3]
        ymax = item[4]
        cv2.rectangle(img, (xmin, ymin), (xmax, ymax), color, 2)
    cv2.imwrite(result_dir + current_filename, img)


def main():
    global current_filename
    img_list = [_ for _ in os.listdir(original_dir) if _.endswith('.jpg')]
    xml_list = [_ for _ in os.listdir(original_dir) if _.endswith('.xml')]

    for page, filename in enumerate(img_list):
        xmlname = xml_list[page]
        current_filename = filename
        if xmlname.split('.')[0] == filename.split('.')[0]:
            pass
        else:
            print('corrupted : ', filename)
        title, table = labelimg_xml.read_xml(original_dir, xmlname)
        img = cv2.imread(original_dir + current_filename)
        print_box(table, img)


if __name__ == '__main__':
    main()