Responsive Design with CSS Media Queries
########################################

:date: 2014-03-31 15:00:00
:tags: responsive, css, media query, lab
:author: Ben Glassman
:hidden: 1

For this excercise we will convert the `layout we previously created <{filename}labs/layout/exercise2.rst>`__) to be responsive. A responsive layout changes based on the available screen real estate
so that it displays properly on a variety of screen resolutions and mobile devices. While the term Responsive design is somewhat nebulous, it is generally characterized by employing one or more of the following approaches:

1. Changing the layout based on the environment (the browser), including the screen resolution and orientation (portrait vs landscape iPad for example). 
2. Avoiding the use of absolute units such as pixels for defining the layout. For example the website width would be defined as 80% (of the total width available) or 80em (width based on font size) as opposed to setting the width to 960px

Changing the layout based on screen size and orientation is achieved using CSS3 media queries, which allow you to apply CSS rules based on available screen size or orientation. Here is an example media query that would turn all the text red when the screen is at least 800 pixels wide.

.. code-block:: css

    @media (min-width : 800px) {

        body {
            color: red;
        }

    }

There are many ways to structure your css to achieve a responsive design, but there is a best practice method called **Mobile First** which we will use for this lab. For this approach, you start with only the CSS you would need to make the website usable on a small screen size (mobile). In practice, this often involves creating a single column layout and then adding CSS rules to change to a multi column layout when a minimum screen width is available.

1. We will be modifying the existing layout to be responsive, so the first step is to go to the `codepen page for the original layout <http://codepen.io/benglass/pen/KEekl>`__ and click on the **Fork** button. This creates a copy of the existing codepen which you can edit.

2. Right now the layout is set to be exactly 960 pixels wide. Since we want the layout to resize with the screen, we need to remove this width constraint. Delete the width constraint on the #container.

3. Now you can see that the layout takes up 100% of the available width. This is not ideal for larger screen sizes because it can make your content difficult to read due to long line length. Lets add a max-width to our container to avoid long line lengths. The specific value would depend on your font choice since some fonts have wider x-widths (the width of the letter x and hence a measure of how vertically wide a font is) but you should shoot for a number that results in the 45 to 75 characters per line, which is optimal for readability. In our case lets use the em unit which is based on font size and set the **max-width** to a value of **80em** for the container.

.. code-block:: css

    #container {
        max-width: 80em;
    }

4. Resize the page and you will see that it will now only resize to a certain maximum size, which keeps our line lengths from getting too long.

5. The approach we will use for converting our layout to be responsive is called **mobile first** which means you make your layout look right for mobile devices first. We will remove any multi column layout rules and then use media queries to add multi column layout when we have the extra screen real estate available. Lets assume that we want to show a single column layout unless the user has at least 768 pixels of screen real estate. This will apply for desktop resolutions at or above 800x600 and for iPads in landscape mode. To achieve this, move the width and float rules of the content and sidebar to a media query that requires a minimum width of 768 pixels.


.. code-block:: css

    #content {
      clear: left;
      padding: 20px;
    }

    #sidebar {
        padding: 20px;
    }

    #footer {
      padding: 25px;
      text-align: center;
      border-top: 5px solid #333;
    }

    @media (min-width : 768px) {

      #content {
        float: left;
        width: 70%;
      }

      #sidebar {
        float: left;
        width: 30%;
      }
      
      #footer {
        clear: both;
      }
      
    }

6. Now resize the browser to a small width and you see that we have a single column layout. However when you resize to a larger screen width you will see that the layout changes to a multi-column one. 

7. You can often use the widths of popular mobile devices and desktop resolutions as guidelines for your breakpoints, which is what we did in step 5 when we added multi column layout for larger resolutions. Another good approach is to just resize your layout and see where it breaks. When you find a size at which the layout doesn't look right you can use media queries to modify it. Resize your browser down to a very small width. You will notice that the logo and tagline overlap. 
   
8. We have discovered that for small mobile devices our layout is broken. Lets change the layout so that by default the logo and tagline are centered but if we have enough width then we apply to current styling to position them as they are now.

.. code-block:: css

    #logo {
      text-align: center;
    }

    #tagline {
      color: #fff;
      font-size: 24px;
      font-weight: bold;
      text-align: center;
    }

    @media (min-width: 500px) {
      #logo {
        position: absolute;
        top: 30px;
        left: 30px;
      }
      
      #tagline {
        position: absolute;
        right: 100px;
        top: 35px;
      }
    }

9. Now resize your browser and you will see that the logo and tagline appear stacked and centered unless your browser is wide enough to correctly render the original layout.

.. raw:: html

    <p data-height="800" data-theme-id="0" data-slug-hash="jhbqf" data-default-tab="result" class='codepen'>See the Pen <a href='http://codepen.io/benglass/pen/jhbqf'>jhbqf by Ben Glassman (<a href='http://codepen.io/benglass'>@benglass</a>) on <a href='http://codepen.io'>CodePen</a>.</p>
