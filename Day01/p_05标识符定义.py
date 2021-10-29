'''
标识符: 开发人员在程序中自定义的一些符号和名称;
标识符是自己定义的,如变量名、函数名、类型名、文件名等
标识符由字母、下划线和数字组成,且数字不能开头
python中标识符是区分大小写的
'''
andy = 1
Andy = 2
print(andy)
print(Andy)

_abcd_1 = 3 # 这个命名是符合规则的
print(_abcd_1)

_1 = 111
print(_1)
'''
上面这个命名虽然是符合规则的,但是很少用因为我们还要尊崇命名规则:
1) 见名知意
    起一个有意义的名字,尽量做到看一眼就知道是什么意思(提高代码可读性)比如: 名字就定义为name,学生就定义为student
2) 驼峰命名法
    小驼峰命名法(lower camel case): 第一个单词以小写字母开始;第二个单词的首字母大写,例如: userName, userLoginFlag
    大驼峰命名法(upper camel case): 没一个单词的首字母都采用大写字母,例如: FirstName, LastName
3) 还有一种命名法是用下划线"_"来链接所有单词,比如: send_buf
    python一般用下划线"_"来定义标识符
'''