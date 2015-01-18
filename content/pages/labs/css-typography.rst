CSS for Typography
##################

:date: 2015-01-14 15:00:00
:tags: css, typography
:author: Ben Glassman
:hidden: 1

1. Create an HTML file called **css-typography.html**. Set the title to "CSS Typography".
   Create a css file named **styles.css**. 
   Link the two together using the html <link> tag.

.. code-block:: html

    <html>
        <head>
            <title>CSS Typography</title>
            <link href="styles.css" rel="stylesheet" type="text/css" />
        </head>
        <body>
        </body>
    </html>

2. Lets start by adding some dummy content to the body tag. We will use all of the common HTML
   tags for content. Add the following HTML to the document between the <body> tags:

   * Level 1 heading
   * Paragraph with a link in the text
   * Level 2 heading
   * Paragraph with a link in the text
   * Level 3 heading
   * Unordered list with at least 2 list items

.. code-block:: html

    <body>
        <h1>Heading 1</h1>
        <p>Lorem ipsum dolor <a href="http://www.yahoo.com">sit amet</a>, consectetur adipiscing elit. Praesent at volutpat mauris, 
        a gravida libero. Pellentesque feugiat risus ut mi iaculis aliquet in sit amet tellus. Donec vitae sem nisi. 
        Nulla scelerisque ligula pellentesque elit volutpat consectetur quis et diam.</p> 
        <h2>Heading 2</h2>
        <p>Lorem ipsum dolor <a href="http://www.google.com">sit amet</a>, consectetur adipiscing elit. Praesent at volutpat mauris, 
        a gravida libero. Pellentesque feugiat risus ut mi iaculis aliquet in sit amet tellus. Donec vitae sem nisi. 
        Nulla scelerisque ligula pellentesque elit volutpat consectetur quis et diam.</p> 
        <h3>Heading 3</h3>
        <ul>
            <li>Item 1</li>
            <li>Item 2</li>
            <li>Item 3</li>
        </ul>
    </body>

3. Now lets select fonts for our website. We need a serif font for our headings and a sans serif font for the body copy.
   Sans serif fonts area easier to read on screens than serif fonts so they are usually used for the body copy of web pages. 
   Google provides a comprehensive library of free web fonts, go to `Google Web Fonts <https://www.google.com/fonts>`_ and select a 
   serif and a sans serif font. Click the **Add to Collection** button for each one. Then click the **Use**
   button at the bottom of the screen. Be sure to select the bold version of the sans serif font you selected
   since our headings will be bold. In order to use a web font, you need to attach it to your HTML page. Copy
   the <link> tag code provided and add it to the <head> of your HTML document.

.. code-block:: html

    <head>
        <link href='http://fonts.googleapis.com/css?family=Bitter:400,700|Open+Sans:700,400' rel='stylesheet' type='text/css'>
    </head>

4. The Google Web Fonts instruction page also includes the CSS you will need to use the fonts you selected. Copy the CSS for the
   sans serif font. In your **styles.css** file, add a new CSS selector to set the font family on the body tag to the sans
   serif font you selected. Set the font size to 14 pixels, the leading (line height) to 1.5em (1.5 times the font size) and the
   color to dark gray (#666666). This will turn all of the text on the page

.. code-block:: css

    body {
        font-family: 'Open Sans', sans-serif;
        font-size: 14px;
        line-height: 1.5em;
        color: #666;
    }

5. Next we want to specify typographic settings for our headings. All of our headings will be the same font
   and color, so we want to create a single CSS selector that applies to h1, h2 and h3 tags. This is achieved by
   combining CSS selectors using a comma between them. Add a CSS rule to **styles.css** to set the font to the
   serif we selected and to a darker gray color (#333333). Lets also ensure that the headings are bold.

.. code-block:: css

    h1, h2, h3 {
        font-family: 'Bitter', serif;
        font-weight: bold;
        color: #333333;
    }

6. Right now, our headings have some default margins around them which are set by the browser automatically. 
   The defaults vary from one browser to another, so for consistency lets set the margins ourselves for our headings.
   Set the top margin for all of the headings to 1.5em (1.5 times the font size) and the bottom margin to 0.5em (half the font size).
   This will make the margin on the bottom smaller so the heading is closer to the content and further away from the previous
   paragraph or heading. **NOTE**: Re-use the selector from the previous step, just adding the lines to specify the margins below
   the last line.

.. code-block:: css

    h1, h2, h3 {
        margin-top: 1.5em;
        margin-bottom: 0.5em;
    }

7. Now we need to specify font sizes for each heading. Once again they are using the browser defaults right now, which may be different
   from one browser to another. Create new CSS properties to set the h1 font size to 36px, h2 to 24px and h3 to 18px. Lets also make
   the h1 black instead of dark gray. This rule will override the earlier rule because it comes later in the css file. **NOTE**:
   CSS is not white space sensitive, in the example below we place each rule on a single line because it is slightly easier to read
   for short rules like this.

.. code-block:: css

    h1 { font-size: 36px; color: #000000; }
    h2 { font-size: 24px; }
    h2 { font-size: 18px; }

8. Our text links are currently blue (or purple if you have already visited the page). This is the browser default so lets change it.
   To start, lets remove the underline from all links.

.. code-block:: css

    a { text-decoration: none; }

9. There are 4 different states which a link can be in,

   #. **link**: A normal link before the user clicks on it
   #. **visited**: A link that the user has already clicked on
   #. **hover**: A link which the user currently has their mouse pointer over
   #. **active**: A link which the user is currently clicking (click and hold on one of the links to see it turn red, which is the default active link style)

10. In order to style our links in these different states, we can use a special CSS selector called a **pseudo-classes**. For example, if we want to 
    add an underline to links only when they are being hovered over, we could use the following code:

.. code-block:: css

    a:hover { text-decoration: underline; }

11. Lets make our links black by default, light gray when visited (#999999), red when hovered and orange when they are being clicked on. Additionally, lets add
    an underline when they are being hovered over.

.. code-block:: css

    a:link { color: #000000; }
    a:visited { color: #999999; }
    a:hover { color: red; text-decoration: underline; }
    a:active { color: orange; }

12. We want to use hanging indentation for the bullets of our lists, so that the text is flush left and the bullets hang in the margins. To achieve this, we need to
    remove the spacing to the left of unordered and ordered lists. Some margins add this spacing with margins and others with padding, so we will remove both to be sure.
    Once again we can use a comma to combine selectors for ordered and unordered list.

.. code-block:: css

    ul, ol { margin-left: 0; padding-left: 0; }

13. Finally, lets customize the unordered lists so they use squares for bullets instead of circles. Create a new selector to target unordered lists and set the list-style
    property to square.


.. code-block:: css

    ul { list-style: square; }

14. You can use the stylesheet we created for future projects, just changing the font families and sizes. Here is the final result:

.. raw:: html

    <p data-height="500" data-theme-id="0" data-slug-hash="yybejJ" data-default-tab="result" class='codepen'>See the Pen <a href='http://codepen.io/benglass/pen/yybejJ'>jALGH</a> by Ben Glassman (<a href='http://codepen.io/benglass'>@benglass</a>) on <a href='http://codepen.io'>CodePen</a>.</p>
