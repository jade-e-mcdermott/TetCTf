# Super Calc

Html.

Pretty baisc

Just the result.

Uses an apache web server running on ubuntu

The html also has a comment

`<!-- Enjoy Tsu's Super Calculator <3, Not Only + - * / but also many other operators <3 <3 <3 -→`

Thats not a real html comment... it doesn't have a real ending line....

+-*/ and many other operators

Can I get it to overflow?

Whats the overflow for a double?

2,147,483,647

Overflow gives me a new result:

Its a youtube video

Nice. Its a meme

Its got an open ssh port.

So thats cool

The html comments say this is "Tsu's calculator.

Too bad there is no ssl or dns, no other names...

This took awhile.

`http://139.180.155.171/?calc=<2,147,483,647`

Hitting it with no param gives me this:

Request: `http://139.180.155.171/?`
Response:
```
jsx
<!-- Enjoy Tsu's Super Calculator <3, Not Only + - * / but also many other operators <3 <3 <3 -->

<?php

ini_set("display_errors", 0);

if(!isset($_GET["calc"])) 
{
    show_source(__FILE__);
}
else
{
    $wl = preg_match('/^[0-9\+\-\*\/\(\)\'\.\~\^\|\&]+$/i', $_GET["calc"]);
    if($wl === 0 || strlen($_GET["calc"]) > 70) {
        die("Tired of calculating? Lets <a href='https://www.youtube.com/watch?v=wDe_aCyf4aE' target=_blank >relax</a> <3");
    }
    echo 'Result: ';
    eval("echo ".eval("return ".$_GET["calc"].";").";");
}
```


`@ini_set( ‘display_errors’, 0 );`

Setup logging of all errors.

otherwise, they go to the /debug.log file?

maybe?

[https://bitofwp.com/blog/php-error-reporting-wordpress/#:~:text=%40ini_set](https://bitofwp.com/blog/php-error-reporting-wordpress/#:~:text=%40ini_set)(%20'display_errors'%2C,under%20the%20wp%2Dcontent%20directory

It makes it so errors are not displayed

Well.... it sends the errors to a file somewhere. Don't know where. Maybe the console?

After that, it is if the operation is NOT GET CALC, show the source file.

Hmmm... ok. so this file exists on the server. Ok cool.

Else.

If the string length is  larger than 70, or $wl === 0.  "die" and throw the meme link up.

Otherwise, keep going, 

echo: result:

`eval("echo ".eval("return ".$_GET["calc"].";").";");`

These look an awful lot like bash commands.

eval allows the execution of arbitrary PHP code.

Neat.

Ok.

So I just need to get the calculator to execute some PHP code for me.

focus on the user provided data.

[https://www.w3schools.com/php/func_misc_eval.asp](https://www.w3schools.com/php/func_misc_eval.asp)

Hmmmm...

So the first line looks like a regex.

Ok. What kind of rude thing can I do that technically matches this regex?

Also, is under 70 characters.

Hammmm if percent encoded, stuff might pass.

percent ended "wow"

%77%30%77

That does not match.... percent is a no go.

Characters to work with:

0-9

"+" 

addition, combine for inciment

"-" 

subtraction, combine for decrement

"*"

Multiplication, combine for exponentation

"/"

Division

"("

)

"'"

Single quote

.

String concatonator in php

~

NOT

"^"

Exclusive OR

|

bitwise OR inclusive

& 

bitwise AND

Hmmm... I don't get the equals sign.... but I get lots of stuff that may be combined with an equals sign to make an assignment operator

Ok. Will probs need the ()

so the preg_match function returns a 0 no match, 1 if match, and "false" if error.

Ok. So if you can force preg_match into an error, it will return false, which this code does not check for, so you can dump arbrtrary crap in there after that and it will execute in the eval statement later.

huhuhuhuhuhuhuhu

`http://139.180.155.171/?calc=99999999999999999999999999999999999%0A`

That is a percent encoded line feed at the end.

It gives this:

Result: 1.0E+35

That shouldn't work.

the reg ex should kick this out for having a percentage.

Hmmm.

Interesting. The version of the php I have running in w3schools rejects this.

It must have something to do with the 

`$_GET["calc"]` part

Ok. So I have bitwise operators, can I bitbang may way to some usefull commands?

What do I want?

I want to run something usefull in the "eval" statement. 

huh....

googled the $_GET variable.

it is an array populated anytime parameters are passed in.

[$_GET](https://www.php.net/manual/en/reserved.variables.get.php)

Fun fact, everything is passed through this first:

[https://www.php.net/manual/en/function.urldecode.php](https://www.php.net/manual/en/function.urldecode.php)

Url decode also converts plus symbols into a space character.

You can't do addition with this calculator.... it gets turned into a space, which fails the regex.

Well.. You can... provided you URL encode them first.

addition

[`http://139.180.155.171/?calc=9%2B9`](http://139.180.155.171/?calc=9%2B9)

### Day 2

Characters to work with:

0-9

"+" 

addition, combine for inciment

"-" 

subtraction, combine for decrement

"*"

Multiplication, combine for exponentation

"/"

Division

"()"

Paren

"'"

Single quote

.

String concatonator in php

~

NOT

"^"

Exclusive OR

|

bitwise OR inclusive

& 

bitwise AND

Options:

Ok. Lets break down the code that executes this crap and see if there is anything weird about it,

Can I eval anything interesting with numbers only?

I wonder if the bitwise and operator needs to be url encoded

Break down the code:

eval("echo ".eval("return ".$_GET["calc"].";").";");

execute the code in a string.

The string starts with "echo "

then add ".eval("

Then add "return "

Then add the injected string.

Then add ";"

Then add );;

echo result of:

return 2*2;

Seems to work like in C/Python. 

it gets returned to an echo statement.

Lets see if we can echo out bitwised new chars.

lets get an "A"

ascii: 65 or 0x41 or 101 in octal

01010&01010

result is 65.

0101&0101

result is 65.....

New test.

0146&02

This returns decimal 102. 

Thats flat out wrong.

oH BOY..

".0146&02."

this returns 0.0146.

Also wrong.

Its taking the bitwise and of.... floats?

🤮

Ok. For this example:

0146&02

returns 102

Is that really octal?

146&02 returns

146.

Also not expected.

expected results are:

2, 50 (ascii 2 in dec), 21 (ascii 2 in hex) 062 (ascii 2 in octal)

huh.

modifying the code in my local,

even without the return "146&02" yeilds 146

ok.

0146&02

yields 102.

But without the return it yields 0146

Turns out 102 is decimal for 0146, octal. 

Ayyyyyeee

That did it.

Its actually doing a bitwise and now.

Still shows up in the echo as decimal though. Hmmpf.

This payload surrounds it in single quotes

"%270146%27%26%2702%27"

the result is 0.

Huh.

I wonder if its evaluating it as a string for the bitwise operation?

I wonder if I can stick a "0" in front of the result to get it to interpret it as octal.

Didn't some forum say doing that would make it interpret it as something else if its a string?But its not a string, its an int.

# Day 3

options:

Figure out how to trick php's echo into interpreting a number as an ascii string.

maybe there is some other php command or trick we can pull with numbers and the operators given. 

Remember how carriage return made it through the regex but it shouldn't have. That was kind of interesting

Still works

999%0A

evaluates to 999

So I guess php just strips it out before it reaches the regex.