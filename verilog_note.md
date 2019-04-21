
# Verilog HDL
- 由模块构成 每个模块由module endmodule包装
- 模块可层次嵌套 可将大型电路分割为小模块
- 模块*2  1为让模块最终能生成电路的结构 2为测试设计电路的逻辑功能
- 每个模块 端口定义 说明输入输出口
- 每个语句和数据定义最后有分号
- /\* */ 注释

## module
### definition
- 模块名 module module_name(口1,口2,口3,口4,...);
- I/O口  input/output/inout[信号位宽-1:0]端口名i; 或 mudule mudule_name(input port1,output port1,...);
- 内部信号 reg/wire[width-1:0]R变量1,R变量2...;

### function
1. assign a=b&c;
2. 实例元件  and #2 ul(outp1,inp1,inp2);
3. always
```
always @(posedge clk or posedge clr)
begin
  if(clr) q<=0;  //<=为赋值运算

   else if(en) q<=d;
end   
```

### Tips
1. 所有过程块(如initial,always), 连续赋值,实例引用都是并行的
2. 他们表示的是一种通过变量名互相连接关系
3. 同一模块三者出现的先后顺序无关
4. 只有连续赋值语句assign和实例引用语句可以独立于过程块而存在于模块功能定义部分
- bufifl mybuf(out,in,enable) //库原件三态驱动元件实例化为mybuf
- mytri tri_inst(.out(sout),.in(sin),.enable(ena)); //实例化自定义模块myfri .表示引用模块的端口

### costant
1. number  2=B ,10=D ,16=H ,8=O <位宽><进制><__数字__>
> 8'b10101100
> 8'ha2

2. x and z/? --->
x代表不定值 z/?代表高阻值
3. 负数 -8'd5
4. underscore_ 只能用在具体数字间提高可读性

### parameter
- 定义一个标识符代表一个常量　

```
parameter 参数名１＝表达式,...,参数名n=表达式;
e.x.m.:
module Decode(A,F);
  parameter Width=1,Polarity=1;
  ...
  ...
endmodule
module Top;
  wire[3:0] A4;
  wire[4:0] A5;
  wire[15:0] F16;
  wire[31:0] F32;
  Decode #(4,0)  D1(A4,F16);  /*#改变定义的常量*/
  Decode #(5) D2(A5,F32);
endmodule  


```




```
initial   //寄存器变量初始化
begin
  ain=0;
  bin=0;
end
```

##### always
```
always # 50 clock = ~clock; //产生一个重复/周期为100个时间单位的时钟信号

always @(posedge clock)
  begin               //{$random}为系统任务 产生随机数
      ain={$random}%2;  //产生随机的位信号流ain %2为模2运算 有时为1有时为0
  #3  bin={$random}%2;   //延迟三个时间单位后产生随机位信号流
end      
always #10000 select=!select ; //产生周期为10000个单位时间的选通信号变化
```
####　变量
wire型数据常用来表示以assign关键字指定的组合逻辑信号，模块输出输入信号类型默认wire型．
```
wire a;
wire [7:0] b;
wire [4:1] c,b;
```
reg 寄存器是数据存储单元的抽象．always块内被赋值的每一个信号都必须为reg

reg [n-1,0] 数据名1,2,3...;

memory
通过对reg变量建立数组对存储器建模，可以描述ram ,rom 存储器和reg文件
reg [n,1] memename[m:1]; 有个 n位存储器

|运算符|作用|
|--|--|
| % |  取余 |
|  ~ & | 反　、按位与  |
| ｜   | 按位或  |
| ^  |  按位异或 |
|^~   |   按位同或|
|  ＆＆ |逻辑与   |
|｜｜   |  逻辑或 |
|！   |  逻辑非 |
|  ＝＝ | 等于  |
|！＝   |   不等于|
|＝＝＝   |   |
|！＝＝   |   |
|<< >>  | 移位  |
|{}   |位拼接   | exm:{b,{2{a,b}}}//{b,a,b,a,b}|

#### 块语句
1. 顺序块
```
begin
  语句１;
  #10 语句２ //延时10个时间单位
  ...
  语句Ｎ;
end  
```
2. 并行块
fork
  语句1xx;
  语句2xx;
join

#### 条件语句
if(xxx)
    begin
    if(xx)
      xxx;
    end  
  else if(xxx)
    xxx;
  else
    xxx;
