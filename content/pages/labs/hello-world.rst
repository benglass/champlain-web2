Hello World
###########

:date: 2014-08-26 15:00:00
:tags: html, css, javascript
:author: Ben Glassman
:hidden: 1

To get back into the swing of things with HTML, CSS and Javascript we will create
a basic HTML page with a some simple CSS and a little Javascript to show a hidden message
when the user clicks on a button.

1. Create a new html file with opening and closing html tags and save it as **hello-world.html**
   The first line of the file should include the **doctype declaration** that tells browsers
   this is HTML.

.. code-block:: html

    <!DOCTYPE html>
    <html>
    </html>

2. Add the head and body tags inside the html tags. Include a title tag inside the head tags with the title "Hello World"

.. code-block:: html

    <!DOCTYPE html>
    <html>
        <head>
            <title>Hello World</title>
        </head>
        <body>
        </body>
    </html>

3. Create a new css file and save it as **styles.css**
   **Note**: Make sure you save it in the same folder as your HTML file.

4. Link the css file to your html file by adding the following code to the <head> of your HTML file:

.. code-block:: html

    <link href="styles.css" rel="stylesheet" type="text/css" />

5. Inside the **body** tag of your HTML file, we want to add a message
   to display to the user. Add a new paragraph using the **p** tag.
   Inside the paragraph tag, add the text "Hello World".

.. code-block:: html

   <p>Hello World</p>

6. We want the message to be hidden when the page first loads.
   To make it easier to to apply styles to our message, add
   an **id** attribute with the value **message**.

.. code-block:: html

   <p id="message">Hello World</p>

7. We can hide the message using CSS. In the **styles.css** file
   we created, we need to select the html tag with id of message.
   The id selector is the **#** symbol followed by the value of 
   the id attribute. Create a new selector in **styles.css**
   for the id of **message**.

.. code-block:: css

   #message {
   }

8. In order to hide the message, we can use the css **display** property
   with the value of **none**.

.. code-block:: css

   #message {
      display: none;
   }

9. Now that the message is hidden, lets add a link the user can click
   in order to display the message. Add a link in the **body** tag
   using the **a** tag with the text "You have 1 unread message". Include
   a **class** attribute on the link with the value of
   **btn-view-message** which we will use to style the link as a button.

.. code-block:: html

   <a class="btn-view-message">You have 1 unread message</a>

10. In **styles.css** lets add a selector for the link using the
    **btn-view-message** class we added. The class selector in CSS is
    the **.** (the period) followed by the class attribute.

.. code-block:: css

   .btn-view-message {
   }

11. Add the following styles inside the selector we created to make the link
    look like a button. We will make the background color blue, add rounded corners,
    add some padding around the text and make the text white. Don't worry about the
    **display: inline-block** code, we will discuss that later in the semester.

.. code-block:: css

   .btn-view-message {
      background: blue;
      color: white;
      padding: 15px;
      border-radius: 15px;
      display: inline-block;
   }

12. We would like the button to change when the user hovers over it. Lets change the opacity
    to make it semi-transparent when the user mouses over it. Copy the **.btn-view-message**    
    selector and add **:hover** to the end (no space before the colon) to make a selector
    that changes the view message button when the user is hovering over it.

.. code-block:: css

   .btn-view-message:hover {
        opacity: 0.5;
   }

13. Now lets add some interactivity by making it so when the user clicks on the button the message
    shows using a fade in effect. In order to do we need to use javascript. We will use the jQuery
    javascript library which provides convenient functionality to easily achieve common javascript
    tasks like selecting html elements and animating them. Before the closing **body** tag, add a **script** tag which includes jQuery onto the page. jQuery is not available by default so you have to 
    link it to your html page before using it. In this case we will use a version of jquery that is 
    hosted by a third party website (**cdnjs.com**) so we don't have to download the jquery.js file.
    This has a number of advantages we will discuss later in the course.

.. code-block:: html

        <script src="http://cdnjs.cloudflare.com/ajax/libs/jquery/1.11.1/jquery.js"></script>
    </body>

14. Now that we've attached jQuery, we can use it in our javascript via the **jQuery** variable 
    (or **$** for short. We can pass jQuery a CSS selector in order to grab an HTML element. Then we
    can use the **click** method to add interactivity when the user clicks on that item. 
    The **alert** function will pop up a message to the user when you click the button.

.. code-block:: html

        <script src="http://cdnjs.cloudflare.com/ajax/libs/jquery/1.11.1/jquery.js"></script>
        <script>
            jQuery('.btn-view-message').click(function() {
                alert('Dont click me bro!');
            });
        </script>
    </body>

15. Now lets replace the alert code we wrote with jQuery code that will grab the message
    by its id using a css selector and fade it in.

.. code-block:: html

        <script src="http://cdnjs.cloudflare.com/ajax/libs/jquery/1.11.1/jquery.js"></script>
        <script>
            jQuery('.btn-view-message').click(function() {
                jQuery('#message').fadeIn();
            });
        </script>
    </body>

16. As mentioned earlier in this lab, the **$** is just a shortcut for **jQuery** which you will
    commonly see in code examples. Change the **jQuery** to **$** in your code.

.. code-block:: html

        <script src="http://cdnjs.cloudflare.com/ajax/libs/jquery/1.11.1/jquery.js"></script>
        <script>
            $('.btn-view-message').click(function() {
                $('#message').fadeIn();
            });
        </script>
    </body>

17. Preview the result in your browser and you should see something like the following.

.. raw:: html

    <p data-height="400" data-theme-id="0" data-slug-hash="gFijJ" data-default-tab="result" class='codepen'>See the Pen <a href='http://codepen.io/benglass/pen/gFijJ'>gFijJ by Ben Glassman (<a href='http://codepen.io/benglass'>@benglass</a>) on <a href='http://codepen.io'>CodePen</a>.</p>

