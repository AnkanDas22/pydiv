# I am pydiv!

----
## Available functions?

Integer Return:-
----
----
>intconvert(decimalnumber,numeratorlimit,denominatorlimit) 

Returns two arrays, first one with list of possible numerators and the second one with list of possible denominators. Matching indices of the two lists represent the numerator and denominator of a number.

**EXAMPLES:-**

1.
----
    import pydiv
    a=3.14
    x=100
    y=100
    m=pydiv.intconvert(a,x,y)
    print(m)

**WOULD PRINT**: 

>([22, 44, 66, 85, 88], [7, 14, 21, 27, 28])

i.e., a tuple containing the numerator list and the denominator list.

2.
----

    import pydiv
    a=3.14
    x=100
    y=100
    m,n=pydiv.intconvert(a,x,y)
    print(m)
    print(n)

**WOULD PRINT:**

>[22, 44, 66, 85, 88]

>[7, 14, 21, 27, 28]

i.e., two separate lists, one stored in m (storing numerator list) and the other in n (storing denominator list).


String Return:-
----
----

>convert(decimalnumber,numeratorlimit,denominatorlimit)

Returns a string array with possible division forms of a decimal number.

**EXAMPLE:-**

    import pydiv
    a=3.14
    x=100
    y=100
    m=pydiv.convert(a,x,y)
    print(m)

**WOULD PRINT:**

>['22/7', '44/14', '66/21', '85/27', '88/28']

i.e., a list of the possible division forms of a decimal number.


Made by Ankan Das, UEM-K
----