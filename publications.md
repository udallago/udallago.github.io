---
layout: default
title: Publications
---

<div id="pub_placeholder">
  Loading Data from DBLP, Please Wait...
</div>
<div id="pub_list">
  <script src="https://bibbase.org/show?bib=https%3A%2F%2Fdblp.org%2Fpid%2F44%2F3105.bib&jsonp=1&fullnames=1&hidemenu=true&commas=true&nocache=1"></script>
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
