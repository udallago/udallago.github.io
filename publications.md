---
layout: default
title: Publications
---

<div id="pub_placeholder">
  Loading Data from DBLP, Please Wait...
</div>
<div id="pub_list">
  <script src="https://bibbase.org/show?bib=https://dblp.org/pid/44/3105.bib&amp;jsonp=1&amp;fullnames=1&amp;hidemenu=true&amp;commas=true"></script>
</div>
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
