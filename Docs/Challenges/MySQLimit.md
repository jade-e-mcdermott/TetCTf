# MySQLimit

id=1

handsome_flag

id=2

ugly_flag

id=3

amazing_goodjob_flag

## Breaking down the code.

contents of "id" param passed through regex to get rid of a bunch of MySql statements.

The, passed through a function called "mysqli_real_escape_string()" this returns a variable called "id"

The, a querry is built using a string with "id" tacked on at the end.

"select * from flag_here_hihi where id=" + $id

select everything from table flag_here_hihi where the contents of column ID = "Id"

Then, there is an if that I THINK means "if the results of the querry are blank, echo the results of function "mysqli_error"

else

echo "<br>"

then, extract from variable run_querry variable fetch_array[1] first element.

echo the results

## Thoughts

So user input is not "evaled"

but user input is tacked onto the end of an SQL querry.

Time to try a new approach, escape chars don't seem to be working.

The sql statement:

select * from flag_here_hihi where id=" + $id;

The hint is MySQL limit

Looks like percent encoded carriage returns may not work.

the function myswli_real_escape_string does something with these characters

NUL (ASCII 0), \n, \r, \, ', ", and Control-Z.

/n line feed

/r carriage return

%5C%72

Strips them out maybe?

Potential control characters to try:

/b backspace

%08

Double Encoded:

want: \b

%5C%62

Maybe:

Want: %08

%25%30%38

/f form feed

%0C

/e escape

%1B

shift in

%0F

Shift out

%0E

Data Link Escape

%10

"selec" gets stripped out.

bug I can inject "SELECT" I think?

I think that function removes incomplete SQL statements.

## SQL LIMIT

so this

"2||1 LIMIT 0, 200000"

returns this:

<br>handsome_flag

 and I think I may legit be getting additional results, but the php code only shows me one result. Because of this line of code: 

$res = $run_query->fetch_array()[1];

That index is hard coded....

I wonder if.... I can return results formated as an array already? So the first element of the array, contains an array of all my data.

Well. I can update the first element of limit, the offset, to offset my way to the other keys.

So thats neat I guess, but its basicly just giving it the ID with more steps.

What I really want is more info.

Are there other tables?

What am I trying to do?

Need more info

I have the name of the flag, or a few flags?

I have a table name that probably has the flag in it somewhere, assuming I can find the right ID.

Does it though?

We already grab everything in the table where the column id="blank"

And the values are strings

How can the flag name be "HandsomeFlag"

Well... It could be "handsomeflag{flagstuff}" with some unknown id.

Ok. So MAYBE one of these rows has id "???" and another column with the value containing the flag.

MAYBE.

If thats true, whats stopping me from just iterating through the whole table, 

Nothings stopping me per say.

What would I need limit for then?

I wonder if there is some other way to see the rest of the results coming back from limit all at once.

Ok. What does limit do

Limit makes it so that only X number of columns are returned.

## Subquerries

this command

(SELECT id FROM flag_here_hihi)

selects ALL ids in the table, but the results get fed into the querry that grabs stuff by id.

Maybe, I could grab Ids that meet certain criteria and feed those back in.

Using Where is tricky, because I can't use equals.

or greater than or less than.

or between

or like

I CAN use in.

IN 

In specifies multiple possible values for a column.