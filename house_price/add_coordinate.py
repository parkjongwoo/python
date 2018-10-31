import os
import csv
import requests
import json
import time

road_addr_request_url = 'http://www.juso.go.kr/addrlink/addrLinkApi.do'
confmKey_road = 'U01TX0FVVEgyMDE4MTAzMTA3MzY1NjEwODI2ODg='
currentPage = 1
countPerPage = 10
keyword = None
resultType = 'json'

coord_request_url = 'http://www.juso.go.kr/addrlink/addrCoordApi.do'
confmKey_coord = 'U01TX0FVVEgyMDE4MTAzMTA3MTgyOTEwODI2ODc='
currentPage = 1
countPerPage = 10
keyword = None
resultType = 'json'


def request_road_info_from_addr(coord_request_url, confmKey, currentPage, countPerPage, addr, resultType):
    result = None
    data = {
        'confmKey':confmKey,
        'currentPage' : currentPage,
        'countPerPage' : countPerPage,
        'keyword' : addr,
        'resultType' : resultType
    }
    res = requests.post(coord_request_url,data=data)
    result = res.json()
    return result


def request_coord_from_road_info(coord_request_url, confmKey, admCd, rnMgtSn, udrtYn, buldMnnm, buldSlno, resultType):
    result = None
    data = {
        'confmKey':confmKey,
        'admCd' : admCd,
        'rnMgtSn' : rnMgtSn,
        'udrtYn' : udrtYn,
        'buldMnnm' : buldMnnm,
        'buldSlno' : buldSlno,
        'resultType' : resultType
    }
    res = requests.post(coord_request_url,data=data)
    result = res.json()
    return result


def get_source_files(path):
    file_list = os.listdir(path)
    result = []
    for fname in file_list:
        if(os.path.isfile(path+fname)):
            result.append(fname)
    return result


def get_copy_file_name(original_file_name):
    file_info = original_file_name.split('.')
    file_name = file_info[0]
    file_ext = file_info[1]
    return file_name+'_copy.'+file_ext


def makeDirIfNotExist(target_folder):
    if (not os.path.isdir(target_folder)):
        try:
            os.mkdir(target_folder)
        except OSError:
            print("Creation of the directory %s failed" % target_folder)
        else:
            print("Successfully created the directory %s " % target_folder)


def createlog(row):
    makeDirIfNotExist(log_folder)
    with open(log_folder + log_filename, 'a', newline='', encoding='utf-8') as outputfile:
        outputfile.write('error:\t['+','.join(row)+']')

source_folder = './data/'
target_folder = './output/'
log_folder = './log/'
log_filename = 'log.txt'
original_file_list = get_source_files(source_folder)

makeDirIfNotExist(target_folder)

for source_file in original_file_list:
    with open(source_folder + source_file, newline='', encoding='utf-8') as csvfile:
        filereader = csv.reader(csvfile, delimiter='\t', quotechar='"')

        with open(target_folder + get_copy_file_name(source_file), 'w', newline='', encoding='utf-8') as outputfile:
            filewriter = csv.writer(outputfile, delimiter='\t', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
            for row in filereader:
                print('keyword_addr:'+row[3])
                road_addr_info = request_road_info_from_addr(road_addr_request_url, confmKey_road, currentPage, countPerPage, row[3], resultType)
                # print(road_addr_info)
                try:

                    road_juso = road_addr_info['results']['juso'][0]
                    coord_info = request_coord_from_road_info(coord_request_url, confmKey_coord, road_juso['admCd'], road_juso['rnMgtSn'], road_juso['udrtYn'], road_juso['buldMnnm'], road_juso['buldSlno'], resultType)
                    print(coord_info)
                    coord_juso = coord_info['results']['juso'][0]
                    row[0] =  coord_juso['entX']
                    row[1] =  coord_juso['entY']
                    filewriter.writerow(row)
                except:
                    createlog(row)
                time.sleep(0.35)









