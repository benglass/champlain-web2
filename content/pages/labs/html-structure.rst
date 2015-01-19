HTML for Structure
##################

:date: 2015-01-14 15:00:00
:tags: html, structure
:author: Ben Glassman
:hidden: 1

Lets create an HTML page for a graphic design portfolio. The portfolio needs to include
work from 3 categories: Print, Web and Branding. We want to include the graphic designer's name
in the masthead and provide navigation links that will allow users to jump to a particular category
of work. This exercise shows how you can use structural HTML tags like main, nav, section and article.

1. Create an HTML file called **html-structure.html**. Set the title to "HTML Structure".
   Create a css file named **styles.css**. 
   Link the two together using the html <link> tag.

.. code-block:: html

    <html>
        <head>
            <title>HTML Structure</title>
            <link href="styles.css" rel="stylesheet" type="text/css" />
        </head>
        <body>
        </body>
    </html>

2. Lets start by adding the header with the graphic designer's name.
   Add a <header> tag to the body. Place a paragraph tag inside the
   header and put the person's name in it. Add a class of "site-name"
   to the paragraph for styling.

.. code-block:: html

    <body>
        <header>
            <p class="site-name">John Johnson Graphic Design</p>
        </header>
    </body>

3. In **styles.css** lets select the paragraph we added using the class
   and set the font size to 48px, color to gray and italicize the text.

.. code-block:: css

    .site-name {
        font-size: 48px;
        font-style: italic;
        color: #333;
    }

4. Below the <header> we just added, lets place our content. First, create a 
   <main> tag, which designates where the main content of a page is. Inside the
   <main> tag we will add a level 1 heading with the name of the page (Portfolio).

.. code-block:: html

    </header>

    <main>
        <h1>Portfolio</h1>
    </main>

5. We have 3 categories of portfolio items we want to display: Print, Web and Branding.
   Lets create a <section> tag for each one within the <main> tag and add a heading level 2 
   with the category name to each section. Add an id attribute to each section with a unique
   id we can use to link to the section. IDs should be all lowercase and should not include spaces.

.. code-block:: html

    <main>
        <h1>Portfolio</h1>
        <section id="print">
            <h2>Print</h2>
        </section>
        <section id="web">
            <h2>Web</h2>
        </section>
        <section id="branding">
            <h2>Branding</h2>
        </section>
    </main>

6. Now that we have section tags set up for each of our portfolio categories, we can add navigation
   that will let users jump to a category. You can create a link that jumps to a specific area of a page
   by adding an id to any HTML tag (we added it to the sections) and then creating a link with the href set to
   #id. Above the <main> tag we created, add a <nav> tag. Inside the <nav> tag add an unordered list. For each section,
   add a list item with a link to the section's id.

.. code-block:: html

    <nav>
        <ul>
            <li><a href="#print">Print</a></li>
            <li><a href="#web">Web</a></li>
            <li><a href="#branding">Branding</a></li>
        </ul>
    </nav>

7. In your browser, click on one of the links we added. It will try to jump you down to the section with the corresponding id.
   Right now we dont have enough content on the page for the scrolling to work properly, but you can see that by assigning
   an id to any html tag (<section> tags in this case) and using a link with the href set to #id you can jump a user down to a particular area
   of the page. 

8. Lets add portfolio items to the sections we created. The <article> tag is a good fit for a portfolio item, because a portfolio item
   represents a piece of content which could stand on its own and still make sense. Other examples of where you might use an article tag might be:
   a blog post, a product or a person's bio. It is a very versatile tag with a slightly confusing name because it is not just for use
   with articles, but any single piece of content that would make sense by itself. Lets add 2 portfolio items to each section, including
   an h3 tag for the portfolio item name and an img tag for the thumbnail. You can use an image placeholder service like `placehold.it <http://placehold.it>`_ for thumbnails.

.. code-block:: html

    <section id="print">
        <h2>Print</h2>
        <article>
          <h3>Item 1</h3>
          <img src="http://placehold.it/100x100" />
        </article>
        <article>
          <h3>Item 2</h3>
          <img src="http://placehold.it/100x100" />
        </article>
    </section>

9. Lets separate the sections by adding a border between them. We could do this by using a CSS selector to add a border to all section tags, as follows:

.. code-block:: css

    section { border-bottom: 1px solid black; }

The problem with this is that the rule is too general, it means that you cannot use section tags for anything else on this page or any page that shares
the style sheet. What we really want to do is add a border to each portfolio category, so lets add a class to each section of "portfolio-category" and use that
to add our border.

.. code-block:: html

    <section id="print" class="portfolio-category">
        ...
    </section>
    <section id="web" class="portfolio-category">
        ...
    </section>
    <section id="branding" class="portfolio-category">
        ...
    </section>

Notice we can re-use the class multiple times. This is the difference between a class and an id. An ID is a unique identifier while a class is a way to share
styles between different elements.

10. Now that we have a portfolio-category class, lets add a bottom border to each portfolio category. We will also add some padding to each category so there is space
    between the portfolio items and the border.

.. code-block:: css

    .portfolio-category { border-bottom: 1px solid black; padding: 20px; }


11. Lets remove the space between the portfolio item name (the h3) and the image itself. Once again, we could do this by creating a CSS selector that finds all
    h3 tags inside article tags but that is too broad. We may have other article tags on the website that are not for portfolio items and we may not want to change them.
    Lets add a portfolio-item class to each article to indicate that it is a portfolio item.

.. code-block:: html

    <article class="portfolio-item">

12. Now we can create a CSS selector that finds h3 tags inside of our portfolio items and removes the bottom margin from them.

.. code-block:: css

    .portfolio-item h3 { margin: 0; }

13. Lets also add some space between the portfolio items by adding 18px of bottom margin to each portfolio item.

.. code-block:: css

    .portfolio-item { margin:-bottom: 18px; }

14. Lets add a footer with a copyright symbol and the current date. Add a <footer> tag after the <main> tag and place a paragraph tag
    in it with the text: &copy; 2015

.. code-block:: html

    </main>

    <footer>
        <p>&copy; 2015</p>
    </footer>

15. To finish up, lets remove the bullets and indent from the navigation and add some styling to the links. Once again we do not want to 
    use the nav tag in our CSS selector since its possible we may have other nav tags on our site that shouldnt receive the portfolio nav styling, so
    lets add a class of nav-portfolio to the nav tag. Now add CSS rules for the following:

    * Remove left margin and padding from the unordered list tag
    * Remove bullets frm the unordered list by setting list-style to none
    * Remove the underline from the links
    * Make the unvisited links dark gray (#666)
    * Make the visited links light gray (#999)
    * Make the links red when you hover over them
    * Make the links orange when you click on them

.. code-block:: css

    .nav-portfolio ul { list-style: none; margin-left: 0; padding-left: 0; }
    .nav-portfolio a { text-decoration: none; }
    .nav-portfolio a:link { color: #666; }
    .nav-portfolio a:visited { color: #999; }
    .nav-portfolio a:hover { color: red; }
    .nav-portfolio a:active { color: orange; }

.. raw:: html

    <p data-height="500" data-theme-id="0" data-slug-hash="yybeEa" data-default-tab="result" class='codepen'>See the Pen <a href='http://codepen.io/benglass/pen/yybeEa'>yybeEa</a> by Ben Glassman (<a href='http://codepen.io/benglass'>@benglass</a>) on <a href='http://codepen.io'>CodePen</a>.</p>
