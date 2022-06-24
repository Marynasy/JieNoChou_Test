from time import sleep

class Test:
  TestCount = 0
  def __init__(self, TestClear, TestClearCount):
    self.TestClear = TestClear
    self.TestClearCount = TestClearCount
  
  '''@titletest.abstractmethod'''
  def TitleTest(self,MainPage, ExpectTitle):
    self.TestCount += 1
    print("标题测试开始:")
    if(MainPage.title == ExpectTitle):
      self.TestClearCount += 1
      print('√\n')
      print('当前页面标题正确')
    else:
      self.TestClear = 0
      print('X\n')
      print('当前页面标题不正确，页面标题为'+MainPage.title)
      
  def LogoTest(self,MainPage):
    self.TestCount += 1
    print("Logo测试开始:")
    Logo = MainPage.find_element_by_class_name('logo')
    if(Logo.is_displayed):
      self.TestClearCount += 1
      print('√\n')
      print('当前页面Logo已显示')
    else:
      self.TestClear = 0
      print('X\n')
      print('当前页面Logo未显示')
