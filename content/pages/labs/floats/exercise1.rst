CSS Floats Exercise 1: Styling Content Images with Floats
#########################################################

:date: 2014-01-19 15:00:00
:tags: floats, css, lab
:author: Ben Glassman
:hidden: 1

The css float property can be used for everything from layout out images and text
in a content area to achieving complex multi-column layouts.

The following layout of an image with text flowing around it is a common requirement
for the content area of a website.

.. raw:: html

    <p data-height="665" data-theme-id="0" data-slug-hash="fkilx" data-default-tab="result" class='codepen'>See the Pen <a href='http://codepen.io/benglass/pen/fkilx'>fkilx</a> by Ben Glassman (<a href='http://codepen.io/benglass'>@benglass</a>) on <a href='http://codepen.io'>CodePen</a>.</p>

Since this type of layout is so common, you will generally want to create some classes in your CSS file which
take care of displaying images on the right or the left side of text. The following instructions will
help you create 2 CSS classes (image-right and image-left) which can be used when displaying images in the content
area of your website.

1. Create a new html file with opening and closing html tags and save it as **css-floats.html**

.. code-block:: html

    <html>
    </html>

2. Add the head and body tags inside the html tags. Include a title tag inside the head tags with the title "CSS Floats"

.. code-block:: html

    <html>
        <head>
            <title>CSS Floats</title>
        </head>
        <body>
        </body>
    </html>

3. Create a new css file and save it as **styles.css**
   **Note**: Make sure you save it in the same folder as your HTML file.

4. Link the css file to your html file by adding the following code to the <head> of your HTML file:

.. code-block:: html

    <link href="styles.css" rel="stylesheet" type="text/css" />

5. In your HTML file, create a new div tag in between the body tags and give it a class of **content**.
   This represents the content area of our website.

.. code-block:: html

    <div class="content">
    </div>

6. Add another div inside the content div and give it a class of **image-right**

.. code-block:: html

    <div class="content">
        <div lass="image-right"></div>
    </div>

7. Add an image tag inside of the div tag we created. Set the src attribute and the alt attributes.
   **Note**: You can use a website like `Placehold.it <http://placehold.it>`_ to generate a dummy image.
   
.. code-block:: html

    <div class="image-right">
        <img src="http://www.placecage.com/200/300" alt="Nick Cage" />
    </div>

8. Add 3 paragraphs of text after the div tag. Use a website like `Picksum Ipsum <http://www.picksumipsum.co.uk/>`_ to generate dummy text. Make sure these are real paragraphs of content as the text needs to be long enough to wrap around the image.

.. code-block:: html

    <div class="image-right">
        <img src="http://www.placecage.com/200/300" alt="Nick Cage" />
    </div>
    <p>...dummy text...</p>
    <p>...dummy text...</p>
    <p>...dummy text...</p>

9. In **styles.css**, add css to select the class of **content** and make it 600 pixels wide.
   **Note** The period (.) character is the 'class selector'

.. code-block:: css

    .content {
        width: 600px;
    }

10. In **styles.css**, add css to select the class of **image-right** and set the **float** property to **right**

.. code-block:: css

    .image-right {
        float: right;
    }

11. The image is now floating to the right of the content text. There is no spacing around the image
    and the text goes right up to the edge of the image. Fix this in **styles.css** by adding left and
    bottom margins to the selector for **image-right**

.. code-block:: css

    .image-right {
        /* Existing rules */
        margin-left: 20px;
        margin-bottom: 20px;
    }

12. We now have a re-usable css class we can use for whenever we want an image to appear to the right of some text.
    Lets create another class for when we want the image to appear on the left.
    Copy and paste the html starting with the **image-right** div and including the paragraphs and add it 
    to the bottom of the **content** div. Change **image-right** to **image-left**.
    Do the same in your css file with the **.image-right** code, changing **image-right** to **image-left** 
    and changing the left margin to a right margin. You can add these classes to any websites you create
    in the future and use them to style your content images. The final result is below:

.. raw:: html

    <p data-height="508" data-theme-id="0" data-slug-hash="KbdvI" data-default-tab="result" class='codepen'>See the Pen <a href='http://codepen.io/benglass/pen/KbdvI'>KbdvI</a> by Ben Glassman (<a href='http://codepen.io/benglass'>@benglass</a>) on <a href='http://codepen.io'>CodePen</a>.</p>
