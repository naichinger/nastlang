# nastlang

naichinger - stackbased - language

nastlang is a stack based programming language.

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