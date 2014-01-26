Layout Exercise 1: HTML Structure for Layout
##################################################

:date: 2014-01-26 15:00:00
:tags: positioning, floats, css, lab, layout
:author: Ben Glassman
:hidden: 1

Most websites share certain common structural elements in their layout. These include:

    * Header

      * Logo

      * Tagline

    * Navigation

    * Primary Content

    * Sidebar

    * Footer

In this exercise we will create an HTML skeleton that can be used as the basis for most layouts
as it includes the elements listed above.

1. Create a new html file with opening and closing html tags and save it as **layout-skeleton.html**

.. code-block:: html

    <html>
    </html>

2. Add the head and body tags inside the html tags. Include a title tag inside the head tags with the title ""HTML Layout Skeleton"

.. code-block:: html

    <html>
        <head>
            <title>HTML Layout Skeleton</title>
        </head>
        <body>
        </body>
    </html>

3. Add a **div** tag inside of the **body** with an **id** atribute of **container**
   This will contain our site layout and can be used for centering our laying and applying a width later on.

.. code-block:: html

    <div id="container">
    </div>

4. Add an html comment right after the closing **div** tag. This comment should contain the css selector for
   an id of **container**. This comment is optional and will not be displayed to visitors of your website
   but it can help when reading your code so you can tell what **div** tag it closes.

.. code-block:: html

    <div id="container">
    </div><!-- #container -->

5. Add a **section** tag inside of the **container** with an **id** atribute of **masthead**
   This is the masthead area of the website where we will place the logo and tagline

.. code-block:: html

    <div id="container">

        <section id="masthead">
        </section>

    </div><!-- #container -->

6. Add a **div** tag inside the masthead with an **id** of **logo**

.. code-block:: html

    <section id="masthead">
        <div id="logo"></div>
    </section>

7. Add an **img** tag inside the **logo** div. Include both a **src** and **alt** attribute.
   **Note**: You can use a website like `Placehold.it <http://placehold.it>`_ to generate a dummy image.
   
.. code-block:: html

    <div id="logo">
        <img src="http://www.placecage.com/200/300" alt="Nick Cage" />
    </div>

8. Make the **img** a link to the home page of the site by adding an **a** tag around it and setting the **href**
   attribute. Set the **href** to the filename of this page.
   
.. code-block:: html

    <div id="logo">
        <a href="layout-skeleton.html">
            <img src="http://www.placecage.com/200/300" alt="Nick Cage" />
        </a>
    </div>

9. Add a **p** tag to the **masthead** after the **logo** with an **id** of **tagline**. Set the text of the paragraph
   to **Some company tagline**. Now we are doing with the masthead.

.. code-block:: html

    <p id="tagline">Some company tagline</p>

8. Add a **nav** tag after the **masthead** with an **id** of **navigation** for our primary navigation.

.. code-block:: html

   <nav id="navigation">
   </nav>

9. Add some example navigation links inside of the **nav** tag by creating an **unordered list** with 2 **list items**
   inside it. Each **list item** should contain an link to an html file on the site. In this case, lets use
   Home (**index.html**) and About (**about.html**).

.. code-block:: html

   <nav id="navigation">
       <ul>
           <li><a href="index.html">Home</a></li>
           <li><a href="about.html">About</a></li>
       </ul>
   </nav>

10. For our main content area, add a new **section** tag with an **id** of **content** after the **nav**.

.. code-block:: html

   <section id="content">
   </section>

11. Add a **level 1 heading** tag to the **content** with the text **Home** and 3 **paragraphs** of text.
    **Note**: Use a website like `Picksum Ipsum <http://www.picksumipsum.co.uk/>`_ to generate dummy text.

.. code-block:: html

   <section id="content">
       <h1>Home</h1>
       <p>... dummy text ..</p>
       <p>... dummy text ..</p>
       <p>... dummy text ..</p>
   </section>

12. For our sidebar, add a **section** tag with an **id** of **sidebar** after the **content**.

.. code-block:: html

    <section id="sidebar">
    </section>

13. Add a **level 2 heading** to the **sidebar** with the text **News** and 1 **paragraph** of dummy text.

.. code-block:: html

    <section id="sidebar">
        <h2>News</h2>
        <p>... dummy text ...</p>
    </section>

14. For the footer of our site, add a **footer** tag after the **sidebar** with an **id** of **footer**.

.. code-block:: html

    <footer id="footer">
    </footer>

15. Add a **paragraph** to the **footer** with a **class** of **copyright**. The text should include the copyright
    symbol followed by the year and the words **All Rights Reserved**.
    **Note**: The copyright symbol can be used in HTML by using **&copy;**. This is called an **html special character**
    so if you need to find one for the trademark symbol you can do a search for **trademark symboly html special character**

.. code-block:: html

    <footer id="footer">
        <p class="copyright">&copy; 2014 All Rights Reserved</p>
    </footer>

16. Add another **paragraph** to the **footer** with a **class** of **navigation** and containing a text version of our navigation. This **paragraph** should have 2 links in it, **Home** and **About**. 
    You can use the **anchors** from step 9 without the **unordered list** or **list items**

.. code-block:: html

    <footer id="footer">
        <p class="copyright">&copy; 2014 All Rights Reserved</p>
        <p><a href="index.html">Home</a> <a href="about.html">About</a></p>
    </footer>

Final Result
------------

.. raw:: html

    <p data-height="947" data-theme-id="0" data-slug-hash="BHKtD" data-default-tab="result" class='codepen'>See the Pen <a href='http://codepen.io/benglass/pen/BHKtD'>BHKtD</a> by Ben Glassman (<a href='http://codepen.io/benglass'>@benglass</a>) on <a href='http://codepen.io'>CodePen</a>.</p>
