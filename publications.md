---
layout: default
title: Publications
---

<section id="pub_placeholder">  
        Please wait...
      </section>
      <section id="pub_list">
        <script src="https://bibbase.org/show?bib=https://dblp.org/pid/44/3105.bib&amp;jsonp=1&amp;fullnames=1&amp;hidemenu=true&amp;commas=true"></script>
      </section>
      <footer>
        <p><small>Hosted on GitHub Pages</small></p>
      </footer>
    </div>
    <script src="/assets/js/scale.fix.js"></script> 
    <script>
      x = $("#pub_list")[0].innerHTML;
      function f(){
          if ($("#pub_list")[0].innerHTML == x)
              setTimeout(f, 5);
          else
              $("#pub_placeholder")[0].innerHTML = "";
      }
      f();
    </script>



<script src="https://bibbase.org/show?bib=https://dblp.org/pid/44/3105.bib&jsonp=1&fullnames=1&hidemenu=true&commas=true"></script>
