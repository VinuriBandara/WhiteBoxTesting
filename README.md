# WhiteBoxTesting


Creators : BANDARA VINURI , ESLAMI YALDA , add your name>

Specification by : DA SILVA NERI MARQUES CARVALHO RICARDO FILIPE , MARTINS ROMAO JOAO DIOGO

<hr>
<div>
    <div id="m_doc" class="m_markdown-body m_container-fluid m_comment-inner m_comment-enabled"><h1 id="m_Specification-of-program-“bst”"><a class="m_anchor m_hidden-xs" title="Specification-of-program-“bst”" rel="noreferrer"><span class="m_octicon m_octicon-link"></span></a><span>Specification of program “bst”</span></h1><h2 id="m_Name"><a class="m_anchor m_hidden-xs" title="Name" rel="noreferrer"><span class="m_octicon m_octicon-link"></span></a><span>Name</span></h2><p><span>bst - Verifies if a provided list of numbers represent a valid binary search tree.</span></p><h2 id="m_Usage"><a class="m_anchor m_hidden-xs" title="Usage" rel="noreferrer"><span class="m_octicon m_octicon-link"></span></a><span>Usage</span></h2><p><span>bst input-file [options]</span></p><h2 id="m_Description"><a class="m_anchor m_hidden-xs" title="Description" rel="noreferrer"><span class="m_octicon m_octicon-link"></span></a><span>Description</span></h2><p><strong><span>bst</span></strong><span> reads a </span><strong><span>list of integers</span></strong><span> from an input file and verifies a if the provided </span><strong><span>integer</span></strong><span> values build a valid </span><a href="https://www.google.com/url?q=https://en.wikipedia.org/wiki/Binary_search_tree&amp;source=gmail-html&amp;ust=1668091938013000&amp;usg=AOvVaw0oIpC0dT9Y36usu6c0pSZR" rel="noopener noreferrer" target="_blank"><span>binary search tree</span></a><span> (BST) when visited following a </span><a href="https://www.google.com/url?q=https://en.wikipedia.org/wiki/Breadth-first_search&amp;source=gmail-html&amp;ust=1668091938013000&amp;usg=AOvVaw0Fvz3_xfurTNKylJWiVwCb" rel="noopener noreferrer" target="_blank"><span>breadth-first search</span></a><span>. The result tree is printed with each level in a different line.</span></p><p><img src="bst_files/unnamed.png" alt=""><br>
<span>The presented tree, which is a valid BST, would be represented by the following input string: </span><code>10 6 18 4 8 15 21</code></p><p><img src="bst_files/unnamed(1).png" alt=""><br>
<span>On the other hand, this image, that would be represented by </span><code>1 2 3 4 5 6 7</code><span>, does not represent a valid BST</span></p><p><span>The program should visit this string provided in a text file and print </span><code>valid</code><span> or </span><code>invalid</code><span>.</span></p><p><span>Tree representation follows this logic:</span><br>
<img src="bst_files/unnamed(2).png" alt=""></p><h2 id="m_Options"><a class="m_anchor m_hidden-xs" title="Options" rel="noreferrer"><span class="m_octicon m_octicon-link"></span></a><span>Options</span></h2><p><span>Options should be provided through the command line.</span></p><ul>
<li><code>-f[ile] &lt;filename&gt;</code><span> - redirect the program output to the specified file.</span></li>
</ul><p><span>The options below should only be executed if the given tree is a valid binary search tree. Each operation should print the result in a new line. Each presented expected output takes the valid BST image shown in the </span><code>Description</code><span> as reference.</span></p><ul>
<li><code>-t[op]</code><span> - prints the top view of the tree. Expected output </span><code>4 6 10 18 21</code></li>
<li><code>-b[ottom]</code><span> - prints the bottom view of the tree. </span><code>4 8 15 21</code></li>
<li><code>-r[ight]</code><span> - prints the right side view of the tree. </span><code>10 18 21</code></li>
<li><code>-l[eft]</code><span> - prints the left side view of the tree. </span><code>10 6 4</code></li>
<li><code>-d[iameter]</code><span> - prints the diameter of the tree. Expected output (one of the following):</span>
<ul>
<li><code>4 6 10 18 21</code></li>
<li><code>4 6 10 18 15</code></li>
<li><code>8 6 10 18 21</code></li>
<li><code>8 6 10 18 15</code></li>
</ul>
</li>
<li><code>-h[eight]</code><span> - prints the height of the tree. Expected output </span><code>3</code></li>
</ul><h2 id="m_Input-Data"><a class="m_anchor m_hidden-xs" title="Input-Data" rel="noreferrer"><span class="m_octicon m_octicon-link"></span></a><span>Input Data</span></h2><ul>
<li><span>File containing a </span><strong><span>list of integers</span></strong><span> (the string provided in the input file must not contain floating point numbers or anything that isn’t an integer) separated by a space.</span></li>
<li><span>No number must exceed 10000.</span></li>
<li><span>The provided binary tree must be </span><strong><span>complete</span></strong><span> (every parent node has 2 and only 2 children nodes). In complete binary trees the number of elements equals to </span><code>2^h – 1</code><span> where </span><code>h</code><span> is the height of the tree. The tree should not have a height superior to 10, meaning that the number of provided elements should not exceed 1023 (2^10 - 1).</span></li>
</ul><h2 id="m_Limitations"><a class="m_anchor m_hidden-xs" title="Limitations" rel="noreferrer"><span class="m_octicon m_octicon-link"></span></a><span>Limitations</span></h2><ul>
<li><span>The commands that are passed on the command line must be the same as in the specification, or the program will not function correctly.</span></li>
</ul></div>
    
</div>


<hr>

<div>
<h2> Implementation </h2>

Vinuri - Implemented the basic functionalities

To Do 
<ul>
<li> Arguments should be integers, no floats etc</li>
<li>Check argument validity</li>
<li>File not found error</li>
<li>Check input validity - each node should be less than x</li>
<li>Check if the binary tree is complete using the height and the number of elements</li>
</ul>

</div>



