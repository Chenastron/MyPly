
### 目录
1. 项目结构介绍
2. 语法介绍


### 1. 项目结构

```
myYacc
  - dyacc.py
  - settings.py
```
- dyacc.py是主出口
- settings是配置文件（目前配置了优先级）



### 2. 语法介绍
- 入口

```
entry -> start
start -> start stmt
      -> empty
```
1. (语法一)提供一个列表作为向外传递的接口
2. (语法二)由无数个语句(stmt)组成, 将每条语句都加入语法一中提供的列表

- 简单的语句

```
stmt -> SPLIT
stmt -> expression SPLIT
```
1. 语句可以是一个换行符或者是表达式加换行符

- 函数语句

```
Rule 1    stmt -> VAR ASSIGN LPAREN RPAREN block_format
Rule 2    stmt -> FUNC VAR LPAREN RPAREN block_format
Rule 3    stmt -> VAR ASSIGN LPAREN func_params RPAREN block_format
Rule 4    stmt -> FUNC VAR LPAREN func_params RPAREN block_format
Rule 5    func_params -> VAR
Rule 6    func_params -> func_params COMMA VAR
Rule 7    stmt -> VAR LPAREN RPAREN SPLIT
Rule 8    stmt -> VAR LPAREN expr_list RPAREN SPLIT
```
1. 函数语句(有声明和非声明的)分为2种 带参数的和不带参数的（127是无参数的, 238是带参数的）
2. 函数的声明又分为两种 一种是直接赋值给变量， 另一种是关键字func声明的 (13是第一种， 24是第二种)
3. 函数的参数由变量+逗号组成, 最终将形成一个list存放所有参数
4. 函数的声明会生成一个执行类的实例,action是函数赋值, 参数是变量名和语句组成的列表（代码块），如果有参数则传递参数列表
5. 函数的执行会生成一个执行类的实例，action是函数执行, 参数变量名, 如果有参数则传递参数列表

- print语句

```
stmt -> PRINT LPAREN expr_list RPAREN SPLIT
```
1. 生成一个执行类的实例，action是print, 参数为表达式列表

- for语句

```
stmt -> FOR VAR IN range block_format
range -> RANGE LPAREN expr_list RPAREN
```
1.  生成一个执行类的实例，action是loop, 参数为for循环中的变量, range的list ,语句块
2. range是通过start, stop step生成一个列表, 不包含stop