import re
import os


def customer_input():
    """
    寻求客户输入的函数，客户输入文件名以打印相关信息
    :return: 返回正确的文件名
    """
    user_input = input('请输入完整的文件名以查询相关信息(包括.txt尾缀): ')
    while os.path.isfile(user_input) is False:
        print('输入错误请重新输入！')
        user_input = input('请输入完整的文件名以查询相关信息(包括.txt尾缀): ')
    return user_input


def ip_uv(record):
    """
    ip地址匹配
    :param record: 日志数据
    :return:  返回从record取出的uv字符串
    """
    uv = re.search(r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}', record).group()
    return uv


def hour_record(record):
    """
    时间匹配
    :param record: 日志数据
    :return: 返回相应的小时
    """
    time_u = re.search(r':\d{2}', record).group().strip(':')

    return time_u


def url_pv(record):
    """
    URL匹配
    :param record: 日志数据
    :return: 返回从record所取的url
    """
    url = re.search('"(.*?)HTTP', record).group().rstrip(' HTTP').lstrip('"')
    return url


def device(record):
    """
    访问设备匹配
    :param record: 日志数据
    :return: 返回访问的设备名
    """
    visit_device = re.search(r'\((.*?)\)', record)
    # visit_device = re.search("Mozilla/.*", record)  # 有一个Mozilla/4.0" 后面没有跟具体的device的如果要算上这个就用这条
    return visit_device


ip = []  # IP地址列表
hour_record_dict = {}  # 以小时为key，pv条数和为value的字典
pv_url = []  # URL列表
device_dic = {}  # 访问设备:访问量字典
top_pv = {}
top_uv = {}

file = customer_input()

with open(file) as web_log:
    web_log_data = []
    for line in web_log:
        if line.startswith('-'):  # 若开头无ip地址，不作为计算内容
            continue
        elif device(line) is not None:
            web_log_data.append(line)

for info in web_log_data:
    device_dic.setdefault(device(info).group(), [])
    device_dic[device(info).group()].append(1)
    ip.append(ip_uv(info))
    pv_url.append(url_pv(info))
    hour_record_dict.setdefault(hour_record(info),[])
    hour_record_dict[hour_record(info)].append(ip_uv(info))

print('uv总数:', len(set(ip)))
print("pv总数:", len(web_log_data))

print('设备及其访问量'.center(100, '-'))
for device_name in device_dic:
    print("设备访问量：%s  设备名称：%s  " % (len(device_dic[device_name]), device_name))

print('top 10访问量页面'.center(100, '-'))
for top in set(pv_url):
    top_pv[pv_url.count(top)] = top
for visit_sum in reversed(sorted(top_pv.keys())[-10:]):
    print("top10访问量的URL（访问量:URL）：", visit_sum, ":", top_pv[visit_sum])

print('top 10uv的IP地址'.center(100, '-'))
for single_ip in set(ip):
    top_uv[ip.count(single_ip)] = single_ip
for amount in reversed(sorted(top_uv.keys())[-10:]):
    print("top10访问量的IP（访问量:IP）：", amount, ":", top_uv[amount])

print('每小时的pv数'.center(100, '-'))
for exact_hour in hour_record_dict:
    print(exact_hour, '时：', len(hour_record_dict[exact_hour]), '条pv')

print('每小时的uv数'.center(100, '-'))
for exact_hour in hour_record_dict:
    print(exact_hour, '时:', len(set(hour_record_dict[exact_hour])), '访问的IP总数')