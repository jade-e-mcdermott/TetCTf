# HPNY

Get some lucky word or number for your new year!

[http://192.46.227.32/?roll=get_lucky_word](http://192.46.227.32/?roll=get_lucky_word)

Its got http and ssh open. Like last time.

root dir has the source.

[http://192.46.227.32/](http://192.46.227.32/)

```jsx
<!-- Let's pray for new year lucky things <3 -->

<?php

function get_lucky_word() {
    $words = array("Chuc mung nam moi", "gongxifacai", "happy new year!", "bonne année", "Akemashite omedeto gozaimasu", "Seh heh bok mahn ee bahd euh sae yo", "kimochi", "Feliz Año Nuevo", "S novim godom", "Gelukkig Nieuwjaar", "selamat tahun baru", "iniya puthandu nal Vazhthukkal");
    return $words[array_rand($words)];
}

function get_lucky_number() {
    $numb = rand(0,100);
    return strval($numb);
}

if(!isset($_GET["roll"])) {
    show_source(__FILE__);
}
else
{
    $wl = preg_match('/^[a-z\(\)\_\.]+$/i', $_GET["roll"]);

    if($wl === 0 || strlen($_GET["roll"]) > 50) {
        die("bumbadum badum");
    }
    eval("echo ".$_GET["roll"]."();");
}

?>
```

Presented use is to provide parameter "?roll=get_lucky_word"

Code breakdown from the top.

two functions.

get_lucky_word.

define array of words.

return one element from the array at random. 

Maybe. technically the line is: 

`return $words[array_rand($words)];`

Next function:

get_lucky_number

define a number, a psudo random int between in min and max.

If there is no value assigned to to "roll" as a parameter.

else

pass the value of parameter "roll" to a regex.

it matches 1 or more of:

characters a-z

"("

")"

"_"

"."

And then the end of the string.

If the regex finds no match. OR the contents of "roll" exceed 50 bytes

Display sassy error.

Else

Eval statement and an echo.

Oh jesus

The eval statement takes the user input and interprets it as this or that function name.

So i can type full php commands, yeah?

[http://192.46.227.32/?roll=scandir(.)](http://192.46.227.32/?roll=scandir(.))

this returns a 500 internal server error.

[http://192.46.227.32/?roll=scandir](http://192.46.227.32/?roll=scandir)

This returns a 200.... the "();"  part is concatonated at the end. So don't include it yourself.

🎇 Ayyyyyy

[http://192.46.227.32/?roll=getcwd](http://192.46.227.32/?roll=getcwd)

Returns this!

/var/www/html

I have a shell basicly!

No space

No semicolons

Also, unless you find a way to tie up the "();" into something else, basicly all your calls have to be functions with no arguments.

can I call python from php?

**list of legal chars**

characters a-z

"("

")"

"_"

"."

no "$" so no vars.

no "/" so no escape characters.

no spaces

**List of useful commands:** 

getcwd

given format:

"echo " + $var + "();"

echo $var();

Note that the first space is free.

echo a;

I think I need an environment to run my own php

Ok. Cool. I have a local env.

[http://localhost:8081/?roll=getcwd().getcwd](http://localhost:8081/?roll=getcwd().getcwd)

This works, outputs the local path twice.

So this proves I can chain two commands together, provided I end it with ".getcwd"

Ok.

shell_exec() executes random bash code.

[http://localhost:8081/?roll=shell_exec(ls).getcwd](http://localhost:8081/?roll=shell_exec(ls).getcwd)

This lists the contents of my local.

```jsx
fl4g_here_but_can_you_get_it_hohoho.php
index.php
/var/www/html
```

Possible ideas:

~-open a server to snag the file

Basicly poping a shell

Grab the file using the existing server, configure it so I can just GET it from my browser.

~-spawn a new process somehow that reaches out and does stuff.... lets me connect to it and run my own bash.

[https://flylib.com/books/en/1.545.1.47/1/](https://flylib.com/books/en/1.545.1.47/1/)
[https://null-byte.wonderhowto.com/how-to/use-command-injection-pop-reverse-shell-web-server-0185760/](https://null-byte.wonderhowto.com/how-to/use-command-injection-pop-reverse-shell-web-server-0185760/)

Looks like there are lots of ways to pop a shell, most of them require characters I can't use yet.

Run the file somehow.

Well, I think it technically runs when I call it from a http call like this:

`GET [http://192.46.227.32/fl4g_here_but_can_you_get_it_hohoho.php](http://192.46.227.32/fl4g_here_but_can_you_get_it_hohoho.php)`

It just returns a 200.

Get details for logging in via ssh.

php ftp is enabled. Maybe that is usefull

Call one php function and pass results into another php function

[https://www.php.net/manual/en/ref.funchand.php](https://www.php.net/manual/en/ref.funchand.php)

[https://www.php.net/manual/en/function.get-defined-functions.php](https://www.php.net/manual/en/function.get-defined-functions.php)

Current user is root. Fun.

All local environment vars.

Also fopen is configured to open files via url.

### Refocus

Ok. The hint

The mysterious function begin with "get"

Not get underscore.

Interesting *new* get function candidates

getmyuid

Get the php script owners userid

getmypid

Get phps process id

*getopt

read in command line arguments

Maybe usefull

getrusage

runs linux rusage command, gets processor info.

getallheaders

gets all the https headers from the current request

gettext

returns a translated string if one is found in the translation table, or the submited message if not found.

*****get_headers

Fetch all the headers sent by the server in response to an http request

get_meta_tags

Gets all the tags from an html file, returns them as an array. Would be handy, if I could type the filename.

Has a second argume3nt, use_include_path, that causes php to try and open the file along the standard include path.

getservbyname

Gets a port number associated with an internet service and protocol

**getservbyport

Get the internet service corresponding to the port and protocol.

Might be interesting to get the service of the ssh port.

getprotobynumber

Get the protocol name associated with protocol number

getlastmod

Gets the time of last page modification.