
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
- settings是配置文件（目前配置了优先级）， 会向外提供一个tuple供dyacc.py引入


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
2. range是通过start, stop step生成一个列表, 不包含stop(可以由大变小, 也可以由小变大)

- if-else语句

```
stmt -> IF condition_list block_format
     -> IF condition_list block_format ELSE block_format
```
1.  生成一个执行类的实例，action是condition, 如果没有else则传入两个参数为别为条件语句, 代码块, 如果有else则在多传入一个代码块 

- block语句

```
block_format -> START_BLOCK SPLIT block END_BLOCK SPLIT
block -> stmt
      -> block stmt
```
1. block_format规定了{xxx}代码块的格式
2. block语法则由多个语法形成, 最终生成一个新的多个语句的list

- 赋值语法

```
stmt -> VAR ASSIGN expression SPLIT
     -> VAR ASSIGN condition_list SPLIT
     -> if_assign IF condition_list ELSE expression SPLIT
if_assign -> VAR ASSIGN expression
```
1. 将表达式的值赋值给变量
2. 将逻辑表达式的值赋值给变量
3. 三元表达式赋值
4. 前两种会生成一个执行类的实例，action是assign, 参数是变量名和表达式的实例
5. 三元表达式会生成一个执行类的实例，action是triple_assign, 参数是变量名和逻辑表达式的实例, 逻辑表达式为true时执行的表达式实例, 和false时执行的表达式实例

- 多个表达式连接

```
Rule 26    expr_list -> expression
Rule 27    expr_list -> expr_list COMMA expression
```
1. 由逗号进行连接的表达式
2. 生成一个表达式的列表

- 逻辑语句

```
Rule 28    condition_list -> expression
Rule 29    condition_list -> condition_list AND expression
Rule 30    condition_list -> condition_list OR expression
```
1. 由and或or组成的表达式构成逻辑表达式
2. 生成一个类似栈的容器, 存放着每个表达式和逻辑操作符
3. 生成一个执行类的实例，action是logop, 参数是2中提到的栈

- 括号

```
Rule 31    condition_list -> LPAREN condition_list RPAREN
Rule 45    expression -> LPAREN expression RPAREN
```
1. 两个表达式的括号用法


- 表达式间的二元操作

```
Rule 32    expression -> expression ADD expression
Rule 33    expression -> expression REM expression
Rule 34    expression -> expression MUL expression
Rule 35    expression -> expression DIV expression
Rule 36    expression -> expression MOD expression
Rule 37    expression -> expression GT expression
Rule 38    expression -> expression LT expression
Rule 39    expression -> expression GE expression
Rule 40    expression -> expression LE expression
Rule 41    expression -> expression EQ expression
Rule 42    expression -> expression NE expression
Rule 43    expression -> expression POW expression
```
1. 生成一个执行类的实例，action是binop, 参数是两个表达式和中间的操作符

- 表达式的终结符
```
Rule 44    expression -> REM NUMBER
Rule 46    expression -> TRUE
Rule 47    expression -> FALSE
Rule 48    expression -> NUMBER
Rule 49    expression -> STRING
Rule 50    expression -> VAR
```

