from flask import Flask, render_template, request, make_response
import operator as op

app = Flask(__name__)
application = app

operations = ['+', '-', '*', '/']
operations_functions = {'+': op.add, '-': op.sub, '*': op.mul, '/': op.truediv}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/args')
def args():
    return render_template('args.html')    

@app.route('/headers')
def headers():
    return render_template('headers.html')   

@app.route('/cookies')
def cookies():
    resp = make_response(render_template('cookies.html'))
    if 'username' in request.cookies:
        resp.set_cookie('username', 'some name', expires=0)
    else:
        resp.set_cookie('username', 'some name')
    return resp     

@app.route('/form', methods=['GET', 'POST'])
def form():
    return render_template('form.html')   

@app.route('/phone', methods=['GET', 'POST'])
def phone():
    format_num = None
    error_msg = None
    num = request.form.get('tel_num')
    if num != None:
        if num.find('-') != -1: 
            num=num.replace('-','')
        if num.find('(') != -1: 
            num=num.replace('(','')
        if num.find(')') != -1: 
            num=num.replace(')','') 
        if num.find('.') != -1: 
            num=num.replace('.','') 
        if num.find('+') != -1: 
            num=num.replace('+','')  
        if num.find(' ') != -1: 
            num=num.replace(' ','')  

        if num.isdigit():
            if len(num) == 10:
                format_num = '8-{}-{}-{}-{}'.format(num[0:3], num[3:6], num[6:8], num[8:])
                
            elif len(num) == 11:
                if num[0] =='7' or num[0] == '8':
                    format_num = '8-{}-{}-{}-{}'.format(num[1:4], num[4:7], num[7:9], num[9:])
            else:
                error_msg = 'Недопустимый ввод. Неверное количество цифр.'
        else:       
            error_msg = 'Недопустимый ввод. В номере телефона встречаются недопустимые символы.' 
    return render_template('phone.html', format_num=format_num, error_msg=error_msg) 



@app.route('/calc', methods=['GET', 'POST'])
def calc():
    try:
        result = None
        error_msg = None
        op1 = float(request.args.get('operand1'))
        op2 = float(request.args.get('operand2'))
        #operation = request.args.get('operation')
        f = operations_functions[request.args.get('operation')]
        result = f(op1, op2)
         
    except ValueError:
        error_msg = 'Пожалуйста, вводите только числа.'
    except ZeroDivisionError:
        error_msg = 'На ноль делить нельзя!'
    except KeyError:
        error_msg = 'Недопустимая операция.'
    return render_template('calc.html', operations=operations, result=result, error_msg=error_msg)  