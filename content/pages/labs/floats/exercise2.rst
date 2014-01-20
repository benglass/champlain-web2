CSS Floats Exercise 2: Column Layouts with CSS Floats
#####################################################

:date: 2014-01-19 15:00:00
:tags: floats, css, lab
:author: Ben Glassman
:hidden: 1

A common styling problem we can solve with css floats is that of multi-column layouts.
This exercise will show you how to create `this 3 column layout <http://codepen.io/benglass/pen/djnte>`_
use floats.

By default html tags like div, p, h1-h6, section and article will be rendering in a stacked vertical
layout. For example, consider the following html for a list of products:

.. code-block:: html

    <section class="product-list">
        <article class="product">
            <h2>Product 1</h2>
            <p class="price">$5.00</p>
        </article>
        <article class="product">
            <h2>Product 2</h2>
            <p class="price">$10.00</p>
        </article>
        <article class="product">
            <h2>Product 3</h2>
            <p class="price">$9.999</p>
        </article>
    </section>

The article tags would be displayed vertically stacked as shown below:

.. raw:: html

    <section class="product-list">
        <article class="product">
            <h2>Product 1</h2>
            <p class="price">$5.00</p>
        </article>
        <article class="product">
            <h2>Product 2</h2>
            <p class="price">$10.00</p>
        </article>
        <article class="product">
            <h2>Product 3</h2>
            <p class="price">$9.999</p>
        </article>
    </section>

What if we would like to display them in a 3 column layout, which each taking up 1/3 of the available space?
We can achieve this by floating each product to the left and giving it a width. Follow the instructions below
to create this 3 column layout.

1. Create a new HTML page and CSS file, linking them together by following the initial steps of the previous exercise.
   Leave the **body** tags of the HTML file empty for now and do not add anything to the CSS file.

2. In the HTML file, add a section tag with a class of **product-list** to the body tag.

.. code-block:: html

    <body>
        <section class="product-list"> 
        </section>
    </body>
    
3. In the **section** tag, add an article tag with a class of **product** for the first product.

.. code-block:: html

    <section class="product-list">
        <article class="product">
        </article>
    </section>

4. In the **article** tag, add an **h2** tag with the text "Product 1"

.. code-block:: html

        <article class="product">
            <h2>Product 1</h2>
        </article>

5. In the **article** tag, add a **p** tag with a class of **price** and the text $5.00

.. code-block:: css

        <article class="product">
            <h2>Product 1</h2>
            <p class="price">$5.00</p>
        </article>

6. Create 2 more **article** tags inside the **section** tag, changing the heading text and the price

7. In your css file, add css that sets **float** to **left** for the class of **product**

.. code-block:: css

    .product {
        float: left;
    }

8. When we preview our code we can see that we have achieved a multi column layout. There is currently
   not space between the columns and they are only as wide as the content inside them. In this case the
   columns are too small because there is not much content inside them. Lets see what happens when we add a 
   long product description. Copy one of the paragraphs from the previous excercise and add it to **each** of the
   article tags to serve as a dummy product description.

.. code-block:: html

    <article class="product">
        <h2>Product 1</h2>
        <p class="price">$5.00</p>
        <p>... dummy text ...</p>
    </article>

9. When we preview our code we can see that now the columns are too long and we have lost our 3 column layout
   because the floated articles expand to the width of the content. When you are creating column layouts
   using floats, you will almost always want to also set a width to prevent this issue. 
   In your css file, add a new CSS rule to **.product** that sets the **width** to **33%**
   **Note** You can also use pixel based widths rather than percent based widths but it is generally
   better to use percent values so your website will work on different screen resolutions (Mobile Phone,
   Tablet and Desktop).

.. code-block:: css

    .product {
        /* Existing rules */
        width: 33%;
    }

10. Now we have 3 columns with each one taking up 1/3 of the available width regardless of how much
    content we add to them. We have a similar issue as we had with the first exercise where there is
    no spacing between the columns, so the text from column 1 runs into the edge of the text from column 2.
    Lets try to fix this by adding padding to all sides of our products. In your css file, add **30px**
    of padding to the css for **.product**

.. code-block:: css

    .product {
        /* Existing rules */
        padding: 30px;
    }

11. Previewing our code we can see our column layout is now broken. This is because of the way that
    the css **width** and **padding** properties interact. By default, the browser will add them all
    together and if they come out to more than 100% then we will have a problem. In this case we have
    33% plus 60px (30 pixels on the left and 30 on the right) for each column. This is confusing behavior
    and not what you would expect. We can tell the browser to just use the **width** we specify and fit
    the padding inside of that width by adding the following css to the top of our css file.

.. code-block:: css

    * { box-sizing: border-box; }

..

Because this is the expected behavior (when you set a width you dont expect the padding to effect it)
it is recommended that you include this in all of your css files. The asterisk selector (*) in the CSS 
selector above means "all html tags" so it fixes this issue with width and padding for all html elements.
The final result is displayed below:

.. raw:: html

    <p data-height="415" data-theme-id="0" data-slug-hash="djnte" data-default-tab="result" class='codepen'>See the Pen <a href='http://codepen.io/benglass/pen/djnte'>djnte</a> by Ben Glassman (<a href='http://codepen.io/benglass'>@benglass</a>) on <a href='http://codepen.io'>CodePen</a>.</p>
