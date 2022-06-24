def DataShow(fulltest):
  if(fulltest.TestClear):
    print("测试通过\n")
  else:
    print("测试未通过\n")
  print("测试总数:")
  print(fulltest.TestCount)
  print("测试通过数:")
  print(fulltest.TestClearCount)
  print("测试未通过数:")
  print((fulltest.TestCount-fulltest.TestClearCount))