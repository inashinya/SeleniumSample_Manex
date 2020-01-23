import os
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

# マネックス_ログインページ
url_manex_login = 'https://mst.monex.co.jp/pc/ITS/login/LoginIDPassword.jsp'
# 保有残高・口座管理＞保有残高　のページ
# MY PAGE＞余力情報（サマリ）　のページ
# マイページ＞保有残高・口座管理　【株式】　のページ
# マイページ＞信用取引＞建玉一覧　のページ
# 保有残高・口座管理＞取引履歴＞全取引履歴　のページ
# 保有残高・口座管理＞株式取引＞注文約定一覧＞約定済注文　のページ
# 取引利益のページ
url_manex_tradehistory = 'https://mxp2.monex.co.jp/pc/servlet/ITS/asset/DealArchive?attrSrcKey=f11b729143a73fba13'
# 売却損益明細のページ
url_manex_statement = 'https://mxp2.monex.co.jp/pc/servlet/ITS/asset/SailPlDetail?attrSrcKey=16efd5e8542d'   # マネックス

LoginId = '144159258'
LoginPass = 'eBg%3479'

path = "C:/Users/ina.shinya/Downloads/chromedriver_win32/chromedriver.exe"
DRIVER_PATH = os.path.join(os.path.dirname(path), "chromedriver")
driver = webdriver.Chrome(DRIVER_PATH)                                            # 非headlessモード

driver.get(url_manex_login)
time.sleep(2)

id_box = driver.find_element_by_id("loginid")                          # ログインID入力ボックス
id_box.send_keys(LoginId)                                              # ログインID入力ボックスにIDを入力
time.sleep(1)
password_box = driver.find_element_by_id("passwd")                    # ログインパスワード入力ボックス
password_box.send_keys(LoginPass)                                     # パスワード入力ボックスにパスワードを入力
time.sleep(1)

driver.find_element_by_xpath("//input[@value='ログイン']").click()    # ログインボタンをクリック
time.sleep(2)

# 取引履歴を取得
driver.get(url_manex_tradehistory)

# 売却損益明細を取得
driver.get(url_manex_statement)
def statement_select_form():
    fromDate_element = driver.find_element_by_css_selector("select[name=fromDate]")
    fromDate_select_element = Select(fromDate_element)
    fromDate_select_element.select_by_value('201901')

    toDate_element = driver.find_element_by_css_selector("select[name=toDate]")
    toDate_select_element = Select(toDate_element)
    toDate_select_element.select_by_value('202001')

def statement_submit():
    driver.find_element_by_css_selector("input[value='この条件で検索']").click()

statement_select_form()
time.sleep(1)
statement_submit()

