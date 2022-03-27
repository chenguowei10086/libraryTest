from LIB.P2P import BookPage
from selenium import webdriver
from hytest import *
import time
force_tags = ['login_test']
class UI_0101:
    name = '检查操作菜单 UI_0101'

    ddt_cases = [
        {
            'name': '登录 UI_0001',
            'para': ['2005050206', '123456', '123456','1234']
        },
        {
            'name': '登录 UI_0002',
            'para': ['2005050207',' 123456','123456','1234' ]
        },
        {
            'name': '登录 UI_0003',
            'para': ['2005050208', '123456','123456','1234' ]
        }
    ]

    # 初始化方法
    def setup(self):
        self.driver=webdriver.Chrome(r'C:\Users\86150\Desktop\chromedriver.exe')
        self.driver.get("http://localhost/")
        mainWindow = self.driver.current_window_handle
        GSTORE['mainWindow'] = mainWindow
        INFO('进入首页')
        self.driver.implicitly_wait(10)
        self.P2P=BookPage(self.driver)


    # 清除方法
    def teardown(self):
       self.driver.quit()

    def teststeps(self):
        STEP(1, '注册图书馆')
        # self.P2P.ZC()
        # username, password, cfpassword ,yzm, info = self.para
        #
        # if username is not None:
        #     self.P2P.userinput(username)
        #
        # if password is not None:
        #     self.P2P.passwordinput(password)
        #
        # if cfpassword is not None:
        #     self.P2P.passwordinput(cfpassword)
        #
        # if yzm is not None:
        #     self.P2P.passwordinput(yzm)
        #
        # notify = self.P2P.switch_to.alert.text
        #
        # CHECK_POINT('弹出提示', notify == info)
        #
        #
        #
        # self.P2P.zcsubmitclick()
        # self.P2P.TCDL()


        self.P2P.ZC()
        mainWindow = self.driver.current_window_handle
        self.P2P.userinput("2005050206")
        self.P2P.passwordinput("123456")
        self.P2P.cfpasswordinput("123456")
        self.P2P.zym("1234")
        self.P2P.zcsubmitclick()
        self.P2P.TCDL()
        STEP(2,'登录图书馆')
        self.P2P.DL()
        self.P2P.dluserinput("2005050206")
        self.P2P.dlpasswordinput("123456")
        self.P2P.zym("1234")
        self.P2P.dlsubmitclick()

        # STEP(3,'修改密码')
        # self.P2P.aqzx()
        # self.P2P.ysmm("123456")
        # self.P2P.xmm("123456")
        # self.P2P.qrxmm("123456")
        # self.P2P.submit()

        STEP(4,'dj')
        # mainWindow= GSTORE['mainWindow']
        self.P2P.switch_to(mainWindow)
        self.P2P.P2P_wyrz()
        # self.P2P.P2P_wytz()

        # STEP(5,'高级检索')
        # self.book.gjjssubmit()
        # self.book.gjjsinput("毛泽东")
        # self.book.ksjssubmit()
        # self.book.jsjgsz(2)
        # # time.sleep(3)
        # SELENIUM_LOG_SCREEN(self.book.driver, width='100%')
        # self.book.dhl('book_fldh')
        # # 点击列表
        # self.book.fldh_img('B')
        # # 选择类别图书
        # self.book.fldh_ztf("B1")
        # self.driver.switch_to.frame(self.driver.find_element_by_css_selector('#clsBrowse_book'))
        # self.driver.find_element_by_css_selector('#clsbookdiv > table > tbody > tr > td:nth-child(2) > span > a').click()
        # SELENIUM_LOG_SCREEN(self.book.driver, width='100%')
        # time.sleep(3)










