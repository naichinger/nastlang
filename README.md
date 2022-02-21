# nastlang

naichinger - stackbased - language

nastlang is a stack based programming language.

## Docs

- add: takes two integers from stack and puts result on stack
- mul: same as add
- div: same as add
- sub: same as add

- if - end: takes one element from stack if 0, block is not entered
- while - end: takes with every iteration one value from stack 0 loop is not continued

- ! : takes two values from stack (bsp: 0 var ! # stores 0 in var) 


- print: takes one element from stack and prints it
- save: saves state of stack
- restore: restores befores saved stack
- size: puts length of stack onto the stack

## examples

### fibonacci
```fs
0 a !
1 b !

15 len !

len while
    a print
    " " print
    b c !
    a b add b !
    c a !
    len 1 sub len ! len
end
```

### pyramid

```fs
10 max !
1 len !

len while
    0 len3 ! 
    1 while
        " " print
        len3 1 add len3 ! len3 max len sub lessThan
    end

    1 len2 !
    len2 while
        "#" print
        len2 1 add len2 ! len2 len 2 mul less
    end
    "\n" print
    len 1 add len ! len max lessThan
end
```
