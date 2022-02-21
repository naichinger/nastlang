from threading import stack_size
from typing import List
import sys

def parse_lang(inp: str):
    #lang_str = ' '.join([i[:i.index("#")] if '#' in i else i for i in inp.split("\n")])
    #.replace("\n"," ")
    lang_str = inp
    start_block = ["if", "while"]
    lang = []

    cur = ""
    in_str = False
    skip_len = 0
    for idx,i in enumerate(lang_str):
        if(skip_len > 0):
            skip_len-=1
            continue
        if not in_str and i == "\"":
            cur = cur + i
            in_str = True
        elif in_str and i == "\"":
            cur = cur + i
            in_str = False
        elif in_str:
            cur = cur + i
        elif i == ' ' or i == '\n':
            #print(cur)
            if(cur != "" and cur in start_block):
                leng, block = parse_lang(lang_str[idx:])
                skip_len = leng
                lang.append(cur)
                lang.append(block)
            elif(cur == "end"):
                return idx, lang
            elif cur != "":
                lang.append(cur)
            cur = ""
        else:
            cur = cur + i

    if(cur == "end"):
        return idx, lang
    elif cur != "":
        lang.append(cur)
    return lang

def apply_arithmetic(val1, val2, i):
    if(i == "add"):
        return val2 + val1
    elif(i == "sub"):
        return val2 - val1
    elif(i == "mul"):
        return val2 * val1
    elif(i == "div"):
        return val2 / val1

def apply_comprators(val1, val2, i):
    if(i == "greater"):
        return val2 > val1 if 1 else 0
    elif(i == "greaterThan"):
        return val2 >= val1 if 1 else 0
    elif(i == "less"):
        return val2 < val1 if 1 else 0
    elif(i == "lessThan"):
        return val2 <= val1 if 1 else 0

def parse_val(inp: str):
    if(inp.isnumeric()):
        return int(inp)
    else:
        return inp

def is_var(inp:str):
    return inp[0] == "\"" or inp.isnumeric()

def con_val(inp, vars):
    if(inp in vars):
        return vars[inp]
    return inp

def print_method(val):
    if(isinstance(val, str)):
        print(val[1:-1].encode('raw_unicode_escape').decode('unicode_escape'),end='')
    else:
        print(val,end='')

stack = []
states = []
def interpret_lang(inp: List[str],vars):
    global stack
    arithmetic = ["mul", "div", "add", "sub"]
    comperators = ["greater", "greaterThan", "less", "lessThan"]
    idx = 0
    while idx < len(inp):
        i = inp[idx].strip()
        idx = idx +1
        if(i in arithmetic):
            stack.append(apply_arithmetic(con_val(stack.pop(), vars),con_val(stack.pop(), vars), i))
        elif(i in comperators):
            stack.append(apply_comprators(con_val(stack.pop(), vars),con_val(stack.pop(), vars), i))
        elif(i == "print"):
            print_method(con_val(stack.pop(), vars))
        elif(i == "duplicate"):
            v = stack.pop()
            stack.append(v)
            stack.append(v)
        elif(i == "pop"):
            stack.pop()
        elif(i == "save"):
            states.append(stack.copy())
        elif(i == "restore"):
            stack = states.pop()
        elif(i == "size"):
            stack.append(len(stack))
        elif(i == "if"):
            if(con_val(stack.pop(), vars) != 0):
                interpret_lang(inp[idx],vars)
            idx = idx + 1
        elif(i == "while"):
            if(con_val(stack.pop(), vars) == 0):
                idx = idx + 1
            else:
                interpret_lang(inp[idx],vars)
                idx = idx - 1
        elif(i == "!"):
            name = stack.pop()
            val = stack.pop()
            vars[name] = con_val(val, vars)
        else:
            stack.append(parse_val(i))

#lang = parse_lang(open("examples/fib.lang").read())
lang = parse_lang(open(sys.argv[1]).read())
#print(lang)
interpret_lang(lang,{})