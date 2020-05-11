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


# def prefix(record):
#     """
#     如果需要去掉URL的前缀可以用这个函数确认前缀以便删除  # 可以取消注释来识别前缀
#     :param record: 日志数据
#     :return: 返回相应的前缀
#     """
#     prefix_search = re.search('"(.*?) /', record).group()
#     return prefix_search
#
#
# prefix_all = set()  # 所有前缀去重
# with open('网站访问日志.txt') as web_log:
#     for line in web_log:
#         if line.startswith('-'):
#             continue
#         prefix_all.add(prefix(line))
# print(prefix_all)

ip = []  # IP地址列表
ip_set = set()  # IP地址列表去重（集合）
time_record_sum = []  # 所有记录的时间点的'时'的集合列表
hour_record_dict = {}  # 以小时为key，pv条数和为value的字典
hour_ip_dict = {}
pv_url = []  # URL列表
device_sum = []  # 访问设备列表
device_dic = {}  # 访问设备:访问量字典
top_pv = {}  
top_uv = {}

file = customer_input()

with open(file) as web_log:
    for line in web_log:
        if line.startswith('-'):  # 若开头无ip地址，不作为计算内容
            continue
        elif device(line) is not None:
            ip.append(ip_uv(line))  # uv总计
            ip_set.add(ip_uv(line))  # uv去重
            pv_url.append(url_pv(line))  # pv总计
            device_sum.append(str(device(line).group()))  # 设备总计
            time_record_sum.append(hour_record(line))  # 时间总计

print("uv总数:", len(ip_set))
print("pv总数:", len(pv_url))

print('设备及其访问量'.center(100, '-'))
device_set = set(device_sum)  # 访问设备集合，列表去重
for single_device in device_set:  # 设备:设备访问量字典
    device_dic[single_device] = device_sum.count(single_device)
for device_name, visit_amount in device_dic.items():
    print("设备访问量：%s  设备名称：%s  " % (visit_amount, device_name))

print('top 10访问量页面'.center(100, '-'))
for top in set(pv_url):  # 生成url为value，访问量为key的字典
    top_pv[pv_url.count(top)] = top
for visit_sum in reversed(sorted(top_pv.keys())[-10:]):
    print("top10访问量的URL（访问量:URL）：", visit_sum, ":", top_pv[visit_sum])

print('top 10uv的IP地址'.center(100, '-'))
for single_ip in ip_set:  # 生成以ip为value，访问量为key的字典
    top_uv[ip.count(single_ip)] = single_ip
for amount in reversed(sorted(top_uv.keys())[-10:]):
    print("top10访问量的IP（访问量:IP）：", amount, ":", top_uv[amount])

print('每小时的pv数（据流量大小排序）'.center(100, '-'))
for exact_hour in set(time_record_sum):  # 生成访问量:时的字典
    hour_record_dict[time_record_sum.count(exact_hour)] = exact_hour
for pv in reversed(sorted(hour_record_dict.keys())):
    print(hour_record_dict[pv], '时：', pv, '条pv')

print('每小时的uv数(据小时排序)'.center(100, '-'))
hour_record_set = set(time_record_sum)  # 小时记录的访问集合，列表去重
for recorded_hour in hour_record_set:
    hour_ip_dict[recorded_hour] = []
with open(file) as web_log:
    for line in web_log:
        if line.startswith('-'):  # 若开头无ip地址，不作为计算内容
            continue
        elif device(line) is not None:
            hour = hour_record(line)
            hour_ip_dict[hour].append(ip_uv(line))
for hour in sorted(hour_ip_dict.keys()):
    print(hour, '时:', len(hour_ip_dict[hour]), '访问的IP总数')
print(hour_ip_dict['00'],'\n',len(set(hour_ip_dict['00'])))