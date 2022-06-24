def TitleTest (MainPage, ExpectTitle):
  if(MainPage.title == ExpectTitle):
    print('√\n')
    print('当前页面标题正确')
  else:
    print('X\n')
    print('当前页面标题不正确，页面标题为'+MainPage.title)
 