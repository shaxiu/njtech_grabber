from selenium import webdriver
import time

option = webdriver.ChromeOptions()
option.add_experimental_option(
    "excludeSwitches", ['enable-automation', 'enable-logging'])

driver = webdriver.Chrome(
    # chromedriver.exe 位置
    executable_path="C:/Program Files/Google/Chrome/Application/chromedriver.exe", options=option)

driver.get(
    'https://jwgl.njtech.edu.cn/xsxk/zzxkyzb_cxZzxkYzbIndex.html?gnmkdm=N253512&layout=default')

try:
    # 获取输入框元素
    username = driver.find_element_by_id('yhm')
    passwd = driver.find_element_by_id('mm')
    # 账号密码填写
    username.send_keys('学号')
    passwd.send_keys('密码')
    # 登录
    login = driver.find_element_by_id('dl')
    login.click()
    # 等待跳转完毕
    while(driver.title != "本科教学管理与服务平台"):
        break
    time.sleep(2)
    # 搜索框输入 尔雅
    searchinput = driver.find_element_by_name('searchInput')
    searchinput.send_keys("尔雅")
    # 选课类型
    # 人文类
    # rw_btn = driver.find_element_by_xpath("//li[@index='kcgs_list_12']")
    # rw_btn.click()
    # 点击有余量按钮（筛选未满的课程）
    yl_btn = driver.find_element_by_xpath("//li[@index='yl_list_1']")
    yl_btn.click()
    while(1):
        # 点击搜索
        search = driver.find_element_by_xpath(
            "//button[@class='btn btn-primary btn-sm']")
        search.click()
        time.sleep(0.4)
        # 查看结果
        # 判断是否有数据
        try:
            # 无数据
            temp = driver.find_element_by_class_name('nodata')
            continue
        except:
            results = driver.find_elements_by_xpath(
                "//div[@class='tjxk_list']//div[@class='panel panel-info']")
            for item in results:
                # 课程名称
                coursename = item.find_element_by_class_name('kcmc')
                print(coursename.text)
                # 面板展开状态
                panel_expand = item.find_element_by_class_name(
                    'expand_close')
                # 如果面板为展开
                if(panel_expand.get_attribute('class') == 'expand_close expand1'):
                    panel_expand.click()
                    time.sleep(0.4)
                # 课程状态：已选/未选
                kch_id = item.find_element_by_name(
                    'kch_id').get_attribute('value')
                zt = item.find_element_by_id('zt_txt_'+kch_id)
                print(zt.text)
                full = item.find_element_by_class_name('full')
                print(full.text)
                # 条件判读，若已选或者课程已满则跳过
                if(zt.text != "状态：未选" or full.text == "已满"):
                    print("跳过")
                    continue
                # 选课按钮
                course_btn = item.find_element_by_tag_name('button')
                print(course_btn)
                course_btn.click()
                try:
                    close_btn = driver.find_element_by_id('btn_ok')
                    close_btn.click()
                except:
                    print("本课程已抢到！")
except:
    print('fail')
